import requests
#from pydantic import BaseModel
import pdb
import json
import re
import asyncio
import json
import anthropic
import re
from typing import Dict, Any, Optional
import httpx


client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

def generate_user_base_assumption_formula_update_prompt(formula, assumption, user_input, product_description):
    prompt =f"""You are an expert in Financial Modeling and User Base Estimation. Your task is to revise an existing five-step formula used to compute the user base. The revised formula must reflect the instruction provided by the user: {user_input}.

    Modify based strictly on the following user Instruction: {user_input}

    Inputs:
    - Assumptions: {assumption}
    - Original Formula: {formula}
    - financial situations Context: {product_description}

    Requirements:
    1. Revise the formula and parameter list based strictly on the provided instruction ({user_input}).
    2. Maintain a **five-step computation process**, as in the original formula.
    3. Each step should:
    - Clearly define and compute intermediate values.
    - Must Use only numeric values from "assumption"
    - Use only mathematical operations: +, -, *, /, %, etc.
    4. Avoid using specific years, months, or date-based variable names.
    5. Ensure the formula calculates for the **entire period in one go** (not broken into time-based subperiods).
    6. If geography is involved (e.g., continents), only include those relevant to the operational countries.
    7. Each formula must be accompanied by a **well-defined unit** on the left-hand side (e.g., "User_base (#)").
    7. Do **not** add any explanations, commentary, or extra text.
    Output Format:
    - Respond in **valid JSON**.
    - Structure the response as:
    - "parameters": A cleaned and updated parameter list based on the revised formula.
    - "formula": A dictionary with 5 clearly labeled steps, showing computations using updated parameters.

    Example Output:

    "parameters": {{
        "Total_Population": 83200000,
        "Penetration_Rate (%)": 20,
        "Total_Vehicle_Population": 340500000,
        "Commercial_Vehicles (%)": 12.5,
        "Passenger_Vehicles (%)": 15.8,
        "Two_Wheelers (%)": 71.7,
        "Average_Wheel_Replacement_Rate_per_Year": 1.2,
        "GDP_Growth_Rate (%)": 7.5,
        "Vehicle_Sales_Growth (%)": 12.5,
        "Urbanization_Rate (%)": 36.5,
        "market_share (%)": 15.3,
        "Average_Wheels_per_Commercial_Vehicle": 6,
        "Average_Wheels_per_Passenger_Vehicle": 4,
        "Average_Wheels_per_Two_Wheeler": 2,
        "New_Vehicle_Sales_Forecast": 32500000,
        "Import/Export_Ratio (%)": 15
    }},

    "formula": {{
        "Step 1 Total Vehicles": [
            "Total_Vehicles (#)= Total_Vehicle_Population"
        ],
        "Step 2 Vehicle Segmentation": [
            "Commercial_Vehicles (#)= Total_Vehicles * (Commercial_Vehicles (%) / 100)",
            "Passenger_Vehicles (#)= Total_Vehicles * (Passenger_Vehicles (%) / 100)",
            "Two_Wheelers (#)= Total_Vehicles * (Two_Wheelers (%) / 100)"
        ],
        "Step 3 Tyre Replacement Computation": [
            "Tyre_Replacements_Commercial (#) = Commercial_Vehicles * Average_Wheel_Replacement_Rate_per_Year * Average_Wheels_per_Commercial_Vehicle",
            "Tyre_Replacements_Passenger (#) = Passenger_Vehicles * Average_Wheel_Replacement_Rate_per_Year * Average_Wheels_per_Passenger_Vehicle",
            "Tyre_Replacements_TwoWheeler (#) = Two_Wheelers * Average_Wheel_Replacement_Rate_per_Year * Average_Wheels_per_Two_Wheeler"
        ],
        "Step 4 Total Tyre Demand": [
            "Total_Tyre_Demand (#) = Tyre_Replacements_Commercial + Tyre_Replacements_Passenger + Tyre_Replacements_TwoWheeler"
        ],
        "Step 5 User Base": [
            "User_Base (#)= Total_Tyre_Demand * (market_share (%) / 100)"
        ]
    }}
    """
    return prompt




