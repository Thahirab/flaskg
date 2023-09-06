from flask import Flask, render_template, Response
from flask_sse import sse
import subprocess
import threading

app = Flask(__name__)

# Flag to track whether the script is running
script_running = False
lock = threading.Lock()
process = None  # Store the subprocess object

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_genie')
def start_genie():
    global script_running, process

    with lock:
        if not script_running:
            script_running = True
            process = subprocess.Popen(['python', 'genie.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return render_template('genie.html')
        else:
            return render_template('genie_already_running.html')

@app.route('/genie_output')
def genie_output():
    def event_stream():
        if process:
            for line in process.stdout:
                yield 'data: {}\n\n'.format(line)
        else:
            yield 'data: {}\n\n'.format('Genie is not running.')

    return Response(event_stream(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(debug=False,host="0.0.0.0")
