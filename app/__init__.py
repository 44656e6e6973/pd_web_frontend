from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    items = list(range(9))

    return render_template('base.html', items=items)

@app.route('/profile')
def profile():
    return "profile"

@app.route('/listing')
def listing():
    return "listing"



if __name__ == "__main__":
    app.run(debug=True )
