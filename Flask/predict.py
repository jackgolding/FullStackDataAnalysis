from flask import Flask, request
from sklearn.externals import joblib


model = joblib.load('../Assets/my_model.pkl')
app = Flask(__name__)

@app.route('/', methods=['POST'])
def predict():
    survivor_data = request.get_json()
    survived = model.predict(
        [
            survivor_data['Pclass'],
            survivor_data['Age'],
            survivor_data['SibSp'],
            survivor_data['Parch'],
            survivor_data['Fare'],
            survivor_data['Embarked'],
            survivor_data['Gender']
        ]
    )
    if survived == 0:
        return('You Died :(')
    else:
        return('You Live :)')


if __name__ == '__main__':

    app.run(debug=True)