formula =  {"Step_1:_Identify_the_size_of_the_population_in_scope":["UK_Europe_AI_Low_Adopters (#) = UK_Europe_Population * UK_Europe_AI_Low_Adopters_Share / 100","UK_Europe_AI_Medium_Adopters (#) = UK_Europe_Population * UK_Europe_AI_Medium_Adopters_Share / 100","UK_Europe_AI_High_Adopters (#) = UK_Europe_Population * UK_Europe_AI_High_Adopters_Share / 100","UK_Europe_Low_Adopters_Basic_Users (#) = UK_Europe_AI_Low_Adopters * Low_Adopters_Basic_Subscription_Rate / 100","UK_Europe_Low_Adopters_Premium_Users (#) = UK_Europe_AI_Low_Adopters * Low_Adopters_Premium_Subscription_Rate / 100","UK_Europe_Medium_Adopters_Basic_Users (#) = UK_Europe_AI_Medium_Adopters * Medium_Adopters_Basic_Subscription_Rate / 100","UK_Europe_Medium_Adopters_Premium_Users (#) = UK_Europe_AI_Medium_Adopters * Medium_Adopters_Premium_Subscription_Rate / 100","UK_Europe_High_Adopters_Basic_Users (#) = UK_Europe_AI_High_Adopters * High_Adopters_Basic_Subscription_Rate / 100","UK_Europe_High_Adopters_Premium_Users (#) = UK_Europe_AI_High_Adopters * High_Adopters_Premium_Subscription_Rate / 100","Middle_East_Africa_AI_Low_Adopters (#) = Middle_East_Africa_Population * Middle_East_Africa_AI_Low_Adopters_Share / 100","Middle_East_Africa_AI_Medium_Adopters (#) = Middle_East_Africa_Population * Middle_East_Africa_AI_Medium_Adopters_Share / 100","Middle_East_Africa_AI_High_Adopters (#) = Middle_East_Africa_Population * Middle_East_Africa_AI_High_Adopters_Share / 100","Middle_East_Africa_Low_Adopters_Basic_Users (#) = Middle_East_Africa_AI_Low_Adopters * Low_Adopters_Basic_Subscription_Rate / 100","Middle_East_Africa_Low_Adopters_Premium_Users (#) = Middle_East_Africa_AI_Low_Adopters * Low_Adopters_Premium_Subscription_Rate / 100","Middle_East_Africa_Medium_Adopters_Basic_Users (#) = Middle_East_Africa_AI_Medium_Adopters * Medium_Adopters_Basic_Subscription_Rate / 100","Middle_East_Africa_Medium_Adopters_Premium_Users (#) = Middle_East_Africa_AI_Medium_Adopters * Medium_Adopters_Premium_Subscription_Rate / 100","Middle_East_Africa_High_Adopters_Basic_Users (#) = Middle_East_Africa_AI_High_Adopters * High_Adopters_Basic_Subscription_Rate / 100","Middle_East_Africa_High_Adopters_Premium_Users (#) = Middle_East_Africa_AI_High_Adopters * High_Adopters_Premium_Subscription_Rate / 100","Indian_Subcontinent_AI_Low_Adopters (#) = Indian_Subcontinent_Population * Indian_Subcontinent_AI_Low_Adopters_Share / 100","Indian_Subcontinent_AI_Medium_Adopters (#) = Indian_Subcontinent_Population * Indian_Subcontinent_AI_Medium_Adopters_Share / 100","Indian_Subcontinent_AI_High_Adopters (#) = Indian_Subcontinent_Population * Indian_Subcontinent_AI_High_Adopters_Share / 100","Indian_Subcontinent_Low_Adopters_Basic_Users (#) = Indian_Subcontinent_AI_Low_Adopters * Low_Adopters_Basic_Subscription_Rate / 100","Indian_Subcontinent_Low_Adopters_Premium_Users (#) = Indian_Subcontinent_AI_Low_Adopters * Low_Adopters_Premium_Subscription_Rate / 100","Indian_Subcontinent_Medium_Adopters_Basic_Users (#) = Indian_Subcontinent_AI_Medium_Adopters * Medium_Adopters_Basic_Subscription_Rate / 100","Indian_Subcontinent_Medium_Adopters_Premium_Users (#) = Indian_Subcontinent_AI_Medium_Adopters * Medium_Adopters_Premium_Subscription_Rate / 100","Indian_Subcontinent_High_Adopters_Basic_Users (#) = Indian_Subcontinent_AI_High_Adopters * High_Adopters_Basic_Subscription_Rate / 100","Indian_Subcontinent_High_Adopters_Premium_Users (#) = Indian_Subcontinent_AI_High_Adopters * High_Adopters_Premium_Subscription_Rate / 100"],"Step_2:_Identify_the_growth_rate_of_the_segment":["Total_UK_Europe_Low_Adopters_Basic_Users (#) = UK_Europe_Low_Adopters_Basic_Users * (1 + UK_Europe_Population_Growth_Rate / 100)","Total_UK_Europe_Low_Adopters_Premium_Users (#) = UK_Europe_Low_Adopters_Premium_Users * (1 + UK_Europe_Population_Growth_Rate / 100)","Total_UK_Europe_Medium_Adopters_Basic_Users (#) = UK_Europe_Medium_Adopters_Basic_Users * (1 + UK_Europe_Population_Growth_Rate / 100)","Total_UK_Europe_Medium_Adopters_Premium_Users (#) = UK_Europe_Medium_Adopters_Premium_Users * (1 + UK_Europe_Population_Growth_Rate / 100)","Total_UK_Europe_High_Adopters_Basic_Users (#) = UK_Europe_High_Adopters_Basic_Users * (1 + UK_Europe_Population_Growth_Rate / 100)","Total_UK_Europe_High_Adopters_Premium_Users (#) = UK_Europe_High_Adopters_Premium_Users * (1 + UK_Europe_Population_Growth_Rate / 100)","Total_Middle_East_Africa_Low_Adopters_Basic_Users (#) = Middle_East_Africa_Low_Adopters_Basic_Users * (1 + Middle_East_Africa_Population_Growth_Rate / 100)","Total_Middle_East_Africa_Low_Adopters_Premium_Users (#) = Middle_East_Africa_Low_Adopters_Premium_Users * (1 + Middle_East_Africa_Population_Growth_Rate / 100)","Total_Middle_East_Africa_Medium_Adopters_Basic_Users (#) = Middle_East_Africa_Medium_Adopters_Basic_Users * (1 + Middle_East_Africa_Population_Growth_Rate / 100)","Total_Middle_East_Africa_Medium_Adopters_Premium_Users (#) = Middle_East_Africa_Medium_Adopters_Premium_Users * (1 + Middle_East_Africa_Population_Growth_Rate / 100)","Total_Middle_East_Africa_High_Adopters_Basic_Users (#) = Middle_East_Africa_High_Adopters_Basic_Users * (1 + Middle_East_Africa_Population_Growth_Rate / 100)","Total_Middle_East_Africa_High_Adopters_Premium_Users (#) = Middle_East_Africa_High_Adopters_Premium_Users * (1 + Middle_East_Africa_Population_Growth_Rate / 100)","Total_Indian_Subcontinent_Low_Adopters_Basic_Users (#) = Indian_Subcontinent_Low_Adopters_Basic_Users * (1 + Indian_Subcontinent_Population_Growth_Rate / 100)","Total_Indian_Subcontinent_Low_Adopters_Premium_Users (#) = Indian_Subcontinent_Low_Adopters_Premium_Users * (1 + Indian_Subcontinent_Population_Growth_Rate / 100)","Total_Indian_Subcontinent_Medium_Adopters_Basic_Users (#) = Indian_Subcontinent_Medium_Adopters_Basic_Users * (1 + Indian_Subcontinent_Population_Growth_Rate / 100)","Total_Indian_Subcontinent_Medium_Adopters_Premium_Users (#) = Indian_Subcontinent_Medium_Adopters_Premium_Users * (1 + Indian_Subcontinent_Population_Growth_Rate / 100)","Total_Indian_Subcontinent_High_Adopters_Basic_Users (#) = Indian_Subcontinent_High_Adopters_Basic_Users * (1 + Indian_Subcontinent_Population_Growth_Rate / 100)","Total_Indian_Subcontinent_High_Adopters_Premium_Users (#) = Indian_Subcontinent_High_Adopters_Premium_Users * (1 + Indian_Subcontinent_Population_Growth_Rate / 100)"],"Step_3:_Company_market_share":["UK_Europe_Low_Adopters_Basic_Addressable_Market (#) = Total_UK_Europe_Low_Adopters_Basic_Users * UK_Europe_Low_Adopters_Basic_Market_Share / 100","UK_Europe_Low_Adopters_Premium_Addressable_Market (#) = Total_UK_Europe_Low_Adopters_Premium_Users * UK_Europe_Low_Adopters_Premium_Market_Share / 100","UK_Europe_Medium_Adopters_Basic_Addressable_Market (#) = Total_UK_Europe_Medium_Adopters_Basic_Users * UK_Europe_Medium_Adopters_Basic_Market_Share / 100","UK_Europe_Medium_Adopters_Premium_Addressable_Market (#) = Total_UK_Europe_Medium_Adopters_Premium_Users * UK_Europe_Medium_Adopters_Premium_Market_Share / 100","UK_Europe_High_Adopters_Basic_Addressable_Market (#) = Total_UK_Europe_High_Adopters_Basic_Users * UK_Europe_High_Adopters_Basic_Market_Share / 100","UK_Europe_High_Adopters_Premium_Addressable_Market (#) = Total_UK_Europe_High_Adopters_Premium_Users * UK_Europe_High_Adopters_Premium_Market_Share / 100","Middle_East_Africa_Low_Adopters_Basic_Addressable_Market (#) = Total_Middle_East_Africa_Low_Adopters_Basic_Users * Middle_East_Africa_Low_Adopters_Basic_Market_Share / 100","Middle_East_Africa_Low_Adopters_Premium_Addressable_Market (#) = Total_Middle_East_Africa_Low_Adopters_Premium_Users * Middle_East_Africa_Low_Adopters_Premium_Market_Share / 100","Middle_East_Africa_Medium_Adopters_Basic_Addressable_Market (#) = Total_Middle_East_Africa_Medium_Adopters_Basic_Users * Middle_East_Africa_Medium_Adopters_Basic_Market_Share / 100","Middle_East_Africa_Medium_Adopters_Premium_Addressable_Market (#) = Total_Middle_East_Africa_Medium_Adopters_Premium_Users * Middle_East_Africa_Medium_Adopters_Premium_Market_Share / 100","Middle_East_Africa_High_Adopters_Basic_Addressable_Market (#) = Total_Middle_East_Africa_High_Adopters_Basic_Users * Middle_East_Africa_High_Adopters_Basic_Market_Share / 100","Middle_East_Africa_High_Adopters_Premium_Addressable_Market (#) = Total_Middle_East_Africa_High_Adopters_Premium_Users * Middle_East_Africa_High_Adopters_Premium_Market_Share / 100","Indian_Subcontinent_Low_Adopters_Basic_Addressable_Market (#) = Total_Indian_Subcontinent_Low_Adopters_Basic_Users * Indian_Subcontinent_Low_Adopters_Basic_Market_Share / 100","Indian_Subcontinent_Low_Adopters_Premium_Addressable_Market (#) = Total_Indian_Subcontinent_Low_Adopters_Premium_Users * Indian_Subcontinent_Low_Adopters_Premium_Market_Share / 100","Indian_Subcontinent_Medium_Adopters_Basic_Addressable_Market (#) = Total_Indian_Subcontinent_Medium_Adopters_Basic_Users * Indian_Subcontinent_Medium_Adopters_Basic_Market_Share / 100","Indian_Subcontinent_Medium_Adopters_Premium_Addressable_Market (#) = Total_Indian_Subcontinent_Medium_Adopters_Premium_Users * Indian_Subcontinent_Medium_Adopters_Premium_Market_Share / 100","Indian_Subcontinent_High_Adopters_Basic_Addressable_Market (#) = Total_Indian_Subcontinent_High_Adopters_Basic_Users * Indian_Subcontinent_High_Adopters_Basic_Market_Share / 100","Indian_Subcontinent_High_Adopters_Premium_Addressable_Market (#) = Total_Indian_Subcontinent_High_Adopters_Premium_Users * Indian_Subcontinent_High_Adopters_Premium_Market_Share / 100"],"Step_4:_Factor_gains_and_losses_of_customers_from_and_to_competitors":["UK_Europe_Low_Adopters_Basic_Churn (#) = UK_Europe_Low_Adopters_Basic_Addressable_Market * UK_Europe_Low_Adopters_Basic_Churn_Rate / 100","UK_Europe_Low_Adopters_Premium_Churn (#) = UK_Europe_Low_Adopters_Premium_Addressable_Market * UK_Europe_Low_Adopters_Premium_Churn_Rate / 100","UK_Europe_Medium_Adopters_Basic_Churn (#) = UK_Europe_Medium_Adopters_Basic_Addressable_Market * UK_Europe_Medium_Adopters_Basic_Churn_Rate / 100","UK_Europe_Medium_Adopters_Premium_Churn (#) = UK_Europe_Medium_Adopters_Premium_Addressable_Market * UK_Europe_Medium_Adopters_Premium_Churn_Rate / 100","UK_Europe_High_Adopters_Basic_Churn (#) = UK_Europe_High_Adopters_Basic_Addressable_Market * UK_Europe_High_Adopters_Basic_Churn_Rate / 100","UK_Europe_High_Adopters_Premium_Churn (#) = UK_Europe_High_Adopters_Premium_Addressable_Market * UK_Europe_High_Adopters_Premium_Churn_Rate / 100","Middle_East_Africa_Low_Adopters_Basic_Churn (#) = Middle_East_Africa_Low_Adopters_Basic_Addressable_Market * Middle_East_Africa_Low_Adopters_Basic_Churn_Rate / 100","Middle_East_Africa_Low_Adopters_Premium_Churn (#) = Middle_East_Africa_Low_Adopters_Premium_Addressable_Market * Middle_East_Africa_Low_Adopters_Premium_Churn_Rate / 100","Middle_East_Africa_Medium_Adopters_Basic_Churn (#) = Middle_East_Africa_Medium_Adopters_Basic_Addressable_Market * Middle_East_Africa_Medium_Adopters_Basic_Churn_Rate / 100","Middle_East_Africa_Medium_Adopters_Premium_Churn (#) = Middle_East_Africa_Medium_Adopters_Premium_Addressable_Market * Middle_East_Africa_Medium_Adopters_Premium_Churn_Rate / 100","Middle_East_Africa_High_Adopters_Basic_Churn (#) = Middle_East_Africa_High_Adopters_Basic_Addressable_Market * Middle_East_Africa_High_Adopters_Basic_Churn_Rate / 100","Middle_East_Africa_High_Adopters_Premium_Churn (#) = Middle_East_Africa_High_Adopters_Premium_Addressable_Market * Middle_East_Africa_High_Adopters_Premium_Churn_Rate / 100","Indian_Subcontinent_Low_Adopters_Basic_Churn (#) = Indian_Subcontinent_Low_Adopters_Basic_Addressable_Market * Indian_Subcontinent_Low_Adopters_Basic_Churn_Rate / 100","Indian_Subcontinent_Low_Adopters_Premium_Churn (#) = Indian_Subcontinent_Low_Adopters_Premium_Addressable_Market * Indian_Subcontinent_Low_Adopters_Premium_Churn_Rate / 100","Indian_Subcontinent_Medium_Adopters_Basic_Churn (#) = Indian_Subcontinent_Medium_Adopters_Basic_Addressable_Market * Indian_Subcontinent_Medium_Adopters_Basic_Churn_Rate / 100","Indian_Subcontinent_Medium_Adopters_Premium_Churn (#) = Indian_Subcontinent_Medium_Adopters_Premium_Addressable_Market * Indian_Subcontinent_Medium_Adopters_Premium_Churn_Rate / 100","Indian_Subcontinent_High_Adopters_Basic_Churn (#) = Indian_Subcontinent_High_Adopters_Basic_Addressable_Market * Indian_Subcontinent_High_Adopters_Basic_Churn_Rate / 100","Indian_Subcontinent_High_Adopters_Premium_Churn (#) = Indian_Subcontinent_High_Adopters_Premium_Addressable_Market * Indian_Subcontinent_High_Adopters_Premium_Churn_Rate / 100"],"Step_5:_Total_user_base":["UK_Europe_Low_Adopters_Basic_Users_Final (#) = UK_Europe_Low_Adopters_Basic_Addressable_Market - UK_Europe_Low_Adopters_Basic_Churn","UK_Europe_Low_Adopters_Premium_Users_Final (#) = UK_Europe_Low_Adopters_Premium_Addressable_Market - UK_Europe_Low_Adopters_Premium_Churn","UK_Europe_Medium_Adopters_Basic_Users_Final (#) = UK_Europe_Medium_Adopters_Basic_Addressable_Market - UK_Europe_Medium_Adopters_Basic_Churn","UK_Europe_Medium_Adopters_Premium_Users_Final (#) = UK_Europe_Medium_Adopters_Premium_Addressable_Market - UK_Europe_Medium_Adopters_Premium_Churn","UK_Europe_High_Adopters_Basic_Users_Final (#) = UK_Europe_High_Adopters_Basic_Addressable_Market - UK_Europe_High_Adopters_Basic_Churn","UK_Europe_High_Adopters_Premium_Users_Final (#) = UK_Europe_High_Adopters_Premium_Addressable_Market - UK_Europe_High_Adopters_Premium_Churn","Middle_East_Africa_Low_Adopters_Basic_Users_Final (#) = Middle_East_Africa_Low_Adopters_Basic_Addressable_Market - Middle_East_Africa_Low_Adopters_Basic_Churn","Middle_East_Africa_Low_Adopters_Premium_Users_Final (#) = Middle_East_Africa_Low_Adopters_Premium_Addressable_Market - Middle_East_Africa_Low_Adopters_Premium_Churn","Middle_East_Africa_Medium_Adopters_Basic_Users_Final (#) = Middle_East_Africa_Medium_Adopters_Basic_Addressable_Market - Middle_East_Africa_Medium_Adopters_Basic_Churn","Middle_East_Africa_Medium_Adopters_Premium_Users_Final (#) = Middle_East_Africa_Medium_Adopters_Premium_Addressable_Market - Middle_East_Africa_Medium_Adopters_Premium_Churn","Middle_East_Africa_High_Adopters_Basic_Users_Final (#) = Middle_East_Africa_High_Adopters_Basic_Addressable_Market - Middle_East_Africa_High_Adopters_Basic_Churn","Middle_East_Africa_High_Adopters_Premium_Users_Final (#) = Middle_East_Africa_High_Adopters_Premium_Addressable_Market - Middle_East_Africa_High_Adopters_Premium_Churn","Indian_Subcontinent_Low_Adopters_Basic_Users_Final (#) = Indian_Subcontinent_Low_Adopters_Basic_Addressable_Market - Indian_Subcontinent_Low_Adopters_Basic_Churn","Indian_Subcontinent_Low_Adopters_Premium_Users_Final (#) = Indian_Subcontinent_Low_Adopters_Premium_Addressable_Market - Indian_Subcontinent_Low_Adopters_Premium_Churn","Indian_Subcontinent_Medium_Adopters_Basic_Users_Final (#) = Indian_Subcontinent_Medium_Adopters_Basic_Addressable_Market - Indian_Subcontinent_Medium_Adopters_Basic_Churn","Indian_Subcontinent_Medium_Adopters_Premium_Users_Final (#) = Indian_Subcontinent_Medium_Adopters_Premium_Addressable_Market - Indian_Subcontinent_Medium_Adopters_Premium_Churn","Indian_Subcontinent_High_Adopters_Basic_Users_Final (#) = Indian_Subcontinent_High_Adopters_Basic_Addressable_Market - Indian_Subcontinent_High_Adopters_Basic_Churn","Indian_Subcontinent_High_Adopters_Premium_Users_Final (#) = Indian_Subcontinent_High_Adopters_Premium_Addressable_Market - Indian_Subcontinent_High_Adopters_Premium_Churn","Total_Basic_Users (#) = UK_Europe_Low_Adopters_Basic_Users_Final + UK_Europe_Medium_Adopters_Basic_Users_Final + UK_Europe_High_Adopters_Basic_Users_Final + Middle_East_Africa_Low_Adopters_Basic_Users_Final + Middle_East_Africa_Medium_Adopters_Basic_Users_Final + Middle_East_Africa_High_Adopters_Basic_Users_Final + Indian_Subcontinent_Low_Adopters_Basic_Users_Final + Indian_Subcontinent_Medium_Adopters_Basic_Users_Final + Indian_Subcontinent_High_Adopters_Basic_Users_Final","Total_Premium_Users (#) = UK_Europe_Low_Adopters_Premium_Users_Final + UK_Europe_Medium_Adopters_Premium_Users_Final + UK_Europe_High_Adopters_Premium_Users_Final + Middle_East_Africa_Low_Adopters_Premium_Users_Final + Middle_East_Africa_Medium_Adopters_Premium_Users_Final + Middle_East_Africa_High_Adopters_Premium_Users_Final + Indian_Subcontinent_Low_Adopters_Premium_Users_Final + Indian_Subcontinent_Medium_Adopters_Premium_Users_Final + Indian_Subcontinent_High_Adopters_Premium_Users_Final","Total_User_Base (#) = Total_Basic_Users + Total_Premium_Users"]}

