from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "OwLim/indonesian-roberta-hate-speech-detection"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

def handleClassification(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=1)
    pred = torch.argmax(probs, dim=1).item()
    return 0 if pred == 0 else 1