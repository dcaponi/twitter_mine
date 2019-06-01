import json
import nltk
import re

from nltk.tokenize import word_tokenize

class Tokenizer:
    emoticons_str = r"""
        (?:
            [:=;] # Eyes
            [oO\-]? # Nose (optional)
            [D\)\]\(\]/\\OpP] # Mouth
        )"""
    
    regex_str = [
        emoticons_str,
        r'<[^>]+>', # HTML tags
        r'(?:@[\w_]+)', # @-mentions
        r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
        r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
    
        r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
        r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
        r'(?:[\w_]+)', # other words
        r'(?:\S)' # anything else
    ]

    def __init__(self):
        # TODO: Enable passing whatever other regexes may be required
        nltk.download('punkt')
        self.tokens_re = re.compile(r'('+'|'.join(self.regex_str)+')', re.VERBOSE | re.IGNORECASE)
        self.emoticon_re = re.compile(r'^'+self.emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

    def __tokenize_without_emoticons(self, s):
        return self.tokens_re.findall(s)
    
    def tokenize(self, s, lowercase=False):
        tokens = self.__tokenize_without_emoticons(s)
        if lowercase:
            tokens = [token if self.emoticon_re.search(token) else token.lower() for token in tokens]
        return tokens