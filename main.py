import requests

GENDER = "male"
WEIGHT_KG = 100
HEIGHT_CM = 190
AGE = 22

URL_CALC_FROM_NATURAL_LNG = "https://trackapi.nutritionix.com/v2/natural/exercise" # method POST

headers = {
    "x-app-key": API_KEY,
    "x-app-id": APP_ID
}

user_input = str(input("What have you exercised?"))

PARAMS = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


response = requests.post(URL_CALC_FROM_NATURAL_LNG, headers=headers, json=PARAMS)

print(response.json())
