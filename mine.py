import sys
from Twitter.TwitterMine import TwitterMine

if len(sys.argv) is 0:
    print("You must tell me the source to mine!")
else:
    if sys.argv[1].lower() == 'twitter':
        mine = TwitterMine()
        mine.start_stream(sys.argv[2:])
    else:
        print("Invalid mine source given")