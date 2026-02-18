from flask import Flask, render_template, request # class

# instance/object of flask
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def aboutmyself():
    name = request.args.get('name') # value, None
    email = request.args.get('email')
    hobby = request.args.get('hobby')

    return render_template('about.html', name=name, email=email, hobby=hobby)

if __name__ == '__main__':
    app.run(debug=True)