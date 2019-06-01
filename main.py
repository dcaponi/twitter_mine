from Tokenizer import Tokenizer
from Twitter.TweetsAnalyzer import TweetsAnalyzer

from FrequencyPlot import make_bar

tweets_analyzer = TweetsAnalyzer('Twitter/raw/tweets.json', Tokenizer())

terms, term_freq = zip(*tweets_analyzer.top_terms(20))
make_bar(terms, term_freq, 'terms_bar.json')

hashtags, ht_freq = zip(*tweets_analyzer.top_hashtags(20))
make_bar(hashtags, ht_freq, 'hashtag_bar.json')

# mentions, mention_freq = zip(*tweets_analyzer.top_mentions(20))
# make_bar(mentions, mention_freq, 'mentions_bar.json')