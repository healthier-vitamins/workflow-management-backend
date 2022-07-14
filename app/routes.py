from app import app_inner, db
# this only works because of __init__.py file, final line, import.
from app.models import User_Accounts, Stock_List
from flask import request, jsonify
from flask_cors import cross_origin

#! flask-wtf sigh
# from app.login_form import LoginForm
# from flask_login import current_user, login_user
# from werkzeug.datastructures import CombinedMultiDict

@app_inner.route('/')
def index():
    return "hello"

@app_inner.route('/sign-up', methods=['POST'])
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
    stocks_arr = []
    for i in range(len(stocks)):
        stock_item = {}
        stock_item['id'] = stocks[i].id
        stock_item['item'] = stocks[i].item
        stocks_arr.append(stock_item)
    return jsonify(stocks_arr)

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

@app_inner.route('/login-user', methods=['POST'])
def loginValidation():
    #! throwaway code sigh
    x = request.get_json()
    logged_in = User_Accounts.query.filter_by(email=x['email'], password_hash=x['password']).first_or_404(description="Invalid user login")

    if logged_in == "Invalid user login":
        return {"is_logged_in": logged_in, "email": x['email']}
    else:
        user_credents = vars(logged_in)
        user_credents.pop("_sa_instance_state")
        return jsonify(user_credents)

    #! flask wtf does not work go kys :(
    # print("var request", vars(request))
    # print("request files", request.files)
    # print("request form", request.form)

    # this is not to store the data...
    # pass in logs for logging in from flask-wtforms
    # form = LoginForm(CombinedMultiDict((request.get_data, request.form)))


    # if form.validate_on_submit():
    #     user = User_Accounts.query.filter_by(email=form.email.data).first()
    #     return "test"
    #     if user is None or not x['password']:
        # User_Accounts.check_password(x['password']):
    #         return "login failed"
    #     login_user(user, remember=True)
    #     return "logged in"
    # return "log in again noob"
    

# create stock POST
# add projects
