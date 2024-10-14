from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dummy data for projects and user interests
projects = [
    {"id": 1, "name": "Project A", "tags": ["web", "python", "django"]},
    {"id": 2, "name": "Project B", "tags": ["mobile", "android", "java"]},
    # Add more projects with tags
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/find_projects', methods=['POST'])
def find_projects():
    user_interests = request.form.get('interests').split(',')
    
    # Dummy recommendation algorithm
    matching_projects = []
    for project in projects:
        common_tags = set(user_interests) & set(project['tags'])
        if common_tags:
            matching_projects.append(project)

    return render_template('results.html', projects=matching_projects)

if __name__ == '__main__':
    app.run(debug=True)
