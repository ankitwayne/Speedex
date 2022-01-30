#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print """
<html>
  <head>
  
  <link href="css/style.css" rel="stylesheet"/>
  <script src="js/slider.js"></script>
  </head>
  <body onload="slider()">
   <div id="outer">
   <!--- header div start--->
    <div id="header">
	   <div id="logo">
	   <img src="images/logo.png" height="150px" width="60%" style="border-radius:100px;" />
	   </div>
	   <div id="pt">
	    <p style="font-size:30px;font-family:constantia;width:40%;">Express Delivery</p>
         <h3 style="text-align:left;font-family:constantia;width:40%;">+098-234545/+098-245677</h3>
	   </div>
	</div>
	 <!--- header div end--->
	  <!--- menu div start--->
	  <div id="menu">
	  <ul>
 <li><a href="index.py">HOME</a></li>
 <li><a href="aboutus.py">ABOUTUS</a></li>
 <li><a href="contactus.py">CONTACTUS</a></li>
 <li><a href="complain.py">COMPLAIN</a></li>
 <li><a href="tracking.py">TRACKING</a></li>
 <li><a href="register.py">REGISTER</a></li>
 <li><a href="login.py">LOGIN</a></li>
 </ul>
	  </div>
	  <!--- menu div end--->
	  <!--- slider div start--->
	    <div id="slider">
		  <img height="350px" width="100%" id="slide" />
		</div>
	  <!--- slider div end--->
	  <!--- main div start--->
	  <div id="main">
	  <h1 style="text-align:center">Complain Form</h1>
	  <hr/>
	  <form action="complaincode.py" method="post" style="text-align:center;">
	  <img src="images/download.jfif" />
	   <table style="margin:0px auto;width:40%;height:350px;text-align:center;>
	   <tr>
	   <td>Enter Name</td>
	   <td><input type="text" name="name" required /></td>
	   </tr>
	   <tr>
	   <td>Enter Mobile No.</td>
	   <td><input type="number" name="mobileno" required /></td>
	   </tr>
	   <tr>
	   <td>Enter Email Id</td>
	   <td><input type="email" name="email" required /></td>
	   </tr>
	   <tr>
	   <td>Reference No.:</td>
	   <td><input type="number" name="refno" required /></td>
	   </tr>
	   <tr>
	   <td>Enter Your Complain :</td>
	   <td><textarea name="ctext" required /></textarea></td>
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
	    <div id="lfooter"><h3>&copy 2015 Speedex Logestics All Rights Reserved</h3></div>
		<div id="rfooter"><h3>Designed and Developed by Ankit Mishra</h3></div>
	  </div>
	  <!--- footer div end--->
	
   </div>
  </body>
</html>




"""