from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("myform.html")

@app.route('/result', methods=['POST'])
def create_user():
    name1 = request.form['name']
    location1 = request.form['location']
    language1 = request.form['language']
    comment1 = request.form['comment']
  
   # redirects back to the '/' route
    return render_template("result.html",name=name1, location=location1, language=language1, comment=comment1)


app.run(debug=True)