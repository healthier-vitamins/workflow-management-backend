from app import app_inner, db
# this only works because of __init__.py file, final line, import.
from app.models import User_Accounts, Stock_List
from flask import request, jsonify, Response, json
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

    is_taken = User_Accounts.query.filter_by(email=x['email']).first()
    if is_taken:
        return Response(json.dumps({"status": "Email taken"}), mimetype='application/json')
    else:
        set = User_Accounts()
        set.set_password(password=x['password'])
        sql_temp = User_Accounts(first_name=x["first_name"], last_name=x["last_name"], email=x["email"], password_hash=set.password_hash)
        db.session.add(sql_temp)
        db.session.commit()
        logged_in = User_Accounts.query.filter_by(email=x['email']).first()
        user_credents = vars(logged_in)
        user_credents.pop("_sa_instance_state")
        stringed = json.dumps(user_credents)
        return Response(stringed, mimetype='application/json')


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
    logged_in = User_Accounts.query.filter_by(email=x['email']).first()

    if logged_in == None:
        stringed = json.dumps({"error": "Invalid email"})
        return Response(stringed, mimetype='application/json')
    else:
        if logged_in.check_password(password=x['password']):
            user_credents = vars(logged_in)
            user_credents.pop("_sa_instance_state")
            stringed = json.dumps(user_credents)
            return Response(stringed, mimetype='application/json')
        else:
            stringed = json.dumps({"error": "Invalid password"})
            return Response(stringed, mimetype='application/json')


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
        stringed = json.dumps({"status": "Account deleted"})
        return Response(stringed, mimetype='application/json')
    else:
        stringed = json.dumps({"status": "Account not found"})
        return Response(stringed, mimetype='application/json')
    #! eventually edit is_deleted instead

@app_inner.route('/change-password/<user_id>', methods=['PUT'])
def changePw(user_id):
    x = request.get_json()
    account_to_edit = User_Accounts.query.get(user_id)
    account_to_edit.password_hash = ""
    account_to_edit.set_password(password=x['new_password_first'])
    db.session.commit()
    # account_to_edit.set_password(password=x['new_password_first'])
    # user_credents = vars(account_to_edit)
    # user_credents.pop("_sa_instance_state")
    # stringed = json.dumps(user_credents)
    # return Response(stringed, mimetype='application/json')
    q = User_Accounts.query.get(user_id)
    user_credents = vars(q)
    user_credents.pop("_sa_instance_state")
    stringed = json.dumps(user_credents)
    return Response(stringed, mimetype='application/json')



'''to-do list'''
# create stock POST
# add projects
# is_delete
# pop hashed password from response
''''''
