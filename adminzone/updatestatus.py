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
	  <h1 style="text-align:center;color:darkred;">Update Tracking Status</h1>
	  <hr>
	  <form action="statuscode.py" method="post">
	  <table>
	  <tr>
	  <td>Change Status :</td>
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
"""
import MySQLdb
con=MySQLdb.connect('127.0.0.1','root','','speedex',3306)
cur=con.cursor()
q="select * from city"
cur.execute(q)
res1=cur.fetchall()

print "<tr>"
print "<td>Change Current City:</td>"
print "<td><select name='curcity'>"
for r in res1:
 print "<option>"+str(r[1])+"</option>"
print "</select>"
print "</td>"
print "</tr>"
print "<tr>"
import cgi
id=cgi.FieldStorage().getvalue('id')
print "<td><input type='hidden' name='id' value='"+str(id)+"'/></td>"
print "</tr>"
print """
<tr>
<td colspan="2" align="center">
<input type="submit" value="Update" />
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