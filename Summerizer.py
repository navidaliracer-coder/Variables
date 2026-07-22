#In this hands-on activity, you'll build and explore an interactive command-line tool that leverages the Hugging Face API for text summarization. Participants will learn how to send HTTP requests, handle JSON responses, and customize summarization parameters such as minimum and maximum summary lengths. The tool also demonstrates integrating colorful terminal outputs using Colorama for enhanced user interaction. By the end of this exercise, you'll have a deeper understanding of how to build AI-powered applications that can transform large blocks of text into concise summaries, making it a practical introduction to working with modern AI APIs.

import requests

from config import Fore, Style, init

init (autoreset=True)

DEFAULT_MODEl = "google/pegasus-xsum"

def build_api_url(model_name):

    return f"https://api-inference.huggingface.co/models/{model_name}"


def query (payload, model_name=DEFAULT_MODEl):

    """
    
    Sends a POST request to the hugging face API using the specified model.
    
    
    """


    api_url = build_api_url(model_name)

    headers = {"Authorization": f"Bearer  {HF_API_KEY}"}

    response = requests.post(api_url, headers=headers, json=payload)

    return response.json()

def summerize_text(text, min_length, max_length, model_name=DEFAULT_MODEl):

    payload = {

        "inputs": text,

        "parameters": {"min_length": min_length, "max_length": max_length}

    }

    print(Fore.BLUE + Style.BRIGHT + f"\n???  Performing AI summization using model: {model_name}")


    result = query(payload, model_name=model_name)






