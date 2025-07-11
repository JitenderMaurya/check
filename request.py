import requests
#from pydantic import BaseModel
import pdb
import json

#class DescriptionRequest(BaseModel):
#    user_description: str

# Base URL of your FastAPI app
BASE_URL = "http://10.112.115.25:8000"  # Change this if your app is hosted elsewhere

proxies = {
    "http": None,
    "https": None
}

'''

# Test /isSufficientUserDescription endpoint
description_payload = {
    "user_description": "I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model, and want to have the model for 5 years straight, starting from 2026 January. I want to operate in both India, Dubai and London"
}

description_response = requests.post(
    f"{BASE_URL}/isSufficientUserDescription",
    json=description_payload
)

print("\nResponse from /isSufficientUserDescription:")
print(description_response.text)

#OUTPUT-------->Response from /isSufficientUserDescription:
#{"Question 1":"Yes","Question 2":"Yes","Question 3":"Yes","Question 4":"No"}

# Test /isSufficientUserDescription endpoint
#@app.post('/restructure_user_description')
#async def restructure_user_description(description: StringSchema):
#    return restructure_user_description(description)

description_payload = {
    "user_description": "I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model, and want to have the model for 5 years straight, starting from 2026 January. I want to operate in both India, Dubai and London"}

description_response2 = requests.post(
    f"{BASE_URL}/restructure_user_description",
    json=description_payload
)

print("\nResponse from /restructure_user_description:")
print(description_response2.text)

#  update_financial_model............pay load
description_payload = {
    "current_logic":str({"financial_model_structure":{"1. Output": [ "1.1 Control Panel", "1.2 Financial Output"], "2. Financial_Statements" : ["2.1 Profit and Loss Statement", "2.2 Balance Sheet", "2.3 Cashflow Statement"], "3. Calculations" : ["3.1 User Base","3.2 Revenue","3.3 Cost","3.4 CapEx","3.5 Depreciation","3.6 Debt Financing"]}}),
    "user_input":"add a step 'overall display' in Output"
}

description_response3 = requests.post(
    f"{BASE_URL}/update_financial_model",
    json=description_payload
)

print("\nResponse from /update_financial_model")
print(description_response3.text)



#  User BAse logic...........pay load
description_payload = {
    "user_description":"I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model, and want to have the model for 5 years straight, starting from 2026 January. I want to operate in both India, Dubai and London",
    "user_base_start_month_init":"January",
    "user_base_end_month_init":"December",
    "user_base_year_init":"2025"
}

description_response4 = requests.post(
    f"{BASE_URL}/get_user_base_logic",
    json=description_payload
)

print("\nResponse from /get_user_base_logic")
print(description_response4.text)
#pdb.set_trace()


description_payload_time = {
    "interval":"halfyearly",
    "years":[2025, 2026, 2027],
    "start_month":"March",
    "end_month":"November"
}
description_response_time = requests.post(
    f"{BASE_URL}/get_time_info",
    json=description_payload_time)

print("\nResponse from /get_time_info")
print(description_response_time.text)



ub_logic =json.loads(description_response4.text)['user_base_logic']


#  Update User BAse logic...........pay load
description_payload = {
    "current_logic":ub_logic,
    "user_input":"Remove last steps",
    "user_description":"I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model, and want to have the model for 5 years straight, starting from 2026 January. I want to operate in both India, Dubai and London"
}

description_response5 = requests.post(
    f"{BASE_URL}/update_user_base_logic",
    json=description_payload
)

print("\nResponse from /update_user_base_logic")
print(description_response5.text)



#  Update User BAse assumption and formula ........pay load
description_payload = {
    "user_description":"I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model, and want to have the model for 5 years straight, starting from 2026 January. I want to operate in both India, Dubai and London",
    "User_Base_logic":ub_logic,
    "base_period":["January","December","2025"],
}



description_response6 = requests.post(
    f"{BASE_URL}/get_user_base_ass_formula",
    json=description_payload,
    proxies=proxies
)

print("\nResponse from /get_user_base_ass_formula")
print(description_response6.text)
#pdb.set_trace()
'''



