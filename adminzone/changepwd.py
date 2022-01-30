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

<h1 style="text-align:center;color:black;"> Admin Can Change The Password Here </h1>
</br>
</br>
</br>
<form action="passcode.py" method="post">
<table style="margin:20px auto; width:50%;height:300px; "border="1">
<tr>
<td>Enter Old Password :</td>
<td>
<input type="password" name="oldpass" required />
</td>
</tr>
<tr>
<td>Enter New Password :</td>
<td>
<input type="password" name="newpass" required />
</td>
</tr>
<tr>
<td>Enter Confirm Password :</td>
<td>
<input type="password" name="cpass" required />
</td>
</tr>
<tr>
<td colspan="2" align="center">
<input type ="submit" value="Update"/>
</td>
</tr>

</table>
</form>
</div>
<!--- main div end --->
<!--- footer div starts --->
<div id="footer">
<div id="lfooter">
<h2 align="center">Copyright &copy; SpeedEx Courier</h2> 
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