import uvicorn
import joblib,os
from flask import flash,Flask,render_template,request,url_for,redirect

app = Flask(__name__)

#pkl
phish_model = open('phishing.pkl','rb')
phish_model_ls = joblib.load(phish_model)

@app.route('/')
def init():
    return render_template('index.html')
# ML Aspect
@app.route('/',methods=['GET','POST'])
def index():
    X_predict = []
    features=request.form.get('url')
    X_predict.append(str(features))
    y_Predict = phish_model_ls.predict(X_predict)
    result=''
    if y_Predict == 'bad':
        result = "This is a Phishing Site"
    else:
        result = "This is not a Phishing Site"
    return render_template('index.html', msg=result)
if __name__ == '__main__':
	app.run(debug=True,host="127.0.0.1",port=5000)