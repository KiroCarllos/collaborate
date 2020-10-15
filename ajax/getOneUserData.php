<?php
	include 'connect.php';

	$stmt = $con->prepare("SELECT * FROM members WHERE id = (:zid)");

	$stmt->execute(array('zid' => $_GET['id'] ));

	$get_member_info = $stmt->fetchAll();

	if(isset($get_member_info)){

		foreach ($get_member_info as $row ){ ?>
			 <table class="table table-hover">
			 	<thead>
				 	<tr>
					 	<th>First Name</th>
					 	<th>Last Name</th>
					 	<th>Phone</th>
					 	<th>Job</th> 	
					</tr>
				</thead>
				<tbody id= "updateMe">
					<tr>
						<td class="active"><?php echo $row['fname'] ; ?> </td>
						<td class="active"><?php echo $row['lame'] ; ?></td>
						<td class="active"><?php echo $row['phone'] ; ?></td>
						<td class="active"><?php echo $row['job'] ; ?></td>
					</tr>
				</tbody>
			</table>	
		<?php
		}
	}else{
		
	}
?>