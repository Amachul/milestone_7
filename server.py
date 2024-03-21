from flask import Flask, request, jsonify

import report.report
from report import report as rep

app = Flask(__name__)

# GET /birthdays?month=april&department=HR
@app.get("/birthdays")
def get_birthdays():
    month = request.args.get('month')
    department = request.args.get('department')
    res = report.report.execute_report_for_dept('report\\database.csv', month, department)
    return jsonify(res['birthdays']), 200

# GET /anniversaries?month=april&department=HR
@app.get("/anniversaries")
def get_anniversaries():
    month = request.args.get('month')
    department = request.args.get('department')
    res = report.report.execute_report_for_dept('report\\database.csv', month, department)
    return jsonify(res['anniversaries']), 200

if __name__ == '__main__':
    app.run(debug=True)