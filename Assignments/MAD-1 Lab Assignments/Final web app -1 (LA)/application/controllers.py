
from flask import render_template
from flask import request
from flask import current_app as app
from flask import redirect, url_for
from application.models import Student, Course, Enrollments
from application.database import db
from flask import Blueprint

main = Blueprint('main', __name__)

@app.route('/',methods=["GET","POST"])
def index():
    students=Student.query.all()
    return render_template("index.html",students=students)

@app.route('/student/create',methods=["GET","POST"])
def add_student():
    if request.method=="GET":
        return render_template("add_student_form.html")
    elif request.method=="POST":
        rollnum = request.form["roll"]
        fname = request.form["f_name"]
        lname = request.form["l_name"]
    
        rnums=[row.roll_number for row in Student.query.with_entities(Student.roll_number).all()]
        if rollnum not in rnums:
            new_student = Student(roll_number=rollnum,first_name=fname,last_name=lname)
            db.session.add(new_student)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            return render_template("error_student.html")


@app.route("/student/<sid>/update",methods=["GET","POST"])    
def update_stud(sid):
    if request.method=="GET":
        s=Student.query.filter(Student.student_id == sid).one()
        current_roll=s.roll_number
        current_f_name=s.first_name
        current_l_name=s.last_name
        courses=Course.query.all()
        return render_template("student_update_form.html",student_id=sid,current_roll=current_roll,current_f_name=current_f_name,current_l_name=current_l_name,courses=courses)
    
    elif request.method=="POST":
            s=Student.query.filter(Student.student_id == sid).one()
            rollnum=s.roll_number
            Student.query.filter(Student.student_id == sid).delete()
            Enrollments.query.filter(Enrollments.estudent_id == sid).delete()
            fname = request.form["f_name"]
            lname = request.form["l_name"]
            course_id = request.form.get("course")
                
            new_student = Student(student_id=sid,roll_number=rollnum,first_name=fname,last_name=lname)
            db.session.add(new_student)
            new_enrol=Enrollments(estudent_id=sid,ecourse_id=course_id)
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
        return render_template("studinfo.html",s_id=sid,roll_no=rollnum,first_name=fname,last_name=lname,courses=courses)

@app.route('/student/<sid>/withdraw/<cid>',methods=["GET","POST"])
def withdraw_stud(sid,cid):
    if request.method=="GET":
        Enrollments.query.filter(Enrollments.estudent_id == sid and Enrollments.ecourse_id==cid).delete()
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/courses',methods=["GET","POST"])
def courses():
    if request.method=="GET":
        courses=Course.query.all()
        return render_template("courses.html",courses=courses)
    
@app.route('/course/create',methods=["GET","POST"])
def add_course():
    if request.method=="GET":
        return render_template("add_course_form.html")
    elif request.method=="POST":
        c_code = request.form["code"]
        c_name = request.form["c_name"]
        c_desc = request.form["desc"]
    
        ccodes=[row.course_code for row in Course.query.with_entities(Course.course_code).all()]
        if c_code not in ccodes:
            new_course = Course(course_code=c_code,course_name=c_name,course_description=c_desc)
            db.session.add(new_course)
            db.session.commit()
            return redirect(url_for('courses'))
        else:
            return render_template("error_course.html")

@app.route('/course/<cid>/update',methods=["GET","POST"])
def update_course(cid):
    if request.method=="GET":
        c=Course.query.filter(Course.course_id == cid).one()
        c_code=c.course_code
        cname=c.course_name
        cdesc=c.course_description
        return render_template("course_update_form.html",course_id=cid,current_code=c_code,current_c_name=cname,current_desc=cdesc)
    elif request.method=="POST":
        c=Course.query.filter(Course.course_id == cid).one()
        c_code=c.course_code
        cname = request.form["c_name"]
        desc = request.form["desc"]
        Course.query.filter(Course.course_id == cid).delete()
        new_course = Course(course_id=cid,course_code=c_code,course_name=cname,course_description=desc)
        db.session.add(new_course)
        db.session.commit()
        return redirect(url_for('courses'))

@app.route('/course/<cid>/delete',methods=["GET","POST"])
def delete_course(cid):
    if request.method=="GET":
        Course.query.filter(Course.course_id == cid).delete()
        Enrollments.query.filter(Enrollments.ecourse_id == cid).delete()
        db.session.commit()
        return redirect(url_for('courses'))

@app.route('/course/<cid>',methods=["GET","POST"])
def course_info(cid):
    if request.method=="GET":
        c=Course.query.filter(Course.course_id == cid).one()
        ccode=c.course_code
        cname = c.course_name
        cdesc = c.course_description
        s=[i.estudent_id for i in Enrollments.query.filter(Enrollments.ecourse_id == cid).all()]
        students=[Student.query.filter(Student.student_id==i) for i in s]
        return render_template("courseinfo.html",c_code=ccode,c_name=cname,c_desc=cdesc,students=students )

