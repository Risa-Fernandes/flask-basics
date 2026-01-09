"""
Part 5: Mini Project - Personal Website with Flask
===================================================
A complete personal website using everything learned in Parts 1-4.

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template

app = Flask(__name__)

# =============================================================================
# YOUR DATA - Customize this section with your own information!
# =============================================================================

PERSONAL_INFO = {
    'name': 'Risa',
    'title': 'Full Stack Developer Intern',
    'bio': 'A passionate developer learning Flask and web development.',
    'email': 'risarajivfernandes@gmail.com',
    'github': 'https://github.com/Risa-Fernandes',
    'linkedin': 'https://linkedin.com/in/risa-fernandes-780145271',
}

SKILLS = [
    {'name': 'Python', 'level': 85},
    {'name': 'HTML/CSS', 'level': 80},
    {'name': 'Flask', 'level': 60},
    {'name': 'JavaScript', 'level': 50},
    {'name': 'Microsoft Excel', 'level': 85},
    {'name': 'SQLite', 'level': 75},
    {'name': 'PHP', 'level': 75},
    {'name': 'Django', 'level': 75},
]

PROJECTS = [
    {'id': 1, 'name': 'Personal Website', 'description': 'A Flask-powered personal portfolio website.', 'tech': ['Python', 'Flask', 'HTML', 'CSS'], 'status': 'Completed'},
    {'id': 2, 'name': 'Pick your Medico Website', 'description': 'Website to manage a particular medical store', 'tech': ['Python', 'Django', 'SQLite'], 'status': 'Completed'},
    {'id': 3, 'name': 'Weather Dashboard', 'description': 'Dashboard that display weather data from an API.', 'tech': ['Python', 'Flask', 'API'], 'status': 'Planned'},
    {'id': 4, 'name': 'Diabetes Prediction ML Model', 'description': 'With the help of details of a person, it predicts whether the person is diabetic or not', 'tech': ['Python', 'API'], 'status': 'Completed'},
    {'id': 5, 'name': 'Event Calendar Telegram Bot', 'description': 'Bot that helps the user to insert their personal events and manipulating any of the events. (insert, edit, view, delete)', 'tech': ['Python', 'Flask', 'API'], 'status': 'Completed'},
]


BLOG_POSTS = [
    {
        "id": 1,
        "title": "Getting Started with Flask",
        "content": "Flask is a lightweight Python web framework that makes web development simple and fun.",
        "date": "Jan 5, 2026"
    },
    {
        "id": 2,
        "title": "Why I Love Python",
        "content": "Python is easy to read, powerful, and has a huge ecosystem of libraries.",
        "date": "Jan 10, 2026"
    },
    {
        "id": 3,
        "title": "My Journey into Web Development",
        "content": "I started learning web development using HTML, CSS, and Flask.",
        "date": "Jan 15, 2026"
    }
]



# =============================================================================
# ROUTES
# =============================================================================

@app.route('/')
def home():
    return render_template('index.html', info=PERSONAL_INFO)


@app.route('/about')
def about():
    return render_template('about.html', info=PERSONAL_INFO, skills=SKILLS)


@app.route('/projects')
def projects():
    return render_template('projects.html', info=PERSONAL_INFO, projects=PROJECTS)


@app.route('/blog')
def blog():
    return render_template(
        'blog.html',
        info=PERSONAL_INFO,
        posts=BLOG_POSTS
    )



@app.route('/project/<int:project_id>')  # Dynamic route for individual project
def project_detail(project_id):
    project = None
    for p in PROJECTS:
        if p['id'] == project_id:
            project = p
            break
    return render_template('project_detail.html', info=PERSONAL_INFO, project=project, project_id=project_id)


@app.route('/skill/<skill_name>')
def skill_projects(skill_name):
    matching_projects = []

    for project in PROJECTS:
        if skill_name in project['tech']:
            matching_projects.append(project)

    return render_template(
        'skill.html',
        info=PERSONAL_INFO,
        skill_name=skill_name,
        projects=matching_projects
    )





@app.route('/contact')
def contact():
    return render_template('contact.html', info=PERSONAL_INFO)


if __name__ == '__main__':
    app.run(debug=True)


# =============================================================================
# PROJECT STRUCTURE:
# =============================================================================
#
# part-5/
# ├── app.py              <- You are here
# ├── static/
# │   └── style.css       <- CSS styles
# └── templates/
#     ├── base.html       <- Base template (inherited by all pages)
#     ├── index.html      <- Home page
#     ├── about.html      <- About page
#     ├── projects.html   <- Projects list
#     ├── project_detail.html <- Single project view
#     └── contact.html    <- Contact page
#
# =============================================================================

# =============================================================================
# EXERCISES:
# =============================================================================
#
# Exercise 5.1: Personalize your website
#   - Update PERSONAL_INFO with your real information
#   - Add your actual skills and projects
#
# Exercise 5.2: Add a new page
#   - Create a /blog route
#   - Add blog posts data structure
#   - Create blog.html template
#
# Exercise 5.3: Enhance the styling
#   - Modify static/style.css
#   - Add your own color scheme
#   - Make it responsive for mobile
#
# Exercise 5.4: Add more dynamic features
#   - Create a /skill/<skill_name> route
#   - Show projects that use that skill
#
# =============================================================================
