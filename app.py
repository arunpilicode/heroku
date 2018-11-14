from flask import Flask, render_template, request
from data import employee
app=Flask(__name__)    
getEmployee= employee()

@app.route('/send', methods=['GET','POST'])
def send():
    if(request.method=='POST'):
        getName=request.form['name']
        getMail=request.form['mail']
        getNumber=request.form['number']
        getSubject=request.form['subject']
        getMessage=request.form['message']
        return render_template('result.html',newName=getName, newMail=getMail, newNumber=getNumber, newSubject=getSubject, newMessage=getMessage)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/employee')
def employee():
        return render_template('empdata.html',myEmployeeList=getEmployee)
if(__name__=='__main__'):
    app.run(debug=True)
