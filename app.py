from flask import Flask, render_template, jsonify,url_for
from database import *

app = Flask(__name__)


"""

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi, India',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote',
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'San Francisco',
        'salary': '$120,000'
    },
]

"""


  

@app.route("/")
def hello_world():
  jobs=get_jobs_from_mydb()
  return render_template('home.html', jobs=jobs)


@app.route('/api/jobs')
def list_jobs():
  jobs=get_jobs_from_mydb()

  return jsonify(jobs)


@app.route("/job/<id>")
def show_job(id):
  job=get_job_details_jobid(id)

  if job==None:
    return "Job Not Found",404
  return render_template('jobpage.html', job=job)
  
  
  


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
