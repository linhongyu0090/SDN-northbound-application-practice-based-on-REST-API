from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_flow_table', methods=['POST'])
def update_flow_table():
    switch = request.form['switch']
    flow_entry = request.form['flow_entry']
    action = request.form['action']

    if action == 'add':
        subprocess.call(['ovs-ofctl', 'add-flow', switch, flow_entry])
        message = f'Added flow entry to {switch}'
    elif action == 'remove':
        subprocess.call(['ovs-ofctl', 'del-flows', switch, flow_entry])
        message = f'Removed flow entry from {switch}'
    else:
        message = 'Invalid action'

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)

