<?php
	include 'connect.php';

	$fname= $_POST['fname'];
	$lname= $_POST['lname'];
	$phone= $_POST['phone'];
	$job= $_POST['job'];





	$stmt=$con->prepare("INSERT INTO members(fname,lame,phone,job) VALUES (:zfname,:zlname,:zphone,:zjob)");

	$result = $stmt->execute(array(
									'zfname' => $fname,
									'zlname' => $lname,
									'zphone' => $phone,
									'zjob' => $job));

?>
