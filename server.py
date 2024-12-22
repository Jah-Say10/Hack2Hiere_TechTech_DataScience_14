from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import pandas as pd
import numpy as np
import joblib

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

df = pd.read_csv("german_credit_data.csv")
df1 = df.drop(df.columns[0], axis=1)

@app.get("/")
def ping():
    return {"hello": "Hello I am alive !!!"}

def new_data_treatment(age_ar, sex_ar, job_ar, house_ar, saving_accounts_ar, checking_account_ar, credit_amount_ar, duration_ar, purpose_ar):

    MAX_AGE = df1["Age"].max()
    MAX_JOB = df1["Job"].max()
    MAX_CREDIT_AMOUNT = df1["Credit amount"].max()
    MAX_DURATION = df1["Duration"].max()

    age = np.array([age_ar / MAX_AGE])

    sex = np.array([1]) if sex_ar == "male" else np.array([0])

    job = np.array([job_ar / MAX_AGE])

    house = np.zeros(3)
    if house_ar == "free":
        house[0] = 1
    elif house_ar == "own":
        house[1] = 1
    elif house_ar == "rent":
        house[2] = 1

    saving_accounts = np.zeros(5)
    if saving_accounts_ar == "Unknown":
        saving_accounts[0] = 1
    elif saving_accounts_ar == "little":
        saving_accounts[1] = 1
    elif saving_accounts_ar == "moderate":
        saving_accounts[2] = 1
    elif saving_accounts_ar == "quite rich":
        saving_accounts[3] = 1
    elif saving_accounts_ar == "rich":
        saving_accounts[4] = 1

    checking_account = np.zeros(4)
    if checking_account_ar == "Unknown":
        checking_account[0] = 1
    elif checking_account_ar == "little":
        checking_account[1] = 1
    elif checking_account_ar == "moderate":
        checking_account[2] = 1
    elif checking_account_ar == "rich":
        checking_account[3] = 1

    credit_amount = np.array([credit_amount_ar / MAX_CREDIT_AMOUNT])

    duration = np.array([duration_ar / MAX_DURATION])

    purpose = np.zeros(8)
    if purpose_ar == "business":
        purpose[0] = 1
    elif purpose_ar == "car":
        purpose[1] = 1
    elif purpose_ar == "domestic appliances":
        purpose[2] = 1
    elif purpose_ar == "education":
        purpose[3] = 1
    elif purpose_ar == "furniture equipment":
        purpose[4] = 1
    elif purpose_ar == "radio TV":
        purpose[5] = 1
    elif purpose_ar == "repairs":
        purpose[6] = 1
    elif purpose_ar == "vacation others":
        purpose[7] = 1


    data = np.concat((age, sex, job, house, saving_accounts, checking_account, credit_amount, duration, purpose))
    return np.array([data])

# saved_model = load_model('model_dropout.h5')
saved_model = joblib.load("random_forest_model")

@app.get("/predict/{data}")
def predict_score(data):

    data_list = data.split(',')
    print(data)
    print(data_list)

    age = int(data_list[0])
    sex = data_list[1]
    job = int(data_list[2])
    house = data_list[3]
    saving_accounts = data_list[4]
    checking_account = data_list[5]
    credit_amount = float(data_list[6])
    duration = int(data_list[7])
    purpose = data_list[8]
    
    data_treat = new_data_treatment(age, sex, job, house, saving_accounts, checking_account, credit_amount, duration, purpose)
    result = saved_model.predict_proba(data_treat)
    print(result)

    bad = result[0][0]
    good = result[0][1]

    return {"good": good, "bad": bad}

if __name__ == "__main__":
    print("Server is starting...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
    print("Server runnig successfully at port 8000...")