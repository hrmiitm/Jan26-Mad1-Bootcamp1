from flask import Flask, render_template, request # class

# instance/object of flask
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hi from home route</h1>'

@app.route('/about')
def aboutmyself():
    name = request.args.get('name') # value, None
    email = request.args.get('email')

    return render_template('about.html', name=name, email=email)


if __name__ == '__main__':
    app.run(debug=True)