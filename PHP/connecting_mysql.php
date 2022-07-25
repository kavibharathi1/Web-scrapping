<?php
$connect = mysqli_connect("localhost" , "root" , "" , "student"); 
$sql = "SELECT * from grade_1"; 

$result =mysqli_query($connect,$sql);
$resultcheck = mysqli_num_rows($result);
if($resultcheck>0);{
	while($row=mysqli_fetch_assoc($result))
	{
		echo $row['student_name'];
		echo "<br>";
		echo $row['student_regno'];
		echo "<br>";
		echo $row['student_age'];
		echo "<br>";
		echo $row['percentage'];




	}
}

 








?>
