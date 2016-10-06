from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = FALSE #only true while testing
@app.route("/")
def hello():
    return render_template('index.html')
@app.route("/sources")
def sources():
    return render_template('source.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
