import os
import warnings

import gensim
import matplotlib.pyplot as plt
import pandas as pd
from gensim.models import CoherenceModel
from nltk.corpus import wordnet as wn

warnings.filterwarnings("ignore",category=DeprecationWarning)


class NLPPreProcess:

    @staticmethod
    def token_corpus_build(sequences):
        """

        :return: Sequence of tokens
        """
        token_corpus = []
        for text in sequences:
            token_list = []
            for token in gensim.utils.simple_preprocess(text, deacc=True):
                if token not in gensim.parsing.preprocessing.STOPWORDS:
                    token_list.append(token)
            token_corpus.append(token_list)
        return token_corpus

    @staticmethod
    def lemma_generation(sequences):
        """

        :return: Sequence of  lemmatized tokens
        """
        lemmatized_sequences = []
        for each_token_list in sequences:
            lemma = [token if wn.morphy(token) is None else wn.morphy(token) for token in each_token_list]
            lemmatized_sequences.append(lemma)
        return lemmatized_sequences


    # TO DO ADD Stanford NLP stuff in class
    @staticmethod
    def get_lemma(no_punct_seq_tokens):
        normalized_sequence = []
        for each_seq in st.tag_sents(sentences=no_punct_seq_tokens):
            normalized_tokens = []
            for tuples in each_seq:
                temp = tuples[0]
                if tuples[1] == "NNP" or tuples[1] == "NNPS":
                    continue
                if tuples[1][:2] in dict_pos_map.keys():
                    temp = lm.lemmatize(tuples[0].lower(),
                                        pos=dict_pos_map[tuples[1][:2]])
                normalized_tokens.append(temp)
            normalized_sequence.append(normalized_tokens)
        return normalized_sequence

    @staticmethod
    def n_gram_generation(sequences):
        """

        :return: Returns a bi and tri-grammed sequences
        """
        bigram = gensim.models.Phrases(sequences, min_count=5, threshold=0.50, scoring='npmi')
        bigram_phraser = gensim.models.phrases.Phraser(bigram)

        trigram = gensim.models.Phrases(bigram[sequences], threshold=0.70, scoring='npmi')
        trigram_phraser = gensim.models.phrases.Phraser(trigram)

        n_grammed_corpus = [trigram_phraser[bigram_phraser[text]] for text in sequences]
        return n_grammed_corpus


class TopicModelling:
    # MAchine Learning for LanguagE Toolkit
    @staticmethod
    def run_mallet_lda(corpus, id2word, num_topics):
        os.environ.update({'MALLET_HOME': r'C:/mallet-2.0.8'})
        mallet_path = 'C:/mallet-2.0.8/bin/mallet'
        mallet_lda_model = gensim.models.wrappers.LdaMallet(mallet_path,
                                                            corpus=corpus,
                                                            num_topics=num_topics,
                                                            id2word=id2word,
                                                            iterations=1000)
        return mallet_lda_model

    @staticmethod
    def compute_coherence_values(id2word, corpus, lemmatized_corpus, x):
        print('Computing coherence values')
        coherence_values = []
        models = []
        for num_topics in x:
            model = TopicModelling.run_mallet_lda(corpus, id2word, num_topics)
            models.append(model)
            cm = CoherenceModel(model=model, texts=lemmatized_corpus, dictionary=id2word, coherence='u_mass')
            coherence_values.append(cm.get_coherence())
            print('Completed topics ' + str(num_topics))
        return models, coherence_values

    @staticmethod
    def get_optimal_model(id2word, corpus, lemmatized_corpus, x):
        models, coherence_values = TopicModelling.compute_coherence_values(id2word, corpus, lemmatized_corpus, x)

        for i, j in zip(x, coherence_values):
            print("Num Topics:", i, "Coherence Value:", round(j, 2))
        # For exploring the topics
        #    for model in models:
        #        topics_list.append(model.show_topic(topn = 15))
        max_cv = max(coherence_values)
        cv_index = coherence_values.index(max_cv)
        return models[cv_index]

    @staticmethod
    def get_dominant_topics_df(model, corpus):
        doc_topics_df = pd.DataFrame()
        for doc in model[corpus]:
            # each row ~ document
            doc = sorted(doc, key=lambda x: (x[1]), reverse=True)
            # Get the Dominant topic, Perc Contribution and Keywords for each document
            for n, (num_topic, perc_contrib) in enumerate(doc):
                if n == 0:  # => dominant topic
                    temp = model.show_topic(num_topic, topn=15)
                    keywords = "; ".join([topic for topic, perc in temp])
                    doc_topics_df = doc_topics_df.append(
                        pd.Series([int(num_topic), round(perc_contrib * 100, 2), keywords]), ignore_index=True)
                else:
                    break
        doc_topics_df.columns = ['Dominant_Topic', 'Percentage_Contribution', 'Contributing_Keywords']
        return doc_topics_df


class Visuals:

    @staticmethod
    def coherence_plot(x, coherence_values):
        plt.plot(x, coherence_values)
        plt.xlabel("Number of Topics")
        plt.ylabel("Coherence Score")
        plt.legend(("No. of Topics vs. Coherence Scores"), loc='best')
        plt.show()
