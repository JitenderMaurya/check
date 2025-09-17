import requests
#from pydantic import BaseModel
import pdb
import json
from datetime import datetime
#class DescriptionRequest(BaseModel):
#    user_description: str
from fastapi import HTTPException
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


client = anthropic.Anthropic(api_key="api03-MTJQgC3-5EaQ6vRqs4tSA3kmVeaeHcmmNS1nFkvQObj90QTwIkP3ZpdhHDA3_-Q8JJI8j1B45wW33DbQUZdelQ-iaeBJwAA", http_client=httpx.Client(verify=False))



# # def user_base_split_for_revenue_sources_with_cross_Selling(Revenue_sources_splits, cross_selling):

# #     prompt = f""" You are an expert in financial modeling, specializing in allocating user base percentages across various revenue streams. You have a deep understanding of revenue segmentation and cross-selling dynamics.
# #     You excel in splitting user base in percentage across various revenue streams provided in descriptions.
# #     we have information of user base split scross revenue streams provided in {Revenue_sources_splits}. You have more information about product cross selling. Your task now is to update user base split across various revenue streams and cross selling of product/services.
# #     Using the given revenue SKUS and its split in descriptions: {Revenue_sources_splits}

# #     Task
# #     - Update the user base distribution across revenue streams and cross-selling opportunities based on the provided descriptions. 
# #     - Update Revenue sources splits form the provided descriptions {Revenue_sources_splits} and cross selling informations {cross_selling}. If there is no clear cross selling information is provided return {Revenue_sources_splits} as it is. 
# #     - Ensure that the each revenue streams and cross selling items becomes the key in splits & provided user base is split.
# #     - If cross selling is **not happeining** or no information regarding cross selling is provided return {Revenue_sources_splits} as it is.
# #     - Make sure to return {Revenue_sources_splits} as-is when:
# #         a) Cross-selling information is not provided.
# #         b) Cross-selling information is unclear.
# #         c) Or there is no cross-selling involved.
# #     Output Requirement:
# #     - Respond splits in JSON format without any additional commentary.
# #     - Sum of split must be always 100
# #     - Determine the realistic Splits, considering industry benchmarks, competition, market demand, and affordability.

# #     Example output
# #         {{  "Splits": {{
# #             "SKU 1 (%)": "28",
# #             "SKU 2 (%)": "20",
# #             "SKU 3 (%)": "27", 
# #             "SKU 1 and SKU 2 (%)": 12,
# #             "SKU 1 and SKU 3 (%)": 13,           
# #         }},
# #         }}
# #     """

# #     try:
# #         response = client.messages.create(
# #             model="claude-3-7-sonnet-20250219",
# #             max_tokens=2048,
# #             messages=[{"role": "user", "content": prompt}]
# #         )

# #         # Check if the response is empty
# #         if not response.content:
# #             print(f"No content returned in user_base_split_for_revenue_sources_with_cross_Selling")
# #             return None

# #         # Ensure the response content is handled whether it's a list or a string
# #         if isinstance(response.content, list):
# #             # Access the actual text in the list of TextBlock objects
# #             response_text = response.content[0].text if response.content else None

# #         elif isinstance(response.content, str):
# #             response_text = response.content.strip()

# #         else:
# #             print(f"Unexpected response format in user_base_split_for_revenue_sources_with_cross_Selling")
# #             return None

# #         # Ensure the response content is a valid JSON string
# #         if not response_text or response_text == "":
# #             print(f"Empty or invalid response received in user_base_split_for_revenue_sources_with_cross_Selling")
# #             return None

# #         # Parse the response as JSON
# #         try:
# #             response_text = re.sub(r'```(json)?\n?', '', response_text)
# #             parsed_data = json.loads(response_text)         

# #             # Check if parsed data contains the required keys
# #             if 'Splits' not in parsed_data:
# #                 print(f"Missing expected keys in the response in user_base_split_for_revenue_sources_with_cross_Selling")
# #                 return None

