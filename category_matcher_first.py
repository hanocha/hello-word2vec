import sys
from gensim.models.keyedvectors import KeyedVectors

wv = KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)

first_cats = ["Animals", "Pet_Supplies", "Apparel", "Accessories", "Arts", "Entertainment", "Baby", "Toddler", "Business", "Industrial", "Cameras", "Optics", "Electronics", "Food", "Beverages", "Tobacco", "Furniture", "Hardware", "Health", "Beauty", "Home", "Garden", "Luggage", "Bags", "Mature", "Media", "Supplies", "Religious", "Ceremonial", "Software", "Sporting_Goods", "Toys", "Games","Vehicles", "Parts"]

inputted_word = sys.argv[1]

try:
  print(wv.most_similar_to_given(inputted_word, first_cats))
except:
  print('error!')
