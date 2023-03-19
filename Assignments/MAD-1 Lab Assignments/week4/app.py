from flask import Flask
from flask import render_template
from flask import request
import csv
from matplotlib import pyplot as plt
import matplotlib as mpl

app=Flask(__name__)

def get_rec(stud_id):
    d,t=[],0
    file=open('data.csv')
    r=list(csv.reader(file))
    file.close()
    for i in r[1:]:
        if str(i[0])==str(stud_id):
            d+=[i]
            t+=float(i[2])
    return d,t

def get_cor_rec(cour_id):
    file=open('data.csv')
    r=list(csv.reader(file))
    file.close()
    max,t=float(r[1][2]),0
    l=[]
    for i in r[1:]:
        if str(i[1])==str(cour_id):
            if float(i[2])>max: 
                max=float(i[2])
            t+=float(i[2])
            l+=[float(i[2])]
    mkHist(l)
    return t/(len(l)),max

def mkHist(l):
    mpl.use('agg')
    mpl.pyplot.hist(l)
    mpl.pyplot.xlabel("Marks")
    mpl.pyplot.ylabel("Frequency")
    mpl.pyplot.show()
    mpl.pyplot.savefig("output.jpeg")

@app.route("/", methods=["GET","POST"])  
def hello_world():
    if request.method=="GET":
        return render_template("form.html")
    elif request.method=="POST":
        id_type = request.form["ID"]
        id_value = request.form["id_value"]
        if id_type == "student_id":
            d,t=get_rec(id_value)
            return render_template("get_stud_detail.html",data=d,total_marks_data=t)
        elif id_type == "course_id":
            am,mm=get_cor_rec(id_value)
            return render_template("get_course_detail.html",avg_marks=am,max_marks=mm)
        else:
            return render_template("wrongin.html")
    else:
        print("Error check")

if __name__=='__main__':
    app.debug=True
    app.run()
