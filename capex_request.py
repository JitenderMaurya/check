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


#......................................................................................Update Revenue..............
price_key = ['base_subscription_quarterly_price (USD)', 'premium_subscription_halfyearly_price (USD)', 'premium_subscription_yearly_price (USD)', 'executive_subscriptions_yearly_price (USD)', 'extramile_subscriptions_yearly_price (USD)']
rev_formula = {'Step 1: Identify user across different product/services': ['Total_user_base = Europe_user + India_user + Dubai_user', 'Basic_LLM_users = Total_user_base * (Basic_LLM (%) / 100) + Total_user_base * (Basic_LLM_and_Standard_LLM (%) / 100) + Total_user_base * (Basic_LLM_and_Executive_LLM (%) / 100)', 'Standard_LLM_users = Total_user_base * (Standard_LLM (%) / 100) + Total_user_base * (Basic_LLM_and_Standard_LLM (%) / 100)', 'Executive_LLM_users = Total_user_base * (Executive_LLM (%) / 100) + Total_user_base * (Basic_LLM_and_Executive_LLM (%) / 100)'], 'Step 2: Breakdown the user base by plan tenure': ['Basic_LLM_monthly_billing_users = Basic_LLM_users * (Basic_LLM_monthly_share (%) / 100) * (monthly_effective_rate (%) / 100)', 'Basic_LLM_quarterly_billing_users = Basic_LLM_users * (Basic_LLM_quarterly_share (%) / 100) * (quarterly_effective_rate (%) / 100)', 'Standard_LLM_quarterly_billing_users = Standard_LLM_users * (Standard_LLM_quarterly_share (%) / 100) * (quarterly_effective_rate (%) / 100)', 'Standard_LLM_halfyearly_billing_users = Standard_LLM_users * (Standard_LLM_halfyearly_share (%) / 100) * (halfyearly_effective_rate (%) / 100)', 'Executive_LLM_halfyearly_billing_users = Executive_LLM_users * (Executive_LLM_halfyearly_share (%) / 100) * (halfyearly_effective_rate (%) / 100)'], 'Step 3: Identify the pricing rate for each product/services': ['Basic_LLM_monthly_discounted_price (USD) = (Basic_LLM_monthly_price * (12 - Basic_LLM_monthly_discount_period) + Basic_LLM_monthly_price * Basic_LLM_monthly_discount_period * (100 - Basic_LLM_monthly_discount) / 100) / 12', 'Basic_LLM_quarterly_discounted_price (USD) = (Basic_LLM_quarterly_price * (12 - Basic_LLM_quarterly_discount_period) + Basic_LLM_quarterly_price * Basic_LLM_quarterly_discount_period * (100 - Basic_LLM_quarterly_discount) / 100) / 12', 'Standard_LLM_quarterly_discounted_price (USD) = (Standard_LLM_quarterly_price * (12 - Standard_LLM_quarterly_discount_period) + Standard_LLM_quarterly_price * Standard_LLM_quarterly_discount_period * (100 - Standard_LLM_quarterly_discount) / 100) / 12', 'Standard_LLM_halfyearly_discounted_price (USD) = (Standard_LLM_halfyearly_price * (12 - Standard_LLM_halfyearly_discount_period) + Standard_LLM_halfyearly_price * Standard_LLM_halfyearly_discount_period * (100 - Standard_LLM_halfyearly_discount) / 100) / 12', 'Executive_LLM_halfyearly_discounted_price (USD) = (Executive_LLM_halfyearly_price * (12 - Executive_LLM_halfyearly_discount_period) + Executive_LLM_halfyearly_price * Executive_LLM_halfyearly_discount_period * (100 - Executive_LLM_halfyearly_discount) / 100) / 12'], 'Step 4: Revenue computation for each product line': ['Basic_LLM_Revenue (USD) = Basic_LLM_monthly_billing_users * Basic_LLM_monthly_discounted_price * 12 + Basic_LLM_quarterly_billing_users * Basic_LLM_quarterly_discounted_price * 4', 'Standard_LLM_Revenue (USD) = Standard_LLM_quarterly_billing_users * Standard_LLM_quarterly_discounted_price * 4 + Standard_LLM_halfyearly_billing_users * Standard_LLM_halfyearly_discounted_price * 2', 'Executive_LLM_Revenue (USD) = Executive_LLM_halfyearly_billing_users * Executive_LLM_halfyearly_discounted_price * 2'], 'Step 5: Total revenue from all product/services': ['LLM_Subscription_Revenue (USD) = Basic_LLM_Revenue + Standard_LLM_Revenue + Executive_LLM_Revenue', 'Additional_Revenue (USD) = LLM_Subscription_Revenue * (Additional_Revenue_Contribution (%) / 100)', 'Total_Company_Revenue (USD) = LLM_Subscription_Revenue + Additional_Revenue']}
rev_assumption={'Basic_LLM (%)': 20, 'Standard_LLM (%)': 30, 'Executive_LLM (%)': 20, 'Basic_LLM_and_Standard_LLM (%)': 15, 'Basic_LLM_and_Executive_LLM (%)': 15, 'Basic_LLM_monthly_share (%)': 65, 'Basic_LLM_quarterly_share (%)': 35, 'Standard_LLM_quarterly_share (%)': 55, 'Standard_LLM_halfyearly_share (%)': 45, 'Executive_LLM_halfyearly_share (%)': 100, 'monthly_effective_rate (%)': 85, 'quarterly_effective_rate (%)': 92, 'halfyearly_effective_rate (%)': 95, 'Basic_LLM_monthly_price (USD)': 60, 'Basic_LLM_quarterly_price (USD)': 180, 'Standard_LLM_quarterly_price (USD)': 360, 'Standard_LLM_halfyearly_price (USD)': 600, 'Executive_LLM_halfyearly_price (USD)': 1200, 'Basic_LLM_monthly_discount (%)': 15, 'Basic_LLM_quarterly_discount (%)': 20, 'Standard_LLM_quarterly_discount (%)': 18, 'Standard_LLM_halfyearly_discount (%)': 25, 'Executive_LLM_halfyearly_discount (%)': 30, 'Basic_LLM_monthly_discount_period (month)': 2, 'Basic_LLM_quarterly_discount_period (month)': 3, 'Standard_LLM_quarterly_discount_period (month)': 2, 'Standard_LLM_halfyearly_discount_period (month)': 4, 'Executive_LLM_halfyearly_discount_period (month)': 3, 'Additional_Revenue_Contribution (%)': 6}

# description_payload = {
#     "user_description":"I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model, and want to have the model for 5 years straight, starting from 2026 January. I want to operate in both India, Dubai and London",
#     "total_user": ["Europe_user", "India_user","Dubai_user"],
#     "billing": "Basic_LLM is billed monthly and quaterly, Standard_LLM is billed quaterly and halfyearly and Executive_LLM is billed halfyearly",
#     "additional_revenue": f"yes, consider 6% of the total revene obtained from the LLM subscriptions", 
#     "revenue_sources_splits":["Basic_LLM", "Standard_LLM", "Executive_LLM"],
#     "currency": "USD",
#     "interval": "yearly",
#     "price_key":price_key,
#     "revenue_formula":rev_formula,
#     "revenue_assumption":rev_assumption,
#     "instruction":"make the revenue formula compact and consize"
# }    


