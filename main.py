from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
@app.route("/boxes",methods = ["POST", "POST"])
def boxes():
    if request.method == 'POST':
        if request.form["item"] == "red":
            return render_template("index2.html")
        if request.form["item"] == "yellow":
            return render_template("index3.html")
        if request.form["item"] == "green":
            return render_template("index4.html")
        if request.form["item"] == "blue":
            return render_template("index5.html")
        if request.form["item"] == "magenta":
            return render_template("index6.html")
        else:
            return render_template("index7.html")
@app.route("/boxes/red")
def red():
    if request.method == "POST":

        return render_template("index8.html", items="")
if __name__ == '__main__':
    app.run(debug=True)