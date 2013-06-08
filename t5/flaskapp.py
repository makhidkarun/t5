from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)

@app.route('/')
def helloworld():
    return 'Traveller5'

# to get the d3 javascript source URL
# url_for('static', filename='js/d3.v3.min.js')
@app.route('/example')
def render_example():
    return render_template('example.html',
                           name='traveller',
                           d3url=url_for('static', filename='js/d3.v3.min.js'))
