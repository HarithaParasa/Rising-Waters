from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    data = [[
        float(request.form['Temp']),
        float(request.form['Humidity']),
        float(request.form['CloudCover']),
        float(request.form['Annual']),
        float(request.form['JanFeb']),
        float(request.form['MarMay']),
        float(request.form['JunSep']),
        float(request.form['OctDec']),
        float(request.form['avgjune']),
        float(request.form['sub'])
    ]]

    data = scaler.transform(data)

    result = model.predict(data)

    if result[0] == 1:
        prediction = "⚠ FLOOD LIKELY"
    else:
        prediction = "✅ NO FLOOD"

    return render_template(
        "index.html",
        prediction=prediction
    )


if __name__ == "__main__":
    app.run(debug=True)