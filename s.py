from flask import Flask, render_template, request, jsonify
import threading
from io import StringIO
import contextlib
from genie import main
app = Flask(__name__)

output_buffer = StringIO()  # Create an in-memory buffer to capture output

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_capture():
    # Clear the buffer and start capturing the output
    output_buffer.seek(0)
    output_buffer.truncate()

    def target():
        try:
            with contextlib.redirect_stdout(output_buffer):
                # Call your main() function or process here
                main()
        except Exception as e:
            print(f"Error: {e}")

    # Start a thread to capture the output
    threading.Thread(target=target).start()
    
    return jsonify({"status": "started"})

@app.route('/get_output')
def get_output():
    # Get the captured output from the buffer
    output = output_buffer.getvalue()
    
    # Return the captured output as JSON
    return jsonify({"output": "\n" + output})

if __name__ == '__main__':
    app.run(debug=False)
