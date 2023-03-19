import sys
import csv
from jinja2 import Template 
from matplotlib import pyplot as plt

Template1='''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8"/>
    <title>result</title>
    <meta name="description" content="result page">

    <style>
table, th, td {
    border: 1px solid black;
    }
</style>

</head>

<body>
    <div id="main">
        <h1>Student Details</h1>
    </div>

    <div id="table">
        <table>
            <thead>
            <tr>
              <th>Student ID</th>
              <th>Course ID</th>
              <th>Marks</th>
            </tr>
        </thead>
        <tbody>
            {% for i in data %}
            <tr>
                <td>{{i[0]}}</td>
                <td>{{i[1]}}</td>
                <td>{{i[2]}}</td>
            </tr>
            {% endfor %}
            </tr>
            <tr>
            <td colspan="2">Total Marks</td>
            <td>{{total}}</td>
            </tr>
        </tbody>
        </table>
    </div>
    </body>
</html>
'''

Template2='''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8"/>
    <title>result</title>
    <meta name="description" content="result page">

    <style>
table, th, td {
    border: 1px solid black;
    }
</style>

</head>

<body>
    <div id="main">
        <h1>Course Details</h1>
    </div>

    <div id="table">
        <table>
            <thead>
            <tr>
              <th>Average Marks</th>
              <th>Maximum Marks</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>{{avg}}</td>
                <td>{{max}}</td>
            </tr>
        </tbody>
        </table>
    </div>
    <div id="graph">
        <img src="output.jpeg" alt="img1">
    </div>
    </body>
</html>
'''
Template3='''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8"/>
    <title>result</title>
    <meta name="description" content="result page">

</head>

<body>
    <div id="main">
        <h1>Wrong Inputs</h1>
    </div>
    <div id="body">
        <p>Something went wrong</p>
    </div>
    </body>
</html>
'''
def getCid(l):
    L=[]
    for i in range(1,len(l)): L+=[l[i][1].strip()]
    return L

def getSid(l):
    L=[]
    for i in range(1,len(l)): L+=[l[i][0].strip()]
    return L

def getStudTable(l,sid):
    L=[]
    t=0
    for i in range(1,len(l)):
        if l[i][0].strip()==sid: 
            L+=[l[i]]
            t+=int(l[i][2].strip())
    return L,t

def GetData(l,c):
    max,s,n=int(l[1][2].strip()),0,0
    d=[]
    for i in range(1,len(l)):
        if l[i][1].strip() == c.strip():
            if int(l[i][2].strip())>max: 
                max=int(l[i][2].strip())
            s+=int(l[i][2].strip())
            n+=1
            d+=[int(l[i][2].strip())]
    return max,s/n,d

def main():
    file=open('data.csv','r')
    r=list(csv.reader(file))
    file.close()
    sc=sys.argv[1]
    arg2=str(sys.argv[2]).strip()
    sids=getSid(r)
    cids=getCid(r)
    #print(type(arg2),len(arg2),arg2,sids,cids,sep='\n')
    if sc=='-s' and arg2 in sids:
        data,total=getStudTable(r,arg2)
        temp=Template(Template1)
        content=temp.render(data=data,total=total)
        h1=open('result.html','w')
        h1.write(content)
        h1.close()
        
    elif sc=='-c' and arg2 in cids:
        max,avg,d=GetData(r,arg2)
        plt.hist(d)
        plt.xlabel("Marks")
        plt.ylabel("Frequency")
        plt.savefig("output.jpeg")
        temp=Template(Template2)
        content=temp.render(max=max,avg=avg)
        h1=open('result.html','w')
        h1.write(content)
        h1.close()

    else:
        temp=Template(Template3)
        content=temp.render()
        h1=open('result.html','w')
        h1.write(content)
        h1.close()
    
    

if __name__=="__main__":
    main() 



