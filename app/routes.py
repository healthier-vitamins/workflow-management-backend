from app import app_inner, db
# this only works because of __init__.py file, final line, import.
from app.models import User_Accounts, Stock_List
from flask import request, jsonify
from flask_cors import cross_origin

'''flask-wtf sigh'''
#! from app.login_form import LoginForm
#! from flask_login import current_user, login_user
#! from werkzeug.datastructures import CombinedMultiDict
''''''

@app_inner.route('/')
def index():
    return "Welcome to <office> management"

@cross_origin()
@app_inner.route('/sign-up', methods=['POST'])
def createNewUser():
    x = request.get_json()

    # hash method lol
    set = User_Accounts()
    set.set_password(password=x['password'])

    sql_temp = User_Accounts(first_name=x["first_name"], last_name=x["last_name"], email=x["email"], password_hash=set.password_hash)
    try:
        db.session.add(sql_temp)
        db.session.commit()
        # print(sql_temp)
        logged_in = User_Accounts.query.filter_by(email=x['email']).first()
        user_credents = vars(logged_in)
        user_credents.pop("_sa_instance_state")
        return jsonify(user_credents)
    except:
        return {"status": "Email taken"}

@app_inner.route('/show-stock-list', methods=['GET'])
def showStocks():
    stocks = Stock_List.query.all()
    stocks_arr = []
    for i in range(len(stocks)):
        stock_item = {}
        stock_item['id'] = stocks[i].id
        stock_item['item'] = stocks[i].item
        stock_item['quantity'] = stocks[i].quantity
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
    logged_in = User_Accounts.query.filter_by(email=x['email']).first_or_404(description="Invalid email")

    if logged_in == "Invalid email":
        return {"error": logged_in}
    else:
        if logged_in.check_password(password=x['password']):
            user_credents = vars(logged_in)
            user_credents.pop("_sa_instance_state")
            return jsonify(user_credents)
        else:
            return {"error": "Invalid password"}


    '''flask wtf does not work go kys :('''
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
    ''''''

@app_inner.route('/delete-user/<user_id>', methods=['DELETE'])
def deleteUser(user_id):
    #! throwaway code
    account_to_delete = User_Accounts.query.get(user_id)
    if account_to_delete:
        db.session.delete(account_to_delete)
        db.session.commit()
        return {"status": "Account deleted"}
    else:
        return {"status": "Account not found"}
    #! eventually edit is_deleted instead




'''to-do list'''
# create stock POST
# add projects
''''''
