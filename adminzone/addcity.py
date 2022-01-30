#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print """
<html>
  <head>
  <link href="admincss/adminstyle.css" rel="stylesheet"/>
  </head>
  <body onload="slider()">
   <div id="outer">
   <!--- header div start--->
    <div id="header">
	   <div id="logo">
	   <img src="images/inamel.png" height="150px" width="60%" style="border-radius:100px;" />
	   </div>
	   <div id="pt">
	     <p style="font-size:30px;font-family:constantia;width:40%;">Express Delivery</p>
         <h3 style="text-align:left;font-family:constantia;width:40%;">+098-234545/+098-245677</h3>
	   </div>
	</div>
	 <!--- header div end--->
	  <!--- menu div start--->
	  <div id="menu" style="text-align:center;">
	  <ul>
 <li><a href="adminhome.py">HOME</a></li>
 <li><a href="complains.py">COMPLAINS</a></li>
 <li><a href="contactmgmt.py">CONTACT MANAGEMENT</a></li>
 <li><a href="consignment.py">CONSIGNMENT</a></li>
 <li><a href="addcity.py">ADD CITY</a></li>
 <li><a href="changepwd.py">CHANGE PWD</a></li>
 <li><a href="logout.py">LOGOUT</a></li>
 </ul>
	  </div>
	  <!--- menu div end--->
	   <!--- main div start--->
	   <div id="main">
	  <h1 style="text-align:center;color:darkred;">Add City</h1>
	  <hr>
	  <form action="addcitycode.py" method="post">
	  <table style="margin:0px auto;width:70%;height:100px;"border="1">
	  <tr>
	  <td>Enter City Name :</td>
	  <td><input type="text" name="cityname" required /></td>
	  <td>
	  <input type="submit" value="ADD CITY" />
	  </td>
	  </tr>
	  </table>
	  </form>
	  <br/>
	  <br/>
	  <table style="margin:0px auto;width:70%;" border="1">
	  <tr>
	  <th>S.no</th>
	  <th>City Name</th>
	  <th>Delete</th>
	  </tr>
"""
import MySQLdb
con=MySQLdb.connect('127.0.0.1','root','','speedex',3306)
cur=con.cursor()
q="select*from city"
cur.execute(q)
res=cur.fetchall()
n=1
for r in res:
 print "<tr>"
 print "<td>",n,"</td>"
 print "<td>",r[1],"</td>"
 print "<td><a href='deletecity.py?id="+str(r[0])+"'>Delete</a></td>"
 print "</tr>"
 n=n+1

print """</table>
	  </div>
	  <!--- main div end--->
	  <!--- footer div start--->
	  <div id="footer">
	    <div id="lfooter"><h3>&copy 2015 Speedex Logistics All Rights Reserved</h3></div>
		<div id="rfooter"><h3>Designed and Developed by Ankit Mishra</h3></div>
	  </div>
	  <!--- footer div end--->
	
   </div>
  </body>
</html>




"""