assumptions= {"India_Total_Population":1400000000,"UAE_Total_Population":10000000,"UK_Total_Population":67000000,"India_Internet_Penetration (%)":45,"UAE_Internet_Penetration (%)":99,"UK_Internet_Penetration (%)":95,"India_High_Income_Share (%)":15,"India_Mid_Income_Share (%)":35,"India_Low_Income_Share (%)":50,"UAE_High_Income_Share (%)":40,"UAE_Mid_Income_Share (%)":45,"UAE_Low_Income_Share (%)":15,"UK_High_Income_Share (%)":30,"UK_Mid_Income_Share (%)":50,"UK_Low_Income_Share (%)":20,"High_Income_AI_Adoption_Rate (%)":25,"Mid_Income_AI_Adoption_Rate (%)":15,"Low_Income_AI_Adoption_Rate (%)":5,"India_Enterprise_Count":65000000,"UAE_Enterprise_Count":400000,"UK_Enterprise_Count":5700000,"Small_Enterprise_Share (%)":85,"Medium_Enterprise_Share (%)":12,"Large_Enterprise_Share (%)":3,"Small_Enterprise_AI_Adoption_Rate (%)":8,"Medium_Enterprise_AI_Adoption_Rate (%)":20,"Large_Enterprise_AI_Adoption_Rate (%)":45,"Average_Seats_Per_Small_Enterprise":5,"Average_Seats_Per_Medium_Enterprise":50,"Average_Seats_Per_Large_Enterprise":500,"India_Population_Growth_Rate (%)":2.3,"UAE_Population_Growth_Rate (%)":2.8,"UK_Population_Growth_Rate (%)":2.1,"India_Enterprise_Growth_Rate (%)":2.5,"UAE_Enterprise_Growth_Rate (%)":2.7,"UK_Enterprise_Growth_Rate (%)":2.2,"Indian_Subcontinent_High_Income_Market_Share (%)":5,"Indian_Subcontinent_Mid_Income_Market_Share (%)":3,"Indian_Subcontinent_Low_Income_Market_Share (%)":1,"Middle_East_Africa_High_Income_Market_Share (%)":12,"Middle_East_Africa_Mid_Income_Market_Share (%)":8,"Middle_East_Africa_Low_Income_Market_Share (%)":4,"UK_Europe_High_Income_Market_Share (%)":15,"UK_Europe_Mid_Income_Market_Share (%)":10,"UK_Europe_Low_Income_Market_Share (%)":6,"Indian_Subcontinent_Small_Enterprise_Market_Share (%)":2,"Indian_Subcontinent_Medium_Enterprise_Market_Share (%)":4,"Indian_Subcontinent_Large_Enterprise_Market_Share (%)":8,"Middle_East_Africa_Small_Enterprise_Market_Share (%)":6,"Middle_East_Africa_Medium_Enterprise_Market_Share (%)":10,"Middle_East_Africa_Large_Enterprise_Market_Share (%)":18,"UK_Europe_Small_Enterprise_Market_Share (%)":8,"UK_Europe_Medium_Enterprise_Market_Share (%)":12,"UK_Europe_Large_Enterprise_Market_Share (%)":22,"Indian_Subcontinent_High_Income_Churn_Rate (%)":15,"Indian_Subcontinent_Mid_Income_Churn_Rate (%)":12,"Indian_Subcontinent_Low_Income_Churn_Rate (%)":8,"Middle_East_Africa_High_Income_Churn_Rate (%)":18,"Middle_East_Africa_Mid_Income_Churn_Rate (%)":14,"Middle_East_Africa_Low_Income_Churn_Rate (%)":10,"UK_Europe_High_Income_Churn_Rate (%)":20,"UK_Europe_Mid_Income_Churn_Rate (%)":16,"UK_Europe_Low_Income_Churn_Rate (%)":12,"Indian_Subcontinent_Small_Enterprise_Churn_Rate (%)":10,"Indian_Subcontinent_Medium_Enterprise_Churn_Rate (%)":8,"Indian_Subcontinent_Large_Enterprise_Churn_Rate (%)":6,"Middle_East_Africa_Small_Enterprise_Churn_Rate (%)":12,"Middle_East_Africa_Medium_Enterprise_Churn_Rate (%)":10,"Middle_East_Africa_Large_Enterprise_Churn_Rate (%)":7,"UK_Europe_Small_Enterprise_Churn_Rate (%)":14,"UK_Europe_Medium_Enterprise_Churn_Rate (%)":11,"UK_Europe_Large_Enterprise_Churn_Rate (%)":8}#,
formula= {"Step 1: Identify the size of the population in scope":["Indian_Subcontinent_Internet_Users = India_Total_Population * India_Internet_Penetration / 100","Indian_Subcontinent_High_Income_AI_Adopters = Indian_Subcontinent_Internet_Users * India_High_Income_Share / 100 * High_Income_AI_Adoption_Rate / 100","Indian_Subcontinent_Mid_Income_AI_Adopters = Indian_Subcontinent_Internet_Users * India_Mid_Income_Share / 100 * Mid_Income_AI_Adoption_Rate / 100","Indian_Subcontinent_Low_Income_AI_Adopters = Indian_Subcontinent_Internet_Users * India_Low_Income_Share / 100 * Low_Income_AI_Adoption_Rate / 100","Middle_East_Africa_Internet_Users = UAE_Total_Population * UAE_Internet_Penetration / 100","Middle_East_Africa_High_Income_AI_Adopters = Middle_East_Africa_Internet_Users * UAE_High_Income_Share / 100 * High_Income_AI_Adoption_Rate / 100","Middle_East_Africa_Mid_Income_AI_Adopters = Middle_East_Africa_Internet_Users * UAE_Mid_Income_Share / 100 * Mid_Income_AI_Adoption_Rate / 100","Middle_East_Africa_Low_Income_AI_Adopters = Middle_East_Africa_Internet_Users * UAE_Low_Income_Share / 100 * Low_Income_AI_Adoption_Rate / 100","UK_Europe_Internet_Users = UK_Total_Population * UK_Internet_Penetration / 100","UK_Europe_High_Income_AI_Adopters = UK_Europe_Internet_Users * UK_High_Income_Share / 100 * High_Income_AI_Adoption_Rate / 100","UK_Europe_Mid_Income_AI_Adopters = UK_Europe_Internet_Users * UK_Mid_Income_Share / 100 * Mid_Income_AI_Adoption_Rate / 100","UK_Europe_Low_Income_AI_Adopters = UK_Europe_Internet_Users * UK_Low_Income_Share / 100 * Low_Income_AI_Adoption_Rate / 100","Indian_Subcontinent_Small_Enterprise_Seats = India_Enterprise_Count * Small_Enterprise_Share / 100 * Small_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Small_Enterprise","Indian_Subcontinent_Medium_Enterprise_Seats = India_Enterprise_Count * Medium_Enterprise_Share / 100 * Medium_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Medium_Enterprise","Indian_Subcontinent_Large_Enterprise_Seats = India_Enterprise_Count * Large_Enterprise_Share / 100 * Large_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Large_Enterprise","Middle_East_Africa_Small_Enterprise_Seats = UAE_Enterprise_Count * Small_Enterprise_Share / 100 * Small_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Small_Enterprise","Middle_East_Africa_Medium_Enterprise_Seats = UAE_Enterprise_Count * Medium_Enterprise_Share / 100 * Medium_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Medium_Enterprise","Middle_East_Africa_Large_Enterprise_Seats = UAE_Enterprise_Count * Large_Enterprise_Share / 100 * Large_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Large_Enterprise","UK_Europe_Small_Enterprise_Seats = UK_Enterprise_Count * Small_Enterprise_Share / 100 * Small_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Small_Enterprise","UK_Europe_Medium_Enterprise_Seats = UK_Enterprise_Count * Medium_Enterprise_Share / 100 * Medium_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Medium_Enterprise","UK_Europe_Large_Enterprise_Seats = UK_Enterprise_Count * Large_Enterprise_Share / 100 * Large_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Large_Enterprise"],"Step 2: Identify the growth rate of the segment":["Total_Indian_Subcontinent_High_Income_AI_Adopters = Indian_Subcontinent_High_Income_AI_Adopters * (1 + India_Population_Growth_Rate / 100)","Total_Indian_Subcontinent_Mid_Income_AI_Adopters = Indian_Subcontinent_Mid_Income_AI_Adopters * (1 + India_Population_Growth_Rate / 100)","Total_Indian_Subcontinent_Low_Income_AI_Adopters = Indian_Subcontinent_Low_Income_AI_Adopters * (1 + India_Population_Growth_Rate / 100)","Total_Middle_East_Africa_High_Income_AI_Adopters = Middle_East_Africa_High_Income_AI_Adopters * (1 + UAE_Population_Growth_Rate / 100)","Total_Middle_East_Africa_Mid_Income_AI_Adopters = Middle_East_Africa_Mid_Income_AI_Adopters * (1 + UAE_Population_Growth_Rate / 100)","Total_Middle_East_Africa_Low_Income_AI_Adopters = Middle_East_Africa_Low_Income_AI_Adopters * (1 + UAE_Population_Growth_Rate / 100)","Total_UK_Europe_High_Income_AI_Adopters = UK_Europe_High_Income_AI_Adopters * (1 + UK_Population_Growth_Rate / 100)","Total_UK_Europe_Mid_Income_AI_Adopters = UK_Europe_Mid_Income_AI_Adopters * (1 + UK_Population_Growth_Rate / 100)","Total_UK_Europe_Low_Income_AI_Adopters = UK_Europe_Low_Income_AI_Adopters * (1 + UK_Population_Growth_Rate / 100)","Total_Indian_Subcontinent_Small_Enterprise_Seats = Indian_Subcontinent_Small_Enterprise_Seats * (1 + India_Enterprise_Growth_Rate / 100)","Total_Indian_Subcontinent_Medium_Enterprise_Seats = Indian_Subcontinent_Medium_Enterprise_Seats * (1 + India_Enterprise_Growth_Rate / 100)","Total_Indian_Subcontinent_Large_Enterprise_Seats = Indian_Subcontinent_Large_Enterprise_Seats * (1 + India_Enterprise_Growth_Rate / 100)","Total_Middle_East_Africa_Small_Enterprise_Seats = Middle_East_Africa_Small_Enterprise_Seats * (1 + UAE_Enterprise_Growth_Rate / 100)","Total_Middle_East_Africa_Medium_Enterprise_Seats = Middle_East_Africa_Medium_Enterprise_Seats * (1 + UAE_Enterprise_Growth_Rate / 100)","Total_Middle_East_Africa_Large_Enterprise_Seats = Middle_East_Africa_Large_Enterprise_Seats * (1 + UAE_Enterprise_Growth_Rate / 100)","Total_UK_Europe_Small_Enterprise_Seats = UK_Europe_Small_Enterprise_Seats * (1 + UK_Enterprise_Growth_Rate / 100)","Total_UK_Europe_Medium_Enterprise_Seats = UK_Europe_Medium_Enterprise_Seats * (1 + UK_Enterprise_Growth_Rate / 100)","Total_UK_Europe_Large_Enterprise_Seats = UK_Europe_Large_Enterprise_Seats * (1 + UK_Enterprise_Growth_Rate / 100)"],"Step 3: Company market share":["Indian_Subcontinent_High_Income_Addressable_Market = Total_Indian_Subcontinent_High_Income_AI_Adopters * Indian_Subcontinent_High_Income_Market_Share / 100","Indian_Subcontinent_Mid_Income_Addressable_Market = Total_Indian_Subcontinent_Mid_Income_AI_Adopters * Indian_Subcontinent_Mid_Income_Market_Share / 100","Indian_Subcontinent_Low_Income_Addressable_Market = Total_Indian_Subcontinent_Low_Income_AI_Adopters * Indian_Subcontinent_Low_Income_Market_Share / 100","Middle_East_Africa_High_Income_Addressable_Market = Total_Middle_East_Africa_High_Income_AI_Adopters * Middle_East_Africa_High_Income_Market_Share / 100","Middle_East_Africa_Mid_Income_Addressable_Market = Total_Middle_East_Africa_Mid_Income_AI_Adopters * Middle_East_Africa_Mid_Income_Market_Share / 100","Middle_East_Africa_Low_Income_Addressable_Market = Total_Middle_East_Africa_Low_Income_AI_Adopters * Middle_East_Africa_Low_Income_Market_Share / 100","UK_Europe_High_Income_Addressable_Market = Total_UK_Europe_High_Income_AI_Adopters * UK_Europe_High_Income_Market_Share / 100","UK_Europe_Mid_Income_Addressable_Market = Total_UK_Europe_Mid_Income_AI_Adopters * UK_Europe_Mid_Income_Market_Share / 100","UK_Europe_Low_Income_Addressable_Market = Total_UK_Europe_Low_Income_AI_Adopters * UK_Europe_Low_Income_Market_Share / 100","Indian_Subcontinent_Small_Enterprise_Addressable_Seats = Total_Indian_Subcontinent_Small_Enterprise_Seats * Indian_Subcontinent_Small_Enterprise_Market_Share / 100","Indian_Subcontinent_Medium_Enterprise_Addressable_Seats = Total_Indian_Subcontinent_Medium_Enterprise_Seats * Indian_Subcontinent_Medium_Enterprise_Market_Share / 100","Indian_Subcontinent_Large_Enterprise_Addressable_Seats = Total_Indian_Subcontinent_Large_Enterprise_Seats * Indian_Subcontinent_Large_Enterprise_Market_Share / 100","Middle_East_Africa_Small_Enterprise_Addressable_Seats = Total_Middle_East_Africa_Small_Enterprise_Seats * Middle_East_Africa_Small_Enterprise_Market_Share / 100","Middle_East_Africa_Medium_Enterprise_Addressable_Seats = Total_Middle_East_Africa_Medium_Enterprise_Seats * Middle_East_Africa_Medium_Enterprise_Market_Share / 100","Middle_East_Africa_Large_Enterprise_Addressable_Seats = Total_Middle_East_Africa_Large_Enterprise_Seats * Middle_East_Africa_Large_Enterprise_Market_Share / 100","UK_Europe_Small_Enterprise_Addressable_Seats = Total_UK_Europe_Small_Enterprise_Seats * UK_Europe_Small_Enterprise_Market_Share / 100","UK_Europe_Medium_Enterprise_Addressable_Seats = Total_UK_Europe_Medium_Enterprise_Seats * UK_Europe_Medium_Enterprise_Market_Share / 100","UK_Europe_Large_Enterprise_Addressable_Seats = Total_UK_Europe_Large_Enterprise_Seats * UK_Europe_Large_Enterprise_Market_Share / 100"],"Step 4: Factor gains and losses of customers from and to competitors":["Indian_Subcontinent_High_Income_Churn = Indian_Subcontinent_High_Income_Addressable_Market * Indian_Subcontinent_High_Income_Churn_Rate / 100","Indian_Subcontinent_Mid_Income_Churn = Indian_Subcontinent_Mid_Income_Addressable_Market * Indian_Subcontinent_Mid_Income_Churn_Rate / 100","Indian_Subcontinent_Low_Income_Churn = Indian_Subcontinent_Low_Income_Addressable_Market * Indian_Subcontinent_Low_Income_Churn_Rate / 100","Middle_East_Africa_High_Income_Churn = Middle_East_Africa_High_Income_Addressable_Market * Middle_East_Africa_High_Income_Churn_Rate / 100","Middle_East_Africa_Mid_Income_Churn = Middle_East_Africa_Mid_Income_Addressable_Market * Middle_East_Africa_Mid_Income_Churn_Rate / 100","Middle_East_Africa_Low_Income_Churn = Middle_East_Africa_Low_Income_Addressable_Market * Middle_East_Africa_Low_Income_Churn_Rate / 100","UK_Europe_High_Income_Churn = UK_Europe_High_Income_Addressable_Market * UK_Europe_High_Income_Churn_Rate / 100","UK_Europe_Mid_Income_Churn = UK_Europe_Mid_Income_Addressable_Market * UK_Europe_Mid_Income_Churn_Rate / 100","UK_Europe_Low_Income_Churn = UK_Europe_Low_Income_Addressable_Market * UK_Europe_Low_Income_Churn_Rate / 100","Indian_Subcontinent_Small_Enterprise_Churn = Indian_Subcontinent_Small_Enterprise_Addressable_Seats * Indian_Subcontinent_Small_Enterprise_Churn_Rate / 100","Indian_Subcontinent_Medium_Enterprise_Churn = Indian_Subcontinent_Medium_Enterprise_Addressable_Seats * Indian_Subcontinent_Medium_Enterprise_Churn_Rate / 100","Indian_Subcontinent_Large_Enterprise_Churn = Indian_Subcontinent_Large_Enterprise_Addressable_Seats * Indian_Subcontinent_Large_Enterprise_Churn_Rate / 100","Middle_East_Africa_Small_Enterprise_Churn = Middle_East_Africa_Small_Enterprise_Addressable_Seats * Middle_East_Africa_Small_Enterprise_Churn_Rate / 100","Middle_East_Africa_Medium_Enterprise_Churn = Middle_East_Africa_Medium_Enterprise_Addressable_Seats * Middle_East_Africa_Medium_Enterprise_Churn_Rate / 100","Middle_East_Africa_Large_Enterprise_Churn = Middle_East_Africa_Large_Enterprise_Addressable_Seats * Middle_East_Africa_Large_Enterprise_Churn_Rate / 100","UK_Europe_Small_Enterprise_Churn = UK_Europe_Small_Enterprise_Addressable_Seats * UK_Europe_Small_Enterprise_Churn_Rate / 100","UK_Europe_Medium_Enterprise_Churn = UK_Europe_Medium_Enterprise_Addressable_Seats * UK_Europe_Medium_Enterprise_Churn_Rate / 100","UK_Europe_Large_Enterprise_Churn = UK_Europe_Large_Enterprise_Addressable_Seats * UK_Europe_Large_Enterprise_Churn_Rate / 100"],"Step 5: Total user base":["Indian_Subcontinent_High_Income_Users = Indian_Subcontinent_High_Income_Addressable_Market - Indian_Subcontinent_High_Income_Churn","Indian_Subcontinent_Mid_Income_Users = Indian_Subcontinent_Mid_Income_Addressable_Market - Indian_Subcontinent_Mid_Income_Churn","Indian_Subcontinent_Low_Income_Users = Indian_Subcontinent_Low_Income_Addressable_Market - Indian_Subcontinent_Low_Income_Churn","Middle_East_Africa_High_Income_Users = Middle_East_Africa_High_Income_Addressable_Market - Middle_East_Africa_High_Income_Churn","Middle_East_Africa_Mid_Income_Users = Middle_East_Africa_Mid_Income_Addressable_Market - Middle_East_Africa_Mid_Income_Churn","Middle_East_Africa_Low_Income_Users = Middle_East_Africa_Low_Income_Addressable_Market - Middle_East_Africa_Low_Income_Churn","UK_Europe_High_Income_Users = UK_Europe_High_Income_Addressable_Market - UK_Europe_High_Income_Churn","UK_Europe_Mid_Income_Users = UK_Europe_Mid_Income_Addressable_Market - UK_Europe_Mid_Income_Churn","UK_Europe_Low_Income_Users = UK_Europe_Low_Income_Addressable_Market - UK_Europe_Low_Income_Churn","Indian_Subcontinent_Small_Enterprise_Users = Indian_Subcontinent_Small_Enterprise_Addressable_Seats - Indian_Subcontinent_Small_Enterprise_Churn","Indian_Subcontinent_Medium_Enterprise_Users = Indian_Subcontinent_Medium_Enterprise_Addressable_Seats - Indian_Subcontinent_Medium_Enterprise_Churn","Indian_Subcontinent_Large_Enterprise_Users = Indian_Subcontinent_Large_Enterprise_Addressable_Seats - Indian_Subcontinent_Large_Enterprise_Churn","Middle_East_Africa_Small_Enterprise_Users = Middle_East_Africa_Small_Enterprise_Addressable_Seats - Middle_East_Africa_Small_Enterprise_Churn","Middle_East_Africa_Medium_Enterprise_Users = Middle_East_Africa_Medium_Enterprise_Addressable_Seats - Middle_East_Africa_Medium_Enterprise_Churn","Middle_East_Africa_Large_Enterprise_Users = Middle_East_Africa_Large_Enterprise_Addressable_Seats - Middle_East_Africa_Large_Enterprise_Churn","UK_Europe_Small_Enterprise_Users = UK_Europe_Small_Enterprise_Addressable_Seats - UK_Europe_Small_Enterprise_Churn","UK_Europe_Medium_Enterprise_Users = UK_Europe_Medium_Enterprise_Addressable_Seats - UK_Europe_Medium_Enterprise_Churn","UK_Europe_Large_Enterprise_Users = UK_Europe_Large_Enterprise_Addressable_Seats - UK_Europe_Large_Enterprise_Churn","Total_User_Base = Indian_Subcontinent_High_Income_Users + Indian_Subcontinent_Mid_Income_Users + Indian_Subcontinent_Low_Income_Users + Middle_East_Africa_High_Income_Users + Middle_East_Africa_Mid_Income_Users + Middle_East_Africa_Low_Income_Users + UK_Europe_High_Income_Users + UK_Europe_Mid_Income_Users + UK_Europe_Low_Income_Users + Indian_Subcontinent_Small_Enterprise_Users + Indian_Subcontinent_Medium_Enterprise_Users + Indian_Subcontinent_Large_Enterprise_Users + Middle_East_Africa_Small_Enterprise_Users + Middle_East_Africa_Medium_Enterprise_Users + Middle_East_Africa_Large_Enterprise_Users + UK_Europe_Small_Enterprise_Users + UK_Europe_Medium_Enterprise_Users + UK_Europe_Large_Enterprise_Users"]}
assumptions={
        "India_Total_Population": 1400000000,
        "UAE_Total_Population": 10000000,
        "UK_Total_Population": 67000000,
        "India_Internet_Penetration (%)": 50,
        "UAE_Internet_Penetration (%)": 95,
        "UK_Internet_Penetration (%)": 95,
        "India_High_Income_Share (%)": 15,
        "India_Mid_Income_Share (%)": 35,
        "India_Low_Income_Share (%)": 50,
        "UAE_High_Income_Share (%)": 45,
        "UAE_Mid_Income_Share (%)": 40,
        "UAE_Low_Income_Share (%)": 15,
        "UK_High_Income_Share (%)": 30,
        "UK_Mid_Income_Share (%)": 55,
        "UK_Low_Income_Share (%)": 15,
        "High_Income_AI_Adoption (%)": 25,
        "Mid_Income_AI_Adoption (%)": 15,
        "Low_Income_AI_Adoption (%)": 5,
        "India_Enterprise_Count": 75000000,
        "UAE_Enterprise_Count": 500000,
        "UK_Enterprise_Count": 5500000,
        "Small_Enterprise_Share (%)": 70,
        "Medium_Enterprise_Share (%)": 25,
        "Large_Enterprise_Share (%)": 5,
        "Small_Enterprise_AI_Adoption (%)": 10,
        "Medium_Enterprise_AI_Adoption (%)": 35,
        "Large_Enterprise_AI_Adoption (%)": 60,
        "Small_Enterprise_Avg_Seats": 5,
        "Medium_Enterprise_Avg_Seats": 50,
        "Large_Enterprise_Avg_Seats": 500,
        "Population_Growth_Rate_Indian_Subcontinent (%)": 2.5,
        "Population_Growth_Rate_Middle_East_and_Africa (%)": 2.8,
        "Population_Growth_Rate_UK_and_Europe (%)": 2.2,
        "Enterprise_Growth_Rate_Indian_Subcontinent (%)": 3.0,
        "Enterprise_Growth_Rate_Middle_East_and_Africa (%)": 2.7,
        "Enterprise_Growth_Rate_UK_and_Europe (%)": 2.3,
        "Indian_Subcontinent_High_Income_Individual_Market_Share (%)": 0.5,
        "Indian_Subcontinent_Mid_Income_Individual_Market_Share (%)": 0.3,
        "Indian_Subcontinent_Low_Income_Individual_Market_Share (%)": 0.1,
        "Middle_East_and_Africa_High_Income_Individual_Market_Share (%)": 2.0,
        "Middle_East_and_Africa_Mid_Income_Individual_Market_Share (%)": 1.5,
        "Middle_East_and_Africa_Low_Income_Individual_Market_Share (%)": 0.8,
        "UK_and_Europe_High_Income_Individual_Market_Share (%)": 3.0,
        "UK_and_Europe_Mid_Income_Individual_Market_Share (%)": 2.5,
        "UK_and_Europe_Low_Income_Individual_Market_Share (%)": 1.0,
        "Indian_Subcontinent_Small_Enterprise_Market_Share (%)": 0.3,
        "Indian_Subcontinent_Medium_Enterprise_Market_Share (%)": 0.8,
        "Indian_Subcontinent_Large_Enterprise_Market_Share (%)": 2.0,
        "Middle_East_and_Africa_Small_Enterprise_Market_Share (%)": 1.2,
        "Middle_East_and_Africa_Medium_Enterprise_Market_Share (%)": 2.5,
        "Middle_East_and_Africa_Large_Enterprise_Market_Share (%)": 5.0,
        "UK_and_Europe_Small_Enterprise_Market_Share (%)": 2.0,
        "UK_and_Europe_Medium_Enterprise_Market_Share (%)": 4.0,
        "UK_and_Europe_Large_Enterprise_Market_Share (%)": 8.0,
        "Indian_Subcontinent_High_Income_Individual_Churn (%)": 8,
        "Indian_Subcontinent_Mid_Income_Individual_Churn (%)": 12,
        "Indian_Subcontinent_Low_Income_Individual_Churn (%)": 15,
        "Middle_East_and_Africa_High_Income_Individual_Churn (%)": 6,
        "Middle_East_and_Africa_Mid_Income_Individual_Churn (%)": 10,
        "Middle_East_and_Africa_Low_Income_Individual_Churn (%)": 12,
        "UK_and_Europe_High_Income_Individual_Churn (%)": 5,
        "UK_and_Europe_Mid_Income_Individual_Churn (%)": 8,
        "UK_and_Europe_Low_Income_Individual_Churn (%)": 10,
        "Indian_Subcontinent_Small_Enterprise_Churn (%)": 18,
        "Indian_Subcontinent_Medium_Enterprise_Churn (%)": 12,
        "Indian_Subcontinent_Large_Enterprise_Churn (%)": 8,
        "Middle_East_and_Africa_Small_Enterprise_Churn (%)": 15,
        "Middle_East_and_Africa_Medium_Enterprise_Churn (%)": 10,
        "Middle_East_and_Africa_Large_Enterprise_Churn (%)": 6,
        "UK_and_Europe_Small_Enterprise_Churn (%)": 12,
        "UK_and_Europe_Medium_Enterprise_Churn (%)": 8,
        "UK_and_Europe_Large_Enterprise_Churn (%)": 5
    }