# updated_revenue_assumption_formula = requests.post(
#     f"{BASE_URL}/update_revenue_formula_assumption",
#     json=description_payload,
#     proxies=proxies
# )

# print("\nResponse from /update revenue_assumption_formula.....................")
# print(updated_revenue_assumption_formula.text)


#.............................................Get assumption values


#.......

steps=["Step 1: Identify user across different product/services","Basic_LLM_and_Executive_LLM","Standard_LLM","Basic_LLM","Executive_LLM","Basic_LLM_and_Standard_LLM","Step 2: Breakdown the user base by plan tenure","quarterly_effective_rate","halfyearly_effective_rate","Basic_LLM_quarterly_share","monthly_effective_rate","Standard_LLM_quarterly_share","Standard_LLM_halfyearly_share","Basic_LLM_monthly_share","Executive_LLM_halfyearly_share","Step 3: Identify the pricing rate for each product/services","Basic_LLM_monthly_discount_period","Standard_LLM_halfyearly_discount","Standard_LLM_quarterly_discount","Executive_LLM_halfyearly_price","Standard_LLM_quarterly_price","Standard_LLM_quarterly_discount_period","Executive_LLM_halfyearly_discount","Basic_LLM_quarterly_discount","Executive_LLM_halfyearly_discount_period","Basic_LLM_monthly_discount","Basic_LLM_monthly_price","Basic_LLM_quarterly_price","Basic_LLM_quarterly_discount_period","Standard_LLM_halfyearly_price","Standard_LLM_halfyearly_discount_period","Step 4: Revenue computation for each product line","Step 5: Total revenue from all product/services","Additional_Revenue_Contribution"]
units=["","%","%","%","%","%","","%","%","%","%","%","%","%","%","","month","%","%","USD","USD","month","%","%","month","%","USD","USD","month","USD","month","","","%"]
values={"2025":["",15,30,20,20,15,"",92,95,35,85,55,45,65,100,"",2,25,18,1200,360,2,30,20,3,15,60,180,3,600,4,"","",6],"2026":["",15,30,20,20,15,"",94,96,35,87,55,45,65,100,"",2,22,15,1280,385,2,28,18,3,12,65,195,3,640,4,"","",6],"2027":["",15,30,20,20,15,"",89,93,35,82,55,45,65,100,"",2,28,21,1150,340,2,32,22,3,18,55,165,3,560,4,"","",6]}


#["Indian_Subcontinent_High_Income_Individual_Net_Users","Indian_Subcontinent_Mid_Income_Individual_Net_Users","Indian_Subcontinent_Low_Income_Individual_Net_Users","Middle_East_and_Africa_High_Income_Individual_Net_Users","Middle_East_and_Africa_Mid_Income_Individual_Net_Users","Middle_East_and_Africa_Low_Income_Individual_Net_Users","UK_and_Europe_High_Income_Individual_Net_Users","UK_and_Europe_Mid_Income_Individual_Net_Users","UK_and_Europe_Low_Income_Individual_Net_Users","Indian_Subcontinent_Small_Enterprise_Net_Users","Indian_Subcontinent_Medium_Enterprise_Net_Users","Indian_Subcontinent_Large_Enterprise_Net_Users","Middle_East_and_Africa_Small_Enterprise_Net_Users","Middle_East_and_Africa_Medium_Enterprise_Net_Users","Middle_East_and_Africa_Large_Enterprise_Net_Users","UK_and_Europe_Small_Enterprise_Net_Users","UK_and_Europe_Medium_Enterprise_Net_Users","UK_and_Europe_Large_Enterprise_Net_Users"]

# SOlve revenue equations..............................
#  update_financial_model............pay load
# description_payload = {
#     "current_logic":str(rev_formula[list(rev_formula.keys())[-1]]),
#     "user_input":str(["Basic_LLM","Standard_LLM","Executive_LLM"])
# }

# fetch_revenue_component = requests.post(
#     f"{BASE_URL}/fetch_revenue_component",
#     json=description_payload
# )

# print("\nResponse from /fetch_revenue_component")
# print(fetch_revenue_component.text)
# #.....................................
# description_payload = {
#     "user_description":"I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model, and want to have the model for 5 years straight, starting from 2026 January. I want to operate in both India, Dubai and London",
#     "total_user": ["Europe_user", "India_user","Dubai_user"],
#     "revenue_sources_splits":["Basic_LLM", "Standard_LLM", "Executive_LLM"],
#     "interval": "yearly",
#     "product_revenue":"LLM_Subscription_Revenue",
#     "total_revenue":"Total_Company_Revenue",
#     "currency":"USD",
# }

# fetch_cost_formula = requests.post(
#     f"{BASE_URL}/fetch_cost_formula_assumption",
#     json=description_payload,
#     proxies=proxies
# )

# print("\nResponse from /fetch_cost_formula_assumption")
# print(fetch_cost_formula.text)



# cost_formula =json.loads(fetch_cost_formula.text)["formula"]
# cost_assumption=json.loads(fetch_cost_formula.text)["assumptions"]



#steps=["Step 1: Identify personnel cost across different product/services","Other_personnel_costs", "Total_Subject_matter_expert_onboarded","back_staff_per_production_staff","production_staff_per_user","Average_Duration_Subject_matter_expert","Cost_per_SME","back_staff_average_salary","production_staff_average_salary","salary_growth_rate","Step 2: Compute direct product-level costs","Standard_LLM_server_cost_per_user_per_month","Basic_LLM_server_cost_per_user_per_month","Basic_LLM_software_subscription_per_user_per_month","Maintenance_and_repairs_share","Standard_LLM_software_subscription_per_user_per_month","Standard_LLM_cost_per_user_per_month","Basic_LLM_database_hosting_per_user_per_month","Basic_LLM_cost_per_user_per_month","Standard_LLM_database_hosting_per_user_per_month","Executive_LLM_cost_per_user_per_month","Executive_LLM_database_hosting_per_user_per_month","Executive_LLM_software_subscription_per_user_per_month","Executive_LLM_server_cost_per_user_per_month","Step 3: Sales and Commission costs","Standard_LLM_fixed_commission_per_subscription","Basic_LLM_variable_commission_per_subscription","Executive_LLM_fixed_commission_per_subscription","Payment_gateway_fee_rate","Executive_LLM_variable_commission_per_subscription","Reservation_system_fee_per_month","Standard_LLM_variable_commission_per_subscription","Basic_LLM_fixed_commission_per_subscription","Step 4: Other overhead costs for operations","Office_supplies_share","Monthly_professional_services_fee","Insurance_cost_share","Marketing_and_Promotions_share","Utilities_share","Monthly_rent_fee","IT_communications_share","Step 5: Total cost","other_cost_share"]
#u#nits=["","%","#","%","%","month","USD per month","USD","USD","%","","USD","USD" ,"USD","%","USD","USD","USD","USD","USD","USD","USD","USD","USD","","USD","USD","USD","%","USD","USD","USD","USD","","%","USD","%","%","%","USD","%","","%"]
##alues={"2025":["",3.2,18,105,9.5,6,8400,57200,67600,3.2,"",11.5,5.8,12.5,4.2,19,46,8.2,25.5,15.5,87,29,36,22.5,"",19,16,37,2.9,47,2600,26,10.5,"", 1.6,3700,1.3,5.5,0.9,19500,2.4,"",0.15],"2026":["",3.4,22,108,9.2,6,8820,59030,69770,3.5,"",12.2,6.1,13.1,4.4,19.9,48.3,8.6,26.8,16.3,91.4,30.5,37.8,23.6,"",20,16.8,39,3.0,49.4,2730,27.3,11,"",1.7,3885,1.4,5.8,1.0,20475,2.5,"",0.18],"2027":["",3.6,28,112,8.8,6,9450,63500,75200,4.2,"",13.8,6.9,14.8,4.8,22.5,54.6,9.7,30.3,18.4,103.4,34.5,42.8,26.7,"",22,19.2,43,3.2,56.3,3100,31.1,12,"",1.8,4420,1.5,6.2,1.1,23300,2.8,"",0.22]}

