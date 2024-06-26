"""

from sqlalchemy import create_engine

username,password,host,database name

connection_string = "mysql+pymysql://root:VhzHTGPlGhzUHrUNAPWtSKzQKTEMEpFu@roundhouse.proxy.rlwy.net/railway?charset=utf8mb4"

engine = create_engine(connection_string, )

with engine.connect() as conn:
  result = conn.execute("select * from jobs")
  print(result.all())

connect_args={
  'ssl':{

  }
}

"""


import mysql.connector as conn
import os

from mysql.connector.types import ResultType
mydb = conn.connect(
    user='root',
    password=os.environ['db_password'],
    host=os.environ['db_host'],
    database=os.environ['db_database'],
    port=os.environ['db_port']
)
# print(mydb)

"""returns rows in a format with columns names as keys and values as values of dict
"""
mycursor=mydb.cursor(dictionary=True)  



def get_jobs_from_mydb():
  cursor=mydb.cursor(dictionary=True)
  cursor.execute("SELECT * FROM jobs")
  result = cursor.fetchall()

  return result



def get_job_details_jobid(id):
  cursor=mydb.cursor(dictionary=True)
  sql=f"select * from jobs where id={id}"
  cursor.execute(sql)
  result = cursor.fetchall()
  if len(result)==0:
    return None
  return result[0]



(2,'hema','hema@gmail.com','link@url','btech','fresher','link@url');

def insert_into_application(job_id,data):
  cursor=mydb.cursor(dictionary=True)





  sql="INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (%s, %s, %s, %s, %s, %s, %s)"

  # Assuming you're using MySQL's Python connector
  cursor.execute(sql, (
      job_id,
      data['fullname'],
      data['email'],
      data['linkedin_url'],
      data['education'],
      data['work_experience'],
      data['resume_url']
  ))

  mydb.commit()






"""
mycursor.execute("SELECT * FROM jobs")

myresult = mycursor.fetchall()

for x in myresult:
  print(type(x),x.keys())
  print()
  print(x.values())
  print('\n')

  print(x)
"""
