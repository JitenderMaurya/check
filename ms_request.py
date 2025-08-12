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
description_payload = {
    "user_description": "I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model, and want to have the model for 5 years straight, starting from 2026 January. I want to operate in both India, Dubai and London"
}

product_name = requests.post(
    f"{BASE_URL}/get_product_name",
    json=description_payload,
    proxies=proxies
)

print("\nResponse from /get_product_name:")
print(product_name.text)

#...................................
description_payload = {
    "product_name":product_name.text,
    "user_description": "I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model, and want to have the model for 5 years straight, starting from 2026 January. I want to operate in both India, Dubai and London",
    "country":"USA",
    "perform":"Estimate Market Size Quantity"
}

product_logic = requests.post(
    f"{BASE_URL}/get_product_logic",
    json=description_payload,
    proxies=proxies
)

print("\nResponse from /product_logic:")
print(product_logic.text)

###.....................................
steps = json.loads(product_logic.text)
description_payload = {
    "product_name":product_name.text,
    "user_description": "I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model, and want to have the model for 5 years straight, starting from 2026 January. I want to operate in both India, Dubai and London",
    "country":"USA",
    "perform":"Estimate Market Size Quantity",
    "current_logic":steps["product_logic"],
    "user_instruction":"remove step 4",
}

new_product_logic = requests.post(
    f"{BASE_URL}/update_product_logic",
    json=description_payload,
    proxies=proxies
)