##>.......Update cost_formula...........................................
# description_payload = {
#     "user_description":"I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model, and want to have the model for 5 years straight, starting from 2026 January. I want to operate in both India, Dubai and London",
#     "total_user":["Europe_user", "India_user","Dubai_user"],
#     "revenue_sources_splits":["Basic_LLM", "Standard_LLM", "Executive_LLM","extramile_LLM"],
#     "interval": "yearly",
#     "product_revenue":"LLM_Subscription_Revenue",
#     "total_revenue":"Total_Company_Revenue",
#     "currency":"USD",
#     "cost_formula":cost_formula,
#     "cost_assumption":cost_assumption,
#     "instruction":"Make the formula compact"
# }

# update_cost_formula = requests.post(
#     f"{BASE_URL}/update_cost_formula_assumption",
#     json=description_payload,
#     proxies=proxies
# )

# print("\nResponse from /update_cost_formula_assumption")
# print(update_cost_formula.text)
#..................Fetch cost assumption values.............................
# description_payload = {
#     "formula":cost_formula,
#     "assumptions":cost_assumption,
#     "analysis_time_frame":['2025', '2026', '2027'],
#     "period_ranges":[['January', 'December', 2025], ['January', 'December', 2026], ['January', 'December', 2027]],
#     "user_description":"I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model, and want to have the model for 5 years straight, starting from 2026 January. I want to operate in both India, Dubai and London",
#     "currency":"USD"
# }

# cost_ass_val = requests.post(
#     f"{BASE_URL}/estimate_cost_assumption_values",
#     json=description_payload,
#     proxies=proxies
# )

# print("\nResponse from /cost_ass_val.....................")
# print(cost_ass_val.text)
#............................compute cost



# cost_steps =json.loads(cost_ass_val.text)["steps"]
# cost_units=json.loads(cost_ass_val.text)["units"]
# cost_values=json.loads(cost_ass_val.text)["values"]


#steps=["Step 1: Identify user across different product/services","Basic_LLM_and_Executive_LLM","Standard_LLM","Basic_LLM","Executive_LLM","Basic_LLM_and_Standard_LLM","Step 2: Breakdown the user base by plan tenure","quarterly_effective_rate","halfyearly_effective_rate","Basic_LLM_quarterly_share","monthly_effective_rate","Standard_LLM_quarterly_share","Standard_LLM_halfyearly_share","Basic_LLM_monthly_share","Executive_LLM_halfyearly_share","Step 3: Identify the pricing rate for each product/services","Basic_LLM_monthly_discount_period","Standard_LLM_halfyearly_discount","Standard_LLM_quarterly_discount","Executive_LLM_halfyearly_price","Standard_LLM_quarterly_price","Standard_LLM_quarterly_discount_period","Executive_LLM_halfyearly_discount","Basic_LLM_quarterly_discount","Executive_LLM_halfyearly_discount_period","Basic_LLM_monthly_discount","Basic_LLM_monthly_price","Basic_LLM_quarterly_price","Basic_LLM_quarterly_discount_period","Standard_LLM_halfyearly_price","Standard_LLM_halfyearly_discount_period","Step 4: Revenue computation for each product line","Step 5: Total revenue from all product/services","Additional_Revenue_Contribution"]
#units=["","%","%","%","%","%","","%","%","%","%","%","%","%","%","","month","%","%","USD","USD","month","%","%","month","%","USD","USD","month","USD","month","","","%"]
#values={"2025":["",15,30,20,20,15,"",92,95,35,85,55,45,65,100,"",2,25,18,1200,360,2,30,20,3,15,60,180,3,600,4,"","",6],"2026":["",15,30,20,20,15,"",94,96,35,87,55,45,65,100,"",2,22,15,1280,385,2,28,18,3,12,65,195,3,640,4,"","",6],"2027":["",15,30,20,20,15,"",89,93,35,82,55,45,65,100,"",2,28,21,1150,340,2,32,22,3,18,55,165,3,560,4,"","",6]}


#["Indian_Subcontinent_High_Income_Individual_Net_Users","Indian_Subcontinent_Mid_Income_Individual_Net_Users","Indian_Subcontinent_Low_Income_Individual_Net_Users","Middle_East_and_Africa_High_Income_Individual_Net_Users","Middle_East_and_Africa_Mid_Income_Individual_Net_Users","Middle_East_and_Africa_Low_Income_Individual_Net_Users","UK_and_Europe_High_Income_Individual_Net_Users","UK_and_Europe_Mid_Income_Individual_Net_Users","UK_and_Europe_Low_Income_Individual_Net_Users","Indian_Subcontinent_Small_Enterprise_Net_Users","Indian_Subcontinent_Medium_Enterprise_Net_Users","Indian_Subcontinent_Large_Enterprise_Net_Users","Middle_East_and_Africa_Small_Enterprise_Net_Users","Middle_East_and_Africa_Medium_Enterprise_Net_Users","Middle_East_and_Africa_Large_Enterprise_Net_Users","UK_and_Europe_Small_Enterprise_Net_Users","UK_and_Europe_Medium_Enterprise_Net_Users","UK_and_Europe_Large_Enterprise_Net_Users"]

