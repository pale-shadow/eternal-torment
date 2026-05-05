import logging
import time

import requests
from bs4 import BeautifulSoup
from flatten_json import flatten


class Util:
    """Utility functions."""

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def flatten_json(y):
        out = {}

        def flatten(x, name=""):
            if type(x) is dict:
                for a in x:
                    flatten(x[a], name + a + "_")
            elif type(x) is list:
                i = 0
                for a in x:
                    flatten(a, name + str(i) + "_")
                    i += 1
            else:
                out[name[:-1]] = x

        flatten(y)
        return out

    def scrape_url(self, url):
        url = requests.get(url).text
        time.sleep(1)
        # self.logger.debug(f"Response file type: {type(url)}")
        print(f"Response file type: {type(url)}")
        # self.logger.debug(f"The length of the response file is: {len(url)}")
        print(f"The length of the response file is: {len(url)}")
        # self.logger.debug(f"Below are the first few lines of the response file: \n {url[:300]}")
        # print(f"Below are the first few lines of the response file: \n {url[:300]}")
        content = BeautifulSoup(url, "lxml")
        print(content.text)

        return content
        self.logger.debug(f"Response file type: {type(url)}")
        self.logger.debug(f"The length of the response file is: {len(url)}")
        self.logger.debug(
            f"Below are the first few lines of the response file: \n {url[:300]}"
        )

    def loadData(self, allurls):
        """ """
        allurlscsv = pd.read_csv(allurls, ",", error_bad_lines=False)  # reading file
        allurlsdata = pd.DataFrame(allurlscsv)  # converting to a dataframe

        allurlsdata = np.array(allurlsdata)  # converting it into an array
        random.shuffle(allurlsdata)  # shuffling
        return allurlsdata

    def getTokens(self, input):
        """ """
        tokensBySlash = str(input.encode("utf-8")).split(
            "/"
        )  # get tokens after splitting by slash
        allTokens = []
        for i in tokensBySlash:
            tokens = str(i).split("-")  # get tokens after splitting by dash
            tokensByDot = []
            for j in range(0, len(tokens)):
                tempTokens = str(tokens[j]).split(
                    "."
                )  # get tokens after splitting by dot
                tokensByDot = tokensByDot + tempTokens
            allTokens = allTokens + tokens + tokensByDot
        allTokens = list(set(allTokens))  # remove redundant tokens
        if "com" in allTokens:
            allTokens.remove(
                "com"
            )  # removing .com since it occurs a lot of times and it should not be included in our features
        return allTokens

    def vectorize(self, allurlsdata):
        """ """
        y = [d[1] for d in allurlsdata]  # all labels
        corpus = [
            d[0] for d in allurlsdata
        ]  # all urls corresponding to a label (either good or bad)
        vectorizer = TfidfVectorizer(
            tokenizer=getTokens
        )  # get a vector for each url but use our customized tokenizer
        X = vectorizer.fit_transform(corpus)  # get the X vector