print("\nResponse from /new_product_logic:")
print(new_product_logic.text)
'''
#.........................................................
logic= "Step 1: Estimate the total addressable population of potential LLM users (businesses, developers, researchers) in India, Dubai,\
    and London. Step 2: Segment the market into enterprise, SMB, individual developer, and academic user categories for each geographic \
    region.Step 3: Calculate the penetration rate of AI/LLM adoption for each user segment in each target market. Step 4: Estimate \
        the subscription distribution across your 4 different LLM subscription tiers for each user segment.Step 5: Project the annual \
            growth rate of LLM adoption and market expansion from 2026-2031 for each region. Step 6: Calculate the total quantity of \
                subscriptions by multiplying addressable users by penetration rates and tier distribution across all markets."

product = "LLM subscriptions"
user_descriptions = "I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model, and want to have the model for 5 years straight, starting from 2026 January. I want to operate in both India, Dubai and London"
perform="Estimate Market Size Quantity"#"Estimate Market Size Revenue"#
cases ={"scenario":["base", "conservative", "aggresive"],"additional_scenario":["include the effect of flood in the country", "include the effect of high inflation"]}
country = "USA"
currency = "USD"
interval = "halfyearly"
analysis_time_period = ["H1 2025", "H2 2025", "H1 2026"]

description_payload = {
    "product":product,
    "user_descriptions":user_descriptions,
    "logic":logic,
    "cases":cases,
    "perform":perform,
    "country":country,
    "currency":currency,
    "interval":interval,
    "analysis_time_period":analysis_time_period
}

# ms_assumption_formula = requests.post(
#     f"{BASE_URL}/get_market_sizing_assumption_formula",
#     json=description_payload,
#     proxies=proxies
# )

# print("\nResponse from /get_market_sizing_assumption_formula:")
# print(ms_assumption_formula.text)


# #....................................................
# formula = json.loads(ms_assumption_formula.text)["formula"]
# assumptions = json.loads(ms_assumption_formula.text)["assumptions"]
# additional_assumptions = json.loads(ms_assumption_formula.text)["additional_assumptions"]
#pdb.set_trace()
formula ={'Step_1_Addressable_Users_by_Segment': ['India_Enterprise_Users (#) = India_Total_Businesses * Enterprise_Segment_Ratio / 100', 'India_SMB_Users (#) = India_Total_Businesses * SMB_Segment_Ratio / 100', 'Dubai_Enterprise_Users (#) = Dubai_Total_Businesses * Enterprise_Segment_Ratio / 100', 'Dubai_SMB_Users (#) = Dubai_Total_Businesses * SMB_Segment_Ratio / 100', 'London_Enterprise_Users (#) = London_Total_Businesses * Enterprise_Segment_Ratio / 100', 'London_SMB_Users (#) = London_Total_Businesses * SMB_Segment_Ratio / 100', 'India_Academic_Users (#) = India_Academic_Institutions * Academic_Users_per_Institution', 'Dubai_Academic_Users (#) = Dubai_Academic_Institutions * Academic_Users_per_Institution', 'London_Academic_Users (#) = London_Academic_Institutions * Academic_Users_per_Institution'], 'Step_2_Penetrated_Users_by_Segment': ['India_Enterprise_Penetrated (#) = India_Enterprise_Users * India_Enterprise_Penetration_Rate / 100', 'India_SMB_Penetrated (#) = India_SMB_Users * India_SMB_Penetration_Rate / 100', 'India_Developer_Penetrated (#) = India_Individual_Developers * India_Developer_Penetration_Rate / 100', 'India_Academic_Penetrated (#) = India_Academic_Users * India_Academic_Penetration_Rate / 100', 'Dubai_Enterprise_Penetrated (#) = Dubai_Enterprise_Users * Dubai_Enterprise_Penetration_Rate / 100', 'Dubai_SMB_Penetrated (#) = Dubai_SMB_Users * Dubai_SMB_Penetration_Rate / 100', 'Dubai_Developer_Penetrated (#) = Dubai_Individual_Developers * Dubai_Developer_Penetration_Rate / 100', 'Dubai_Academic_Penetrated (#) = Dubai_Academic_Users * Dubai_Academic_Penetration_Rate / 100', 'London_Enterprise_Penetrated (#) = London_Enterprise_Users * London_Enterprise_Penetration_Rate / 100', 'London_SMB_Penetrated (#) = London_SMB_Users * London_SMB_Penetration_Rate / 100', 'London_Developer_Penetrated (#) = London_Individual_Developers * London_Developer_Penetration_Rate / 100', 'London_Academic_Penetrated (#) = London_Academic_Users * London_Academic_Penetration_Rate / 100'], 'Step_3_Total_Penetrated_Users_by_Region': ['India_Total_Penetrated_Users (#) = India_Enterprise_Penetrated + India_SMB_Penetrated + India_Developer_Penetrated + India_Academic_Penetrated', 'Dubai_Total_Penetrated_Users (#) = Dubai_Enterprise_Penetrated + Dubai_SMB_Penetrated + Dubai_Developer_Penetrated + Dubai_Academic_Penetrated', 'London_Total_Penetrated_Users (#) = London_Enterprise_Penetrated + London_SMB_Penetrated + London_Developer_Penetrated + London_Academic_Penetrated'], 'Step_4_Subscription_Distribution_by_Tier': ['Global_Total_Users (#) = India_Total_Penetrated_Users + Dubai_Total_Penetrated_Users + London_Total_Penetrated_Users', 'Tier_1_Subscriptions (#) = Global_Total_Users * Tier_1_Subscription_Distribution / 100', 'Tier_2_Subscriptions (#) = Global_Total_Users * Tier_2_Subscription_Distribution / 100', 'Tier_3_Subscriptions (#) = Global_Total_Users * Tier_3_Subscription_Distribution / 100', 'Tier_4_Subscriptions (#) = Global_Total_Users * Tier_4_Subscription_Distribution / 100'], 'Step_5_Final_Market_Size_with_Scenario_Impact': ['Total_LLM_Subscriptions_Base (#) = Tier_1_Subscriptions + Tier_2_Subscriptions + Tier_3_Subscriptions + Tier_4_Subscriptions', 'Flood_Impact_Reduction (#) = Total_LLM_Subscriptions_Base * flood_impact_factor / 100', 'Inflation_Impact_Reduction (#) = Total_LLM_Subscriptions_Base * high_inflation_impact_factor / 100', 'Total_Market_Size_Quantity (#) = (Total_LLM_Subscriptions_Base - Flood_Impact_Reduction - Inflation_Impact_Reduction) * Halfyearly_Period_Factor']}
#json.loads(ms_assumption_formula.text)["formula"]
assumptions={'India_Total_Businesses (#)': 63400000, 'Dubai_Total_Businesses (#)': 450000, 'London_Total_Businesses (#)': 850000, 'India_Individual_Developers (#)': 4800000, 'Dubai_Individual_Developers (#)': 75000, 'London_Individual_Developers (#)': 320000, 'India_Academic_Institutions (#)': 52000, 'Dubai_Academic_Institutions (#)': 180, 'London_Academic_Institutions (#)': 450, 'India_Enterprise_Penetration_Rate (%)': 15, 'Dubai_Enterprise_Penetration_Rate (%)': 25, 'London_Enterprise_Penetration_Rate (%)': 35, 'India_SMB_Penetration_Rate (%)': 8, 'Dubai_SMB_Penetration_Rate (%)': 18, 'London_SMB_Penetration_Rate (%)': 28, 'India_Developer_Penetration_Rate (%)': 12, 'Dubai_Developer_Penetration_Rate (%)': 22, 'London_Developer_Penetration_Rate (%)': 30, 'India_Academic_Penetration_Rate (%)': 20, 'Dubai_Academic_Penetration_Rate (%)': 35, 'London_Academic_Penetration_Rate (%)': 45, 'Enterprise_Segment_Ratio (%)': 5, 'SMB_Segment_Ratio (%)': 95, 'Tier_1_Subscription_Distribution (%)': 45, 'Tier_2_Subscription_Distribution (%)': 30, 'Tier_3_Subscription_Distribution (%)': 20, 'Tier_4_Subscription_Distribution (%)': 5, 'Academic_Users_per_Institution': 150, 'Halfyearly_Period_Factor': 0.5}#json.loads(ms_assumption_formula.text)["assumptions"]
additional_assumptions={'flood_impact_factor (%)': 15, 'high_inflation_impact_factor (%)': 20}#json.loads(ms_assumption_formula.text)["additional_assumptions"]
'''
instruction = "make the formula compact"
description_payload = {
    "product":product,
    "user_descriptions":user_descriptions,
    "logic":logic,
    "cases":cases,
    "perform":perform,
    "country":country,
    "currency":currency,
    "interval":interval,
    "analysis_time_period":analysis_time_period,
    "formula":formula,
    "assumptions":assumptions,
    "additional_assumptions":additional_assumptions,
    "instruction":instruction,
}

