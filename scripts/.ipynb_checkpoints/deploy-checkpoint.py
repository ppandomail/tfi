from flask import Flask, request, render_template, jsonify
import pickle

# Cargar el modelo
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

variables = ['doc_language_ok', 'alt_texts_ok', 'input_labels_ok', 'empty_buttons_ok', 'empty_links_ok', 'color_contrast_ok', 
             'doc_language_fail', 'alt_texts_fail', 'input_labels_fail', 'empty_buttons_fail', 'empty_links_fail', 'color_contrast_fail']
data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

@app.route("/")
def index():
    results = dict(zip(variables, data))
    return render_template("index.html", results=results)

@app.route('/predict', methods=['POST'])
def predict():
    data.clear()
    for var in variables:
        data.append(int(request.form.get(var)))
    prediction = model.predict([data])
    results = dict(zip(variables, data))
    return render_template('index.html', results=results, prediction=prediction[0])
