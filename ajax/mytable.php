<?php
	include 'connect.php';

	$stmt = $con->prepare("SELECT * FROM members ORDER BY id ASC");

	$stmt->execute();

	$get_member_info = $stmt->fetchAll();

	if($get_member_info){
		
		foreach ($get_member_info as $row ){
?>
			<tr>
				<td class="active"><?php echo $row['fname'] ; ?> </td>
				<td class="active"><?php echo $row['lame'] ; ?></td>
				<td class="active"><?php echo $row['phone'] ; ?></td>
				<td class="active"><?php echo $row['job'] ; ?></td>
				<td ><a class="btn btn-primary" href="login.php?edit=<?php echo $row['id']; ?>">Edit</a></td>
				<td ><a class="btn btn-danger" href="login.php?delete=<?php echo $row['id']; ?>" onclick="return deleteUser(<?php echo $row['id']; ?>);">Delete</a></td>
			</tr>
<?php
		}
	}else{
		echo "Sorry We Coundnt Fetch Your Information";
	}
?>









































