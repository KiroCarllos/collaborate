<?php
	include 'connect.php';

	$stmt = $con->prepare("SELECT * FROM members ORDER BY id ASC");

	$stmt->execute();

	$get_member_info = $stmt->fetchAll();

	if($get_member_info){?>
		<form>
			<select onchange="showUserInfo(this.value);">
				<option value="">Select User</option>
	<?php
		foreach ($get_member_info as $row ){?>
		
			<option value="<?php echo $row['id'] ;?>"><?php echo $row['fname']." ".$row['lame'] ; ?></option>	
	<?php
		}
	?>
			</select>
		</form>
	<?php
	}else{
		echo "Sorry We Coundnt Fetch Your Information";
	}
?>









































