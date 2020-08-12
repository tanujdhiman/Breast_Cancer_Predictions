  
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


@app.route('/predict', methods=['POST'])
def predict():
        features = [float(x) for x in request.form.values()]
        final_features = [np.array(features)]
        my_prediction = classifier.predict(final_features)

        if my_prediction[0] == 1:
            out = 'Oops, Danger you have to take care of yourself. You are Malignant'
        elif my_prediction[0] == 0:
            out = 'Great, you need not to worry. You are Benign'


        return render_template('index.html', prediction_text='{}'.format(out))

if __name__ == '__main__':
    app.run(debug=True)
