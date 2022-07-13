from app import app_inner, db
from app.models import User_Accounts, Stock_List
from flask import request, jsonify
from flask_cors import cross_origin

@app_inner.route('/')
def index():
    return "hello"

@app_inner.route('/create-new-user', methods=['POST'])
@cross_origin()
def createNewUser():

    x = request.get_json()
    # run hash method
    password_hashed = x["password"]

    sql_temp = User_Accounts(first_name=x["first_name"], last_name=x["last_name"], email=x["email"], password_hash=password_hashed)
    db.session.add(sql_temp)
    db.session.commit()
    return x

@app_inner.route('/show-stock-list', methods=['GET'])
def showStocks():
    stocks = Stock_List.query.all()
    stocks_dict = {}
    for i in stocks:
        stocks_dict[i.id] = i.item
    return jsonify(stocks_dict)

@app_inner.route('/update-user/<user_id>', methods=['PUT'])
def updateAcc(user_id):
    x = request.get_json()
    account_to_edit = User_Accounts.query.get(user_id)
    account_to_edit.first_name = x["first_name"]
    account_to_edit.last_name = x["last_name"]
    account_to_edit.email = x["email"]
    account_to_edit.job_position = x["job_position"]
    account_to_edit.current_workflow = x["current_workflow"]
    db.session.commit()
    return x