assumptions =  {"UK_Europe_Population":748000000,"Middle_East_Africa_Population":1800000000,"Indian_Subcontinent_Population":2000000000,"UK_Europe_AI_Non_Adopters_Share (%)":40,"UK_Europe_AI_Low_Adopters_Share (%)":35,"UK_Europe_AI_Medium_Adopters_Share (%)":20,"UK_Europe_AI_High_Adopters_Share (%)":5,"Middle_East_Africa_AI_Non_Adopters_Share (%)":60,"Middle_East_Africa_AI_Low_Adopters_Share (%)":25,"Middle_East_Africa_AI_Medium_Adopters_Share (%)":12,"Middle_East_Africa_AI_High_Adopters_Share (%)":3,"Indian_Subcontinent_AI_Non_Adopters_Share (%)":70,"Indian_Subcontinent_AI_Low_Adopters_Share (%)":20,"Indian_Subcontinent_AI_Medium_Adopters_Share (%)":8,"Indian_Subcontinent_AI_High_Adopters_Share (%)":2,"Low_Adopters_Basic_Subscription_Rate (%)":3,"Low_Adopters_Premium_Subscription_Rate (%)":2,"Medium_Adopters_Basic_Subscription_Rate (%)":15,"Medium_Adopters_Premium_Subscription_Rate (%)":10,"High_Adopters_Basic_Subscription_Rate (%)":25,"High_Adopters_Premium_Subscription_Rate (%)":35,"UK_Europe_Population_Growth_Rate (%)":2.3,"Middle_East_Africa_Population_Growth_Rate (%)":2.8,"Indian_Subcontinent_Population_Growth_Rate (%)":2.5,"UK_Europe_Low_Adopters_Basic_Market_Share (%)":2.5,"UK_Europe_Low_Adopters_Premium_Market_Share (%)":3.5,"UK_Europe_Medium_Adopters_Basic_Market_Share (%)":6,"UK_Europe_Medium_Adopters_Premium_Market_Share (%)":8,"UK_Europe_High_Adopters_Basic_Market_Share (%)":12,"UK_Europe_High_Adopters_Premium_Market_Share (%)":15,"Middle_East_Africa_Low_Adopters_Basic_Market_Share (%)":1.5,"Middle_East_Africa_Low_Adopters_Premium_Market_Share (%)":2.5,"Middle_East_Africa_Medium_Adopters_Basic_Market_Share (%)":4,"Middle_East_Africa_Medium_Adopters_Premium_Market_Share (%)":5,"Middle_East_Africa_High_Adopters_Basic_Market_Share (%)":10,"Middle_East_Africa_High_Adopters_Premium_Market_Share (%)":12,"Indian_Subcontinent_Low_Adopters_Basic_Market_Share (%)":1,"Indian_Subcontinent_Low_Adopters_Premium_Market_Share (%)":2,"Indian_Subcontinent_Medium_Adopters_Basic_Market_Share (%)":3,"Indian_Subcontinent_Medium_Adopters_Premium_Market_Share (%)":4,"Indian_Subcontinent_High_Adopters_Basic_Market_Share (%)":8,"Indian_Subcontinent_High_Adopters_Premium_Market_Share (%)":10,"UK_Europe_Low_Adopters_Basic_Churn_Rate (%)":15,"UK_Europe_Low_Adopters_Premium_Churn_Rate (%)":12,"UK_Europe_Medium_Adopters_Basic_Churn_Rate (%)":10,"UK_Europe_Medium_Adopters_Premium_Churn_Rate (%)":8,"UK_Europe_High_Adopters_Basic_Churn_Rate (%)":5,"UK_Europe_High_Adopters_Premium_Churn_Rate (%)":3,"Middle_East_Africa_Low_Adopters_Basic_Churn_Rate (%)":18,"Middle_East_Africa_Low_Adopters_Premium_Churn_Rate (%)":15,"Middle_East_Africa_Medium_Adopters_Basic_Churn_Rate (%)":12,"Middle_East_Africa_Medium_Adopters_Premium_Churn_Rate (%)":10,"Middle_East_Africa_High_Adopters_Basic_Churn_Rate (%)":6,"Middle_East_Africa_High_Adopters_Premium_Churn_Rate (%)":4,"Indian_Subcontinent_Low_Adopters_Basic_Churn_Rate (%)":20,"Indian_Subcontinent_Low_Adopters_Premium_Churn_Rate (%)":18,"Indian_Subcontinent_Medium_Adopters_Basic_Churn_Rate (%)":15,"Indian_Subcontinent_Medium_Adopters_Premium_Churn_Rate (%)":12,"Indian_Subcontinent_High_Adopters_Basic_Churn_Rate (%)":8,"Indian_Subcontinent_High_Adopters_Premium_Churn_Rate (%)":6}
user_input = "I wan to update"
user_description =  "I want to open a competitor for OpenAI which provides 2 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model. I want to operate in both India, Dubai and London"

