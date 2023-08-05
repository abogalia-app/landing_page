import requests

query={'text': 'la verdad no volvería a trabajar con este abogado, no lo recomiendo'}
response = requests.get('http://127.0.0.1:8000/sentiment_analysis/', params=query)
print(response.json())