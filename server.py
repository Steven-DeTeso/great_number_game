from flask import Flask, session, render_template, redirect, request
import random

app = Flask(__name__)
app.secret_key = '1234ABCD' #Need secret key anytime we use the import session

@app.route('/')
def index():
    if "num" not in session: #won't get executed unless session has a num already stored
        session['num'] = random.randint(1, 100) #storing the value of a random number as session['num']
    return render_template('index.html')

@app.route('/guess', methods=['POST']) #post methods hide critical data from the url
def guess(): #trigged on the a tag submit button that is has a value='guess'
    session['guess'] = int(request.form['guess']) #gives session a value in int form. Value comes over from request.form['guess']. Then key of session['guess'] is applied to value
    return redirect('/')

@app.route('/reset') #trigged on a tag with href set to /reset 
def reset():
    print (session['guess'])
    session.clear() #this clears the session of its key/val pairs and redirects below to index.html
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)