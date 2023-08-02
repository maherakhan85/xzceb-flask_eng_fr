"""
Language convertor
"""
import json
import os
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Receives a text in English and returns its French translation.
    """
    french_text = MyMemoryTranslator(source='en-GB', target ='fr-FR').translate(english_text)
    print(french_text)
    return french_text

def french_to_english(french_text):
    """
    Receives a text in French and returns its English translation.
    """
    english_text = MyMemoryTranslator(source = 'fr-FR', target = 'en-GB').translate(french_text)
    print(english_text)
    return english_text
