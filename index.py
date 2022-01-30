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

 <li><a href="contactus.py">CONTACT US</a></li>
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
	  <div id="main" style="background-image:url("images/4.jpeg");">
	  <h1 style="text-align:center">Home</h1>
      <hr/>
	  <p style="text-align:center;font-family:Ariel;font-size:28px;">Specialities</p><br/>
	  
       <p style="text-align:center;font-size:20px;font-family:Comic Sans MS"> I. International Express: SPEEDEX is accepted by customers for its international<br/> standard quality services for documents and parcels. With its immense understanding and reputation,<br/><br/>
       II. Domestic Express:Premium Express service by Air:<br/>Your time sensitive Documents / Non-documents are delivered next day in all Major airport Cities on priority basis.Deferred Service by Surface and place.<br/><br/>

        III.  Air Freight Service:We offer reliable and efficient air freight forwarding service throughout the world.<br/>With an excellent network of operations, we promise a timely and cost effective transportation of goods to the desired destinations. SPEEDEX clears smoothly through customs, and forwards to its final destinations.<br/>
		</p>
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