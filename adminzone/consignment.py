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
	  <h1 style="text-align:center;color:darkred;text-align center;">Consignment Management</h1>
	  <h3>
	  <a href="showconsignment.py" style="text-decoration:none;color:green;">View Consignment</a>
	  </h3>
	  <hr>
	  <form action="concode.py" method="post">
	  <table style="margin:0px auto;height:550px;width:70%;margin-top:100px;"border="1">
	  <tr>
	  <td>Reference No.</td>
	  <td>
	  <input type="number" name="refno" required />
	  </td>
	  </tr>
	  <tr>
	  <td>Sender Name:</td>
	  <td>
	  <input type="text" name="sname" required />
	  </td>
	  </tr>
	  <tr>
	  <td>Sender Address:
	  </td>
	  <td><textarea name="saddress" required></textarea>
	  </td>
	  </tr>
	  <tr>
	  <td>Sender Contact No.</td>
	  <td>
	  <input type="number" name="scontact" required />
	  </td>
	  </tr>
	  <tr>
	  <td>Receiver Name:</td>
	  <td>
	  <input type="text" name="rname" required />
	  </td>
	  </tr>
	  <tr>
	  <td>Receiver Address:</td>
	  <td>
	  <textarea name="raddress" required></textarea>
	  </td>
	  </tr>
	  <tr>
	  <td>Receiver Contact No.</td>
	  <td>
	  <input type="number" name="rcontact" required />
	  </td>
	  </tr>
"""
import MySQLdb
con=MySQLdb.connect('127.0.0.1','root','','speedex',3306)
cur=con.cursor()
q="select * from city"
cur.execute(q)
res1=cur.fetchall()
cur.execute(q)
res2=cur.fetchall()
cur.execute(q)
res3=cur.fetchall()
print "<tr>"
print "<td>Select Source Location:</td>"
print "<td><select name='source'>"
print "<option>Select Source</option>"
for r in res1:
 print "<option>"+str(r[1])+"</option>"
print "</select>"
print "</td>"
print "</tr>"

print "<tr>"
print "<td>Select Current Location:</td>"
print "<td><select name='curcity'>"
print "<option>Select Current</option>"
for r in res2:
 print "<option>"+str(r[1])+"</option>"
print "</select>"
print "</td>"
print "</tr>"

print "<tr>"
print "<td>Select Destination Location:</td>"
print "<td><select name='destination'>"
print "<option>Select Destination</option>"
for r in res3:
 print "<option>"+str(r[1])+"</option>"
print "</select>"
print "</td>"
print "</tr>"

print """
<tr>
<td>Status</td>
<td>
<select name="status" required>
<option value="">Select Status</option>
<option>Initiated</option>
<option>Pipeline</option>
<option>Delivered</option>
<option>Cancelled</option>
</select>
</td>
</tr>
<tr>
<td colspan="2" align="center">
<input type="submit" value="SUBMIT"/>
</td>
</tr>

</table>
	  </form>
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