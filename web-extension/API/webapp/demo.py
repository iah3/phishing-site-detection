from featureExtraction import UsefulFeatures
url = 'https://cash-fly.com'
url2 = 'art.com'

features = UsefulFeatures(url)
print(features.predict())