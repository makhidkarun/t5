from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloworld():
    return 'Traveller5'

# to get the d3 javascript source URL
# url_for('static', filename='js/d3.v3.min.js')
