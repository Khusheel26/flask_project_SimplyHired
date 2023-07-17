from flask import Flask,render_template,jsonify

app = Flask(__name__)
JOBS=[
     {
     'id': 1,
     'title':'Data Analyst',
     'company_name':'Lenskart',
     'location':'Bengaluru , India',
     'salary':'Rs 10,00,000'
     },
      {
     'id': 2,
     'title':'Data Scientist',
     'company_name':'Seimens',
     'location':'New Delhi , India',
     'salary':'Rs 12,00,000'
     },
       {
     'id': 3,
     'title':'Front-End Developer',
     'company_name':'Juspay',
     'location':'Mumbai, India',
     'salary':'Rs 16,00,000'
     },
        {
     'id': 4,
     'title':'Junior SDE',
     'company_name':'TCS',
     'location':'Pune , India',
     'salary':'Rs 7,50,000'
     },
]
@app.route("/")
def hello_world(): 
     return render_template('home.html',jobs=JOBS)
 
@app.route("/api/jobs")
def to_joblist():
     return jsonify(JOBS)
if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)