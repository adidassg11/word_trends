import bs4
from pprint import pprint
import requests


class WTException(Exception):
    pass


def get_urls():
    FRIENDS_URL = 'https://fangj.github.io/friends/'
    res = requests.get(FRIENDS_URL)

    if res.status_code != 200:
        raise WTException("Status code not OK for url {0}".format(FRIENDS_URL))

    print(res.text)
    soup = bs4.BeautifulSoup(res.text)
    for a in soup.find_all('a', href=True):
        print("Found the URL: {}".format(a['href']))

    return [FRIENDS_URL + path['href'] for path in soup.find_all('a', href=True)]


def get_word_frequency(url, word):
    print("getting words for {0}...".format(url))
    res = requests.get(url)
    count = res.text.lower().count(word.lower())
    print("Count: {0}".format(str(count)))
    return count


def chart_word_count(freqs):
    """ Assumes ordered list with frequencies """
    pass


if __name__ == "__main__":
    urls = get_urls()
    #pprint("Urls: {}".format(urls))
    pprint(urls)
    word = 'sex'
    freqs = []
    for url in urls:
        num_occurrences = get_word_frequency(url, word)
        freqs.append((url, num_occurrences))

    print(freqs)

    [pprint("url: {0} has {1} {2} times".format(url, word, num_occurrences)) for (url, num_occurrences) in freqs]

    #TODO - print chart