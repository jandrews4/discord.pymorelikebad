import google_trans_new
import requests
from google_trans_new import google_translator

translator = google_translator()
text = "lava los platos"

def translate(text):
    return(translator.translate(text, lang_tgt="en"))
