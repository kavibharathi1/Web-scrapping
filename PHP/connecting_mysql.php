<?php
$connect = mysqli_connect("localhost" , "root" , "" , "student"); //here, we have connected database
$sql = "SELECT * from grade_1"; // here, we have selected table

$result =mysqli_query($connect,$sql);//next, we going to link database and table
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