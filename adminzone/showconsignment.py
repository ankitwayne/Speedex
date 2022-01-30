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
	  <div id="menu" id="menu" style="text-align:center;">
	  <ul>
 <li><a href="adminhome.py">HOME</a></li>
 <li><a href="complains.py">COMPLAINS</a></li>
 <li><a href="contactmgmt.py">CONTACT MGMT</a></li>
 <li><a href="consignment.py">CONSIGNMENT</a></li>
 <li><a href="addcity.py">ADD CITY</a></li>
 <li><a href="changepwd.py">CHANGE PWD</a></li>
 <li><a href="logout.py">LOGOUT</a></li>
 </ul>
	  </div>
	  <!--- menu div end--->
	  
	  
	  <!--- main div start--->
	  <div id="main">
	  <h1 style="text-align:center;color:darkred;">View Consignment</h1>
	  <h3 style="text-align:left;display:inline;">
	  <a href="consignment.py" style="text-decoration:none;color:light;">Consignment Management</a>
	  </h3>
	  <hr>
	  <table style="margin:0px auto;height:100px;width:70%;margin-top:100px;"border="1">
	  <tr>
	  <th>Ref No.</th>
	  <th>Sender Name</th>
	  <th>Sender Address</th>
	  <th>Sender Contact</th>
	  <th>Receiver Name</th>
	  <th>Receiver Address</th>
	  <th>Receiver Contact</th>
	  <th>Source</th>
	  <th>Current City</th>
	  <th>Destination</th>
	  <th>Status</th>
	  <th>Post Date</th>
	  <th>Update</th>
	  <th>Delete</th>
	  </tr>
"""
import MySQLdb
con=MySQLdb.connect('127.0.0.1','root','','speedex',3306)
cur=con.cursor()
q="select * from consignment"
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
 print "<td>",r[7],"</td>"
 print "<td>",r[8],"</td>"
 print "<td>",r[9],"</td>"
 print "<td>",r[10],"</td>"
 print "<td>",r[11],"</td>"
 print "<td><a href='updatestatus.py?id="+str(r[0])+"'>Update</a></td>"
 print "<td><a href='deletecon.py?id="+str(r[0])+"'>Delete</a></td>"
 print "</tr>"
print """
     </table>
	  </div>
	  <!--- main div end--->
	  <!--- footer div start--->
	  <div id="footer">
	    <div id="lfooter"><h3>&copy 2020 Bolt Pvt. Ltd.</h3></div>
		<div id="rfooter"><h3>Designed and Developed by Ankit Mishra</h3></div>
	  </div>
	  <!--- footer div end--->
	
   </div>
  </body>
</html>




"""