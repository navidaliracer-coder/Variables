from textblob import TextBlob

text = input("Enter how do you feel today? :")
Blob=TextBlob(text)
sentiment = blob.sentiment

print("Polarity", sentiment.polarity)

if sentiment.polarity>0:
    print("Positve!! =)")
elif sentiment.polarity<0:
    print("Negitive =( )")
else:
    print("Neutral")
    