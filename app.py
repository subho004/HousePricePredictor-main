#flask, scikit-learn, pandas, pickle-mixin, pymongo[srv], certifi, python-dotenv
import os
import pprint
import certifi

from pymongo import MongoClient
import pandas as pd
import pickle

from flask import Flask, render_template, request
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
connectionString = os.environ.get("MONGODB_URL")
client=MongoClient(connectionString, tlsCAFile=certifi.where())

dbs=client.list_database_names()
print(dbs)
test_db=client.test

app = Flask(__name__)
data=pd.read_csv('Cleaned_Housedata.csv')
pipe=pickle.load(open("RidgeHouseModel.pkl",'rb'))


@app.route('/')
def index():

    locations=sorted(data['location'].unique())
    return render_template('index.html',locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    name = request.form.get('name')
    email = request.form.get('email')
    location = request.form.get('location')
    bhk = request.form.get('bhk')
    bath = request.form.get('bath')
    sqft = request.form.get('total_sqft')

    print(location, bhk, bath, sqft)

    input_data = pd.DataFrame([[location, sqft, bath, bhk]],
                              columns=['location', 'total_sqft', 'bath', 'bhk'])

    input_data['total_sqft'] = pd.to_numeric(input_data['total_sqft'])
    input_data['bath'] = pd.to_numeric(input_data['bath'])
    input_data['bhk'] = pd.to_numeric(input_data['bhk'])

    input_data = input_data[['location', 'total_sqft', 'bath', 'bhk']]

    print("Input Data:")
    print(input_data)

    prediction = pipe.predict(input_data)
    prediction_data = str(prediction[0])

    insert_prediction_data(name, email, location, bhk, bath, sqft, prediction_data)

    all_data = retrieve_all_data()
    pprint.pprint(all_data)

    return prediction_data


def insert_prediction_data(name, email,location, bhk, bath, sqft, predictionData):
    collection = test_db.predictions
    prediction_document = {
        "name":name,
        "email":email,
        "location": location,
        "bhk": bhk,
        "bath": bath,
        "sqft": sqft,
        "prediction": predictionData,
        
    }
    inserted_id = collection.insert_one(prediction_document).inserted_id
    print(f"Prediction data inserted with ID: {inserted_id}")

def retrieve_all_data():
    collection = test_db.predictions
    all_data_cursor = collection.find({}, {'_id': 0})
    all_data = list(all_data_cursor)
    return all_data

if __name__ == "__main__":
    app.run(debug=True, port=5001)