# SOlve revenue equations..............................
#{"assumptions":{"production_staff_per_user (%)":10,"back_staff_per_production_staff (%)":100,"production_staff_average_salary (USD)":12000,"back_staff_average_salary (USD)":9000,"salary_growth_rate (%)":2.5,"Total_Subject_matter_expert_onboarded (#)":10,"Average_Duration_Subject_matter_expert (month)":0.5,"Cost_per_SME (USD per month)":3000,"Other_personnel_costs (%)":2,"Basic_LLM_cost_per_user_per_month (USD)":15,"Standard_LLM_cost_per_user_per_month (USD)":25,"Executive_LLM_cost_per_user_per_month (USD)":50,"Basic_LLM_software_cost_per_user_per_month (USD)":5,"Standard_LLM_software_cost_per_user_per_month (USD)":8,"Executive_LLM_software_cost_per_user_per_month (USD)":12,"Basic_LLM_database_cost_per_user_per_month (USD)":3,"Standard_LLM_database_cost_per_user_per_month (USD)":5,"Executive_LLM_database_cost_per_user_per_month (USD)":8,"Basic_LLM_server_cost_per_user_per_month (USD)":4,"Standard_LLM_server_cost_per_user_per_month (USD)":7,"Executive_LLM_server_cost_per_user_per_month (USD)":10,"Maintenance_and_repairs_share (%)":3,"Basic_LLM_variable_commission_per_subscription (USD)":5,"Basic_LLM_fixed_commission_per_subscription (USD)":3,"Standard_LLM_variable_commission_per_subscription (USD)":8,"Standard_LLM_fixed_commission_per_subscription (USD)":5,"Executive_LLM_variable_commission_per_subscription (USD)":15,"Executive_LLM_fixed_commission_per_subscription (USD)":10,"Reservation_system_fixed_fee (USD)":2000,"Payment_gateway_fee_rate (%)":2.5,"Marketing_and_Promotions_share (%)":4,"Monthly_rent_fee (USD)":25000,"Office_supplies_share (%)":1.5,"Utilities_share (%)":2,"IT_communications_share (%)":1.8,"Monthly_professional_services_fee (USD)":5000,"Insurance_cost_share (%)":1.2,"other_cost_share (%)":0.1},"formula":{"Step 1: Identify personnel cost across different product/services":["Total_users (#) = Europe_user + India_user + Dubai_user","production_staff (#) = Total_users * (production_staff_per_user / 100)","back_staff (#) = production_staff * (back_staff_per_production_staff / 100)","Production_staff_base_salary (USD) = production_staff * production_staff_average_salary","Back_staff_base_salary (USD) = back_staff * back_staff_average_salary","Production_staff_salary_with_growth (USD) = Production_staff_base_salary * (1 + salary_growth_rate / 100)","Back_staff_salary_with_growth (USD) = Back_staff_base_salary * (1 + salary_growth_rate / 100)","Subject_matter_expert_salary (USD) = Total_Subject_matter_expert_onboarded * Average_Duration_Subject_matter_expert * Cost_per_SME","Base_personnel_cost (USD) = Production_staff_salary_with_growth + Back_staff_salary_with_growth + Subject_matter_expert_salary","Total_personnel_cost (USD) = Base_personnel_cost * (1 + Other_personnel_costs / 100)"],"Step 2: Compute direct product-level costs":["Basic_LLM_users (#) = (Europe_user + India_user + Dubai_user) * 0.4","Standard_LLM_users (#) = (Europe_user + India_user + Dubai_user) * 0.35","Executive_LLM_users (#) = (Europe_user + India_user + Dubai_user) * 0.25","Basic_LLM_cost (USD) = Basic_LLM_users * Basic_LLM_cost_per_user_per_month * 12","Standard_LLM_cost (USD) = Standard_LLM_users * Standard_LLM_cost_per_user_per_month * 12","Executive_LLM_cost (USD) = Executive_LLM_users * Executive_LLM_cost_per_user_per_month * 12","Basic_LLM_software_cost (USD) = Basic_LLM_users * Basic_LLM_software_cost_per_user_per_month * 12","Standard_LLM_software_cost (USD) = Standard_LLM_users * Standard_LLM_software_cost_per_user_per_month * 12","Executive_LLM_software_cost (USD) = Executive_LLM_users * Executive_LLM_software_cost_per_user_per_month * 12","Basic_LLM_database_cost (USD) = Basic_LLM_users * Basic_LLM_database_cost_per_user_per_month * 12","Standard_LLM_database_cost (USD) = Standard_LLM_users * Standard_LLM_database_cost_per_user_per_month * 12","Executive_LLM_database_cost (USD) = Executive_LLM_users * Executive_LLM_database_cost_per_user_per_month * 12","Basic_LLM_server_cost (USD) = Basic_LLM_users * Basic_LLM_server_cost_per_user_per_month * 12","Standard_LLM_server_cost (USD) = Standard_LLM_users * Standard_LLM_server_cost_per_user_per_month * 12","Executive_LLM_server_cost (USD) = Executive_LLM_users * Executive_LLM_server_cost_per_user_per_month * 12","Total_LLM_costs (USD) = Basic_LLM_cost + Standard_LLM_cost + Executive_LLM_cost","Total_software_costs (USD) = Basic_LLM_software_cost + Standard_LLM_software_cost + Executive_LLM_software_cost","Total_database_costs (USD) = Basic_LLM_database_cost + Standard_LLM_database_cost + Executive_LLM_database_cost","Total_server_costs (USD) = Basic_LLM_server_cost + Standard_LLM_server_cost + Executive_LLM_server_cost","Maintenance_and_repairs_cost (USD) = Total_Company_Revenue * (Maintenance_and_repairs_share / 100)","Total_direct_product_cost (USD) = Total_LLM_costs + Total_software_costs + Total_database_costs + Total_server_costs + Maintenance_and_repairs_cost"],"Step 3: Sales and Commission costs":["Basic_LLM_commission_and_incentive_cost (USD) = Basic_LLM_users * (Basic_LLM_variable_commission_per_subscription + Basic_LLM_fixed_commission_per_subscription)","Standard_LLM_commission_and_incentive_cost (USD) = Standard_LLM_users * (Standard_LLM_variable_commission_per_subscription + Standard_LLM_fixed_commission_per_subscription)","Executive_LLM_commission_and_incentive_cost (USD) = Executive_LLM_users * (Executive_LLM_variable_commission_per_subscription + Executive_LLM_fixed_commission_per_subscription)","Total_commission_and_incentive_cost (USD) = Basic_LLM_commission_and_incentive_cost + Standard_LLM_commission_and_incentive_cost + Executive_LLM_commission_and_incentive_cost","Reservation_system_cost (USD) = Reservation_system_fixed_fee * 12","Payment_gateway_cost (USD) = LLM_Subscription_Revenue * (Payment_gateway_fee_rate / 100)","Total_sales_and_commission_cost (USD) = Total_commission_and_incentive_cost + Reservation_system_cost + Payment_gateway_cost"],"Step 4: Other overhead costs":["Marketing_and_Promotions_cost (USD) = LLM_Subscription_Revenue * (Marketing_and_Promotions_share / 100)","Rent_cost (USD) = Monthly_rent_fee * 12","Office_supplies_cost (USD) = Total_Company_Revenue * (Office_supplies_share / 100)","Utilities_cost (USD) = Total_Company_Revenue * (Utilities_share / 100)","IT_communications_cost (USD) = Total_Company_Revenue * (IT_communications_share / 100)","Professional_services_cost (USD) = Monthly_professional_services_fee * 12","Insurance_cost (USD) = Total_Company_Revenue * (Insurance_cost_share / 100)","Total_overhead_cost (USD) = Marketing_and_Promotions_cost + Rent_cost + Office_supplies_cost + Utilities_cost + IT_communications_cost + Professional_services_cost + Insurance_cost"],"Step 5: Total cost":["cost (USD) = Total_personnel_cost + Total_direct_product_cost + Total_sales_and_commission_cost + Total_overhead_cost","Total_cost (USD) = cost * (1 + other_cost_share / 100)"]}}
# cost_formula ={"Step 1: Identify personnel cost across different product/services":["Total_users (#) = Europe_user + India_user + Dubai_user","production_staff (#) = Total_users * (production_staff_per_user / 100)","back_staff (#) = production_staff * (back_staff_per_production_staff / 100)","Production_staff_base_salary (USD) = production_staff * production_staff_average_salary","Back_staff_base_salary (USD) = back_staff * back_staff_average_salary","Production_staff_salary_with_growth (USD) = Production_staff_base_salary * (1 + salary_growth_rate / 100)","Back_staff_salary_with_growth (USD) = Back_staff_base_salary * (1 + salary_growth_rate / 100)","Subject_matter_expert_salary (USD) = Total_Subject_matter_expert_onboarded * Average_Duration_Subject_matter_expert * Cost_per_SME","Base_personnel_cost (USD) = Production_staff_salary_with_growth + Back_staff_salary_with_growth + Subject_matter_expert_salary","Total_personnel_cost (USD) = Base_personnel_cost * (1 + Other_personnel_costs / 100)"],"Step 2: Compute direct product-level costs":["Basic_LLM_users (#) = (Europe_user + India_user + Dubai_user) * 0.4","Standard_LLM_users (#) = (Europe_user + India_user + Dubai_user) * 0.35","Executive_LLM_users (#) = (Europe_user + India_user + Dubai_user) * 0.25","Basic_LLM_cost (USD) = Basic_LLM_users * Basic_LLM_cost_per_user_per_month * 12","Standard_LLM_cost (USD) = Standard_LLM_users * Standard_LLM_cost_per_user_per_month * 12","Executive_LLM_cost (USD) = Executive_LLM_users * Executive_LLM_cost_per_user_per_month * 12","Basic_LLM_software_cost (USD) = Basic_LLM_users * Basic_LLM_software_cost_per_user_per_month * 12","Standard_LLM_software_cost (USD) = Standard_LLM_users * Standard_LLM_software_cost_per_user_per_month * 12","Executive_LLM_software_cost (USD) = Executive_LLM_users * Executive_LLM_software_cost_per_user_per_month * 12","Basic_LLM_database_cost (USD) = Basic_LLM_users * Basic_LLM_database_cost_per_user_per_month * 12","Standard_LLM_database_cost (USD) = Standard_LLM_users * Standard_LLM_database_cost_per_user_per_month * 12","Executive_LLM_database_cost (USD) = Executive_LLM_users * Executive_LLM_database_cost_per_user_per_month * 12","Basic_LLM_server_cost (USD) = Basic_LLM_users * Basic_LLM_server_cost_per_user_per_month * 12","Standard_LLM_server_cost (USD) = Standard_LLM_users * Standard_LLM_server_cost_per_user_per_month * 12","Executive_LLM_server_cost (USD) = Executive_LLM_users * Executive_LLM_server_cost_per_user_per_month * 12","Total_LLM_costs (USD) = Basic_LLM_cost + Standard_LLM_cost + Executive_LLM_cost","Total_software_costs (USD) = Basic_LLM_software_cost + Standard_LLM_software_cost + Executive_LLM_software_cost","Total_database_costs (USD) = Basic_LLM_database_cost + Standard_LLM_database_cost + Executive_LLM_database_cost","Total_server_costs (USD) = Basic_LLM_server_cost + Standard_LLM_server_cost + Executive_LLM_server_cost","Maintenance_and_repairs_cost (USD) = Total_Company_Revenue * (Maintenance_and_repairs_share / 100)","Total_direct_product_cost (USD) = Total_LLM_costs + Total_software_costs + Total_database_costs + Total_server_costs + Maintenance_and_repairs_cost"],"Step 3: Sales and Commission costs":["Basic_LLM_commission_and_incentive_cost (USD) = Basic_LLM_users * (Basic_LLM_variable_commission_per_subscription + Basic_LLM_fixed_commission_per_subscription)","Standard_LLM_commission_and_incentive_cost (USD) = Standard_LLM_users * (Standard_LLM_variable_commission_per_subscription + Standard_LLM_fixed_commission_per_subscription)","Executive_LLM_commission_and_incentive_cost (USD) = Executive_LLM_users * (Executive_LLM_variable_commission_per_subscription + Executive_LLM_fixed_commission_per_subscription)","Total_commission_and_incentive_cost (USD) = Basic_LLM_commission_and_incentive_cost + Standard_LLM_commission_and_incentive_cost + Executive_LLM_commission_and_incentive_cost","Reservation_system_cost (USD) = Reservation_system_fixed_fee * 12","Payment_gateway_cost (USD) = LLM_Subscription_Revenue * (Payment_gateway_fee_rate / 100)","Total_sales_and_commission_cost (USD) = Total_commission_and_incentive_cost + Reservation_system_cost + Payment_gateway_cost"],"Step 4: Other overhead costs":["Marketing_and_Promotions_cost (USD) = LLM_Subscription_Revenue * (Marketing_and_Promotions_share / 100)","Rent_cost (USD) = Monthly_rent_fee * 12","Office_supplies_cost (USD) = Total_Company_Revenue * (Office_supplies_share / 100)","Utilities_cost (USD) = Total_Company_Revenue * (Utilities_share / 100)","IT_communications_cost (USD) = Total_Company_Revenue * (IT_communications_share / 100)","Professional_services_cost (USD) = Monthly_professional_services_fee * 12","Insurance_cost (USD) = Total_Company_Revenue * (Insurance_cost_share / 100)","Total_overhead_cost (USD) = Marketing_and_Promotions_cost + Rent_cost + Office_supplies_cost + Utilities_cost + IT_communications_cost + Professional_services_cost + Insurance_cost"],"Step 5: Total cost":["cost (USD) = Total_personnel_cost + Total_direct_product_cost + Total_sales_and_commission_cost + Total_overhead_cost","Total_cost (USD) = cost * (1 + other_cost_share / 100)"]}


