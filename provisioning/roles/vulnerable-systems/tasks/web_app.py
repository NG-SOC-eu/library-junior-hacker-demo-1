from flask import Flask, request, render_template_string
import sqlite3
import os

app = Flask(__name__)

# --- Setup Fake Database ---
def init_db():
    conn = sqlite3.connect('bank.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS accounts (id INTEGER, username TEXT, hash TEXT)')
    c.execute('DELETE FROM accounts') # Clear old data
    c.execute("INSERT INTO accounts VALUES (1, 'bank_manager', 'BSides{Fl4g2_SQL_1nj3ct10n_M4st3r}')")
    c.execute("INSERT INTO accounts VALUES (2, 'helpdesk', 'Password123')")
    conn.commit()
    conn.close()

init_db()

# --- FLAG 2: SQL Injection Vulnerability ---
@app.route('/employee_portal', methods=['GET', 'POST'])
def portal():
    html = '''
    <h2>IronVault Customer Lookup</h2>
    <form method="POST">
        Username: <input type="text" name="user">
        <input type="submit" value="Search">
    </form>
    '''
    if request.method == 'POST':
        user = request.form['user']
        conn = sqlite3.connect('bank.db')
        c = conn.cursor()
        # VULNERABLE: Direct string formatting instead of parameterized queries
        query = f"SELECT * FROM accounts WHERE username = '{user}'"
        try:
            c.execute(query)
            results = c.fetchall()
            html += "<h3>Results:</h3><ul>"
            for row in results:
                html += f"<li>User: {row[1]} | Hash: {row[2]}</li>"
            html += "</ul>"
        except Exception as e:
            html += f"<p>Database Error: {e}</p>"
    return html

# --- FLAG 3: Command Injection Vulnerability ---
@app.route('/atm_diagnostic', methods=['GET', 'POST'])
def diagnostic():
    html = '''
    <h2>ATM Diagnostic Ping Tool</h2>
    <form method="POST">
        IP Address: <input type="text" name="ip">
        <input type="submit" value="Ping ATM">
    </form>
    '''
    if request.method == 'POST':
        ip = request.form['ip']
        # VULNERABLE: Directly passing user input to the OS shell
        # An attacker can input: 127.0.0.1 ; cat /root/flag3.txt
        command = f"ping -c 1 {ip}"
        output = os.popen(command).read()
        html += f"<pre>{output}</pre>"
    return html

if __name__ == '__main__':
    # Run openly on port 80
    app.run(host='0.0.0.0', port=80)
