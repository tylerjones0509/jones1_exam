from flask import Flask, render_template
import os

# Define the path to the templates folder inside the 'app' folder
template_folder = os.path.join(os.getcwd(), 'app', 'templates')

# Initialize the Flask app and specify the custom template folder
app = Flask(__name__, template_folder=template_folder)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/exam')
def exam():
    return render_template('exam.html')

if __name__ == '__main__':
    app.run(debug=True)
