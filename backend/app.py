from flask import Flask, jsonify, send_file
from backend.jira.fetch_data import get_jira_data
from backend.reports.generate_excel import generate_sprint_report
import os

app = Flask(__name__)

@app.route("/ping", methods=["GET"])
def health_check():
 return jsonify({"message": "Scrum Star backend is live!"})

@app.route("/generate-report", methods=["GET"])
def generate_report():
 jira_data = get_jira_data()
 filename = "sprint_report.xlsx"
 report_path = generate_sprint_report(jira_data, filename)
 return send_file(report_path, as_attachment=True)

if __name__ == "__main__":
 app.run(debug=True)
