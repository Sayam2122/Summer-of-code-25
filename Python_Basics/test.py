from transformers import pipeline

classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=None)

text = "Tu pagal h kya"

results = classifier(text)[0]

emotion = max(results, key=lambda x: x['score'])

print(f"Emotion: {emotion['label']}")

