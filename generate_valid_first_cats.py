from gensim.models.keyedvectors import KeyedVectors
wv = KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)

first_cats = ["Animals", "Pet_Supplies", "Apparel", "Accessories", "Arts", "Entertainment", "Baby", "Toddler", "Business", "Industrial", "Cameras", "Optics", "Electronics", "Food", "Beverages", "Tobacco", "Furniture", "Hardware", "Health", "Beauty", "Home", "Garden", "Luggage", "Bags", "Mature", "Media", "Office_Supplies", "Religious", "Ceremonial", "Software", "Sporting_Goods", "Toys", "Games","Vehicles", "Parts"]

for cat in first_cats:
  try:
    print(wv.word_vec(cat)[0])
  except KeyError:
    print('error!' + cat)

#=> ["Animals", "Pet_Supplies", "Apparel", "Accessories", "Arts", "Entertainment", "Baby", "Toddler", "Business", "Industrial", "Cameras", "Optics", "Electronics", "Food", "Beverages", "Tobacco", "Furniture", "Hardware", "Health", "Beauty", "Home", "Garden", "Luggage", "Bags", "Mature", "Media", "Supplies", "Religious", "Ceremonial", "Software", "Sporting_Goods", "Toys", "Games","Vehicles", "Parts"]
