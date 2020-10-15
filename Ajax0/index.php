<?php
	include 'connect.php';

?>
<!DOCTYPE html>
<html>
<head>
	<title>AJAX</title>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
	<style>
		input{
			margin-bottom: 20px;
		}
	</style>
</head>
<body>
	<div class="row">
		<div class="container">
			<h1>Insert Data</h1>	
			<form  onsubmit="return insertMemberInfo(); ">
				<input class="form-control" required="required" placeholder="Enter Your Name" type="text" id="Name" name="Name">
				<input class="form-control" required="required" placeholder="Enter Your Email" type="text" id="Email" name="Email">
				<button id="button" class="btn btn-primary btn-block" type="submit">Insert</button>
			</form>
			<h1>Select Data</h1>

		<div>
			

			<div id="Data"></div>

			<div id="S"></div>
		

		</div>
		</div>
	 </div>
	<script src="js/jquery-1.12.0.min.js"></script>	
	<script src="js/bootstrap.min.js"></script>
	<script src="js/main.js"></script>
	<script>
	getUsers();
</script>
</body>
</html>