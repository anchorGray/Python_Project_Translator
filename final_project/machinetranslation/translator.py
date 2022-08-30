''' 
This is a translation module using IBM Watson Language Translator V3 
'''

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(text1):
    '''
    This translates english to french
    '''
    translationrun = language_translator.translate(
        text= text1,
        model_id= 'en-fr').get_result()
    print(json.dumps(translationrun, indent=2, ensure_ascii=False))
    return translationrun.get('translations')[0].get('translation')

def french_to_english(text1):
    '''
    This translates french to english
    '''
    translationrun = language_translator.translate(
        text= text1,
        model_id= 'fr-en').get_result()
    print(json.dumps(translationrun, indent=2, ensure_ascii=False))
    return translationrun.get('translations')[0].get('translation')
