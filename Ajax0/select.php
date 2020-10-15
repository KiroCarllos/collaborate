?php
	include 'connect.php';
	$stmt = $con->prepare("SELECT * FROM user ");

	$stmt->execute();

	$get_member_info = $stmt->fetchAll();

	if($get_member_info > 0){
		
	
		foreach ($get_member_info as $row ){
		
			echo "<h3 class='container'>"."The Name is ".$row['Name']." and Email is ".$row['Email'] ."</h3>";
			?>
			<a class="btn btn-primary" href="update.php?edit&id=<?php echo $row['id']; ?>">Update</a>

			
			<a class="btn btn-danger" href="index.php?delete=<?php echo $row['id']; ?>" onclick="return DeleteUser(<?php echo $row['id']; ?>);">Delete</a>	
		
		<?php
		}
	}