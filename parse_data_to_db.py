import re, datetime
from models import *
from app import db

def parse_data(school_name, date):
    kids = []
    for kid in Student.query.order_by(Student.sensor_id):
        kids.append(kid.name)
    for i in range(0,16):
        file_kid = i
        file_to_read = school_name + "/" + date + "/" + str(file_kid) + ".txt"
        f = open(file_to_read,'r')
        data = {}

        expr_zero = re.compile('\d{8}\n')
        expr_single = re.compile('\d{9}\n')
        expr_double = re.compile('\d{10}\n')

        lines = f.readlines()
        for line in lines:
          row = None
          if expr_zero.match(line):
              secondary_kid = kids[0]
              rsval = line[:2]
              hour = line[2:4]
              minute = line[4:6]
              sec = line[6:8]
              timestamp = hour + "-" + minute + "-" + sec
              complete_date = date + "-" + timestamp
              date_field = datetime.datetime.strptime(complete_date, '%m-%d-%y-%H-%M-%S')
              row = SocialProximity(school_name, date_field, kids[i], secondary_kid, rsval)
          elif expr_single.match(line):
              kid = line[0]
              secondary_kid = kids[int(kid)]
              rsval = line[1:3]
              hour = line[3:5]
              minute = line[5:7]
              sec = line[7:9]
              timestamp = hour + "-" + minute + "-" + sec
              complete_date = date + "-" + timestamp
              date_field = datetime.datetime.strptime(complete_date, '%m-%d-%y-%H-%M-%S')
              row = SocialProximity(school_name, date_field, kids[i], secondary_kid, rsval)
          elif expr_double.match(line):
              kid = line[:2]
              secondary_kid = kids[int(kid)]
              rsval = line[2:4]
              hour = line[4:6]
              minute = line[6:8]
              sec = line[8:10]
              timestamp = hour + "-" + minute + "-" + sec
              complete_date = date + "-" + timestamp
              date_field = datetime.datetime.strptime(complete_date, '%m-%d-%y-%H-%M-%S')
              row = SocialProximity(school_name, date_field, kids[i], secondary_kid, rsval)
          if row is not None:
            db.session.add(row)
        db.session.commit()
        f.close()

if __name__ == "__main__":
  parse_data("Wildflower", "3-28-16")
