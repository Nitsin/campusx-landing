from flask import Flask ,render_template

app=Flask(__name__)


@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/class')
def myclass():
    return render_template('myclass.html')



if __name__=="__main__":
    app.run(debug=True)