import datetime
import praw
import pymongo
import time

import config

client = pymongo.MongoClient(config.mdb_uri)
collection = client[config.db][config.collection]

reddit = praw.Reddit(
    client_id=config.reddit_client_id,
    client_secret=config.reddit_client_secret,
    user_agent=config.reddit_user_agent,
    username=config.reddit_username,
    password=config.reddit_password
    )

def post_to_document(post, subreddit):
    document = {}
    document['permalink'] = post.permalink
    document['created_utc'] = datetime.datetime.fromtimestamp(post.created_utc)
    document['locked'] = post.locked
    document['upvote_ratio'] = post.upvote_ratio
    document['title'] = post.title
    document['score'] = post.score
    document['subreddit'] = subreddit

    if not post.author:
        document['author'] = 'None'
    else:
        document['author'] = post.author.name

    if post.selftext == '':
        document['content_url'] = post.url
    else:
        document['selftext'] = post.selftext

    return document

def get_new(sub, limitn):
    posts = []
    for post in reddit.subreddit(sub).new(limit=limitn):
        posts.append(post_to_document(post, sub))
    return posts

def to_mdb(posts, collection):
    for post in posts:
            if collection.find_one({"permalink": post['permalink']}) == None:
                print(post['permalink'])
                print(collection.insert_one(post))


if __name__ == "__main__":
    print('Initializing reddit to mdb crawler.')
    subreddits = config.subreddits_most_popular + config.subreddits_other
    while True:
        for sr in subreddits:
            posts = get_new(sr, 25)
            to_mdb(posts, collection)
        time.sleep(10)
        print('Sleeping for 10 seconds')
