#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print """
<html>
  <head>
  <link href="css/font-awesome.min.css" rel="stylesheet"/>
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
	    <p style="font-size:30px;text-align:left;font-family:constantia;width:40%;">Express Delivery</p>
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
	  <h1 style="text-align:center">Grievance Redressal</h1>
	  <hr>
	  <div>
	  
	  <div style="height:500px;width:60%;float:left;text-align:center;">
	  <p style="font-size:20px;font-family:Comic Sans MS;margin-top:100px;">
	                                        Rathod Premises once no. 3<br/>
                                            Telly Galliide,s Fly Over Signal,</br>
                                            Opp. Sai Baba Temple,<br/>
											Andheri East, Mumbai 400069.<br/>
											Tel: 022 26834555 / 26834888<br/>
											Mobile: 9892406506 / 9889498236<br/>
											Email Id:<a href="http://www.gmail.com"> propertygrievance@gmail.com </a><br/>(mailto:<a href="http://www.gmail.com">portal.grievance@gmail.com</a>)<br/>
											<br/>

											</p>
											</div>
	  <div style="height:400px;width:400px;float:left;border:1px solid;margin-top:50px;">
	  <form action="contactuscode.py" method="post">
	  <table style="margin 0px auto;width:80%;height:300px;margin-top:50px;margin-left:40px;">
	  <tr>
	  <td>Enter Name</td>
	  <td><input type="text" name="name" required /></td>
	  </tr>
	  <tr>
	  <td>Enter Mobile No</td>
	  <td><input type="number" name="mobileno" required /></td>
	  </tr>
	  <tr>
	  <td>Enter Email Id</td>
	  <td><input type="email" name="email" required /></td>
	  </tr>
	  <tr>
	  <td>Enter Address</td>
	  <td><textarea name="address" required /></textarea></td>
	  </tr>
	  <tr>
	  <td>Enter Detailed Grievance</td>
	  <td><textarea name="purpose" required></textarea></td>
	  </tr>
	  <tr>
	   <td colspan="2" align="center">
	   <input type="submit" value="Submit"/></td>
	  </tr>
	  </table>
	  </form>
	  </div>
	  </div>
	  </div>
	  <div id="map" style=" height:290px;width:99%;margin-left:5px;border-radius:20px 20px 20px 20px;">
<iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d14234.67795370525!2d80.94821!3d26.88224!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x730fe46201abc68a!2sSoftpro+India!5e0!3m2!1sen!2sin!4v1411887056855" width="100%" height="100%"></iframe>

</div>
	  <!--- main div end--->
	  <!--- footer div start--->
	  <div id="footer">
	    <div id="lfooter"><h3>Copyright &copy Speedex Courier</h3></div>
		<div id="rfooter"><h3>Designed and Developed by Ankit Mishra</h3></div>
	  </div>
	  <!--- footer div end--->
	
   </div>
  </body>
</html>




"""