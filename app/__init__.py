from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index.html')

@app.route('/profile')
def profile():
    return "profile"

@app.route('/listing')
def listing():
    items = list(range(20))

    return render_template('listing.html', items=items)

@app.route('/dashboard')
def dashboard():


    return render_template('dashboard.html')



if __name__ == "__main__":
    app.run(debug=True )
