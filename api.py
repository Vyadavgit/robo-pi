from flask import Flask, render_template
import subprocess

app = Flask(__name__)
process = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    global process
    process = subprocess.Popen(['python', 'main.py'])
    return 'Process started', 200

@app.route('/stop')
def stop():
    global process
    if process:
        process.terminate()
        process = None
        return 'Process stopped', 200
    else:
        return 'No process running', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context=('cert.pem', 'key.pem'))
