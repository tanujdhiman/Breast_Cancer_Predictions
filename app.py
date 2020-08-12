  
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Model
filename = 'classifier.pkl'
classifier = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
  
  
@app.route('/')
def home():
    return render_template('aboutus.html')
  
  
@app.route('/')
def home():
    return render_template('testyourself.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        radius_mean = float(request.form['Enter the Radius'])
        texture_mean = float(request.form['Enter the Texture'])
        area_mean = float(request.form['Enter the Area'])
        concavity_mean = float(request.form['Enter the concavity'])
        concave_points_mean = float(request.form['Enter the Concave points'])
        radius_se = float(request.form['Enter the Radius'])
        area_se = float(request.form['Enter the Area'])
        radius_worst = float(request.form['Enter the Radius'])
        texture_worst = float(request.form['Enter the Texture'])
        perimeter_worst = float(request.form['Enter the Parameters'])
        area_worst = float(request.form['Enter the Area'])
        smoothness_worst = float(request.form['Enter the Smoothness'])
        compactness_worst = float(request.form['Enter the Compactness'])
        concave_points_worst = float(request.form['Enter the Concave points'])

        input_data = np.array([[radius_mean, texture_mean, area_mean, concavity_mean, concave_points_mean, radius_se, area_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concave points_worst]])

        my_prediction = classifier.predict(input_data)

        if prediction[0][0] == 1:
            out = 'Oops, Danger you have to take care of yourself. You are Malignant'
        elif prediction[0][0] == 0:
            out = 'Great, you need not to worry. You are Benign'
        return render_template('testyourself.html', prediction_text='{}'.format(out))

if __name__ == '__main__':
    app.run(debug=True)
