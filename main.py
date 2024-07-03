from flask import Flask, render_template, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = '/home/YOURNAME/uploadsite/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
MAX_CONTENT_LENGTH = 1024 * 1024 * 1024  # 1 GB limit
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file"
    
    # Ensure the "uploads" directory exists
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    
    return f"File uploaded successfully! Saved at: {file_path}"

if __name__ == '__main__':
    custom_message = '\nUpload files to "http://ip:8003/upload". Run command: "curl -F file=@/path/to/your/file.txt http://ip:8003/upload"\n'
    print(custom_message)
    app.run(host="0.0.0.0", port=8000, debug=False)
