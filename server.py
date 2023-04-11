from flask import Flask, jsonify,request,make_response,render_template,send_file
import util
import pandas as pd
import numpy as np
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import seaborn as sns
app = Flask(__name__,template_folder='templates')

diabetes_df=pd.read_csv("project.csv")


@app.route('/',methods=["GET", "POST"])
def main():
    return render_template("app.html")

@app.route('/predict_page',methods=["GET", "POST"])
def predict_page():
    return render_template("app.html")

@app.route('/visualization',methods=["GET", "POST"])
def visualization():
    x = diabetes_df['sbp']
    y = diabetes_df['glucose']
    fig, ax = plt.subplots(figsize=(6, 6))
    ax = sns.set(style="darkgrid")
    sns.lineplot(x, y)
    canvas = FigureCanvas(fig)
    img = io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='img/png')




@app.route('/vis_page',methods=["GET", "POST"])
def vis_page():
    return render_template("visualization.html")

@app.route('/predict_glucose', methods=['POST'])
def predict_glucose():
    print(request.form['age'],request.form['sbp'],request.form['dbp'],request.form['pulse'],request.form['bmi'],request.form['weight'],request.form['gender'])
    age = float(request.form['age'])
    sbp=float(request.form['sbp'])
    dbp=float(request.form['dbp'])
    pulse=float(request.form['pulse'])
    bmi=float(request.form['bmi'])
    weight=float(request.form['weight'])
    gender=request.form['gender']
    print(age,sbp,dbp,pulse,bmi,weight,gender)
    if gender == 'M':
        m = 1
        f = 0
    else:
        m = 0
        f = 1
    print(m, f)
    result=util.get_estimated_glucose(age,sbp,dbp,pulse,bmi,weight,f,m)
    print(result)
    return render_template("result.html", output=result)



if __name__ == "__main__":
    print("Starting model for glucose prediction..")
    app.run()