#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print """
<html>
<head>
<link href="css/style.css" rel="stylesheet"/>
  <script src="js/slider.js"></script>

</head>
<body onload="slider()" bgcolor="white">
<div id="outer">
<!--- header div start --->
<div id="header">
<div id="logo">
<img src="images/logo.png" height="150px" width="60%" style="border-radius:100px;" />
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
<li><a href="index.py">HOME</a></li>
<li><a href="aboutus.py">ABOUT US</a></li>
<li><a href="contactus.py">CONTACT US</a></li>
<li><a href="complain.py">COMPLAIN</a></li>
<li><a href="tracking.py">TRACKING</a></li>
<li><a href="register.py">REGISTER</a></li>
<li><a href="login.py">LOGIN</a></li>


</ul>
</div>

<!--- menu div ends --->
<!--- slider div starts --->
<div id="slider">
 <img height="350px" width="100%" id="slide"/>
 </div>
<!--- slider div ends --->
<!--- main div starts --->
<div id="main">

<h1 style="text-align:center;color:black;font-weight:bold;"> REGISTER HERE </h1>
<hr/>
<img src="images/register.jpg" height="30%" width="30%" style="float:left;margin:80px auto;margin-left:70px;"/>
<form action="regcode.py" method="post">
<table style="margin:20px auto;width:60%; height:450px;float:right;" border="1">
<tr>
<td>&nbsp&nbspEnter User Name : </td>
<td>&nbsp&nbsp <input type="text" name="name" required /></td>
</tr>
<tr>
<td>&nbsp&nbspSelect Gender :</td>
<td>
<input type="radio" name="gender" value="male" />Male
<input type="radio" name="gender" value="female" />Female
</td>
</tr>
<tr>
<td>&nbsp&nbspEnter Mobile No : </td>
<td>&nbsp&nbsp
<input type="number" name="mobileno" required />
</td>
</tr>
<tr>
<td>&nbsp&nbspEnter Email Id :</td>
<td>&nbsp&nbsp
<input type="email" name="email" required />
</td>
</tr>
<tr>
<td>&nbsp&nbspEnter Address :</td>
<td>&nbsp&nbsp
<textarea name="address" required></textarea>
</td>
</tr>
<tr>
<td>&nbsp&nbspPin Code</td>
<td>&nbsp&nbsp
<input type="number" name="pinno" required />
</td>
"""
import random
a=[0,1,2,3,4,5,6,7,8,9]
n1=random.choice(a)
n2=random.choice(a)
sum=n1+n2
print "<td colspan='2' align='center'> <input type='hidden' value='"+str(sum)+"' name='sum'/>"
print "<input value='"+str(n1)+"' style='width:20px;' readonly      />"
print "<input value='"+str(n2)+"' style='width:20px;' readonly      />"
print " = <input type='number' name='t' style='width:50px' required />"
print "</td>"


print """
</tr>
<tr>
<td colspan="2" align="center"/>&nbsp
<input type="submit" value="SUBMIT"/>
</td>
</tr>
</table>
</form>
</div>
<!--- main div end --->
<!--- footer div starts --->
<div id="footer">
<div id="lfooter">
<h2 align="center">&copy 2020 Bolt Pvt. Ltd.</h2> 
</div>
<div id="rfooter">
<h2 align="center">Design & Developed by : Ankit Mishra </h2>
</div>
</div>
<!--- footer div end --->






</div>
</body>
</html>
"""