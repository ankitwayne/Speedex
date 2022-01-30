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
<li><a href="logout.py">LOG-OUT</a></li>


</ul>
</div>

<!--- menu div ends --->

<!--- main div starts --->
<div id="main">

<h1 style="text-align:center;color:black;"> CONTACT MANAGEMENT </h1>

<table style="margin:0px auto; width:90%; height:200px;" border="1">
<tr>
<th>Id</th>
<th>Name</th>
<th>Mobile No</th>
<th>E-mail Id</th>
<th>Address</th>
<th>Purpose</th>
<th>Post Date</th>
<th>Delete</th>
</tr>
"""
import MySQLdb
con=MySQLdb.connect('127.0.0.1','root','','speedex',3306)
cur=con.cursor()
q="select * from contactus"
cur.execute(q)
res=cur.fetchall()
for r in res:
 print "<tr>"
 print "<td>",r[0],"</td>"
 print "<td>",r[1],"</td>"
 print "<td>",r[2],"</td>"
 print "<td>",r[3],"</td>"
 print "<td>",r[4],"</td>"
 print "<td>",r[5],"</td>"
 print "<td>",r[6],"</td>"
 print "<td><a href='dcon.py?id="+str(r[0])+"'>Delete</a></td>"
 print "</tr>"
print """
</table>

</div>
<!--- main div end --->
<!--- footer div starts --->
<div id="footer">
<div id="lfooter">
<h2 align="center">&copy 2020 Bolt Pvt. Ltd.</h2> 
</div>
<div id="rfooter">
<h2 align="center">Design & Developed by : Yash </h2>
</div>
</div>
<!--- footer div end --->






</div>
</body>
</html>
"""