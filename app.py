import pickle
from flask import Flask, render_template, request

app = Flask(__name__)
model = pickle.load(open('models/insurance_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    age = float(request.form.get("age"))
    prediction = model.predict([[age]])[0]
    probability = model.predict_proba([[age]])[0]
    prob_percentage = round(probability[prediction] * 100, 2)
    return render_template('index.html', prediction=prediction, probability=prob_percentage)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
