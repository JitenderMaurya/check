import requests
#from pydantic import BaseModel
import pdb
import json
from datetime import datetime
#class DescriptionRequest(BaseModel):
#    user_description: str

# Base URL of your FastAPI app
BASE_URL = "http://10.112.115.25:8000"  # Change this if your app is hosted elsewhere

proxies = {
    "http": None,
    "https": None
}

from typing import Dict, List
from datetime import datetime
from openai import OpenAI
import anthropic
import json
import httpx
import re
import logging
import pandas as pd
import numpy as np
# Get logger
logger = logging.getLogger(__name__)


description_payload = {
    "user_description":"I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model. I want to operate in both India, Dubai and London.",
}

time_period_from_user_description = requests.post(
    f"{BASE_URL}/get_time_period_from_user_description",
    json=description_payload,
    proxies=proxies
)

print("\nResponse from /time_period_from_user_description.....................")
print(time_period_from_user_description.text)


#Response from /get_time_period_from_user_description would look like this. You have to use this time information to initialize Time period.
# Input will be the initial user descriptions which user write himself.
#{"Start_Time":{"Month":"September","Year":"2025"},"End_Time":{"Month":"December","Year":"2025"}}
