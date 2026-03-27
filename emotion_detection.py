import requests

def emotion_detector(text):
    url = "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/YOUR_API_KEY/v1/analyze?version=2021-08-01"
    
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "text": text,
        "features": {
            "emotion": {}
        }
    }

    response = requests.post(url, json=data, headers=headers)

    return response.json()

# Test
text = "I am very happy today!"
result = emotion_detector(text)

print(result)