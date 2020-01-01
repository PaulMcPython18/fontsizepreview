from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/', methods=['POST'])
def output():
    namequery1 = request.form['namequery1']
    namequery2 = request.form['namequery2']
    fontsize = str(namequery1) + "px"
    print(fontsize)
    color = str(namequery2)
    print(color)
    return render_template('index.html', output = 'Random text!', fontstyle=fontsize, fontcolor=color, message="* Not seeing the correct color? Make sure you have inputted an existant color. *")
@app.route('/about')
def about():
    return render_template('about.html')
if __name__ == "__main__":
    app.run(debug=True)