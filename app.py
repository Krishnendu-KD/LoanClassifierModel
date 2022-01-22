from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("LoanClassification.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        
        Gender=request.form['Gender']
        if(Gender=='Male'):
            Gender=1.0
        else:
            Gender=0.0


        Married=request.form['Married']
        if(Married=='Yes'):
            Married=1.0
        else:
            Married=0.0

        Dependents=request.form['Dependents']
        if (Dependents=='0'):
            Dependents=0.0
        elif (Dependents=='1'):
            Dependents=1.0
        elif (Dependents=='2'):
            Dependents=2.0
        else:
            Dependents=3.0

        Education=request.form['Education']
        if(Education=='Graduate'):
            Education=1
        else:
            Education=0

        Self_Employed=request.form['Self_Employed']
        if (Self_Employed=='Yes'):
            Self_Employed=1.0
        else:
            Self_Employed=0.0


        ApplicantIncome=int(str(request.form['ApplicantIncome']).strip())
        CoapplicantIncome=float(str(request.form['CoapplicantIncome']).strip())
        LoanAmount=float(str(request.form['LoanAmount']).strip())
        Loan_Amount_Term=float(str(request.form['Loan_Amount_Term']).strip())

        Credit_Hostory=request.form['Credit_Hostory']
        if (Credit_Hostory==1.0):
            Credit_Hostory=1.0
        else:
            Credit_Hostory=0.0


        

        Property_Area=request.form['Property_Area']
        if (Property_Area=='Urban'):
            Property_Area=1
        elif (Property_Area=='Rural'):
            Property_Area=0
        elif (Property_Area=='Semiurban'):
            Property_Area=2
        

        
        prediction=model.predict_proba([[
            Gender,
            Married,
            Dependents,
            Education,
            Self_Employed,
            ApplicantIncome,
            CoapplicantIncome,
            LoanAmount,
            Loan_Amount_Term,
            Credit_Hostory,
            Property_Area,
        ]])

        output=prediction[0][1]



        return render_template('home.html',prediction_text="The probability for you to get the loan is: {} %".format(round(output*100),2))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)