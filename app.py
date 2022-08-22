from flask import Flask, render_template, request
from sklearn.linear_model import LinearRegression
import pickle
import numpy as np
app = Flask(__name__)
hk = pickle.load(open('model.pkl','rb'))
hk1 = pickle.load(open('model_1.pkl','rb'))
hk2 = pickle.load(open('modelss.pkl','rb'))



@app.route("/",methods=['GET','POST'])
def pro():
    if request.method == 'POST':
        _card_1 = request.form['card_1']
        _card_2 = request.form['card_2']
        _card_3 = request.form['card_3']
        _sumcard = request.form['sumcard']
        _losscard = request.form['losscard']
        _passcard = request.form['passcard']
        _wincard = request.form['wincard']
        _card_deler = request.form['card_deler_2']
        _round = hk2.predict([[_card_1,_card_2,_card_3,_sumcard,_card_deler,_losscard,_passcard,_wincard]])
        # _prediction = hk2.predict([[_card_1,_card_2,_round,_card_deler]])
        return render_template('index1.html',prediction=round(_round[0]))

    return render_template('index1.html')


if __name__ == "__main__":
    app.run()