# #             return {"Revenue splits":parsed_data["Splits"]}
# #         except json.JSONDecodeError as e:
# #             print(f"Error parsing JSON: {e}")
# #             return None

# #     except Exception as e:
# #         print(f"Error fetching or parsing response for user_base_split_for_revenue_sources_with_cross_Selling")
# #         return None 
    
# # Revenue_sources_splits = str({"Base Subscription (%)":45,"Premium Subscription (%)":35,"Executive Subscription (%)":15,"Extramile Subscription (%)":5})
# # cross_selling ="no"
# # output = user_base_split_for_revenue_sources_with_cross_Selling(Revenue_sources_splits, cross_selling)
# # print("Output",output)
# description_payload = {
#     "user_description":"I want to provide 4 types of LLM subscriptions service. which are base subscription, premium subscription, executive subscriptions and extramile subscriptions"
# }

# revenue_split_output = requests.post(
#     f"{BASE_URL}/revenue_splits",
#     json=description_payload,
#     proxies=proxies
# )

# print("\nResponse from /revenue_splits.....................")
# print(revenue_split_output.text)

# # #...................................................
# description_payload = {
#     "current_logic":revenue_split_output.text,
#     "user_input":"yes there would be cross selling between base subscription and premium subscription, premium subscription and executive subscriptions"
# }

# revenue_split_output_cross = requests.post(
#     f"{BASE_URL}/revenue_splits_with_cross_Selling",
#     json=description_payload,
#     proxies=proxies
# )

# print("\nResponse from /revenue_splits_with_cross_Selling.....................")
# print(revenue_split_output_cross.text)

# def get_time_period_from_description_prompt(user_description):
#     prompt =f"""
#     you are an expert in financial modeling. Your task is to determine the time period of the financial model from the descriptions. The time period have a Start_Time and End_Time.
#     from provided description: {user_description}, you need to be able extract Time period of the financial model.

#     ## Instructions
#     - if time period (like start year, start month, end year, end month) is not explictly told then retuen **""**    
#     - Make sure there is No additional commentry than the output in the example format.
#     Respond in JSON format

#     Example output

#         {{  "Start_Time": {{
#             "Month": "January",
#             "Year": "2024",       
#             }},
#             "End_Time": {{
#             "Month": "December",
#             "Year": "2025",       
#             }},
#         }}

#     """
#     return prompt
# def _get_time_period_from_description(description):
#     prompt = get_time_period_from_description_prompt(description)

#     try:
#         response_a = client.messages.create(
#             model="claude-sonnet-4-20250514",
#             max_tokens=1500,
#             messages=[{"role": "user", "content": prompt}]
#         )

#         # Check if the response is empty
#         if not response_a.content:
#             print(f"No content returned ")
#             return None

#         # Print the raw response content to inspect it
#         #print(f"building assumptions Raw Response Content: {response_a.content[0].text}")

#         # Ensure the response content is handled whether it's a list or a string
#         if isinstance(response_a.content, list):
#             # Access the actual text in the list of TextBlock objects
#             response_a_text = response_a.content[0].text if response_a.content else None
#             #print(f'the response Formula is {response_a_text}')
#         elif isinstance(response_a.content, str):
#             response_a_text = response_a.content.strip()
#             #print(f"response text if string {response_a_text}")
#         else:
#             print(f"Unexpected response format")
#             return None

#         # Ensure the response content is a valid JSON string
#         if not response_a_text or response_a_text == "":
#             print(f"Empty or invalid response received")
#             return None

#         # Parse the response as JSON
#         #pdb.set_trace()
#         try:
#             response_a_text = re.sub(r'```(json)?\n?', '', response_a_text)
#             parsed_a_data = json.loads(response_a_text)
#             #print(f"Parsed Data: {parsed_a_data}")            

#             # Check if parsed data contains the required keys
#             if 'Start_Time' not in parsed_a_data:
#                 print(f"Missing expected keys in the response")
#                 return None

#             return parsed_a_data
#         except json.JSONDecodeError as e:
#             print(f"Error parsing JSON: {e}")
#             return None