formula = {
        "Step 1: Identify the size of the population in scope": [
            "India_Internet_Users = India_Total_Population * India_Internet_Penetration / 100",
            "UAE_Internet_Users = UAE_Total_Population * UAE_Internet_Penetration / 100",
            "UK_Internet_Users = UK_Total_Population * UK_Internet_Penetration / 100",
            "Indian_Subcontinent_High_Income_Individual_Adopters = India_Internet_Users * India_High_Income_Share / 100 * High_Income_AI_Adoption / 100",
            "Indian_Subcontinent_Mid_Income_Individual_Adopters = India_Internet_Users * India_Mid_Income_Share / 100 * Mid_Income_AI_Adoption / 100",
            "Indian_Subcontinent_Low_Income_Individual_Adopters = India_Internet_Users * India_Low_Income_Share / 100 * Low_Income_AI_Adoption / 100",
            "Middle_East_and_Africa_High_Income_Individual_Adopters = UAE_Internet_Users * UAE_High_Income_Share / 100 * High_Income_AI_Adoption / 100",
            "Middle_East_and_Africa_Mid_Income_Individual_Adopters = UAE_Internet_Users * UAE_Mid_Income_Share / 100 * Mid_Income_AI_Adoption / 100",
            "Middle_East_and_Africa_Low_Income_Individual_Adopters = UAE_Internet_Users * UAE_Low_Income_Share / 100 * Low_Income_AI_Adoption / 100",
            "UK_and_Europe_High_Income_Individual_Adopters = UK_Internet_Users * UK_High_Income_Share / 100 * High_Income_AI_Adoption / 100",
            "UK_and_Europe_Mid_Income_Individual_Adopters = UK_Internet_Users * UK_Mid_Income_Share / 100 * Mid_Income_AI_Adoption / 100",
            "UK_and_Europe_Low_Income_Individual_Adopters = UK_Internet_Users * UK_Low_Income_Share / 100 * Low_Income_AI_Adoption / 100",
            "Indian_Subcontinent_Small_Enterprise_Seats = India_Enterprise_Count * Small_Enterprise_Share / 100 * Small_Enterprise_AI_Adoption / 100 * Small_Enterprise_Avg_Seats",
            "Indian_Subcontinent_Medium_Enterprise_Seats = India_Enterprise_Count * Medium_Enterprise_Share / 100 * Medium_Enterprise_AI_Adoption / 100 * Medium_Enterprise_Avg_Seats",
            "Indian_Subcontinent_Large_Enterprise_Seats = India_Enterprise_Count * Large_Enterprise_Share / 100 * Large_Enterprise_AI_Adoption / 100 * Large_Enterprise_Avg_Seats",
            "Middle_East_and_Africa_Small_Enterprise_Seats = UAE_Enterprise_Count * Small_Enterprise_Share / 100 * Small_Enterprise_AI_Adoption / 100 * Small_Enterprise_Avg_Seats",
            "Middle_East_and_Africa_Medium_Enterprise_Seats = UAE_Enterprise_Count * Medium_Enterprise_Share / 100 * Medium_Enterprise_AI_Adoption / 100 * Medium_Enterprise_Avg_Seats",
            "Middle_East_and_Africa_Large_Enterprise_Seats = UAE_Enterprise_Count * Large_Enterprise_Share / 100 * Large_Enterprise_AI_Adoption / 100 * Large_Enterprise_Avg_Seats",
            "UK_and_Europe_Small_Enterprise_Seats = UK_Enterprise_Count * Small_Enterprise_Share / 100 * Small_Enterprise_AI_Adoption / 100 * Small_Enterprise_Avg_Seats",
            "UK_and_Europe_Medium_Enterprise_Seats = UK_Enterprise_Count * Medium_Enterprise_Share / 100 * Medium_Enterprise_AI_Adoption / 100 * Medium_Enterprise_Avg_Seats",
            "UK_and_Europe_Large_Enterprise_Seats = UK_Enterprise_Count * Large_Enterprise_Share / 100 * Large_Enterprise_AI_Adoption / 100 * Large_Enterprise_Avg_Seats"
        ],
        "Step 2: Identify the growth rate of the segment": [
            "Total_Indian_Subcontinent_High_Income_Individual_Adopters = Indian_Subcontinent_High_Income_Individual_Adopters * (1 + Population_Growth_Rate_Indian_Subcontinent / 100)",
            "Total_Indian_Subcontinent_Mid_Income_Individual_Adopters = Indian_Subcontinent_Mid_Income_Individual_Adopters * (1 + Population_Growth_Rate_Indian_Subcontinent / 100)",
            "Total_Indian_Subcontinent_Low_Income_Individual_Adopters = Indian_Subcontinent_Low_Income_Individual_Adopters * (1 + Population_Growth_Rate_Indian_Subcontinent / 100)",
            "Total_Middle_East_and_Africa_High_Income_Individual_Adopters = Middle_East_and_Africa_High_Income_Individual_Adopters * (1 + Population_Growth_Rate_Middle_East_and_Africa / 100)",
            "Total_Middle_East_and_Africa_Mid_Income_Individual_Adopters = Middle_East_and_Africa_Mid_Income_Individual_Adopters * (1 + Population_Growth_Rate_Middle_East_and_Africa / 100)",
            "Total_Middle_East_and_Africa_Low_Income_Individual_Adopters = Middle_East_and_Africa_Low_Income_Individual_Adopters * (1 + Population_Growth_Rate_Middle_East_and_Africa / 100)",
            "Total_UK_and_Europe_High_Income_Individual_Adopters = UK_and_Europe_High_Income_Individual_Adopters * (1 + Population_Growth_Rate_UK_and_Europe / 100)",
            "Total_UK_and_Europe_Mid_Income_Individual_Adopters = UK_and_Europe_Mid_Income_Individual_Adopters * (1 + Population_Growth_Rate_UK_and_Europe / 100)",
            "Total_UK_and_Europe_Low_Income_Individual_Adopters = UK_and_Europe_Low_Income_Individual_Adopters * (1 + Population_Growth_Rate_UK_and_Europe / 100)",
            "Total_Indian_Subcontinent_Small_Enterprise_Seats = Indian_Subcontinent_Small_Enterprise_Seats * (1 + Enterprise_Growth_Rate_Indian_Subcontinent / 100)",
            "Total_Indian_Subcontinent_Medium_Enterprise_Seats = Indian_Subcontinent_Medium_Enterprise_Seats * (1 + Enterprise_Growth_Rate_Indian_Subcontinent / 100)",
            "Total_Indian_Subcontinent_Large_Enterprise_Seats = Indian_Subcontinent_Large_Enterprise_Seats * (1 + Enterprise_Growth_Rate_Indian_Subcontinent / 100)",
            "Total_Middle_East_and_Africa_Small_Enterprise_Seats = Middle_East_and_Africa_Small_Enterprise_Seats * (1 + Enterprise_Growth_Rate_Middle_East_and_Africa / 100)",
            "Total_Middle_East_and_Africa_Medium_Enterprise_Seats = Middle_East_and_Africa_Medium_Enterprise_Seats * (1 + Enterprise_Growth_Rate_Middle_East_and_Africa / 100)",
            "Total_Middle_East_and_Africa_Large_Enterprise_Seats = Middle_East_and_Africa_Large_Enterprise_Seats * (1 + Enterprise_Growth_Rate_Middle_East_and_Africa / 100)",
            "Total_UK_and_Europe_Small_Enterprise_Seats = UK_and_Europe_Small_Enterprise_Seats * (1 + Enterprise_Growth_Rate_UK_and_Europe / 100)",
            "Total_UK_and_Europe_Medium_Enterprise_Seats = UK_and_Europe_Medium_Enterprise_Seats * (1 + Enterprise_Growth_Rate_UK_and_Europe / 100)",
            "Total_UK_and_Europe_Large_Enterprise_Seats = UK_and_Europe_Large_Enterprise_Seats * (1 + Enterprise_Growth_Rate_UK_and_Europe / 100)"
        ],
        "Step 3: Company market share": [
            "Indian_Subcontinent_High_Income_Individual_Addressable_Market = Total_Indian_Subcontinent_High_Income_Individual_Adopters * Indian_Subcontinent_High_Income_Individual_Market_Share / 100",
            "Indian_Subcontinent_Mid_Income_Individual_Addressable_Market = Total_Indian_Subcontinent_Mid_Income_Individual_Adopters * Indian_Subcontinent_Mid_Income_Individual_Market_Share / 100",
            "Indian_Subcontinent_Low_Income_Individual_Addressable_Market = Total_Indian_Subcontinent_Low_Income_Individual_Adopters * Indian_Subcontinent_Low_Income_Individual_Market_Share / 100",
            "Middle_East_and_Africa_High_Income_Individual_Addressable_Market = Total_Middle_East_and_Africa_High_Income_Individual_Adopters * Middle_East_and_Africa_High_Income_Individual_Market_Share / 100",
            "Middle_East_and_Africa_Mid_Income_Individual_Addressable_Market = Total_Middle_East_and_Africa_Mid_Income_Individual_Adopters * Middle_East_and_Africa_Mid_Income_Individual_Market_Share / 100",
            "Middle_East_and_Africa_Low_Income_Individual_Addressable_Market = Total_Middle_East_and_Africa_Low_Income_Individual_Adopters * Middle_East_and_Africa_Low_Income_Individual_Market_Share / 100",
            "UK_and_Europe_High_Income_Individual_Addressable_Market = Total_UK_and_Europe_High_Income_Individual_Adopters * UK_and_Europe_High_Income_Individual_Market_Share / 100",
            "UK_and_Europe_Mid_Income_Individual_Addressable_Market = Total_UK_and_Europe_Mid_Income_Individual_Adopters * UK_and_Europe_Mid_Income_Individual_Market_Share / 100",
            "UK_and_Europe_Low_Income_Individual_Addressable_Market = Total_UK_and_Europe_Low_Income_Individual_Adopters * UK_and_Europe_Low_Income_Individual_Market_Share / 100",
            "Indian_Subcontinent_Small_Enterprise_Addressable_Market = Total_Indian_Subcontinent_Small_Enterprise_Seats * Indian_Subcontinent_Small_Enterprise_Market_Share / 100",
            "Indian_Subcontinent_Medium_Enterprise_Addressable_Market = Total_Indian_Subcontinent_Medium_Enterprise_Seats * Indian_Subcontinent_Medium_Enterprise_Market_Share / 100",
            "Indian_Subcontinent_Large_Enterprise_Addressable_Market = Total_Indian_Subcontinent_Large_Enterprise_Seats * Indian_Subcontinent_Large_Enterprise_Market_Share / 100",
            "Middle_East_and_Africa_Small_Enterprise_Addressable_Market = Total_Middle_East_and_Africa_Small_Enterprise_Seats * Middle_East_and_Africa_Small_Enterprise_Market_Share / 100",
            "Middle_East_and_Africa_Medium_Enterprise_Addressable_Market = Total_Middle_East_and_Africa_Medium_Enterprise_Seats * Middle_East_and_Africa_Medium_Enterprise_Market_Share / 100",
            "Middle_East_and_Africa_Large_Enterprise_Addressable_Market = Total_Middle_East_and_Africa_Large_Enterprise_Seats * Middle_East_and_Africa_Large_Enterprise_Market_Share / 100",
            "UK_and_Europe_Small_Enterprise_Addressable_Market = Total_UK_and_Europe_Small_Enterprise_Seats * UK_and_Europe_Small_Enterprise_Market_Share / 100",
            "UK_and_Europe_Medium_Enterprise_Addressable_Market = Total_UK_and_Europe_Medium_Enterprise_Seats * UK_and_Europe_Medium_Enterprise_Market_Share / 100",
            "UK_and_Europe_Large_Enterprise_Addressable_Market = Total_UK_and_Europe_Large_Enterprise_Seats * UK_and_Europe_Large_Enterprise_Market_Share / 100"
        ],
        "Step 4: Factor gains and losses of customers from and to competitors": [
            "Indian_Subcontinent_High_Income_Individual_Churn_Loss = Indian_Subcontinent_High_Income_Individual_Addressable_Market * Indian_Subcontinent_High_Income_Individual_Churn / 100",
            "Indian_Subcontinent_Mid_Income_Individual_Churn_Loss = Indian_Subcontinent_Mid_Income_Individual_Addressable_Market * Indian_Subcontinent_Mid_Income_Individual_Churn / 100",
            "Indian_Subcontinent_Low_Income_Individual_Churn_Loss = Indian_Subcontinent_Low_Income_Individual_Addressable_Market * Indian_Subcontinent_Low_Income_Individual_Churn / 100",
            "Middle_East_and_Africa_High_Income_Individual_Churn_Loss = Middle_East_and_Africa_High_Income_Individual_Addressable_Market * Middle_East_and_Africa_High_Income_Individual_Churn / 100",
            "Middle_East_and_Africa_Mid_Income_Individual_Churn_Loss = Middle_East_and_Africa_Mid_Income_Individual_Addressable_Market * Middle_East_and_Africa_Mid_Income_Individual_Churn / 100",
            "Middle_East_and_Africa_Low_Income_Individual_Churn_Loss = Middle_East_and_Africa_Low_Income_Individual_Addressable_Market * Middle_East_and_Africa_Low_Income_Individual_Churn / 100",
            "UK_and_Europe_High_Income_Individual_Churn_Loss = UK_and_Europe_High_Income_Individual_Addressable_Market * UK_and_Europe_High_Income_Individual_Churn / 100",
            "UK_and_Europe_Mid_Income_Individual_Churn_Loss = UK_and_Europe_Mid_Income_Individual_Addressable_Market * UK_and_Europe_Mid_Income_Individual_Churn / 100",
            "UK_and_Europe_Low_Income_Individual_Churn_Loss = UK_and_Europe_Low_Income_Individual_Addressable_Market * UK_and_Europe_Low_Income_Individual_Churn / 100",
            "Indian_Subcontinent_Small_Enterprise_Churn_Loss = Indian_Subcontinent_Small_Enterprise_Addressable_Market * Indian_Subcontinent_Small_Enterprise_Churn / 100",
            "Indian_Subcontinent_Medium_Enterprise_Churn_Loss = Indian_Subcontinent_Medium_Enterprise_Addressable_Market * Indian_Subcontinent_Medium_Enterprise_Churn / 100",
            "Indian_Subcontinent_Large_Enterprise_Churn_Loss = Indian_Subcontinent_Large_Enterprise_Addressable_Market * Indian_Subcontinent_Large_Enterprise_Churn / 100",
            "Middle_East_and_Africa_Small_Enterprise_Churn_Loss = Middle_East_and_Africa_Small_Enterprise_Addressable_Market * Middle_East_and_Africa_Small_Enterprise_Churn / 100",
            "Middle_East_and_Africa_Medium_Enterprise_Churn_Loss = Middle_East_and_Africa_Medium_Enterprise_Addressable_Market * Middle_East_and_Africa_Medium_Enterprise_Churn / 100",
            "Middle_East_and_Africa_Large_Enterprise_Churn_Loss = Middle_East_and_Africa_Large_Enterprise_Addressable_Market * Middle_East_and_Africa_Large_Enterprise_Churn / 100",
            "UK_and_Europe_Small_Enterprise_Churn_Loss = UK_and_Europe_Small_Enterprise_Addressable_Market * UK_and_Europe_Small_Enterprise_Churn / 100",
            "UK_and_Europe_Medium_Enterprise_Churn_Loss = UK_and_Europe_Medium_Enterprise_Addressable_Market * UK_and_Europe_Medium_Enterprise_Churn / 100",
            "UK_and_Europe_Large_Enterprise_Churn_Loss = UK_and_Europe_Large_Enterprise_Addressable_Market * UK_and_Europe_Large_Enterprise_Churn / 100"
        ],
        "Step 5: Total User base": [
            "Indian_Subcontinent_High_Income_Individual_Net_Users = Indian_Subcontinent_High_Income_Individual_Addressable_Market - Indian_Subcontinent_High_Income_Individual_Churn_Loss",
            "Indian_Subcontinent_Mid_Income_Individual_Net_Users = Indian_Subcontinent_Mid_Income_Individual_Addressable_Market - Indian_Subcontinent_Mid_Income_Individual_Churn_Loss",
            "Indian_Subcontinent_Low_Income_Individual_Net_Users = Indian_Subcontinent_Low_Income_Individual_Addressable_Market - Indian_Subcontinent_Low_Income_Individual_Churn_Loss",
            "Middle_East_and_Africa_High_Income_Individual_Net_Users = Middle_East_and_Africa_High_Income_Individual_Addressable_Market - Middle_East_and_Africa_High_Income_Individual_Churn_Loss",
            "Middle_East_and_Africa_Mid_Income_Individual_Net_Users = Middle_East_and_Africa_Mid_Income_Individual_Addressable_Market - Middle_East_and_Africa_Mid_Income_Individual_Churn_Loss",
            "Middle_East_and_Africa_Low_Income_Individual_Net_Users = Middle_East_and_Africa_Low_Income_Individual_Addressable_Market - Middle_East_and_Africa_Low_Income_Individual_Churn_Loss",
            "UK_and_Europe_High_Income_Individual_Net_Users = UK_and_Europe_High_Income_Individual_Addressable_Market - UK_and_Europe_High_Income_Individual_Churn_Loss",
            "UK_and_Europe_Mid_Income_Individual_Net_Users = UK_and_Europe_Mid_Income_Individual_Addressable_Market - UK_and_Europe_Mid_Income_Individual_Churn_Loss",
            "UK_and_Europe_Low_Income_Individual_Net_Users = UK_and_Europe_Low_Income_Individual_Addressable_Market - UK_and_Europe_Low_Income_Individual_Churn_Loss",
            "Indian_Subcontinent_Small_Enterprise_Net_Users = Indian_Subcontinent_Small_Enterprise_Addressable_Market - Indian_Subcontinent_Small_Enterprise_Churn_Loss",
            "Indian_Subcontinent_Medium_Enterprise_Net_Users = Indian_Subcontinent_Medium_Enterprise_Addressable_Market - Indian_Subcontinent_Medium_Enterprise_Churn_Loss",
            "Indian_Subcontinent_Large_Enterprise_Net_Users = Indian_Subcontinent_Large_Enterprise_Addressable_Market - Indian_Subcontinent_Large_Enterprise_Churn_Loss",
            "Middle_East_and_Africa_Small_Enterprise_Net_Users = Middle_East_and_Africa_Small_Enterprise_Addressable_Market - Middle_East_and_Africa_Small_Enterprise_Churn_Loss",
            "Middle_East_and_Africa_Medium_Enterprise_Net_Users = Middle_East_and_Africa_Medium_Enterprise_Addressable_Market - Middle_East_and_Africa_Medium_Enterprise_Churn_Loss",
            "Middle_East_and_Africa_Large_Enterprise_Net_Users = Middle_East_and_Africa_Large_Enterprise_Addressable_Market - Middle_East_and_Africa_Large_Enterprise_Churn_Loss",
            "UK_and_Europe_Small_Enterprise_Net_Users = UK_and_Europe_Small_Enterprise_Addressable_Market - UK_and_Europe_Small_Enterprise_Churn_Loss",
            "UK_and_Europe_Medium_Enterprise_Net_Users = UK_and_Europe_Medium_Enterprise_Addressable_Market - UK_and_Europe_Medium_Enterprise_Churn_Loss",
            "UK_and_Europe_Large_Enterprise_Net_Users = UK_and_Europe_Large_Enterprise_Addressable_Market - UK_and_Europe_Large_Enterprise_Churn_Loss",
            "Total_User_Base = Indian_Subcontinent_High_Income_Individual_Net_Users + Indian_Subcontinent_Mid_Income_Individual_Net_Users + Indian_Subcontinent_Low_Income_Individual_Net_Users + Middle_East_and_Africa_High_Income_Individual_Net_Users + Middle_East_and_Africa_Mid_Income_Individual_Net_Users + Middle_East_and_Africa_Low_Income_Individual_Net_Users + UK_and_Europe_High_Income_Individual_Net_Users + UK_and_Europe_Mid_Income_Individual_Net_Users + UK_and_Europe_Low_Income_Individual_Net_Users + Indian_Subcontinent_Small_Enterprise_Net_Users + Indian_Subcontinent_Medium_Enterprise_Net_Users + Indian_Subcontinent_Large_Enterprise_Net_Users + Middle_East_and_Africa_Small_Enterprise_Net_Users + Middle_East_and_Africa_Medium_Enterprise_Net_Users + Middle_East_and_Africa_Large_Enterprise_Net_Users + UK_and_Europe_Small_Enterprise_Net_Users + UK_and_Europe_Medium_Enterprise_Net_Users + UK_and_Europe_Large_Enterprise_Net_Users"
        ]
    }

