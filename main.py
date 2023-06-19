import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 66.2
HEIGHT_CM = 170.18
AGE = 20

# Nutrition API
APP_ID = "16c2b3c7"
API_KEY = "1c0f8b962225eee3331f280d25a4810e"
NUTR_HEADERS = {
    "x-app-id":APP_ID, 
    "x-app-key":API_KEY, 
    "Content-Type":"application/json"
}

# Sheety API
USERNAME = "321fa58bde94038b3168c692dff224b7"
PROJECT_NAME = "myCardioWorkouts"
SHEETNAME = "workouts"
SHTY_HEADERS = (("rsankar","uh45g3hu5v34u5hv3j45b"))

nutr_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutr_config = {
    "query":input("Tell me which exercises you did: "),
    "gender":GENDER,
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT_CM,
    "age":AGE
}
response = requests.post(url=nutr_endpoint, json=nutr_config, headers=NUTR_HEADERS)
result = response.json()["exercises"]


sheety_endpoint = f"https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEETNAME}"
now = datetime.now()
for item in result:
    workout = {
        "workout": {
            "date":now.strftime(r"%m/%d/%Y"),
            "time":now.strftime(r"%H:%M:%S"),
            "exercise":item["name"].title(),
            "duration":round(item["duration_min"]),
            "calories":round(item["nf_calories"])
        }
    }
    response = requests.post(url=sheety_endpoint,json=workout,auth=SHTY_HEADERS)
    print(response.text)