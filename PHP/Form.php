<?php

if(isset($_POST['submit'])){
	
$username=$_POST['username'];
$password=$_POST['password'];
echo "hello " . $username;

echo " your password is " . $password;
	
}
?>





<!DOCTYPE html>
<html>
<body>

<form action="new.php" method="post">

<input type= "text" name="username" placeholder="Enter username">
<br>
<input type= "password" name="password" placeholder="Enter password">
<br>

<input type= "submit" name="submit" >

</form>
 
</body>
</html>	