#     except Exception as e:
#         print(f"Error fetching or parsing response for sufficient user description provided")
#         return None   

# def get_time_period_from_description(user_description):
#     response = _get_time_period_from_description(user_description)

#     # Get current date and time
#     now = datetime.now()

#     # Get year month name
#     curr_month = now.strftime("%B")
#     curr_year = now.year

#     if response["Start_Time"]['Year']=='':
#         response["Start_Time"]['Year'] = str(curr_year)
#     if response["Start_Time"]['Month']=='':
#         if response["Start_Time"]['Year'] == str(curr_year):
#             response["Start_Time"]['Month'] = curr_month 
#         else:           
#             response["Start_Time"]['Month'] = "January"
#     if response["End_Time"]['Year']=='':
#         response["End_Time"]['Year'] = response["Start_Time"]['Year']
#     if response["End_Time"]['Month']=='':
#         response["End_Time"]['Month'] = 'December'
#     return response
# #user_description = "I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model, and want to have the model for 5 years straight, starting from 2026 January. I want to operate in both India, Dubai and London."
# user_description = "I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model, and want to have the model starting from 2025. I want to operate in both India, Dubai and London."
# response = get_time_period_from_description(user_description)


# print(response)

# description_payload = {
#     "user_description":"I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model. I want to operate in both India, Dubai and London.",
# }

# time_period_from_user_description = requests.post(
#     f"{BASE_URL}/get_time_period_from_user_description",
#     json=description_payload,
#     proxies=proxies
# )

# print("\nResponse from /time_period_from_user_description.....................")
# print(time_period_from_user_description.text)


#Response from /get_time_period_from_user_description would look like this. You have to use this time information to initialize Time period.
# Input will be the initial user descriptions which user write himself.
#{"Start_Time":{"Month":"September","Year":"2025"},"End_Time":{"Month":"December","Year":"2025"}}

def get_user_base_logic_intent_prompt(steps, user_request):
    prompt = f"""
    You are an intelligent financial market expert and intent classification agent.  A user have just read financial market user base logic steps and made a request. Your task is to classify the user's request into one of the following intents:
    - update_steps: if the user wants to modify/update, insert/add, or remove/delete something in the user base steps.
    - ask_question: if the user is asking a clear question about the user base steps or its steps/contents or about any variable.
    - unclear_or_other: if the input is vague, ambiguous, or doesn't clearly fit the above.

    ##Inputs
    financial market user base logic steps: {steps} 
    User Request: {user_request}
    - **update_steps**: The user wants to modify, add, insert, or delete something in the user base steps.
    - **ask_question**: The user is asking a clear question about the user base steps, variables, or meaning.
    - **unclear_or_other**: The request is vague, ambiguous, or does not clearly fit into the above categories.

    ## Instructions:
    - Return only one of the following values: `update_steps`, `ask_question`, or `unclear_or_other`.
    - Do **not** include any explanation or commentary, just return the intent in the format shown below.

    ### Examples:

    **User request**: "Can you help me with this?"  
    {{"Intent": "unclear_or_other"}}

    **User request**: "Remove the electric cycle component."  
    {{"Intent": "update_table"}}

    **User request**: "What does sample output mean?"  
    {{"Intent": "ask_question"}}

    ---
    Now classify the following user request:

    **User request**: "{user_request}"  
    {{""Intent"":??}}
    """
    return prompt

def get_user_base_intent(steps, user_request):
    """
    Parses the LLM response and returns a validated intent.
    Expected intents: 'update_steps', 'ask_question', 'unclear_or_other'
    """
    prompt = get_user_base_intent_prompt(steps, user_request)
    response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1500,
            messages=[{"role": "user", "content": prompt}]
        )
    valid_intents = {"update_steps", "ask_question", "unclear_or_other"}
    #print("Response-->",response.content[0].text)
    intent = json.loads(response.content[0].text)["Intent"].lower()

    # Validate intent
    if intent in valid_intents:
        return intent
    else:
        # Fallback if the response is unexpected
        return "unclear_or_other"

