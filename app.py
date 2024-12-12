from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cancion.mp4')
def serve_video():
    return send_from_directory('.', 'cancion.mp4')

if __name__ == '__main__':
    app.run(debug=True)
