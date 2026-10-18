import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return 'Community Issue Reporter is running!'

@app.route('/report', methods=['GET', 'POST'])
def report():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        location = request.form['location']
        category = request.form['category']

        connection = sqlite3.connect('issues.db')
        connection.execute(
            'INSERT INTO issues (title, description, location, category) VALUES (?, ?, ?, ?)',
            (title, description, location, category)
        )
        connection.commit()
        connection.close()

        return 'Issue submitted! <a href="/report">Report another</a>'

    return render_template('report.html')

@app.route('/issues')
def issues():
    connection = sqlite3.connect('issues.db')
    connection.row_factory = sqlite3.Row
    all_issues = connection.execute(
        'SELECT * FROM issues ORDER BY created_at DESC'
    ).fetchall()
    connection.close()
    return render_template('issues.html', issues=all_issues)

@app.route('/issues/<int:issue_id>')
def issue_detail(issue_id):
    connection = sqlite3.connect('issues.db')
    connection.row_factory = sqlite3.Row
    issue = connection.execute(
        'SELECT * FROM issues WHERE id = ?', (issue_id,)
    ).fetchone()
    connection.close()

    if issue is None:
        return 'Issue not found', 404

    return render_template('issue_detail.html', issue=issue)

@app.route('/issues/<int:issue_id>/status', methods=['POST'])
def update_status(issue_id):
    new_status = request.form['status']

    connection = sqlite3.connect('issues.db')
    connection.execute(
        'UPDATE issues SET status = ? WHERE id = ?',
        (new_status, issue_id)
    )
    connection.commit()
    connection.close()

    return redirect(f'/issues/{issue_id}')

if __name__ == '__main__':
    app.run(debug=True)