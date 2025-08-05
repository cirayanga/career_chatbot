from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Career descriptions
career_info = {
    "Software Developer": "Software Developers create computer programs and apps.",
    # ... [same as yours, truncated for brevity]
    "HR Specialist": "Handles hiring and staff relations."
}

career_map = {
    "technology": ["Software Developer", "Data Scientist", "Cybersecurity Analyst", "AI Engineer", "DevOps Engineer"],
    # ... [rest of your mapping here]
    "social": ["Social Worker", "Psychologist", "Community Manager", "HR Specialist"]
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        interests = request.form["interests"].lower()
        skills = request.form["skills"].lower()
        subjects = request.form["subjects"].lower()

        combined_input = f"{interests} {skills} {subjects}"
        suggestions = []

        for keyword, careers in career_map.items():
            if keyword in combined_input:
                suggestions.extend(careers)

        if len(suggestions) < 3:
            default_careers = ["Engineer", "Content Creator", "Teacher", "Data Analyst", "Marketing Specialist"]
            for career in default_careers:
                if career not in suggestions:
                    suggestions.append(career)
                if len(suggestions) >= 3:
                    break

        suggestions = list(set(suggestions))  # Remove duplicates
        return render_template("results.html", name=name, suggestions=suggestions, career_info=career_info)

    return render_template("index.html")

# ✅ Only one app.run block
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)







