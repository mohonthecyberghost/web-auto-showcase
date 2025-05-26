from flask import Flask, render_template
import os

app = Flask(__name__)

# Project data
projects = {
    'web_scraping': [
        # Add more web scraping projects here
    ]
}

@app.route('/')
def home():
    return render_template('index.html', projects=projects)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True) 