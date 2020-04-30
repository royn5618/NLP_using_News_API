# NLP_using_News_API
Structured Text Analysis using resources from the NewsAPI

How to use:

This repository works in two stages -

## 1. Data Processor

Data Processor gets reads the data from [NewsAPI](https://newsapi.org/) and places then in structured folder.

### Arguments:

```-aim=<download or process>  -q=<query term> -c=<country code> -s=<source>```

`
### Arguments in Details:

-aim: Download or process. The downloader and processor works separately.

-q: The query term. Only one query term is handled.

-c: Country Code or 'ALL'. This is only set-up for India and Ireland specifically. So ALL inditaes both Ireland and India as opposed to all countries.

-s: Source as specified in NewAPI other wise will not be able to scrape. ALL sources refer to those configured at [Contants](https://github.com/royn5618/NLP_using_News_API/blob/master/DataProcessor/NewsAPIGetData/constants.py)`
