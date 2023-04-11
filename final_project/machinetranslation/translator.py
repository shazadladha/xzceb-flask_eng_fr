import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
translator = LanguageTranslatorV3(version='2021-09-01', authenticator=authenticator)
translator.set_service_url(url)


def english_to_french(english_text):
    """
    This function translates english text to french text
    """
    if english_text is None:
        raise ValueError('text must be provided')
    else:
        translation = translator.translate(text=english_text, source='en', target='fr').get_result()
        french_text = translation['translations'][0]['translation']
        return french_text


def french_to_english(french_text):
    """
    This function translates french text to english text
    """
    if french_text is None:
        raise ValueError('text must be provided')
    else:
        translation = translator.translate(text=french_text, source='fr', target='en').get_result()
        english_text = translation['translations'][0]['translation']
        return english_text
'''
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
translator = ibm_watson.LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

translator.set_service_url(url)

def english_to_french(text):
    try:
        response = translator.translate(
            text=text,
            source='en',
            target='fr'
        ).get_result()
        french_text = response['translations'][0]['translation']
        return french_text
    except Exception as e:
        print("Exception occurred: {}".format(e))
        return ""

def french_to_english(text):
    try:
        response = translator.translate(
            text=text,
            source='fr',
            target='en'
        ).get_result()
        english_text = response['translations'][0]['translation']
        return english_text
    except Exception as e:
        print("Exception occurred: {}".format(e))
        return ""
        '''
