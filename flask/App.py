import pickle
from flask import Flask, render_template, request 
import pandas as pd
import numpy as np


app=Flask (__name__)

model = pickle.load(open('blue.pkl', 'rb')) 

@app.route('/') 
@app.route('/home', methods=['GET', 'POST']) 
def Home():
    # with app.app_context():
       return render_template("index.html")
    
    
@app.route('/details', methods=['GET', 'POST'])
def details():
    # with app.app_context():
       return render_template("details.html")

@app.route('/result', methods=['GET', 'POST'])
def result():
# loading model which we saved
    Row = float(request.form['Row#']) 
    MinOfUpperTRange= float(request.form['MinOfUpperTRange']) 
    MaxOfLowerTRange= float(request.form['MaxOfLowerTRange'])
    MinOfLowerTRange= float(request.form['MinOfLowerTRange'])
    AverageOfUpperTRange= float(request.form['AverageOfUpperTRange'])
    AverageRainingDays= float(request.form['AverageRainingDays'])
    AverageOfLowerTRange = float(request.form['AverageOfLowerTRange'])
    MaxOfUpperTRange= float(request.form['MaxOfUpperTRange']) 
    andrena= float(request.form['andrena'])
    Honeybees= float(request.form['Honeybees'])
    clonesize= float(request.form['clonesize'])
    bumbles= float(request.form['bumbles'])
    osmia= float(request.form['osmia'])
    RainingDays= float(request.form['RainingDays'])
    fruitset= float(request.form['fruitset'])
    fruitmass= float(request.form['fruitmass'])
    seeds= float(request.form['seeds'])
    
    
    prediction =model.predict(pd.DataFrame([[ Row,MinOfUpperTRange, MaxOfLowerTRange,MinOfLowerTRange, AverageOfUpperTRange,AverageRainingDays,AverageOfLowerTRange,MaxOfUpperTRange,andrena,Honeybees,
                                             clonesize,bumbles,osmia,RainingDays,fruitset,fruitmass,seeds]]))
    return render_template('predict.html', prediction_text = "{}".format(abs(prediction)))
if __name__ == "__main__":
    app.run(debug=True)