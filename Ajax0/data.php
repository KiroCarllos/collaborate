<?php
	include 'connect.php';
	
	if($_SERVER['REQUEST_METHOD']  == 'POST'){

		$Name = $_POST['Name'];
		$Email = $_POST['Email'];




	$stmt=$con->prepare("INSERT INTO user(Name,Email) VALUES (:Name,:Email)");

	$result = $stmt->execute(array(
									'Name' => $Name,
									'Email' => $Email));
	echo "Success Inserted";

		
}

?>
