import tweepy
import os
from dotenv import load_dotenv
from pprint import pprint, pformat
import psycopg2
import logging

logging.basicConfig(filename='tweet_api.log',
                    format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s ',
                    datefmt='%Y-%m-%d:%H:%M:%S', level=logging.DEBUG)
logger = logging.getLogger(__name__)

load_dotenv(verbose=True)
print("Application starting...")

consumer_key = ""
consumer_secret = ""
access_token = "1"
access_token_secret = ""
bearer_token = "AxDoI"
# hostname = "db"
username = ""
password = ""
port = "5432"
database = ""
hostname = ""


INSERT_SQL = ''' 
        INSERT INTO tweets (created_at, text, source, name, username, location, is_verified, description)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        '''

CREATE_SQL = '''
        create table tweets
( tweet_id SERIAL PRIMARY KEY,created_at varchar(1000), text varchar(3000),
source varchar(1000), name varchar(1000),
username varchar(1000), location varchar(100),is_verified varchar(100), description varchar(3000))
'''

query = "#covid19"
# Here we set up our search_query to fetch tweets with #covid19 but exclude retweets
tweet_search_query = "#covid19 lang:en -is:retweet"

# your start and end time for fetching tweets
start_time = "2022-07-15T00:00:00Z"
end_time = "2022-07-17T00:00:00Z"


connection = psycopg2.connect(user=username, password=password, host=hostname, port=port, database=database)
logger.info("Connection is created...")
cursor = connection.cursor()

logger.info("Cursor is created...")
try:
    cursor.execute(CREATE_SQL)
except Exception as e:
    logger.error(e)

client = tweepy.Client(bearer_token=bearer_token)

def search_tweet(tweet_search_query, start_time, end_time ):
    tweets = client.search_recent_tweets(query=tweet_search_query,
                                         start_time=start_time,
                                         end_time=end_time,
                                         tweet_fields=["created_at", "text", "source"],
                                         user_fields=["name", "username", "location", "verified", "description"],
                                         max_results=10,
                                         expansions='author_id'
                                     )
    return tweets

def get_nth_tweet(number):
    tweets = search_tweet(tweet_search_query, start_time, end_time)
    logger.info(len(tweets.data))
    return dict(tweets.data[number])

def get_user_of_the_nth_tweet(number):
    tweets = search_tweet(tweet_search_query, start_time, end_time)
    nth_tweet_user = tweets.includes["users"][number]
    logger.info(dict(nth_tweet_user))
    return dict(nth_tweet_user)

def create_the_dataset():
    tweets = search_tweet(tweet_search_query, start_time, end_time)
    # print(tweets.data)
    tweet_info_full = []
    for tweet, user in zip(tweets.data, tweets.includes['users']):
        tweet_info = {
            'created_at': tweet.created_at,
            'text': tweet.text,
            'source': tweet.source,
            'name': user.name,
            'username': user.username,
            'location': user.location,
            'verified': user.verified,
            'description': user.description
        }
        tweet_info_full.append(tweet_info)
    logger.info('All the tweet data has been fetched and list has been created...')
    return tweet_info_full

def insert(row):
    try:
        cursor.execute(INSERT_SQL, row)
        print(f"Insertion is done for the values...")
        logger.info("Insertion is done for the values...")
        print(str(row))
        logger.info(str(row))
        connection.commit()
    except Exception as error:
        print(str(row))
        connection.rollback()
        logger.error("Error while inserting to PostgreSQL", error)

def create_row_to_insert():
    all_tweets = create_the_dataset()
    for tweet in all_tweets:
        row = (tweet['created_at'], tweet['text'], tweet['source'], tweet['name'], tweet['username'], tweet['location'],
               tweet['verified'], tweet['description'])

        insert(row)
    return


if __name__ == '__main__':
    print("Application is starting...")
    logger.info('Application is starting...')

    # print("Which number of tweet do you want to see?")
    # x = int(input())
    # print(f'''Here is the {x}th user of the tweet {query} \n''')
    # get_user_of_the_nth_tweet(x)

    create_row_to_insert()
    logger.info('All the tweet data insertion has been completed...Application is shutting down...')
    cursor.close()
    connection.close()
    logger.info("PostgreSQL connection is closed")
    print("Application is Completed...")




print("Application stoping...")