updated_ms_assumption_formula = requests.post(
    f"{BASE_URL}/update_market_sizing_assumption_formula",
    json=description_payload,
    proxies=proxies
)

print("\nResponse from /update_market_sizing_assumption_formula:")
print(updated_ms_assumption_formula.text)

'''
description_payload = {
    "formula":formula,
    "assumptions":assumptions,
    "analysis_time_frame": ["H1 2025", "H2 2025", "H1 2026"],
    "period_ranges": [["January", "June", "2025"],["July", "December", "2025"], ["January", "June", "2026"]],
    "product":product,
    "currency":"USD",
    "scenario":["Base","conservative","aggresive"],
}

# ms_assumption_values = requests.post(
#     f"{BASE_URL}/get_market_sizing_assumption_values",
#     json=description_payload,
#     proxies=proxies
# )

# print("\nResponse from /get_market_sizing_assumption_values:")
# print(ms_assumption_values.text)

#....................................................
#pdb.set_trace()
Steps = ["Step_1_Addressable_Users_by_Segment","London_Academic_Institutions","Enterprise_Segment_Ratio","Dubai_Total_Businesses","London_Total_Businesses","India_Academic_Institutions","Academic_Users_per_Institution","India_Total_Businesses","SMB_Segment_Ratio","Dubai_Academic_Institutions","Step_2_Penetrated_Users_by_Segment","Dubai_Enterprise_Penetration_Rate","Dubai_Developer_Penetration_Rate","India_Individual_Developers","India_Developer_Penetration_Rate","India_Academic_Penetration_Rate","India_SMB_Penetration_Rate","India_Enterprise_Penetration_Rate","London_Individual_Developers","Dubai_Academic_Penetration_Rate","London_Developer_Penetration_Rate","Dubai_Individual_Developers","London_SMB_Penetration_Rate","London_Academic_Penetration_Rate","London_Enterprise_Penetration_Rate","Dubai_SMB_Penetration_Rate","Step_3_Total_Penetrated_Users_by_Region","Step_4_Subscription_Distribution_by_Tier","Tier_2_Subscription_Distribution","Tier_3_Subscription_Distribution","Tier_1_Subscription_Distribution","Tier_4_Subscription_Distribution","Step_5_Final_Market_Size_with_Scenario_Impact","Halfyearly_Period_Factor","flood_impact_factor","high_inflation_impact_factor"]
Units = ["","#","%","#","#","#","#","#","%","#","","%","%","#","%","%","%","%","#","%","%","#","%","%","%","%","","","%","%","%","%","","#","%","%"]
#Values{"U":{"H1 2025":["",450,5,450000,850000,52000,150,63400000,95,180,"",25,22,4800000,12,20,8,15,320000,35,30,75000,28,45,35,18,"","",30,20,45,5,"",0.5],"H2 2025":["",465,5.2,468000,876000,54080,158,65908000,94.8,189,"",28,25,5280000,14,23,10,18,352000,38,33,82500,31,48,38,21,"","",32,22,42,4,"",0.5],"H1 2026":["",480,5.4,486240,902880,56243,166,68543280,94.6,198,"",31,28,5808000,16,26,12,21,387200,41,36,90750,34,51,41,24,"","",34,24,39,3,"",0.5]},"S":{"H1 2025":["",465,5.2,468120,876440,54122,158,65971640,94.8,189,"",22,19,4176000,10,17,6,12,278400,31,26,65250,24,39,29,14,"","",27,17,51,5,"",0.5],"H2 2025":["",480,5.4,486365,903201,56286,166,68623509,94.6,198,"",19,16,3627840,8,14,4,9,242112,27,22,56738,20,33,23,10,"","",24,14,57,5,"",0.5],"H1 2026":["",510,5.8,525842,960733,60895,183,74272270,94.2,218,"",16,14,3200000,7,12,3,7,210000,23,19,48000,16,28,18,8,"","",22,12,61,5,"",0.5]},"D":{"H1 2025":["",420,4.2,387500,739250,43600,117,52527500,95.8,142,"",34,30,6400000,17,28,13,23,430000,47,41,102000,40,62,52,28,"","",38,28,29,5,"",0.5],"H2 2025":["",385,3.5,325000,625000,35000,85,42500000,96.5,105,"",45,40,8500000,23,38,19,33,575000,62,55,135000,55,82,72,40,"","",48,38,10,4,"",0.5],"H1 2026":["",350,2.8,275000,530000,28500,65,35800000,97.2,85,"",55,48,10200000,28,45,23,40,680000,75,65,160000,65,95,85,48,"","",55,42,2,1,"",0.5]}}}
steps = ['Step_1_Addressable_Users_by_Segment', 'London_Academic_Institutions', 'Enterprise_Segment_Ratio', 'Dubai_Total_Businesses', 'London_Total_Businesses', 'India_Academic_Institutions', 'Academic_Users_per_Institution', 'India_Total_Businesses', 'SMB_Segment_Ratio', 'Dubai_Academic_Institutions', 'Step_2_Penetrated_Users_by_Segment', 'Dubai_Enterprise_Penetration_Rate', 'Dubai_Developer_Penetration_Rate', 'India_Individual_Developers', 'India_Developer_Penetration_Rate', 'India_Academic_Penetration_Rate', 'India_SMB_Penetration_Rate', 'India_Enterprise_Penetration_Rate', 'London_Individual_Developers', 'Dubai_Academic_Penetration_Rate', 'London_Developer_Penetration_Rate', 'Dubai_Individual_Developers', 'London_SMB_Penetration_Rate', 'London_Academic_Penetration_Rate', 'London_Enterprise_Penetration_Rate', 'Dubai_SMB_Penetration_Rate', 'Step_3_Total_Penetrated_Users_by_Region', 'Step_4_Subscription_Distribution_by_Tier', 'Tier_2_Subscription_Distribution', 'Tier_3_Subscription_Distribution', 'Tier_1_Subscription_Distribution', 'Tier_4_Subscription_Distribution', 'Step_5_Final_Market_Size_with_Scenario_Impact', 'Halfyearly_Period_Factor',"flood_impact_factor","high_inflation_impact_factor"]#json.loads(ms_assumption_values.text)["Steps"]
Units = ['', '#', '%', '#', '#', '#', '#', '#', '%', '#', '', '%', '%', '#', '%', '%', '%', '%', '#', '%', '%', '#', '%', '%', '%', '%', '', '', '%', '%', '%', '%', '', '#',"%","%"]#json.loads(ms_assumption_values.text)["Units"]
Values = {'Base': {'H1 2025': ['', 450, 5, 450000, 850000, 52000, 150, 63400000, 95, 180, '', 25, 22, 4800000, 12, 20, 8, 15, 320000, 35, 30, 75000, 28, 45, 35, 18, '', '', 30, 20, 45, 5, '', 0.5, 15, 20], 'H2 2025': ['', 465, 5.2, 468000, 876000, 54080, 158, 65908000, 94.8, 189, '', 28, 25, 5280000, 14, 23, 10, 18, 352000, 38, 33, 82500, 31, 48, 38, 21, '', '', 32, 22, 42, 4, '', 0.5,15,20], 'H1 2026': ['', 480, 5.4, 486240, 902880, 56243, 166, 68543280, 94.6, 198, '', 31, 28, 5808000, 16, 26, 12, 21, 387200, 41, 36, 90750, 34, 51, 41, 24, '', '', 34, 24, 39, 3, '', 0.5,15, 20]}, 'Conservative': {'H1 2025': ['', 465, 5.2, 468120, 876440, 54122, 158, 65971640, 94.8, 189, '', 22, 19, 4176000, 10, 17, 6, 12, 278400, 31, 26, 65250, 24, 39, 29, 14, '', '', 27, 17, 51, 5, '', 0.5,15,20], 'H2 2025': ['', 480, 5.4, 486365, 903201, 56286, 166, 68623509, 94.6, 198, '', 19, 16, 3627840, 8, 14, 4, 9, 242112, 27, 22, 56738, 20, 33, 23, 10, '', '', 24, 14, 57, 5, '', 0.5,15,20], 'H1 2026': ['', 510, 5.8, 525842, 960733, 60895, 183, 74272270, 94.2, 218, '', 16, 14, 3200000, 7, 12, 3, 7, 210000, 23, 19, 48000, 16, 28, 18, 8, '', '', 22, 12, 61, 5, '', 0.5,15,20]}, 'Aggresive': {'H1 2025': ['', 420, 4.2, 387500, 739250, 43600, 117, 52527500, 95.8, 142, '', 34, 30, 6400000, 17, 28, 13, 23, 430000, 47, 41, 102000, 40, 62, 52, 28, '', '', 38, 28, 29, 5, '', 0.5,15,20], 'H2 2025': ['', 385, 3.5, 325000, 625000, 35000, 85, 42500000, 96.5, 105, '', 45, 40, 8500000, 23, 38, 19, 33, 575000, 62, 55, 135000, 55, 82, 72, 40, '', '', 48, 38, 10, 4, '', 0.5,15,20], 'H1 2026': ['', 350, 2.8, 275000, 530000, 28500, 65, 35800000, 97.2, 85, '', 55, 48, 10200000, 28, 45, 23, 40, 680000, 75, 65, 160000, 65, 95, 85, 48, '', '', 55, 42, 2, 1, '', 0.5,15,20]}}#json.loads(ms_assumption_values.text)["Values"]
description_payload = {
    "assumption_values":Values,
    "units":Units,
    "currency": "USD",
    "formula":formula,
    "steps":steps
}

computed_market_size = requests.post(
    f"{BASE_URL}/market_size_compute",
    json=description_payload,
    proxies=proxies
)

print("\nResponse from /computed_market_size:")
print(computed_market_size.text)