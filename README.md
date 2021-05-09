# Search Engine Comparison 

We are comparing the search results from Google versus different search engines.
Many search engine comparison studies have been done. All of them use samples of data, some
small and some large, so no definitive conclusions can be drawn. But it is always instructive to
see how two search engines match up, even on a small data set.

The process we will follow is to issue a set of queries and to evaluate how closely the results of
the two search engines compare. We are comparing the results from the search engine to the results from Google.

Multiple Search Engine results have been provided in data with their Google results in separate json files.

## Query Comparison

Bing - Google_Result1\
Yahoo! - Google_Result2\
Ask - Google_Result3\
DuckDuckGo - Google_Result4

## Process

First we are crawling the webpages to search for queries using beautifulsoup. Done in searchengine.py. This result is then compared with the Google search results which can be found in their respective json, which is done in CompareSE.py.
