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

<?php 
    $id = isset($_GET['id']) && is_numeric($_GET['id']) ? intval($_GET['id']) : 0;

	$stmt = $con->prepare("SELECT * FROM user WHERE id = :zid");
	$stmt->execute(array('zid' => $id));
	$rows = $stmt->fetchAll();
	foreach ($rows as $row) {
?>
	<div class="col-sm-3"></div>
	<div class="col-sm-6">
		<form>
	<input  style="margin-top: 20px" value="<?php echo $row['Name'] ?>" class="form-control" required="required" placeholder="Enter Your Name" type="text" name="Name">
	<input class="form-control" value="<?php echo $row['Email'] ?>" required="required" placeholder="Enter Your Email" type="text" name="Email">
	<button class="btn btn-primary btn-block" onsubmit="return update()" type="submit" >Edit Information</button>
	</form>
	</div>	
<?php }?>

	<script src="js/jquery-1.12.0.min.js"></script>	
	<script src="js/bootstrap.min.js"></script>
	<script src="js/main.js"></script>
<script>


		
</script>
</body>
</html>