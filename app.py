from flask import Flask, render_template, request
from templates import generate_readme

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    readme = ""
    if request.method == "POST":
        name = request.form["name"]
        bio = request.form["bio"]
        skills = request.form["skills"]
        projects = request.form["projects"]
        github = request.form["github"]
        theme = request.form["theme"]

        readme = generate_readme(name, bio, skills, projects, github, theme)

    return render_template("index.html", readme=readme)

if __name__ == "__main__":
    app.run(debug=True)