# cost_formula={"Step 1: Identify personnel cost across different product/services":["Total_users (#) = Europe_user + India_user + Dubai_user","production_staff (#) = Total_users * (production_staff_per_user / 100)","back_staff (#) = production_staff * (back_staff_per_production_staff / 100)","Production_staff_salary_base (USD) = production_staff * production_staff_average_salary","Back_staff_salary_base (USD) = back_staff * back_staff_average_salary","Production_staff_salary_adjusted (USD) = Production_staff_salary_base * (1 + salary_growth_rate / 100)","Back_staff_salary_adjusted (USD) = Back_staff_salary_base * (1 + salary_growth_rate / 100)","Subject_matter_expert_salary (USD) = Total_Subject_matter_expert_onboarded * Average_Duration_Subject_matter_expert * Cost_per_SME","Base_personnel_cost (USD) = Production_staff_salary_adjusted + Back_staff_salary_adjusted + Subject_matter_expert_salary","Total_personnel_cost (USD) = Base_personnel_cost * (1 + Other_personnel_costs / 100)"],"Step 2: Compute direct product-level costs":["Basic_LLM_annual_cost (USD) = Basic_LLM * Basic_LLM_cost_per_user_per_month * 12","Standard_LLM_annual_cost (USD) = Standard_LLM * Standard_LLM_cost_per_user_per_month * 12","Executive_LLM_annual_cost (USD) = Executive_LLM * Executive_LLM_cost_per_user_per_month * 12","Total_LLM_costs (USD) = Basic_LLM_annual_cost + Standard_LLM_annual_cost + Executive_LLM_annual_cost","Software_subscription_costs (USD) = Total_users * Software_subscription_cost_per_user_per_month * 12","Database_hosting_costs (USD) = Total_users * Database_hosting_cost_per_user_per_month * 12","Server_costs (USD) = Total_users * Server_cost_per_user_per_month * 12","Maintenance_and_repairs_cost (USD) = Total_Company_Revenue * (Maintenance_and_repairs_share / 100)","Total_direct_product_cost (USD) = Total_LLM_costs + Software_subscription_costs + Database_hosting_costs + Server_costs + Maintenance_and_repairs_cost"],"Step 3: Sales and Commission costs":["Basic_LLM_commission_and_incentive_cost (USD) = Basic_LLM * (Basic_LLM_variable_commission_per_subscription + Basic_LLM_fixed_commission_per_subscription)","Standard_LLM_commission_and_incentive_cost (USD) = Standard_LLM * (Standard_LLM_variable_commission_per_subscription + Standard_LLM_fixed_commission_per_subscription)","Executive_LLM_commission_and_incentive_cost (USD) = Executive_LLM * (Executive_LLM_variable_commission_per_subscription + Executive_LLM_fixed_commission_per_subscription)","Total_commission_and_incentive_cost (USD) = Basic_LLM_commission_and_incentive_cost + Standard_LLM_commission_and_incentive_cost + Executive_LLM_commission_and_incentive_cost","Reservation_system_cost (USD) = Reservation_system_fixed_fee_per_month * 12","Payment_gateway_cost (USD) = LLM_Subscription_Revenue * (Payment_gateway_fee_rate / 100)","Total_sales_and_commission_cost (USD) = Total_commission_and_incentive_cost + Reservation_system_cost + Payment_gateway_cost"],"Step 4: Other overhead costs for business operations":["Marketing_and_promotions_cost (USD) = LLM_Subscription_Revenue * (Marketing_and_Promotions_share / 100)","Rent_cost (USD) = Monthly_rent_fee * 12","Office_supplies_cost (USD) = Total_Company_Revenue * (Office_supplies_share / 100)","Utilities_cost (USD) = Total_Company_Revenue * (Utilities_share / 100)","IT_communications_cost (USD) = Total_Company_Revenue * (IT_communications_share / 100)","Professional_services_cost (USD) = Monthly_professional_services_fee * 12","Insurance_cost (USD) = Total_Company_Revenue * (Insurance_cost_share / 100)","Total_overhead_cost (USD) = Marketing_and_promotions_cost + Rent_cost + Office_supplies_cost + Utilities_cost + IT_communications_cost + Professional_services_cost + Insurance_cost"],"Step 5: Total cost":["cost (USD) = Total_personnel_cost + Total_direct_product_cost + Total_sales_and_commission_cost + Total_overhead_cost","Total_cost (USD) = cost * (1 + other_cost_share / 100)"]}

