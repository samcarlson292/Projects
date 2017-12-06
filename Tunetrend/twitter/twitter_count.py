import argparse
from TwitterAPI import TwitterAPI, TwitterOAuth, TwitterRestPager, TwitterResponse
import datetime
from DB import DB, DB_NAME
from twython import Twython, TwythonError
import time

__author__ = "Jonas Geduldig"
__date__ = "December 7, 2012"
__license__ = "MIT"

COUNT = 100 # search download batch size
MAX_REQUESTS = 180

def count_old_tweets(api, word_list):
        words = ' AND '.join(word_list)
        print words
	flag = False
	db = DB(DB_NAME)
	con = db.connection()
	cur = db.cursor()

        count = 0
        today = datetime.date.today()
        one_day = datetime.timedelta(days=1)
        yesterday = today - one_day
        today_string = str(today)
        yesterday_string = str(yesterday)
        print 'Today: ', today
        print 'Yesterday: ', yesterday
        
	while True:
                r = api.request('search/tweets', {'q':words, 'count':COUNT})
		for item in r.get_iterator():
			if r.get_rest_quota()['remaining'] == 1:
				print "Wait 15 min"
				if flag:
                                        print 'Skipping'
                                        flag = False
                                        for i in range(0,14):
                                        	time.sleep(60)
                                        	print i
					return
				for i in range(0,14):
					time.sleep(60)
					print i, ' '
				print "Going again"
				flag = True

			if 'text' in item:
				full_time = item['created_at'].split()
                                tweet_date = '2015-04-'
                                tweet_date = tweet_date+full_time[2]
                                if tweet_date == yesterday_string:
                                        print 'Song: ',words,'Count: ', count, ' Date: ',yesterday
                                        cur.execute('Insert into twitter_info (song, song_id, collected_on) values (%s,%s,%s)',(words, count, yesterday))
					con.commit()
					yesterday = yesterday - one_day
					yesterday_string =  str(yesterday)
                                        count = 0
                                count += 1
                        elif 'message' in item:
                                if item['code'] == 131:
                                        continue # ignore internal server error
                                elif item['code'] == 88:
                                        print('Suspend search until %s' % search.get_quota()['reset'])
                                raise Exception('Message from twitter: %s' % item['message'])


def count_new_tweets(api, word_list):
        words = ','.join(word_list)
        count = 0
        total_skip = 0
        while True:
                skip = 0
                try:
                        r = api.request('statuses/filter', {'track':words})
                        while True:
                                for item in r.get_iterator():
                                        if 'text' in item:
                                                count += 1
                                                print(count + skip + total_skip)
                                        elif 'limit' in item:
                                                skip = item['limit'].get('track')
                                                #print('\n\n\n*** Skipping %d tweets\n\n\n' % (total_skip + skip))
                                        elif 'disconnect' in item:
                                                raise Exception('Disconnect: %s' % item['disconnect'].get('reason'))
                except Exception as e:
                        print('*** MUST RECONNECT %s' % e)
                total_skip += skip


if __name__ == '__main__':
        parser = argparse.ArgumentParser(description='Count occurance of word(s).')
        parser.add_argument('-past', action='store_true', help='search historic tweets')
        #parser.add_argument('-oauth', metavar='FILENAME', type=str, help='read OAuth credentials from file')
        parser.add_argument('words', metavar='W', type=str, nargs='+', help='word(s) to count the occurance of')
        args = parser.parse_args()

        #oauth = TwitterOAuth.read_file(args.oauth)
        api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
	twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
        try:
                if args.past:
                        count_old_tweets(api, args.words)
                else:
			count_new_tweets(api, args.words)
        except KeyboardInterrupt:
                print('\nTerminated by user\n')
        except Exception as e:
                print('*** STOPPED %s\n' % e)

