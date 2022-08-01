import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import pymongo
import pprint

import config

if __name__ == "__main__":
    client = pymongo.MongoClient(config.mdb_uri)
    collection = client[config.db][config.collection]

    change_stream = collection.watch()

    for change in change_stream:
        if change['operationType'] == 'insert':
            pprint.pprint(change)
            doc = change['fullDocument']
            updates = {}
            updates['title_score'] = SentimentIntensityAnalyzer().polarity_scores(doc['title'])
            if 'selftext' in doc:
                updates['self_score'] = SentimentIntensityAnalyzer().polarity_scores(doc['selftext'])
            crud = collection.update_one(
                {'_id': doc['_id']},
                {'$set': {'sentiment': updates}}
            )
            pprint.pprint(updates)
