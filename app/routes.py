from app import app_inner, db
from app.models import User_Accounts, Job_Positions
from flask import request, jsonify


@app_inner.route('/')
def index():
    return "hello"
@app_inner.route('/create-new-user', methods=['POST'])
def createNewUser():
    # print("request: ", request.get_json()['first_name'])

    x = request.get_json()
    sql_temp = User_Accounts(first_name=x["first_name"], last_name=x["last_name"], email=x["email"], username=x["username"], password_hash=x["password_hash"], job_position=x["job_position"])
    
    db.session.add(sql_temp)
    db.session.commit()
    return x