# def generate_response(formula, assumptions, user_input, user_description):
#     prompt = generate_user_base_assumption_formula_update_prompt(formula, assumptions, user_input, user_description)
#     response = client.messages.create(
#         model="claude-sonnet-4-20250514",#"claude-3-5-sonnet-20241022",
#         max_tokens=20192,
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return response.content[0].text

def get_user_base_assumptions_formula_update_response(formula, assumptions, user_input, user_description):
    prompt = generate_user_base_assumption_formula_update_prompt(formula,assumptions, user_input, user_description)
    pdb.set_trace()
    try: 
        response = client.messages.create(
            model="claude-sonnet-4-20250514",#"claude-3-5-sonnet-20241022",
            max_tokens=12192,
            messages=[{"role": "user", "content": prompt}]
        )

        # Check if the response is empty
        if not response.content :
            print(f"No updated content returned during update user base formula")
            return None

        # Ensure the response content is handled whether it's a list or a string
        if isinstance(response.content, list):
            # Access the actual text in the list of TextBlock objects
            response_text = response.content[0].text if response.content else None
            #print(f'the response text in function is {response_text} ')

        elif isinstance(response.content, str):
            response_text = response.content.strip()
            #print(f"response text if string {response_text}")

        else:
            print(f"Unexpected response format")
            return None

        # Ensure the response content is a valid JSON string
        if  not response_text or response_text == "":
            print(f"Empty or invalid response received ")
            return None

        # Parse the response as JSON
        try:
            parameters_match = re.search(r'"parameters":\s*{.*?}', response_text, re.DOTALL)
            formula_match = re.search(r'"formula":\s*{.*?}', response_text, re.DOTALL)   
            assumptions = json.loads(f"{{{parameters_match.group(0)}}}") if parameters_match else {}
            formula = json.loads(f"{{{formula_match.group(0)}}}") if formula_match else {}        


            # Return the final structured analysis
            return {
                "assumptions": {**assumptions['parameters']}, 
                "formula": formula
            }

        except json.JSONDecodeError as e:
            print(f"Error parsing JSON in update user base formula: {e}")
            return None

    except Exception as e:
        print(f"Error fetching or parsing response from update user base formula")
        return None

output = get_user_base_assumptions_formula_update_response(formula, assumptions, user_input, user_description)
print(output)
