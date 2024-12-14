import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("german_credit_data.csv")

df1 = df.drop(df.columns[0], axis=1)

df1["Age"].isnull().sum()
MAX_AGE = df1["Age"].max()
age = df1["Age"] / MAX_AGE

df1["Sex"].isnull().sum()
df1["Sex"].value_counts()
le_sex = LabelEncoder()
sex = le_sex.fit_transform(df1["Sex"])
sex = pd.DataFrame(sex, columns=["Sex"])

df1["Job"].isnull().sum()
df1["Job"].value_counts()
job = pd.get_dummies(df1["Job"], prefix="job count", dtype=int)

df1["Housing"].isnull().sum()
df1["Housing"].value_counts()
house = pd.get_dummies(df1["Housing"], dtype=int)

df1["Saving accounts"].isnull().sum()
df1["Saving accounts"].value_counts()
saving_accounts = pd.get_dummies(df1["Saving accounts"], dtype=int)


df1["Checking account"].isnull().sum()
df1["Checking account"].value_counts()
checking_account = pd.get_dummies(df1["Checking account"], dtype=int)

df1["Credit amount"].isnull().sum()
MAX_CREDIT_AMOUNT = df1["Credit amount"].max()
credit_amount = df1["Credit amount"] / MAX_CREDIT_AMOUNT

MAX_DURATION = df1["Duration"].max()
df1["Duration"].isnull().sum()
duration = df1["Duration"] / MAX_DURATION

df1["Purpose"].isnull().sum()
df1["Purpose"].value_counts()
purpose = pd.get_dummies(df1["Purpose"], dtype=int)

df1["Risk"].isnull().sum()
df1["Risk"].value_counts()
le_risk = LabelEncoder()
risk = le_risk.fit_transform(df1["Risk"])

X = pd.concat([age, sex, job, house, saving_accounts, checking_account, credit_amount, duration, purpose], axis="columns")
Y = pd.DataFrame(risk, columns=["Risk"])

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

import tensorflow as tf
from tensorflow import keras
from keras import layers, regularizers

model_1 = keras.Sequential()
model_1.add(keras.Input(shape=(26,)))
model_1.add(layers.Dense(50, activation="relu", name="Hidden1", kernel_regularizer=regularizers.l2(0.05)))
model_1.add(layers.Dense(2, activation="softmax"))

model_1.compile(
    loss=keras.losses.SparseCategoricalCrossentropy(),
    optimizer=keras.optimizers.Adam(learning_rate=0.02),
    metrics=["accuracy"]
)

model_1.fit(X_train, y_train, epochs=100)

model_1.evaluate(X_test, y_test)