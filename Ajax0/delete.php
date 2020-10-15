<?php
	include 'connect.php';
		
			$userid = $_GET['userid'];
			$stmt=$con->prepare("DELETE FROM user WHERE id =:id");
			$result = $stmt->execute(array('id' => $userid));

		