from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('heart_disease_feature.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')
standard_to = StandardScaler()
@app.route("/predict", methods=['GET','POST'])
def predict():
    if request.method == 'POST':
         #age
        age=int(request.form['age'])
        # cholestrol
        chol=float(request.form['chol'])
        #sex
        sex=request.form['sex']
        if(sex=='Male'):
            sex=1
        else:
            sex=0
        # EXercised-Induced angina
        exang=request.form['exang']
        if(exang=='Yes'):
            exang=1
        else:
            exang=0    
        #CP type
        cp=request.form['cp']
        if (cp =='atypical_angina'):
            cp_2=1
            cp_4=0
        elif(cp =='asymptomatic'):
            cp_2=0
            cp_4=1
        else:
            cp_2=0
            cp_4=0   
      
        # ECG
        ecg=request.form['ecg']
        if (ecg =='hypertrophy'):
            restecg_2=1
        else:
            restecg_2=0

        # slope of the peak
        slope=request.form['slope']
        if (slope=='down'):
            slope_2=0
            slope_3=1
        elif (slope=='flat'):
            slope_2=1
            slope_3=0   
        else:
            slope_2=0
            slope_3=0
        # Major Vessols
        major_vessels=request.form['major_vessels']
        if (major_vessels =='major_vessels_1'):
            major_vessels_1=1
            major_vessels_2=0
            major_vessels_3=0

        elif (major_vessels =='major_vessels_2'):
            major_vessels_1=0
            major_vessels_2=1
            major_vessels_3=0
        elif (major_vessels =='major_vessels_3'):
            major_vessels_1=0
            major_vessels_2=0
            major_vessels_3=1    
        else:
            major_vessels_1=0
            major_vessels_2=0
            major_vessels_3=0
      
        prediction=model.predict([[age,chol, sex,exang, cp_2, cp_4, restecg_2, slope_2, slope_3, major_vessels_1, major_vessels_2, major_vessels_3]]) 
        output=round(prediction[0])
        if output==0:
            return render_template('index.html',prediction_texts="person Not having a disease")
        else:
            return render_template('index.html',prediction_texts="person having a disease")
            # return render_template('index.html',prediction_text="sensitivitiy of heart disease is {}".format(output))
    else:
        return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)