from app import app_inner, db
from app.models import User_Accounts, Job_Positions

@app_inner.shell_context_processor
def make_shell_context():
    return {'db': db, 'User_Accounts': User_Accounts, 'Job_Positions': Job_Positions}
