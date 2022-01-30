#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
id=cgi.FieldStorage().getvalue('id')
con=MySQLdb.connect('127.0.0.1','root','','speedex',3306)
cur=con.cursor()
q="delete from city where id='"+id+"'"

n=cur.execute(q)
if n==1:
 print "<script>alert('Deleted');window.location.href='addcity.py';</script>"
else:
 print "<script>alert('NOT Deleted');window.location.href='addcity.py';</script>"