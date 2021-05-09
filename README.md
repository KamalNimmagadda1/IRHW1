# Search Engine Comparison 

We are comparing the search results from Google versus different search engines.
Many search engine comparison studies have been done. All of them use samples of data, some
small and some large, so no definitive conclusions can be drawn. But it is always instructive to
see how two search engines match up, even on a small data set.

The process we will follow is to issue a set of queries and to evaluate how closely the results of
the two search engines compare. We are comparing the results from the search engine to the results from Google.

Multiple Search Engine results have been provided in data with their Google results in separate json files.

## Query Comparison

[Bing](Data/BingQuery.txt) - [Google_Result1](Data/Google_Result1.json)\
[Yahoo!](Data/YahooQuery.txt) - [Google_Result2](Data/Google_Result2.json)\
[Ask](Data/AskQuery.txt) - [Google_Result3](Data/Google_Result3.json)\
[DuckDuckGo](Data/DDGQuery.txt) - [Google_Result4](Data/Google_Result4.json)

## Process

First we are crawling the webpages to search for queries using beautifulsoup. Done in [searchengine](searchengine.py) python file. This result is then compared with the Google search results which can be found in their respective json, which is done in [CompareSE](CompareSE.py) python file.
