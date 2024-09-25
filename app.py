from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load model and vectorizer
loaded_model = pickle.load(open('linear_regression_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def main():
    return render_template("index.html")  # Assumes index.html is in a templates folder

@app.route('/back', methods=['POST','GET'])
def change():
    return render_template("index.html")

@app.route('/predict', methods=['POST','GET'])
def prediction():

    longitude = float(request.form.get('longitude'))
    latitude = float(request.form.get('latitude') )
    housing_median_age = float(request.form.get('housing_median_age') )
    total_rooms = float(request.form.get('total_rooms') )
    total_bedrooms = float(request.form.get('total_bedrooms') )
    population = float(request.form.get('population') )
    households = float(request.form.get('households') )
    median_income = float(request.form.get('median_income') )
    ocean_proximity = float(request.form.get('ocean_proximity'))

    user_input = np.array([[longitude, latitude, housing_median_age, total_rooms,
                        total_bedrooms, population, households, median_income,
                        ocean_proximity]])
    
    user_input_scaled = scaler.transform(user_input)

    prediction = abs((loaded_model.predict(user_input_scaled))* 500001)

    return render_template("result.html", pred=prediction[0], long = longitude, lat = latitude, age = housing_median_age, room = total_rooms, bed = total_bedrooms, pop = population, house=households, income = median_income, prox=ocean_proximity)
    

    

if __name__ == "__main__":
    app.run(debug=True)