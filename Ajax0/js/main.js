
function get(theUrl,callback) {
	var myRequest;
 		myRequests = new XMLHttpRequest();
		myRequests.onreadystatechange = function() {
		if(myRequests.readyState == 4 && myRequests.status == 200){
				callback(myRequests.responseText); // refresh Data
			}

		}
		
			myRequests.open("GET",theUrl,true);
			myRequests.send();
	

	
	return false;
}


//get("SelectUser.php",function(e){
//	var table = document.getElementById("S");
//	table.innerHTML=e;
//});

	// insert User
	$('#button').on('click',function insertMemberInfo(){
		var myRequest;
		var Name = document.getElementById("Name").value;
		var Email = document.getElementById("Email").value;
		if(window.XMLHttpRequest){
	 		myRequest = new XMLHttpRequest();
		} 
		myRequest.onreadystatechange = function MyData () {
			if(myRequest.readyState == 4 && myRequest.status == 200){
				document.getElementById("Email").value = "";
				document.getElementById("Name").value ="";
				return (location).reload();
			}
		}
		if(Name =="" || Email == ""){
			return false;
		}else{
				myRequest.open("POST","data.php",true);
				myRequest.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
				myRequest.send("Name="+ Name +"&Email="+ Email);
		}
	
		return false;
	});

	function getUsers() {
	var myRequest;
 		myRequests = new XMLHttpRequest();
		myRequests.onreadystatechange = function() {
		var table = document.getElementById("Data");

		if(myRequests.readyState == 4 && myRequests.status == 200){
				table.innerHTML = myRequests.responseText; // refresh Data
			}

		}
		
			myRequests.open("GET","SelectUser.php",true);
			myRequests.send();
	
	return false;
}
function DeleteUser(userid) {
		var myRequest;
	if(confirm("Are You Sure To Delete myRequest Member")){
 		myRequest = new XMLHttpRequest();
		myRequest.onreadystatechange = function() {
		var table = document.getElementById("S");
		if(myRequest.readyState == 4 && myRequest.status == 200){
				return (location).reload(); // refresh Data
			}
		}
		myRequest.open("GET","delete.php?userid="+userid,true);
		myRequest.send();
	}
	return false;
}

function update() {
		var myRequest;
 		myRequest = new XMLHttpRequest();
		myRequest.onreadystatechange = function() {
		var table = document.getElementById("S");
		if(myRequest.readyState == 4 && myRequest.status == 200){
				console.log("JSAD");
			}
		}
		myRequest.open("POST","userUpdate.php",true);
					myRequest.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
		
		myRequest.send();
	
	return false;
}








		