user_request = "What does you do?"
steps= ["Step 1: Analyze AI/LLM market across India, Dubai, and London to determine total addressable users in developer, enterprise, academic, and consumer segments","Step 2: Segment addressable market into four user categories aligned with LLM subscription tiers based on usage patterns and organizational requirements","Step 3: Apply regional adoption rates and AI penetration coefficients for realistic user acquisition estimates across target markets","Step 4: Adjust user base for competitive dynamics, market barriers, and regional preferences to determine market share capture probability","Step 5: Apply conversion rates and growth trajectories across subscription tiers to generate final user base projections per service level"]
obtained_intent = get_user_base_intent(steps, user_request)
print("obtained_intent--> ",obtained_intent)


# def answer_restructure_whole_prompt(user_description, qa_list):
#     prompt = f"""You are an expert in financial modelling and rewriting user responses into clear, well-structured language. Your task is to refine the all user's answer based on the provided context and question, without adding any new information.
#     There could be many question answers. So you rewrite all answers and concatenate all answer.
#     ### Context
#     Description: {user_description}

#     ### Task to refine answer
#     - Question Answer pairs: {qa_list}

#     ### Instructions
#     - Rewrite the answer in a clearer and more professional, explainatory way.
#     - Do not add, remove, or infer any information beyond what is already in the original answer.
#     - Return the result in **JSON format** using the following structure:
#     {{ 
#     "Answer": "Rewritten answer here"
#     }}"""
#     return prompt

# def answer_restructure_whole(user_description, ques_to_ans, answer):
    
#     # Validate input types
#     if not isinstance(user_description, str):
#         raise HTTPException(status_code=422, detail="Input 'user_description' must be a string.")
#     if not isinstance(ques_to_ans, list):
#         raise HTTPException(status_code=422, detail="Input 'ques_to_ans' must be a list.")
#     if not isinstance(answer, list):
#         raise HTTPException(status_code=422, detail="Input 'answer' must be a list.")

#     # Validate length consistency
#     num_no_answers = sum(1 for a in ques_to_ans if a.strip().lower() == "no")
#     if num_no_answers != len(answer):
#         raise HTTPException(
#             status_code=400,
#             detail=f"Mismatch: Number of 'No' responses in 'ques_to_ans' ({num_no_answers}) does not match length of 'answer' list ({len(answer)})."
#         )

#     # Original question list
#     Question_list =["How do you plan to have the calculation structured? (e.g., by country, by continent, or by product, by industry)","In which countries do you plan to operate?","What industry do you plan to operate in, and what products do you offer?","Are any expansions or entries being considered as part of the financial model, beyond core business operations highlighted in Question 3"]
#     filtered_questions = [q for q, a in zip(Question_list, ques_to_ans) if a.strip().lower() == "no"]
#     qa_list = [
#         f"Question {i+1}: {q}\nAnswer {i+1}: {a}\n"
#         for i, (q, a) in enumerate(zip(filtered_questions, answer))
#     ]
#     prompt = answer_restructure_whole_prompt(user_description, qa_list)

#     try:
#         response = client.messages.create(
#             model="claude-sonnet-4-20250514",
#             max_tokens=2048,
#             messages=[{"role": "user", "content": prompt}]
#         )

#         if not response.content or not response.content[0].text:
#             raise HTTPException(status_code=500, detail="No content returned from model.")

#         try:
#             rewritten = json.loads(response.content[0].text)
#             return {"Answer": rewritten.get("Answer", "")}
#         except json.JSONDecodeError:
#             raise HTTPException(status_code=500, detail="Failed to parse model response as JSON.")

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
    
# user_description = "I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model. I want to operate in both India, Dubai and London."
# ques_to_ans = ["No", "Yes", "Yes","No"]
# answer = ["Country", "Yes we planning to expand in Brazil"]
# final_ans = answer_restructure_whole(user_description, ques_to_ans, answer)
# print(final_ans)
