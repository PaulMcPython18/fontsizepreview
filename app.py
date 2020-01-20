from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/', methods=['POST'])
def output():
    try:
        namequery1 = request.form['namequery1']
        namequery2 = request.form['namequery2']
        fontsize = str(namequery1) + "px"
        print(fontsize)
        color = str(namequery2)
        if len(color) > 100:
            return render_template('index.html',
                                   other_message="* Sorry! You must input a sequence of characters less than 100! *")
        print(color)
        return render_template('index.html', output = 'Random text!', fontstyle=fontsize, fontcolor=color, message="* Not seeing the correct color? Make sure you have inputted an existant color. *")
    except:
        return render_template('index.html', message="* Sorry! An error occured, reload the page and try again! *")
@app.route('/about')
def about():
    return render_template('about.html')
if __name__ == "__main__":
    app.run(debug=True)
