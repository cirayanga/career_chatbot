from flask import Flask, render_template, request

app = Flask(__name__)

# Career descriptions
career_info = {
    "Software Developer": "Software Developers create computer programs and apps.",
    "Graphic Designer": "Graphic Designers create visual content like logos and posters.",
    "Nurse": "Nurses care for patients in hospitals and clinics.",
    "Counselor": "Counselors help people deal with personal and academic challenges.",
    "Marketing Specialist": "Marketing Specialists promote products and services.",
    "Entrepreneur": "Entrepreneurs start and manage businesses.",
    "Journalist": "Journalists report news for newspapers, TV, or online.",
    "Content Creator": "Content Creators produce content for blogs, YouTube, and social media.",
    "Data Analyst": "Data Analysts interpret data to guide decisions.",
    "Engineer": "Engineers design and build solutions.",
    "Data Scientist": "Data Scientists analyze data using ML and statistics.",
    "Cybersecurity Analyst": "Protects data and systems from cyber threats.",
    "AI Engineer": "Builds intelligent systems like recommendation engines.",
    "DevOps Engineer": "Automates and improves software development pipelines.",
    "Animator": "Creates motion graphics and animations.",
    "UX/UI Designer": "Designs user-friendly and attractive interfaces.",
    "Art Director": "Oversees the visual style of creative projects.",
    "Doctor": "Diagnoses and treats medical conditions.",
    "Pharmacist": "Dispenses medications and advises patients.",
    "Medical Technologist": "Performs diagnostic lab tests.",
    "Radiographer": "Operates imaging equipment for diagnosis.",
    "Accountant": "Manages financial records.",
    "Financial Analyst": "Evaluates business and investment data.",
    "Auditor": "Checks financial accuracy and compliance.",
    "Investment Banker": "Manages company financial transactions.",
    "Civil Engineer": "Designs infrastructure like roads and bridges.",
    "Mechanical Engineer": "Works on machines and mechanical systems.",
    "Electrical Engineer": "Designs electrical systems.",
    "Mechatronics Engineer": "Combines electronics and mechanics.",
    "Teacher": "Teaches students at schools.",
    "Lecturer": "Teaches at colleges and universities.",
    "Curriculum Designer": "Designs educational materials.",
    "Online Educator": "Teaches using digital platforms.",
    "Business Analyst": "Improves processes through data insights.",
    "Product Manager": "Leads development of products.",
    "Operations Manager": "Oversees business operations.",
    "Lawyer": "Handles legal cases and advice.",
    "Paralegal": "Assists lawyers with legal tasks.",
    "Compliance Officer": "Ensures legal and policy compliance.",
    "Legal Advisor": "Provides legal advice to organizations.",
    "Athlete": "Competes in professional sports.",
    "Coach": "Trains and guides athletes.",
    "Sports Analyst": "Analyzes sports performance and data.",
    "Physiotherapist": "Rehabilitates physical injuries.",
    "Environmental Scientist": "Solves environmental problems.",
    "Ecologist": "Studies ecosystems and nature.",
    "Urban Planner": "Plans cities and communities.",
    "Sustainability Consultant": "Promotes eco-friendly practices.",
    "Author": "Writes books or creative works.",
    "Copywriter": "Writes marketing and web content.",
    "Social Worker": "Helps people in difficult situations.",
    "Psychologist": "Studies behavior and mental health.",
    "Community Manager": "Engages online or local communities.",
    "HR Specialist": "Handles hiring and staff relations."
}

career_map = {
    "technology": ["Software Developer", "Data Scientist", "Cybersecurity Analyst", "AI Engineer", "DevOps Engineer"],
    "art": ["Graphic Designer", "Animator", "UX/UI Designer", "Art Director"],
    "medicine": ["Doctor", "Nurse", "Pharmacist", "Medical Technologist", "Radiographer"],
    "finance": ["Accountant", "Financial Analyst", "Auditor", "Investment Banker"],
    "engineering": ["Civil Engineer", "Mechanical Engineer", "Electrical Engineer", "Mechatronics Engineer"],
    "education": ["Teacher", "Lecturer", "Curriculum Designer", "Online Educator"],
    "business": ["Entrepreneur", "Business Analyst", "Product Manager", "Operations Manager"],
    "law": ["Lawyer", "Paralegal", "Compliance Officer", "Legal Advisor"],
    "sports": ["Athlete", "Coach", "Sports Analyst", "Physiotherapist"],
    "environment": ["Environmental Scientist", "Ecologist", "Urban Planner", "Sustainability Consultant"],
    "writing": ["Author", "Journalist", "Copywriter", "Content Creator"],
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
if __name__ == "__main__":
    app.run(debug=True, port=5050)