# cost_steps = ['Step 1: Identify personnel cost across different product/services', 'production_staff_per_user', 'back_staff_per_production_staff', 'production_staff_average_salary', 'back_staff_average_salary', 'Average_Duration_Subject_matter_expert', 'Cost_per_SME', 'Total_Subject_matter_expert_onboarded', 'salary_growth_rate', 'Other_personnel_costs', 'Step 2: Compute direct product-level costs', 'Maintenance_and_repairs_share', 'Software_subscription_cost_per_user_per_month', 'Executive_LLM_cost_per_user_per_month', 'Standard_LLM_cost_per_user_per_month', 'Database_hosting_cost_per_user_per_month', 'Server_cost_per_user_per_month', 'Basic_LLM_cost_per_user_per_month', 'Step 3: Sales and Commission costs', 'Standard_LLM_variable_commission_per_subscription', 'Payment_gateway_fee_rate', 'Basic_LLM_variable_commission_per_subscription', 'Reservation_system_fixed_fee_per_month', 'Executive_LLM_variable_commission_per_subscription', 'Standard_LLM_fixed_commission_per_subscription', 'Executive_LLM_fixed_commission_per_subscription', 'Basic_LLM_fixed_commission_per_subscription', 'Step 4: Other overhead costs for business operations', 'Office_supplies_share', 'Monthly_rent_fee', 'Utilities_share', 'Insurance_cost_share', 'Monthly_professional_services_fee', 'IT_communications_share', 'Marketing_and_Promotions_share', 'Step 5: Total cost', 'other_cost_share','Total_Company_Revenue', 'LLM_Subscription_Revenue','Europe_user', 'India_user', 'Dubai_user', 'Basic_LLM', 'Standard_LLM', 'Executive_LLM','extramile_LLM']
# cost_units = ['', '%', '%', 'USD', 'USD', 'month', 'USD per month', '#', '%', '%', '', '%', 'USD', 'USD', 'USD', 'USD', 'USD', 'USD', '', 'USD', '%', 'USD', 'USD', 'USD', 'USD', 'USD', 'USD', '', '%', 'USD', '%', '%', 'USD', '%', '%', '', '%','USD','USD','#','#','#','%','%','%','%']
# cost_values = {'2025': ['', 9.5, 95, 77250, 61800, 6, 8240, 15, 3.5, 2.2, '', 2.8, 16, 85, 48, 13, 19, 27, '', 26, 2.6, 16, 5200, 47, 21, 37, 11, '', 1.6, 12600, 0.85, 1.6, 8400, 1.3, 4.5, '', 0.12, 23434, 21393,454634,225551,56882,40,30,20,10], '2026': ['', 9.2, 92, 79950, 63965, 6, 8530, 18, 3.8, 2.4, '', 2.6, 17, 92, 52, 14, 21, 29, '', 28, 2.7, 17, 5460, 51, 23, 40, 12, '', 1.7, 13230, 0.9, 1.7, 8820, 1.4, 5.2, '', 0.15, 46356, 42374, 286386,64888,48489,40,30,18,12], '2027': ['', 8.5, 88, 86500, 69200, 6, 9200, 24, 4.2, 2.8, '', 2.2, 19, 105, 58, 16, 24, 33, '', 32, 2.9, 19, 5950, 58, 26, 45, 14, '', 1.9, 14800, 1.0, 1.9, 9650, 1.6, 6.8, '', 0.18, 69397, 65673,286868,646486,798739,42,28,18,12]}

# description_payload = {
#     "assumption_values":cost_values,
#     "units":cost_units,
#     "currency":"USD",
#     "formula":cost_formula,
#     "steps":cost_steps
# }

# cost_compute = requests.post(
#     f"{BASE_URL}/compute_user_base",
#     json=description_payload,
#     proxies=proxies
# )

# print("\nResponse from /Cost.....................")
# print(cost_compute.text)





