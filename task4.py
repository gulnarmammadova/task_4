from textblob import TextBlob
import matplotlib.pyplot as plt

reviews = [
    "I really like this product! It works perfectly and went beyond what I expected.",
    "The item came late and the quality was disappointing. Not happy with it.",
    "It's alright, neither great nor terrible.",
    "Fantastic! I would definitely recommend it to everyone.",
    "Awful experience, I want a refund.",
]

sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}

for review in reviews:
    blob = TextBlob(review)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        sentiment = "Positive"
    elif polarity < -0.1:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    sentiment_counts[sentiment] += 1

# Print the summary of sentiment analysis
total = len(reviews)
print("Summary of Sentiment Analysis:")
for sentiment, count in sentiment_counts.items():
    print(f"{sentiment}: {count} reviews ({count/total*100:.1f}%)")

# Plot the sentiment distribution as a bar chart
plt.bar(sentiment_counts.keys(), sentiment_counts.values(), color=['lightgreen', 'red', 'yellow'])
plt.title("Distribution of Sentiment in Reviews")
plt.ylabel("Number of Reviews")
plt.show()
