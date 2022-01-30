#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
f=cgi.FieldStorage()
name=f.getvalue('name')
gender=f.getvalue('gender')
mobileno=f.getvalue('mobileno')
email=f.getvalue('email')
address=f.getvalue('address')
pinno=f.getvalue('pinno')

con=MySQLdb.connect('127.0.0.1','root','','speedex',3306)
cur=con.cursor()

query="insert into register values('"+name+"','"+gender+"','"+mobileno+"','"+email+"','"+address+"','"+pinno+"',sysdate())"
n=cur.execute(query)
if n==1:
 print "<script>alert('Registration Successsfully Submitted');window.location.href='register.py';</script>"
else:
 print "<script>alert('Not Submitted');window.location.href='register.py';</script"
