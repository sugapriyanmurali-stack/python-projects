text = input("Enter text: ").lower()

positive = ["good", "happy", "excellent"]
negative = ["bad", "sad", "poor"]

if any(word in text for word in positive):
    print("Positive Sentiment")
elif any(word in text for word in negative):
    print("Negative Sentiment")
else:
    print("Neutral Sentiment ")