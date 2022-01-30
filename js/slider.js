var arr=["slider1.jpg","slider2.jpg","slider3.jpg","slider4.jpeg","2.jpg"];
   var i=0;
   function slider()
   {
   var img=document.getElementById("slide");
   img.src="images/"+arr[i];
   i++;
   if(i==4)
   {
     i=0;
   }
   
   window.setTimeout("slider()",2000);
   
   }