#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print """
<html>
<head>
<link href="admincss/adminstyle.css" rel="stylesheet"/>

</head>
<body onload="slider()" bgcolor="white">
<div id="outer">
<!--- header div start --->
<div id="header">
<div id="logo">
<img src="images/inamel.png" height="150px" width="60%" style="border-radius:100px;" />
</div>
<div id="pt">
<p style="font-size:30px;font-family:constantia;width:40%;">Express Delivery</p>
         <h3 style="text-align:left;font-family:constantia;width:40%;">+098-234545/+098-245677</h3>
	   
</div>
</div>
<!--- header div end --->
<!--- menu div starts --->
<div id="menu">
<ul>
<li><a href="adminhome.py">HOME</a></li>
<li><a href="complains.py">COMPLAINS</a></li>
<li><a href="contactmgmt.py">CONTACT MANAGEMENT</a></li>
<li><a href="consignment.py">CONSIGNMENT</a></li>
<li><a href="addcity.py">ADD CITY</a></li>
<li><a href="changepwd.py">CHANGE PASSWORD</a></li>
<li><a href="complains.py">COMPLAINS</a></li>
<li><a href="logout.py">LOG-OUT</a></li>


</ul>
</div>

<!--- menu div ends --->

<!--- main div starts --->
<div id="main">

<h1 style="text-align:center;color:black;"> User Management </h1>
</br>
</br>
</br>

<table style="margin:0px auto;width:90%;height:400px;"border="1">
<tr>
<th>S.No</th>
<th>Name</th>
<th>Gender</th>
<th>Contact No.</th>
<th>E-mail</th>
<th>Address</th>
<th>Pin-No</th>
<th>Reg.Date</th>
<th>Delete</th>
</tr>
"""
import MySQLdb
con=MySQLdb.connect('127.0.0.1','root','','speedex',3306)
cur=con.cursor()
q="select * from register"
cur.execute(q)
res=cur.fetchall()
n=1
for r in res:
 print "<tr>"
 print "<td>",n,"</td>"
 print "<td>",r[0],"</td>"
 print "<td>",r[1],"</td>"
 print "<td>",r[2],"</td>"
 print "<td>",r[3],"</td>"
 print "<td>",r[4],"</td>"
 print "<td>",r[5],"</td>"
 print "<td>",r[6],"</td>"
 print "<td><a href='du.py?id="+r[3]+"'>Delete</a></td>"
 print "</tr>"
 n=n+1
print """

</table>
</div>
<!--- main div end --->
<!--- footer div starts --->
<div id="footer">
<div id="lfooter">
<h2 align="center">Copyright &copy;Bolt Pvt. Ltd.</h2> 
</div>
<div id="rfooter">
<h2 align="center">Design & Developed by </h2>
</div>
</div>
<!--- footer div end --->






</div>
</body>
</html>
"""