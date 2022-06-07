from flask import Flask,request,render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/login',methods=['POST','GET'])
def login():
    return render_template("login.html")

@app.route('/signup',methods=['POST','GET'])
def signup():
    return render_template("signup.html")

@app.route('/home',methods=['POST','GET'])
def home():
    return render_template("home.html")

@app.route('/features',methods=['POST','GET'])
def features():
    return render_template("features.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    float_features = [float(x) for x in request.form.values()]
    final = [np.array(float_features)]
    prediction = model.predict(final)


    if prediction == "Pass":
        return render_template('prediction.html', pred="Student will pass")
    else:
        return render_template('prediction.html', pred="Student may fail!!!")


if __name__ == '__main__':
    app.run(debug=True)