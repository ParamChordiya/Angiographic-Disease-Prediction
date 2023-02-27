from flask import Flask, render_template, request
# import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('knn_model_hdp_v2.pkl', 'rb'))


@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@app.route("/predict", methods=['POST'])
def predict():
    # Fuel_Type_Diesel=0
    # gender=-1

    if request.method == 'POST':
        age = int(request.form['age'])
        # sex=float(request.form['sex'])
        # cp = int(request.form['cp'])
        trestbps = int(request.form['trestbps'])
        chol = int(request.form['chol'])
        # fbs = int(request.form['fbs'])

        # restecg = int(request.form['age'])
        thalach = int(request.form['thalach'])
        # exang = int(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        # slope = int(request.form['slope'])
        ca = int(request.form['ca'])
        thal = int(request.form['thal'])

        # Kms_Driven2=np.log(Kms_Driven)
        # Owner=int(request.form['Owner'])
        # Fuel_Type_Petrol=request.form['Fuel_Type_Petrol']
        # if(Fuel_Type_Petrol=='Petrol'):
        #   Fuel_Type_Petrol=1
        #   Fuel_Type_Diesel=0
        # else:
        #   Fuel_Type_Petrol=0
        #   Fuel_Type_Diesel=1
        # Year=2020-Year
        # Seller_Type_Individual=request.form['Seller_Type_Individual']
        # if(Seller_Type_Individual=='Individual'):
        #   Seller_Type_Individual=1
        # else:
        #   Seller_Type_Individual=0
        sex = request.form['sex']
        if (sex == 'Male'):
            sex = 1
        else:
            sex = 0

        cp = request.form['cp']
        if (cp == 'typical_angina'):
            cp = 0
        elif cp == 'atypical_angina':
            cp = 1
        elif cp == 'non_anginal_pain':
            cp = 2
        else:
            cp = 3

        fbs = request.form['fbs']
        if (fbs == 'yes'):
            fbs = 1
        else:
            fbs = 0

        restecg = request.form['restecg']
        if (restecg == 'normal'):
            restecg = 0
        elif restecg == 'stt':
            restecg = 1
        else:
            restecg = 2

        exang = request.form['exang']
        if (exang == 'yes'):
            exang = 1
        else:
            exang = 0

        slope = request.form['slope']
        if (slope == 'us'):
            slope = 0
        elif slope == 'flat':
            slope = 1
        else:
            slope = 2

        prediction = model.predict([[
            age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang,
            oldpeak, slope, ca, thal
        ]])

        output = prediction
        if output == 0:
            return render_template(
                'no.html', prediction_text='No the diameter is not Narrowing!')
        else:
            return render_template(
                'yes.html', prediction_text="Yes, the Diameter is narrowing!")
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(  # Starts the site
        host='0.0.0.0', port=5000)
