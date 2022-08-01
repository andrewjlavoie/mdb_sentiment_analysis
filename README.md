# MongoDB for Sentiment Analysis on Social Media Posts
**Project Description**
This project utilizes Reddit's API to poll subreddits for new posts and continuously analyze text for sentiment, storing both raw data and metadata in a single MongoDB collection. The idea is to simulate three systems:
1. Operational Web Application: The reddit posts retrieved and stored can be similar to a multi-user single-view CRUD application.
2. Analytics Engine: System that continuously monitors the database for new entries, using change streams, and analyzes the post title and selftext for sentiment. These sentiment scores are then updated in their source MongoDB document.
3. Data Analyst: Jupyter Notebooks with analysis of JSON data.

# Features
- Flexbile Schema:
  - Multishaped Data: several different data schemas exist in the same collection to easily query and work with in data analysis.
  - Appended Data: the analytics engine adds the sentiment analysis to the original document without needing to make any changes to the database.
- Change Streams: Change streams allow applications to access real-time data changes without the complexity and risk of tailing the oplog, and immediately analyze for continuous analytics.
- Mongo Query Language and Aggregation Pipelines: 
  - A dataframe is commonly used in data analytics and the Python library Pandas. The dataframe is a row/column oriented data structure. The JSON document can be easily flattened with an aggregation pipeline to project important fields to the top level to readily convert into a dataframe.
  - Programmatically interact with the database: no need to translate from Python dictionary objects to MongoDB document or vice versa. Using the PyMongo supported driver to directly store and retrieve objects in native data structures.

# Requirements
- Python 3.9.7
  - pymongo==3.12
  - praw==7.6.0
  - nltk==3.6.5
- MongoDB Instance
- 

# Setup
1. Edit config.py accounts/settings
  - 
2. todo
# Steps
Running the project.
1.
