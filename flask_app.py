# pythonanywhere.com     vitapele   vitapele@guerrillamail.com      vitap123       vitapele.pythonanywhere.com

# https://tailwind.run/new
# https://www.pythonanywhere.com/user/vitapele/files/home/vitapele/mysite/flask_app.py?edit

from flask import Flask, render_template, request
from os import system

app = Flask(__name__)
# system("python3 ./result.py")

@app.route('/')
def home_page():
    return render_template("home.html")


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/vote')
def vote():
    return render_template("vote.html", image_name="votes.jpg")
# Change "contestant" to candidate
# Add CPI to image
# https://www.bing.com/images/search?q=Muppala+nageswara+rao+CPI


@app.route('/feedback')
def feedback():
    return render_template("feedback.html")


@app.route('/thank', methods=['GET', 'POST'])
def feedt():
    if request.method == 'POST':
        result = request.form
        feedback = request.form.to_dict(result)["feedback"]+' '+request.form.to_dict(result)["experience"]
        system("echo '" + str(feedback) + "' >> mysite/feedback.txt")
        return render_template("thank.html")


@app.route('/reg_done', methods=['GET', 'POST'])
def reg_done():
    if request.method == 'POST':
        result = request.form
        resp = request.form.to_dict(result)["a_num"]+' '+request.form.to_dict(result)["b_year"] #+' '+request.form.to_dict(result)["name"]
        system("echo '" + str(resp) + "' >> mysite/reg_data.txt")
        return render_template("reg_done.html")


@app.route('/vote_done', methods=['GET', 'POST'])
def vote_done():
    if request.method == 'POST':
        result = request.form
        vote = request.form.to_dict(result)["vote"] + ' ' + request.form.to_dict(result)["a_num"]
        system("echo '" + str(vote) + "' >> mysite/vote_data.txt")
        return render_template("vote_done.html")

@app.route('/result')
def result():
    return render_template("result.html", image_name="res.jpg")


if __name__ == '__main__':
    app.run()




