from app import application as app

@app.route('/')
def index():
    return 'Hello World!'