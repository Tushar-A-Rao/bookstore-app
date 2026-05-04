from flask import Flask, render_template

#initiate Flask app
app = Flask(__name__)

#html render
@app.route('/')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
