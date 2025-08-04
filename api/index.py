from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def suggest():
    if request.method == "POST":
        name = request.form['name']
        interests = request.form['interests']
        skills = request.form['skills']
        subjects = request.form['subjects']
        return f"<h2>Hi {name}!</h2><p>Based on your interests ({interests}), skills ({skills}), and favorite subjects ({subjects}), we suggest exploring careers like Data Scientist, UX Designer, or Biotech Analyst.</p>"
    return "<h1>Career Chatbot API</h1>"

# Needed for Vercel
def handler(environ, start_response):
    return app(environ, start_response)
<form action="/api" method="POST">
  ...
</form>
