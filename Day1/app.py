from flask import Flask, render_template # class

app = Flask(__name__, template_folder='.') # object


@app.route('/abc')
def myfunc():
    return render_template('a.html')

@app.route('/abc/xyz')
def myfunc2():
    return 'Hi from myfunc2'



app.run(debug=True) # method