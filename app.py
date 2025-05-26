from flask import Flask, render_template
import os

app = Flask(__name__)

# Project data
projects = {
    'web_scraping': [
        {
            'title': 'Web Scraping Project 1',
            'description': 'Description of your web scraping project',
            'github_url': 'https://github.com/yourusername/project1',
            'technologies': ['Python', 'BeautifulSoup4', 'Requests']
        },
        # Add more web scraping projects here
    ],
    'other_projects': [
        {
            'title': 'Other Project 1',
            'description': 'Description of your other project',
            'github_url': 'https://github.com/yourusername/other-project1',
            'technologies': ['Python', 'Flask']
        },
        # Add more projects here
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