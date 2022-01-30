#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print """
<html>
  <head>
  <link href="admincss/adminstyle.css" rel="stylesheet"/>
 <script>
function logout()
{
   window.history.forward();
   window.setTimeout("window.location.href='../login.py'",2000)
 }
  </script>
  </head>
  <body onload="logout()">
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
	  <h1 style="text-align:center;color:darkred;">Log Out</h1>
	  <hr/>
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