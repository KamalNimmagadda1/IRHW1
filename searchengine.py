from bs4 import BeautifulSoup
import requests
from random import randint
import json
import time
from html.parser import HTMLParser

USER_AGENT = {'User-Agent':'Safari/15610.3.7.1.10'}


class SearchEngine:
    @staticmethod
    def search(query, sleep=True):
        if sleep:
            # Prevents loading too many pages too soon
            time.sleep(randint(10, 100))
        temp_url = '+'.join(query.split())  # for adding + between words for the query
        url = ' https://www.duckduckgo.com/html/?q=' + temp_url
        soup = BeautifulSoup(requests.get(url, headers=USER_AGENT).text, "html.parser")
        new_results = SearchEngine.scrape_search_result(soup)
        for res1 in new_results:
            print(res1)
        return new_results

    @staticmethod
    def scrape_search_result(soup):
        raw_results = soup.find_all("a", {"class": "result__a"})
        results = []
        # implement a check to get only 10 results and also check that URLs must not be duplicated
        for result in raw_results:
            link = result.get('href')[25:]
            results.append(str(requests.utils.unquote(link)))
            if len(results) == 10:
                break
        return results


if __name__ == "__main__":
    print("started")
    file = open('Data/DDGQuery.txt', 'r')
    queries = file.readlines()
    print("data read")
    res = {}
    i = 0
    for query in queries:
        i += 1
        print("Query", i)
        top10 = SearchEngine.search(query.strip())
        res[query.strip()] = top10
    file.close()

    print("Done")
    with open('hw1.json', 'w') as f:
        json.dump(res, f, indent=3)
        f.close()
