# This program cleans and sorts Amazon reviews
# into sentiment category based on their authors
# star rating.
# Negative reviews are defined as < 3 stars.
# Positive reviews are defined as > 3 stars.
# ==============================================
# Author: Ray Blandford
# Date: 12.18.2017
# ==============================================
# Works Cited:
# The initial review data files were obtained
# from Julian McAuley.
# http://jmcauley.ucsd.edu/data/amazon/

import json
import gzip

# create parseable json file with data

def parse(path):
  g = gzip.open(path, 'r')
  for l in g:
    yield json.dumps(eval(l))

i = 0
f = open("./data/clean_review_data.txt", 'w')
f.write("{\"reviews\": [")
for l in parse("./data/reviews_Video_Games_5.json.gz"):
  if i < 99999:
    f.write(l + ',\n')
    i += 1
  elif i == 99999:
    f.write(l + '\n')
    i += 1
  else:
      break
f.write("]}")
f.close()

# Sort review text based on author's rating

with open("./data/clean_review_data.txt", 'r') as f:
  datastore = json.load(f)

pos_reviews = open("./data/pos_reviews.txt", 'w')
neg_reviews = open("./data/neg_reviews.txt", 'w')
for review in datastore["reviews"]:
  rating = review["overall"]
  review_text = review["reviewText"]
  if rating > 3:
    pos_reviews.write(review_text + '\n')
  if rating < 3:
    neg_reviews.write(review_text + '\n')

pos_reviews.close()
neg_reviews.close()

# Create equal sized positive and negative review data sets

with open("./data/clean_review_data.txt", 'r') as f:
  datastore = json.load(f)

pos_reviews_5000 = open("./data/pos_reviews_5k.txt", 'w')
neg_reviews_5000 = open("./data/neg_reviews_5k.txt", 'w')

pos = 0
neg = 0

for review in datastore["reviews"]:
  rating = review["overall"]
  review_text = review["reviewText"]
  if rating > 3 and pos < 5000:
    pos_reviews_5000.write(review_text + '\n')
    pos += 1
  if rating < 3 and neg < 5000:
    neg_reviews_5000.write(review_text + '\n')
    neg += 1

pos_reviews_5000.close()
neg_reviews_5000.close()
