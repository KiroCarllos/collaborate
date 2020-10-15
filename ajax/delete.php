<?php
	include 'connect.php';
	$userid = $_GET['userid'];
	$stmt=$con->prepare("DELETE FROM members WHERE id =:id");
	$result = $stmt->execute(array('id' => $userid));
?>