#pdb.set_trace()
#formula =json.loads(description_response6)["formula"]
#assumptions=json.loads(description_response6)["assumptions"]

#....................................................................fetching UB asss values


description_payload = {
    "formula":formula,
    "assumptions":assumptions,
    "analysis_time_frame":['2025', '2026', '2027'],
    "period_ranges":[['January', 'December', 2025], ['January', 'December', 2026], ['January', 'December', 2027]],
    "user_description":"I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model, and want to have the model for 5 years straight, starting from 2026 January. I want to operate in both India, Dubai and London",
}

user_base_ass_val = requests.post(
    f"{BASE_URL}/estimate_user_base_assumption_values",
    json=description_payload,
    proxies=proxies
)

print("\nResponse from /user_base_ass_val.....................")
print(user_base_ass_val.text)

#......................................................................
'''
description_payload = {
    "formula":f"""{formula}""",
    "assumptions":f"""{assumptions}""",
    "user_input":"Make the formula compact and keep only most important components",
    "user_description":"I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model, and want to have the model for 5 years straight, starting from 2026 January. I want to operate in both India, Dubai and London",
}

description_response7 = requests.post(
    f"{BASE_URL}/update_user_base_ass_formula",
    json=description_payload,
    proxies=proxies
)

#print("\nResponse from /update_user_base_ass_formula")
#print(description_response7.text)
'''
formula= {"Step 1: Identify the size of the population in scope":["Indian_Subcontinent_Internet_Users = India_Total_Population * India_Internet_Penetration / 100","Indian_Subcontinent_High_Income_AI_Adopters = Indian_Subcontinent_Internet_Users * India_High_Income_Share / 100 * High_Income_AI_Adoption_Rate / 100","Indian_Subcontinent_Mid_Income_AI_Adopters = Indian_Subcontinent_Internet_Users * India_Mid_Income_Share / 100 * Mid_Income_AI_Adoption_Rate / 100","Indian_Subcontinent_Low_Income_AI_Adopters = Indian_Subcontinent_Internet_Users * India_Low_Income_Share / 100 * Low_Income_AI_Adoption_Rate / 100","Middle_East_Africa_Internet_Users = UAE_Total_Population * UAE_Internet_Penetration / 100","Middle_East_Africa_High_Income_AI_Adopters = Middle_East_Africa_Internet_Users * UAE_High_Income_Share / 100 * High_Income_AI_Adoption_Rate / 100","Middle_East_Africa_Mid_Income_AI_Adopters = Middle_East_Africa_Internet_Users * UAE_Mid_Income_Share / 100 * Mid_Income_AI_Adoption_Rate / 100","Middle_East_Africa_Low_Income_AI_Adopters = Middle_East_Africa_Internet_Users * UAE_Low_Income_Share / 100 * Low_Income_AI_Adoption_Rate / 100","UK_Europe_Internet_Users = UK_Total_Population * UK_Internet_Penetration / 100","UK_Europe_High_Income_AI_Adopters = UK_Europe_Internet_Users * UK_High_Income_Share / 100 * High_Income_AI_Adoption_Rate / 100","UK_Europe_Mid_Income_AI_Adopters = UK_Europe_Internet_Users * UK_Mid_Income_Share / 100 * Mid_Income_AI_Adoption_Rate / 100","UK_Europe_Low_Income_AI_Adopters = UK_Europe_Internet_Users * UK_Low_Income_Share / 100 * Low_Income_AI_Adoption_Rate / 100","Indian_Subcontinent_Small_Enterprise_Seats = India_Enterprise_Count * Small_Enterprise_Share / 100 * Small_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Small_Enterprise","Indian_Subcontinent_Medium_Enterprise_Seats = India_Enterprise_Count * Medium_Enterprise_Share / 100 * Medium_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Medium_Enterprise","Indian_Subcontinent_Large_Enterprise_Seats = India_Enterprise_Count * Large_Enterprise_Share / 100 * Large_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Large_Enterprise","Middle_East_Africa_Small_Enterprise_Seats = UAE_Enterprise_Count * Small_Enterprise_Share / 100 * Small_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Small_Enterprise","Middle_East_Africa_Medium_Enterprise_Seats = UAE_Enterprise_Count * Medium_Enterprise_Share / 100 * Medium_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Medium_Enterprise","Middle_East_Africa_Large_Enterprise_Seats = UAE_Enterprise_Count * Large_Enterprise_Share / 100 * Large_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Large_Enterprise","UK_Europe_Small_Enterprise_Seats = UK_Enterprise_Count * Small_Enterprise_Share / 100 * Small_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Small_Enterprise","UK_Europe_Medium_Enterprise_Seats = UK_Enterprise_Count * Medium_Enterprise_Share / 100 * Medium_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Medium_Enterprise","UK_Europe_Large_Enterprise_Seats = UK_Enterprise_Count * Large_Enterprise_Share / 100 * Large_Enterprise_AI_Adoption_Rate / 100 * Average_Seats_Per_Large_Enterprise"],"Step 2: Identify the growth rate of the segment":["Total_Indian_Subcontinent_High_Income_AI_Adopters = Indian_Subcontinent_High_Income_AI_Adopters * (1 + India_Population_Growth_Rate / 100)","Total_Indian_Subcontinent_Mid_Income_AI_Adopters = Indian_Subcontinent_Mid_Income_AI_Adopters * (1 + India_Population_Growth_Rate / 100)","Total_Indian_Subcontinent_Low_Income_AI_Adopters = Indian_Subcontinent_Low_Income_AI_Adopters * (1 + India_Population_Growth_Rate / 100)","Total_Middle_East_Africa_High_Income_AI_Adopters = Middle_East_Africa_High_Income_AI_Adopters * (1 + UAE_Population_Growth_Rate / 100)","Total_Middle_East_Africa_Mid_Income_AI_Adopters = Middle_East_Africa_Mid_Income_AI_Adopters * (1 + UAE_Population_Growth_Rate / 100)","Total_Middle_East_Africa_Low_Income_AI_Adopters = Middle_East_Africa_Low_Income_AI_Adopters * (1 + UAE_Population_Growth_Rate / 100)","Total_UK_Europe_High_Income_AI_Adopters = UK_Europe_High_Income_AI_Adopters * (1 + UK_Population_Growth_Rate / 100)","Total_UK_Europe_Mid_Income_AI_Adopters = UK_Europe_Mid_Income_AI_Adopters * (1 + UK_Population_Growth_Rate / 100)","Total_UK_Europe_Low_Income_AI_Adopters = UK_Europe_Low_Income_AI_Adopters * (1 + UK_Population_Growth_Rate / 100)","Total_Indian_Subcontinent_Small_Enterprise_Seats = Indian_Subcontinent_Small_Enterprise_Seats * (1 + India_Enterprise_Growth_Rate / 100)","Total_Indian_Subcontinent_Medium_Enterprise_Seats = Indian_Subcontinent_Medium_Enterprise_Seats * (1 + India_Enterprise_Growth_Rate / 100)","Total_Indian_Subcontinent_Large_Enterprise_Seats = Indian_Subcontinent_Large_Enterprise_Seats * (1 + India_Enterprise_Growth_Rate / 100)","Total_Middle_East_Africa_Small_Enterprise_Seats = Middle_East_Africa_Small_Enterprise_Seats * (1 + UAE_Enterprise_Growth_Rate / 100)","Total_Middle_East_Africa_Medium_Enterprise_Seats = Middle_East_Africa_Medium_Enterprise_Seats * (1 + UAE_Enterprise_Growth_Rate / 100)","Total_Middle_East_Africa_Large_Enterprise_Seats = Middle_East_Africa_Large_Enterprise_Seats * (1 + UAE_Enterprise_Growth_Rate / 100)","Total_UK_Europe_Small_Enterprise_Seats = UK_Europe_Small_Enterprise_Seats * (1 + UK_Enterprise_Growth_Rate / 100)","Total_UK_Europe_Medium_Enterprise_Seats = UK_Europe_Medium_Enterprise_Seats * (1 + UK_Enterprise_Growth_Rate / 100)","Total_UK_Europe_Large_Enterprise_Seats = UK_Europe_Large_Enterprise_Seats * (1 + UK_Enterprise_Growth_Rate / 100)"],"Step 3: Company market share":["Indian_Subcontinent_High_Income_Addressable_Market = Total_Indian_Subcontinent_High_Income_AI_Adopters * Indian_Subcontinent_High_Income_Market_Share / 100","Indian_Subcontinent_Mid_Income_Addressable_Market = Total_Indian_Subcontinent_Mid_Income_AI_Adopters * Indian_Subcontinent_Mid_Income_Market_Share / 100","Indian_Subcontinent_Low_Income_Addressable_Market = Total_Indian_Subcontinent_Low_Income_AI_Adopters * Indian_Subcontinent_Low_Income_Market_Share / 100","Middle_East_Africa_High_Income_Addressable_Market = Total_Middle_East_Africa_High_Income_AI_Adopters * Middle_East_Africa_High_Income_Market_Share / 100","Middle_East_Africa_Mid_Income_Addressable_Market = Total_Middle_East_Africa_Mid_Income_AI_Adopters * Middle_East_Africa_Mid_Income_Market_Share / 100","Middle_East_Africa_Low_Income_Addressable_Market = Total_Middle_East_Africa_Low_Income_AI_Adopters * Middle_East_Africa_Low_Income_Market_Share / 100","UK_Europe_High_Income_Addressable_Market = Total_UK_Europe_High_Income_AI_Adopters * UK_Europe_High_Income_Market_Share / 100","UK_Europe_Mid_Income_Addressable_Market = Total_UK_Europe_Mid_Income_AI_Adopters * UK_Europe_Mid_Income_Market_Share / 100","UK_Europe_Low_Income_Addressable_Market = Total_UK_Europe_Low_Income_AI_Adopters * UK_Europe_Low_Income_Market_Share / 100","Indian_Subcontinent_Small_Enterprise_Addressable_Seats = Total_Indian_Subcontinent_Small_Enterprise_Seats * Indian_Subcontinent_Small_Enterprise_Market_Share / 100","Indian_Subcontinent_Medium_Enterprise_Addressable_Seats = Total_Indian_Subcontinent_Medium_Enterprise_Seats * Indian_Subcontinent_Medium_Enterprise_Market_Share / 100","Indian_Subcontinent_Large_Enterprise_Addressable_Seats = Total_Indian_Subcontinent_Large_Enterprise_Seats * Indian_Subcontinent_Large_Enterprise_Market_Share / 100","Middle_East_Africa_Small_Enterprise_Addressable_Seats = Total_Middle_East_Africa_Small_Enterprise_Seats * Middle_East_Africa_Small_Enterprise_Market_Share / 100","Middle_East_Africa_Medium_Enterprise_Addressable_Seats = Total_Middle_East_Africa_Medium_Enterprise_Seats * Middle_East_Africa_Medium_Enterprise_Market_Share / 100","Middle_East_Africa_Large_Enterprise_Addressable_Seats = Total_Middle_East_Africa_Large_Enterprise_Seats * Middle_East_Africa_Large_Enterprise_Market_Share / 100","UK_Europe_Small_Enterprise_Addressable_Seats = Total_UK_Europe_Small_Enterprise_Seats * UK_Europe_Small_Enterprise_Market_Share / 100","UK_Europe_Medium_Enterprise_Addressable_Seats = Total_UK_Europe_Medium_Enterprise_Seats * UK_Europe_Medium_Enterprise_Market_Share / 100","UK_Europe_Large_Enterprise_Addressable_Seats = Total_UK_Europe_Large_Enterprise_Seats * UK_Europe_Large_Enterprise_Market_Share / 100"],"Step 4: Factor gains and losses of customers from and to competitors":["Indian_Subcontinent_High_Income_Churn = Indian_Subcontinent_High_Income_Addressable_Market * Indian_Subcontinent_High_Income_Churn_Rate / 100","Indian_Subcontinent_Mid_Income_Churn = Indian_Subcontinent_Mid_Income_Addressable_Market * Indian_Subcontinent_Mid_Income_Churn_Rate / 100","Indian_Subcontinent_Low_Income_Churn = Indian_Subcontinent_Low_Income_Addressable_Market * Indian_Subcontinent_Low_Income_Churn_Rate / 100","Middle_East_Africa_High_Income_Churn = Middle_East_Africa_High_Income_Addressable_Market * Middle_East_Africa_High_Income_Churn_Rate / 100","Middle_East_Africa_Mid_Income_Churn = Middle_East_Africa_Mid_Income_Addressable_Market * Middle_East_Africa_Mid_Income_Churn_Rate / 100","Middle_East_Africa_Low_Income_Churn = Middle_East_Africa_Low_Income_Addressable_Market * Middle_East_Africa_Low_Income_Churn_Rate / 100","UK_Europe_High_Income_Churn = UK_Europe_High_Income_Addressable_Market * UK_Europe_High_Income_Churn_Rate / 100","UK_Europe_Mid_Income_Churn = UK_Europe_Mid_Income_Addressable_Market * UK_Europe_Mid_Income_Churn_Rate / 100","UK_Europe_Low_Income_Churn = UK_Europe_Low_Income_Addressable_Market * UK_Europe_Low_Income_Churn_Rate / 100","Indian_Subcontinent_Small_Enterprise_Churn = Indian_Subcontinent_Small_Enterprise_Addressable_Seats * Indian_Subcontinent_Small_Enterprise_Churn_Rate / 100","Indian_Subcontinent_Medium_Enterprise_Churn = Indian_Subcontinent_Medium_Enterprise_Addressable_Seats * Indian_Subcontinent_Medium_Enterprise_Churn_Rate / 100","Indian_Subcontinent_Large_Enterprise_Churn = Indian_Subcontinent_Large_Enterprise_Addressable_Seats * Indian_Subcontinent_Large_Enterprise_Churn_Rate / 100","Middle_East_Africa_Small_Enterprise_Churn = Middle_East_Africa_Small_Enterprise_Addressable_Seats * Middle_East_Africa_Small_Enterprise_Churn_Rate / 100","Middle_East_Africa_Medium_Enterprise_Churn = Middle_East_Africa_Medium_Enterprise_Addressable_Seats * Middle_East_Africa_Medium_Enterprise_Churn_Rate / 100","Middle_East_Africa_Large_Enterprise_Churn = Middle_East_Africa_Large_Enterprise_Addressable_Seats * Middle_East_Africa_Large_Enterprise_Churn_Rate / 100","UK_Europe_Small_Enterprise_Churn = UK_Europe_Small_Enterprise_Addressable_Seats * UK_Europe_Small_Enterprise_Churn_Rate / 100","UK_Europe_Medium_Enterprise_Churn = UK_Europe_Medium_Enterprise_Addressable_Seats * UK_Europe_Medium_Enterprise_Churn_Rate / 100","UK_Europe_Large_Enterprise_Churn = UK_Europe_Large_Enterprise_Addressable_Seats * UK_Europe_Large_Enterprise_Churn_Rate / 100"],"Step 5: Total user base":["Indian_Subcontinent_High_Income_Users = Indian_Subcontinent_High_Income_Addressable_Market - Indian_Subcontinent_High_Income_Churn","Indian_Subcontinent_Mid_Income_Users = Indian_Subcontinent_Mid_Income_Addressable_Market - Indian_Subcontinent_Mid_Income_Churn","Indian_Subcontinent_Low_Income_Users = Indian_Subcontinent_Low_Income_Addressable_Market - Indian_Subcontinent_Low_Income_Churn","Middle_East_Africa_High_Income_Users = Middle_East_Africa_High_Income_Addressable_Market - Middle_East_Africa_High_Income_Churn","Middle_East_Africa_Mid_Income_Users = Middle_East_Africa_Mid_Income_Addressable_Market - Middle_East_Africa_Mid_Income_Churn","Middle_East_Africa_Low_Income_Users = Middle_East_Africa_Low_Income_Addressable_Market - Middle_East_Africa_Low_Income_Churn","UK_Europe_High_Income_Users = UK_Europe_High_Income_Addressable_Market - UK_Europe_High_Income_Churn","UK_Europe_Mid_Income_Users = UK_Europe_Mid_Income_Addressable_Market - UK_Europe_Mid_Income_Churn","UK_Europe_Low_Income_Users = UK_Europe_Low_Income_Addressable_Market - UK_Europe_Low_Income_Churn","Indian_Subcontinent_Small_Enterprise_Users = Indian_Subcontinent_Small_Enterprise_Addressable_Seats - Indian_Subcontinent_Small_Enterprise_Churn","Indian_Subcontinent_Medium_Enterprise_Users = Indian_Subcontinent_Medium_Enterprise_Addressable_Seats - Indian_Subcontinent_Medium_Enterprise_Churn","Indian_Subcontinent_Large_Enterprise_Users = Indian_Subcontinent_Large_Enterprise_Addressable_Seats - Indian_Subcontinent_Large_Enterprise_Churn","Middle_East_Africa_Small_Enterprise_Users = Middle_East_Africa_Small_Enterprise_Addressable_Seats - Middle_East_Africa_Small_Enterprise_Churn","Middle_East_Africa_Medium_Enterprise_Users = Middle_East_Africa_Medium_Enterprise_Addressable_Seats - Middle_East_Africa_Medium_Enterprise_Churn","Middle_East_Africa_Large_Enterprise_Users = Middle_East_Africa_Large_Enterprise_Addressable_Seats - Middle_East_Africa_Large_Enterprise_Churn","UK_Europe_Small_Enterprise_Users = UK_Europe_Small_Enterprise_Addressable_Seats - UK_Europe_Small_Enterprise_Churn","UK_Europe_Medium_Enterprise_Users = UK_Europe_Medium_Enterprise_Addressable_Seats - UK_Europe_Medium_Enterprise_Churn","UK_Europe_Large_Enterprise_Users = UK_Europe_Large_Enterprise_Addressable_Seats - UK_Europe_Large_Enterprise_Churn","Total_User_Base = Indian_Subcontinent_High_Income_Users + Indian_Subcontinent_Mid_Income_Users + Indian_Subcontinent_Low_Income_Users + Middle_East_Africa_High_Income_Users + Middle_East_Africa_Mid_Income_Users + Middle_East_Africa_Low_Income_Users + UK_Europe_High_Income_Users + UK_Europe_Mid_Income_Users + UK_Europe_Low_Income_Users + Indian_Subcontinent_Small_Enterprise_Users + Indian_Subcontinent_Medium_Enterprise_Users + Indian_Subcontinent_Large_Enterprise_Users + Middle_East_Africa_Small_Enterprise_Users + Middle_East_Africa_Medium_Enterprise_Users + Middle_East_Africa_Large_Enterprise_Users + UK_Europe_Small_Enterprise_Users + UK_Europe_Medium_Enterprise_Users + UK_Europe_Large_Enterprise_Users"]}

