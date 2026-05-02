from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("attrition_model.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = {
        "Age": int(request.form['age']),
        "MonthlyIncome": int(request.form['income']),
        "YearsAtCompany": int(request.form['years'])
    }

    df = pd.DataFrame([data])  # create input dataframe

    prediction = model.predict(df)[0]

    result = "Will Leave" if prediction == 1 else "Will Stay"

    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)