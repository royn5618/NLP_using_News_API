# NLP_using_News_API
Structured Text Analysis using resources from the NewsAPI

How to use:

This repository works in two stages -

## 1. Data Processor

Data Processor gets reads the data from [NewsAPI](https://newsapi.org/) and places then in structured folder.

### Arguments:

```-aim=<download or process>  -q=<query term> -c=<country code> -s=<source>```

**Arguments in Details:**

-aim: download or process. The downloader and processor works separately. 

Option **download** only downloads the texts and stores them in folders. Option **process** processes the folder contents and saves the folder contents into a pandas dataframe pickle file.

-q: The query term. Only one query term is handled. *This query term is also the Folder Name in which the jsons are stored.*

-c: Country Code or 'ALL'. This is only set-up for India and Ireland specifically. So ALL inditaes both Ireland and India as opposed to all countries.

-s: Source as specified in NewAPI other wise will not be able to scrape. ALL sources refer to those configured at [Contants](https://github.com/royn5618/NLP_using_News_API/blob/master/DataProcessor/NewsAPIGetData/constants.py)


## *** NLP Processor in progress ***