# SOlve user base equations..............................
description_payload = {
    "assumption_values":{'2025': ['', 5, 12, 5825400, 99.5, 14, 18, 410800, 16, 31, 19, 3, 48, 66625000, 520, 10280000, 85, 24, 1432200000, 96, 46, 52, 40, 50, 7, 68407000, 52, 30, 11, 52, 36, '', 3.1, 2.4, 3.0, 2.8, 2.3, 2.6, '', 7, 5, 25, 4, 12, 3, 2, 10, 10, 6, 18, 14, 7, 12, 10, 5, 20, 14, '', 13, 10, 9, 16, 6, 18, 10, 12, 7, 5, 8, 8, 8, 12, 14, 6, 10, 7, ''], '2026': ['', 5, 12, 5967208, 99.8, 13, 22, 423124, 17, 32, 18, 3, 46, 68490500, 540, 10598680, 85, 29, 1469472000, 97, 47, 54, 40, 50, 9, 69983610, 60, 36, 14, 58, 37, '', 3.4, 2.6, 3.3, 3.1, 2.5, 2.9, '', 8, 6, 28, 5, 14, 4, 3, 12, 12, 7, 21, 16, 8, 14, 12, 6, 22, 16, '', 11, 8, 7, 14, 5, 16, 8, 10, 6, 4, 6, 6, 6, 10, 12, 4, 8, 6, ''], '2027': ['', 5, 12, 6265766, 99.9, 11, 32, 447894, 19, 34, 16, 3, 42, 72142470, 580, 11224178, 85, 42, 1542926600, 98, 49, 58, 40, 50, 14, 73333000, 78, 48, 22, 72, 39, '', 4.2, 3.1, 4.0, 3.8, 3.0, 3.6, '', 11, 9, 35, 8, 19, 7, 6, 17, 17, 10, 28, 21, 11, 19, 17, 9, 27, 21, '', 8, 5, 4, 11, 3, 13, 5, 7, 4, 2, 3, 3, 3, 7, 9, 2, 5, 4, '']},
    "units":['', '#', '%', '#', '%', '%', '%', '#', '%', '%', '%', '%', '%', '#', '#', '#', '%', '%', '#', '%', '%', '#', '%', '%', '%', '#', '%', '%', '%', '%', '%', '', '%', '%', '%', '%', '%', '%', '', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', ''],
    "currency":"USD",
    "formula":formula,
    "steps":['Step 1: Identify the size of the population in scope', 'Average_Seats_Per_Small_Enterprise', 'Medium_Enterprise_Share', 'UK_Enterprise_Count', 'UAE_Internet_Penetration', 'UAE_Low_Income_Share', 'Mid_Income_AI_Adoption_Rate', 'UAE_Enterprise_Count', 'India_High_Income_Share', 'UK_High_Income_Share', 'UK_Low_Income_Share', 'Large_Enterprise_Share', 'India_Low_Income_Share', 'India_Enterprise_Count', 'Average_Seats_Per_Large_Enterprise', 'UAE_Total_Population', 'Small_Enterprise_Share', 'Medium_Enterprise_AI_Adoption_Rate', 'India_Total_Population', 'UK_Internet_Penetration', 'UAE_Mid_Income_Share', 'Average_Seats_Per_Medium_Enterprise', 'UAE_High_Income_Share', 'UK_Mid_Income_Share', 'Low_Income_AI_Adoption_Rate', 'UK_Total_Population', 'Large_Enterprise_AI_Adoption_Rate', 'High_Income_AI_Adoption_Rate', 'Small_Enterprise_AI_Adoption_Rate', 'India_Internet_Penetration', 'India_Mid_Income_Share', 'Step 2: Identify the growth rate of the segment', 'UAE_Population_Growth_Rate', 'UK_Enterprise_Growth_Rate', 'UAE_Enterprise_Growth_Rate', 'India_Enterprise_Growth_Rate', 'UK_Population_Growth_Rate', 'India_Population_Growth_Rate', 'Step 3: Company market share', 'Middle_East_Africa_Small_Enterprise_Market_Share', 'Indian_Subcontinent_Medium_Enterprise_Market_Share', 'UK_Europe_Large_Enterprise_Market_Share', 'Indian_Subcontinent_Mid_Income_Market_Share', 'Middle_East_Africa_Medium_Enterprise_Market_Share', 'Indian_Subcontinent_Small_Enterprise_Market_Share', 'Indian_Subcontinent_Low_Income_Market_Share', 'Middle_East_Africa_Mid_Income_Market_Share', 'Indian_Subcontinent_Large_Enterprise_Market_Share', 'Indian_Subcontinent_High_Income_Market_Share', 'UK_Europe_High_Income_Market_Share', 'Middle_East_Africa_High_Income_Market_Share', 'UK_Europe_Low_Income_Market_Share', 'UK_Europe_Mid_Income_Market_Share', 'UK_Europe_Small_Enterprise_Market_Share', 'Middle_East_Africa_Low_Income_Market_Share', 'Middle_East_Africa_Large_Enterprise_Market_Share', 'UK_Europe_Medium_Enterprise_Market_Share', 'Step 4: Factor gains and losses of customers from and to competitors', 'Indian_Subcontinent_High_Income_Churn_Rate', 'UK_Europe_Low_Income_Churn_Rate', 'UK_Europe_Medium_Enterprise_Churn_Rate', 'Middle_East_Africa_High_Income_Churn_Rate', 'Middle_East_Africa_Large_Enterprise_Churn_Rate', 'UK_Europe_High_Income_Churn_Rate', 'Indian_Subcontinent_Mid_Income_Churn_Rate', 'Middle_East_Africa_Mid_Income_Churn_Rate', 'Indian_Subcontinent_Medium_Enterprise_Churn_Rate', 'Indian_Subcontinent_Large_Enterprise_Churn_Rate', 'Middle_East_Africa_Low_Income_Churn_Rate', 'Middle_East_Africa_Medium_Enterprise_Churn_Rate', 'Indian_Subcontinent_Small_Enterprise_Churn_Rate', 'UK_Europe_Small_Enterprise_Churn_Rate', 'UK_Europe_Mid_Income_Churn_Rate', 'Indian_Subcontinent_Low_Income_Churn_Rate', 'Middle_East_Africa_Small_Enterprise_Churn_Rate', 'UK_Europe_Large_Enterprise_Churn_Rate', 'Step 5: Total user base'],
}

user_base_compute = requests.post(
    f"{BASE_URL}/compute_user_base",
    json=description_payload,
    proxies=proxies
)

print("\nResponse from /user_base_compute.....................")
print(user_base_compute.text)

