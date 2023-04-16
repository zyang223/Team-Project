from flask import Flask, render_template, request
app = Flask(__name__)
    

@app.route('/welcome/')
def welcome_page():
    return render_template ("welcome.html")

if __name__ == '__main__':
    app.run(debug=True)
