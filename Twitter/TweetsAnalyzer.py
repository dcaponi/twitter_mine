from Tokenizer import Tokenizer

import json
import string

from collections import Counter

import nltk
from nltk.corpus import stopwords

class TweetsAnalyzer:
    nltk.download('stopwords')

    def __init__(self, filename, tokenizer):
        self.tokenizer = tokenizer
        self.count_terms = Counter()
        self.count_hts = Counter()
        self.count_mentions = Counter()

        punctuation = list(string.punctuation)
        stop = stopwords.words('english') + punctuation + ['rt', 'via', '…', '’', '“', '”', 'u', 'r', 'ur']

        with open(filename, 'r') as f:
            for line in f:
                tweet = json.loads(line) # load it as Python dict
                
                words = [
                    token for token in self.tokenizer.tokenize(tweet['text'], lowercase=True)
                    if token not in stop and
                    len(token) >= 3 and
                    not token.startswith(('#', '@'))
                ]

                hashtags = [
                    token for token in self.tokenizer.tokenize(tweet['text'])
                    if token.startswith('#')
                ]

                mentions = [
                    token for token in self.tokenizer.tokenize(tweet['text'])
                    if token.startswith('@')
                ]

                self.count_terms.update(words)
                self.count_hts.update(hashtags)
    
    def top_hashtags(self, n=5):
        return self.count_hts.most_common(n)
    
    def top_mentions(self, n=5):
        return self.count_mentions.most_common(n)

    def top_terms(self, n=5):
        return self.count_terms.most_common(n)