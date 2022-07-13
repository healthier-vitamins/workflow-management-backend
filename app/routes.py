from audioop import cross
from app import app_inner, db
from app.models import User_Accounts, Stocks
from flask import request, jsonify


@app_inner.route('/')
def index():
    return "hello"

@app_inner.route('/create-new-user', methods=['POST'])
@cross_origin()
def createNewUser():
    # print("request: ", request.get_json()['first_name'])

    x = request.get_json()
    sql_temp = User_Accounts(first_name=x["first_name"], last_name=x["last_name"], email=x["email"], username=x["username"], password_hash=x["password_hash"], job_position=x['job_position'])

    db.session.add(sql_temp)
    db.session.commit()
    return x

@app_inner.route('/show-stocks', methods=['GET'])
def showStocks():
    stocks = Stocks.query.all()
    print(stocks)
    stocks_dict = {}
    for i in stocks:
        stocks_dict[i.id] = i.item
    return stocks_dict

@app_inner.route('/update-user/<user_id>', methods=['PUT'])
def updateAcc(user_id):
    x = request.get_json()
    account_to_edit = User_Accounts.query.get(user_id)
    account_to_edit.first_name = x["first_name"]
    account_to_edit.last_name = x["last_name"]
    account_to_edit.email = x["email"]
    account_to_edit.username = x["username"]
    account_to_edit.current_workflow = x["current_workflow"]
    db.session.commit()
    return x