#.....................................
'''
description_payload = {
    "user_description":"I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model, and want to have the model for 5 years straight, starting from 2026 January. I want to operate in both India, Dubai and London",
    "total_staff":["previous_period_Total_staff","current_period_Increase_in_staff"],
    "revenue_sources_splits":["Basic_LLM", "Standard_LLM", "Executive_LLM"],
    "interval": "yearly",
    "total_revenue":"Total_Company_Revenue",
    "currency":"USD",
}

fetch_capex_formula = requests.post(
    f"{BASE_URL}/fetch_capex_formula_assumption",
    json=description_payload,
    proxies=proxies
)

print("\nResponse from /fetch_capex_formula_assumption")
print(fetch_capex_formula.text)



#>.......Update capex_formula...........................................
capex_formula =json.loads(fetch_capex_formula.text)["formula"]
capex_assumption=json.loads(fetch_capex_formula.text)["assumptions"]

# description_payload = {
#     "user_description":"I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model, and want to have the model for 5 years straight, starting from 2026 January. I want to operate in both India, Dubai and London",
#     "total_staff":["previous_period_Total_staff","current_period_Increase_in_staff"],
#     "revenue_sources_splits":["Basic_LLM", "Standard_LLM", "Executive_LLM"],
#     "interval": "yearly",
#     "total_revenue":"Total_Company_Revenue",
#     "currency":"USD",
#     "capex_formula":capex_formula,
#     "capex_assumption":capex_assumption,
#     "instruction":"Make the formula compact"
# }

# update_capex_formula = requests.post(
#     f"{BASE_URL}/update_capex_formula_assumption",
#     json=description_payload,
#     proxies=proxies
# )

# print("\nResponse from /update_capex_formula")
# print(update_capex_formula.text)


#..........................
description_payload = {
    "formula":capex_formula,
    "assumptions":capex_assumption,
    "analysis_time_frame":['2025', '2026', '2027'],
    "period_ranges":[['January', 'December', 2025], ['January', 'December', 2026], ['January', 'December', 2027]],
    "user_description":"I want to open a competitor for OpenAI which provides 4 LLM subscriptions. I want to build a financial model which tests the feasibility and the overall return of this. I want to structure the model per subscription model, and want to have the model for 5 years straight, starting from 2026 January. I want to operate in both India, Dubai and London",
    "currency":"USD"
}

capex_ass_val = requests.post(
    f"{BASE_URL}/estimate_cost_assumption_values",
    json=description_payload,
    proxies=proxies
)

print("\nResponse from /capex_ass_val.....................")
print(capex_ass_val.text)

#..........................Compute capex......................

capex_steps =json.loads(capex_ass_val.text)["steps"]
capex_units=json.loads(capex_ass_val.text)["units"]
capex_values=json.loads(capex_ass_val.text)["values"]
#pdb.set_trace()


capex_steps= ['Step 1: Estimate the cost required to set-up the product/service industry', 'Security_Systems_Cost_per_Location', 'Backup_Power_Systems_Cost_per_Location', 'GPUs_per_Server', 'Number_of_Locations', 'Network_Infrastructure_Cost_per_Location', 'GPU_Servers_last_year', 'Cooling_Systems_Cost_per_Location', 'Cost_per_GPU', 'Data_Center_Setup_Cost_per_Location', 'Replacement_for_Older_GPU_Servers_share', 'GPU_Servers_increase_this_year', 'Step 2: Estimate the cost required to set-up systems to launch and operate the service', 'User_Analytics_Dashboards_per_Location', 'API_Management_Systems_per_Location', 'Data_Storage_Systems_per_Location', 'Cost_per_Monitoring_Tool', 'Model_Training_Platforms_per_Location', 'Cost_per_User_Analytics_Dashboard', 'Cost_per_Model_Training_Platform', 'Cost_per_Data_Storage_System', 'Cost_per_API_Management_System', 'Cost_per_Customer_Portal_System', 'Monitoring_Tools_per_Location', 'Customer_Portal_Systems_per_Location', 'Step 3: Estimate the capEx to set-up the office furniture and infrastructure', 'Office_Space_per_Location', 'Wireless_Access_Points_per_Location', 'Cost_per_Workstation', 'Cost_per_Meeting_Room_Setup', 'Network_Cabling_per_Location', 'Routers_per_Location', 'Cost_per_Wireless_Access_Point', 'Cost_per_Firewall_System', 'Meeting_Rooms_per_Location', 'Cost_per_Switch', 'Office_Furniture_Cost_per_sq_ft', 'Reception_Areas_per_Location', 'Cost_per_Reception_Area', 'Cost_per_Router', 'Workstations_per_Location', 'Switches_per_Location', 'Firewall_Systems_per_Location', 'Step 4: Estimate the capex for IT-staff', 'Laptop_License_and_Phones_Budget_per_staff', 'Older_staff_replacement_share', 'current_period_Increase_in_staff', 'previous_period_Total_staff', 'Step 5: Total capex by company', 'other_capex_Share','previous_period_Total_staff','current_period_Increase_in_staff','Basic_LLM', 'Standard_LLM', 'Executive_LLM','Total_Company_Revenue']
capex_units = ['', 'USD', 'USD', '#', '#', 'USD', '#', 'USD', 'USD', 'USD', '%', '#', '', '#', '#', '#', 'USD', '#', 'USD', 'USD', 'USD', 'USD', 'USD', '#', '#', '', 'sq_ft', '#', 'USD', 'USD', 'USD', '#', 'USD', 'USD', '#', 'USD', 'USD', '#', 'USD', 'USD', '#', '#', '#', '', 'USD', '%', '#', '#', '', '%','#','#','%','%','%','USD']
capex_values = {'2025': ['', 468000, 364000, 8, 3, 832000, 225, 624000, 26250, 2625000, 12, 90, '', 4, 3, 5, 52500, 2, 84000, 315000, 126000, 157500, 210000, 6, 2, '', 5500, 25, 2625, 15750, 78750, 12, 840, 12600, 10, 1575, 158, 1, 26250, 3150, 65, 18, 4, '', 3675, 12, 150, 300, '', 0.12,1000,200,40,35,25,2342442], '2026': ['', 491400, 382200, 8, 3, 873600, 315, 655200, 27563, 2756250, 15, 108, '', 5, 4, 6, 55125, 3, 88200, 330750, 132300, 165375, 220500, 7, 3, '', 6050, 30, 2756, 16538, 82688, 15, 882, 13230, 12, 1654, 166, 1, 27563, 3308, 78, 22, 5, '', 3859, 15, 180, 450, '', 0.14,1200,300,40,35,25,2562442], '2027': ['', 540540, 420420, 8, 3, 960960, 423, 720720, 30319, 3031875, 18, 137, '', 6, 5, 7, 60638, 4, 97020, 363825, 145530, 181913, 242550, 8, 4, '', 6655, 35, 3032, 18192, 90957, 18, 970, 14553, 14, 1819, 183, 1, 30319, 3639, 90, 26, 6, '', 4245, 18, 216, 630, '', 0.16,1500,350,40,35,25,2782442]}
capex_formula = {'Step 1: Estimate the cost required to set-up the product/service industry': ['GPU_Infrastructure_Costs (USD) = GPU_Servers_increase_this_year * GPUs_per_Server * Cost_per_GPU + GPU_Servers_last_year * GPUs_per_Server * Cost_per_GPU * Replacement_for_Older_GPU_Servers_share / 100', 'Data_Center_Infrastructure_Costs (USD) = Number_of_Locations * (Data_Center_Setup_Cost_per_Location + Network_Infrastructure_Cost_per_Location + Security_Systems_Cost_per_Location + Cooling_Systems_Cost_per_Location + Backup_Power_Systems_Cost_per_Location)', 'LLM_Setup_Costs (USD) = GPU_Infrastructure_Costs + Data_Center_Infrastructure_Costs'], 'Step 2: Estimate the cost required to set-up systems to launch and operate the service': ['API_Management_Costs (USD) = Number_of_Locations * API_Management_Systems_per_Location * Cost_per_API_Management_System', 'Analytics_Dashboard_Costs (USD) = Number_of_Locations * User_Analytics_Dashboards_per_Location * Cost_per_User_Analytics_Dashboard', 'Model_Training_Platform_Costs (USD) = Number_of_Locations * Model_Training_Platforms_per_Location * Cost_per_Model_Training_Platform', 'Data_Storage_Costs (USD) = Number_of_Locations * Data_Storage_Systems_per_Location * Cost_per_Data_Storage_System', 'Monitoring_Tools_Costs (USD) = Number_of_Locations * Monitoring_Tools_per_Location * Cost_per_Monitoring_Tool', 'Customer_Portal_Costs (USD) = Number_of_Locations * Customer_Portal_Systems_per_Location * Cost_per_Customer_Portal_System', 'Digital_Systems_Setup_Costs (USD) = API_Management_Costs + Analytics_Dashboard_Costs + Model_Training_Platform_Costs + Data_Storage_Costs + Monitoring_Tools_Costs + Customer_Portal_Costs'], 'Step 3: Estimate the capEx to set-up the office furniture and infrastructure': ['Office_Furniture_Costs (USD) = Number_of_Locations * (Office_Space_per_Location * Office_Furniture_Cost_per_sq_ft + Workstations_per_Location * Cost_per_Workstation + Meeting_Rooms_per_Location * Cost_per_Meeting_Room_Setup + Reception_Areas_per_Location * Cost_per_Reception_Area)', 'Office_Networking_Infrastructure_Costs (USD) = Number_of_Locations * (Routers_per_Location * Cost_per_Router + Switches_per_Location * Cost_per_Switch + Network_Cabling_per_Location + Wireless_Access_Points_per_Location * Cost_per_Wireless_Access_Point + Firewall_Systems_per_Location * Cost_per_Firewall_System)', 'Office_Setup_Costs (USD) = Office_Furniture_Costs + Office_Networking_Infrastructure_Costs'], 'Step 4: Estimate the capex for IT-staff': ['Total_IT_staff_cost (USD) = current_period_Increase_in_staff * Laptop_License_and_Phones_Budget_per_staff + previous_period_Total_staff * Laptop_License_and_Phones_Budget_per_staff * Older_staff_replacement_share / 100'], 'Step 5: Total capex by company': ['Total_capex (USD) = LLM_Setup_Costs + Digital_Systems_Setup_Costs + Office_Setup_Costs + Total_IT_staff_cost + Total_Company_Revenue * other_capex_Share / 100']}
description_payload = {
    "assumption_values":capex_values,
    "units":capex_units,
    "currency":"USD",
    "formula":capex_formula,
    "steps":capex_steps
}

capex_compute = requests.post(
    f"{BASE_URL}/compute_user_base",
    json=description_payload,
    proxies=proxies
)

print("\nResponse from /Capex.....................")
print(capex_compute.text)
'''
#........................................
cost_formula={"Step 1: Identify personnel cost across different product/services":["Total_users (#) = Europe_user + India_user + Dubai_user","production_staff (#) = Total_users * (production_staff_per_user / 100)","back_staff (#) = production_staff * (back_staff_per_production_staff / 100)","Production_staff_salary_base (USD) = production_staff * production_staff_average_salary","Back_staff_salary_base (USD) = back_staff * back_staff_average_salary","Production_staff_salary_adjusted (USD) = Production_staff_salary_base * (1 + salary_growth_rate / 100)","Back_staff_salary_adjusted (USD) = Back_staff_salary_base * (1 + salary_growth_rate / 100)","Subject_matter_expert_salary (USD) = Total_Subject_matter_expert_onboarded * Average_Duration_Subject_matter_expert * Cost_per_SME","Base_personnel_cost (USD) = Production_staff_salary_adjusted + Back_staff_salary_adjusted + Subject_matter_expert_salary","Total_personnel_cost (USD) = Base_personnel_cost * (1 + Other_personnel_costs / 100)"],"Step 2: Compute direct product-level costs":["Basic_LLM_annual_cost (USD) = Basic_LLM * Basic_LLM_cost_per_user_per_month * 12","Standard_LLM_annual_cost (USD) = Standard_LLM * Standard_LLM_cost_per_user_per_month * 12","Executive_LLM_annual_cost (USD) = Executive_LLM * Executive_LLM_cost_per_user_per_month * 12","Total_LLM_costs (USD) = Basic_LLM_annual_cost + Standard_LLM_annual_cost + Executive_LLM_annual_cost","Software_subscription_costs (USD) = Total_users * Software_subscription_cost_per_user_per_month * 12","Database_hosting_costs (USD) = Total_users * Database_hosting_cost_per_user_per_month * 12","Server_costs (USD) = Total_users * Server_cost_per_user_per_month * 12","Maintenance_and_repairs_cost (USD) = Total_Company_Revenue * (Maintenance_and_repairs_share / 100)","Total_direct_product_cost (USD) = Total_LLM_costs + Software_subscription_costs + Database_hosting_costs + Server_costs + Maintenance_and_repairs_cost"],"Step 3: Sales and Commission costs":["Basic_LLM_commission_and_incentive_cost (USD) = Basic_LLM * (Basic_LLM_variable_commission_per_subscription + Basic_LLM_fixed_commission_per_subscription)","Standard_LLM_commission_and_incentive_cost (USD) = Standard_LLM * (Standard_LLM_variable_commission_per_subscription + Standard_LLM_fixed_commission_per_subscription)","Executive_LLM_commission_and_incentive_cost (USD) = Executive_LLM * (Executive_LLM_variable_commission_per_subscription + Executive_LLM_fixed_commission_per_subscription)","Total_commission_and_incentive_cost (USD) = Basic_LLM_commission_and_incentive_cost + Standard_LLM_commission_and_incentive_cost + Executive_LLM_commission_and_incentive_cost","Reservation_system_cost (USD) = Reservation_system_fixed_fee_per_month * 12","Payment_gateway_cost (USD) = LLM_Subscription_Revenue * (Payment_gateway_fee_rate / 100)","Total_sales_and_commission_cost (USD) = Total_commission_and_incentive_cost + Reservation_system_cost + Payment_gateway_cost"],"Step 4: Other overhead costs for business operations":["Marketing_and_promotions_cost (USD) = LLM_Subscription_Revenue * (Marketing_and_Promotions_share / 100)","Rent_cost (USD) = Monthly_rent_fee * 12","Office_supplies_cost (USD) = Total_Company_Revenue * (Office_supplies_share / 100)","Utilities_cost (USD) = Total_Company_Revenue * (Utilities_share / 100)","IT_communications_cost (USD) = Total_Company_Revenue * (IT_communications_share / 100)","Professional_services_cost (USD) = Monthly_professional_services_fee * 12","Insurance_cost (USD) = Total_Company_Revenue * (Insurance_cost_share / 100)","Total_overhead_cost (USD) = Marketing_and_promotions_cost + Rent_cost + Office_supplies_cost + Utilities_cost + IT_communications_cost + Professional_services_cost + Insurance_cost"],"Step 5: Total cost":["cost (USD) = Total_personnel_cost + Total_direct_product_cost + Total_sales_and_commission_cost + Total_overhead_cost","Total_cost (USD) = cost * (1 + other_cost_share / 100)"]}

description_payload = {
    "formula":cost_formula,
}

staff_component_name = requests.post(
    f"{BASE_URL}/get_staff_component_name",
    json=description_payload,
    proxies=proxies
)

print("\nResponse from /get_staff_component_name.....................")
print(staff_component_name.text)