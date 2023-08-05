from transformers import pipeline
from fastapi import FastAPI

nlp = pipeline(task='sentiment-analysis',
               model='nlptown/bert-base-multilingual-uncased-sentiment')

app = FastAPI()

@app.get('/')
def get_root():
    return {'message':'Da la puntuación en estrellas a los comentarios'}
@app.get('/sentiment_analysis/')
async def query_sentiment_analysis(text: str):
    return analyze_sentiment(text)

def analyze_sentiment(text):
    """Get and process result"""
    result = nlp(text)
    sent = ''
    if (result[0]['label'] == '1 star'):
        sent = '1 estrella'
    elif(result[0]['label' == '2 stars']):
        sent = '2 estrellas'
    elif(result[0]['label'== '3 stars']):
        sent = '3 estrellas'
    elif(result[0]['label'=='4 stars']):
        sent = '4 estrellas'
    else:
        sent = '5 estrellas'
    prob = result[0]['score']
    # format and return results
    return{'sentiment': sent, 'probability':prob}