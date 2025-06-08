# import requests  
# def emotion_detector(text_to_analyze):  
#     URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
#     myobj = { "raw_document": { "text": text_to_analyze } }
#     headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
#     response = requests.post(URL, json=myobj, headers=headers) 
#     return response.text  

# convert the response text into a dictionary using json library function
import requests  
import json  

def emotion_detector(text_to_analyze):  
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(URL, json=myobj, headers=headers) 
    result = json.loads(response.text)
    emotions = result['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    dominant_emotion = max(emotions, key=emotions.get)
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }



