import os
from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask import redirect, url_for

cur_dir=os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(cur_dir,"database.sqlite3")
db=SQLAlchemy()
db.init_app(app)
app.app_context().push()

class Course(db.Model):
    __tablename__='course'
    course_id=db.Column(db.Integer, autoincrement=True,primary_key=True)
    course_code=db.Column(db.String,unique=True,nullable=False)
    course_name=db.Column(db.String,nullable=False)
    course_description=db.Column(db.String)

class Student(db.Model):
    __tablename__='student'
    student_id=db.Column(db.Integer, autoincrement=True,primary_key=True)
    roll_number=db.Column(db.String,unique=True,nullable=False)
    first_name=db.Column(db.String,nullable=False)
    last_name=db.Column(db.String)
    courses=db.relationship("Course",secondary="enrollments") 

class Enrollments(db.Model):
    __tablename__='enrollments'
    enrollment_id=db.Column(db.Integer, primary_key=True)
    estudent_id=db.Column(db.Integer, db.ForeignKey("student.student_id"),nullable=False)
    ecourse_id=db.Column(db.Integer, db.ForeignKey("course.course_id"),nullable=False)
    
    

@app.route('/',methods=["GET","POST"])
def index():
    students=Student.query.all()
    return render_template("index.html",students=students)

@app.route('/student/create',methods=["GET","POST"])
def add():
    if request.method=="GET":
        return render_template("add_form.html")
    elif request.method=="POST":
        rollnum = request.form["roll"]
        fname = request.form["f_name"]
        lname = request.form["l_name"]
        courses = request.form.getlist("courses[]")

        rnums=[row.roll_number for row in Student.query.with_entities(Student.roll_number).all()]
        sid=len(rnums)+1
        if rollnum not in rnums:
            new_student = Student(student_id=sid,roll_number=rollnum,first_name=fname,last_name=lname)
            db.session.add(new_student)
            for course in courses:
                if course=="course_1" : 
                    new_enrol=Enrollments(estudent_id=sid,ecourse_id=1)
                    db.session.add(new_enrol)
                if course=="course_2" : 
                    new_enrol=Enrollments(estudent_id=sid,ecourse_id=2)
                    db.session.add(new_enrol)
                if course=="course_3" : 
                    new_enrol=Enrollments(estudent_id=sid,ecourse_id=3)
                    db.session.add(new_enrol)
                if course=="course_4" : 
                    new_enrol=Enrollments(estudent_id=sid,ecourse_id=4)
                    db.session.add(new_enrol)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            return render_template("error.html")


@app.route("/student/<sid>/update",methods=["GET","POST"])    
def update_stud(sid):
    if request.method=="GET":
        s=Student.query.filter(Student.student_id == sid).one()
        current_roll=s.roll_number
        current_f_name=s.first_name
        current_l_name=s.last_name
        courses=[i.ecourse_id for i in Enrollments.query.filter(Enrollments.estudent_id == sid).all()]
        return render_template("updateform.html",student_id=sid,current_roll=current_roll,current_f_name=current_f_name,current_l_name=current_l_name,courses=courses)
    
    elif request.method=="POST":
            s=Student.query.filter(Student.student_id == sid).one()
            rollnum=s.roll_number
            Student.query.filter(Student.student_id == sid).delete()
            Enrollments.query.filter(Enrollments.estudent_id == sid).delete()
            fname = request.form["f_name"]
            lname = request.form["l_name"]
            courses = request.form.getlist("courses[]")
                
            new_student = Student(student_id=sid,roll_number=rollnum,first_name=fname,last_name=lname)
            db.session.add(new_student)
            for course in courses:
                if course=="course_1" : 
                    new_enrol=Enrollments(estudent_id=sid,ecourse_id=1)
                    db.session.add(new_enrol)
                if course=="course_2" : 
                    new_enrol=Enrollments(estudent_id=sid,ecourse_id=2)
                    db.session.add(new_enrol)
                if course=="course_3" : 
                    new_enrol=Enrollments(estudent_id=sid,ecourse_id=3)
                    db.session.add(new_enrol)
                if course=="course_4" : 
                    new_enrol=Enrollments(estudent_id=sid,ecourse_id=4)
                    db.session.add(new_enrol)
            db.session.commit()
            return redirect(url_for('index'))
        

@app.route("/student/<sid>/delete")    
def detele_stud(sid):
    if request.method=="GET":
        Student.query.filter(Student.student_id == sid).delete()
        Enrollments.query.filter(Enrollments.estudent_id == sid).delete()
        db.session.commit()
        return redirect(url_for('index'))

@app.route("/student/<sid>",methods=["GET","POST"])    
def stud_info(sid):
    if request.method=="GET":
        s=Student.query.filter(Student.student_id == sid).one()
        rollnum=s.roll_number
        fname = s.first_name
        lname = s.last_name
        c=[i.ecourse_id for i in Enrollments.query.filter(Enrollments.estudent_id == sid).all()]
        courses=[Course.query.filter(Course.course_id==i).all() for i in c]
        return render_template("studinfo.html",roll_no=rollnum,first_name=fname,last_name=lname,courses=courses)
            

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True,port=8080)

