from app import app_inner

@app_inner.route('/')
@app_inner.route('/index')
def index():
    return "Hello, World index!"
