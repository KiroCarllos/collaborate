<!DOCTYPE html>
<html>
<head>
	<title>
	</title>
	<link rel="stylesheet" type="text/css" href="css/all.css">
	<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
	<link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<body>
	<div class="row">
		<div id="responseHeader"></div>
		<div class="col-sm-5">
			<div class="Form" onsubmit="return insertMemberInfo();">
				<form action="" method="POST">
					<br>
					<input type="text"
							id="fname" 
							name="fname" 
							class="form-control" 
							placeholder="Enter Your First Name"
							required="required" 
					>

					<input type="text" 
							id="lname"
							class="form-control" 
							name="lname" 
							placeholder="Enter Your Last Name"
							required="required" 
					>
					<input type="text" 
							id="phone"
							class="form-control" 
							name="phone" 
							placeholder="Enter Your Phone"
							required="required" 
					>

					<input type="text" 
							id="job"
							class="form-control" 
							name="job" 
							placeholder="Enter Your Job"
							required="required" 
					>
					<input type="Submit" 
							class="btn btn-primary btn-block" 
							value="Login" 
							name="btn2"
					>
				</form>
			</div>
		</div>
		<div class="col-sm-1"></div>
		<div class="col-sm-5">
			 <table class="table table-hover">
			 	<thead>
				 	<tr>
					 	<th class="active">First Name</th>
					 	<th class="active">Last Name</th>
					 	<th class="active">Phone</th>
					 	<th class="active">Job</th>
					 	<th class="active">Controls</th>
					 
					</tr>
				</thead>
				<tbody id= "updateMe">
					<?php 
						//include 'mytable.php';
					?>
				</tbody>
			 </table>
			 <button id="update" class="btn btn-success"> Update Now</button>
		 </div>
	</div>
	<div class="clearfiv"></div>
	<div id="ChooseUser"></div>
	<div id="displayUser"></div>
	<script type="text/javascript" src="js/jquery-1.12.0.min.js"></script>
	<script type="text/javascript" src="js/bootstrap.min.js"></script>
	<script type="text/javascript" src="js/ajax.js"></script>
</body>
</html>