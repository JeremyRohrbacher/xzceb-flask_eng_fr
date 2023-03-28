"""Module for python project"""
import json
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


load_dotenv()

#apikey = os.environ['apikey']
#url = os.environ['url']
APIKEY='mGXCIwRPr6tzcmZdn7a5UvgVo5XXZ2LfcFhi2Y7gjqGT'
URL='https://api.us-south.language-translator.watson.cloud.ibm.com/instances/ea45be82-7ad0-4e69-9b51-5be72616a894'
authenticator=IAMAuthenticator(APIKEY)

language_translator = LanguageTranslatorV3(version='2018-08-01',authenticator=authenticator)
language_translator.set_service_url(URL)

def english_to_french(english_text):
    #Watson API english to french
    """Watson API english to french"""
    french_text = language_translator.translate(text=english_text,model_id='en-fr').get_result()
    french_text = french_text.get("translations")[0].get("translation")
    return french_text

def french_to_english(french_text):
    #Watson API english to french
    """Watson API english to french"""
    english_text = language_translator.translate(text=french_text,model_id='fr-en').get_result()
    english_text = english_text.get("translations")[0].get("translation")
    return english_text
