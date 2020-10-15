function run () {
		// Create My New Request Ajax
		/* 
			== XMLHttpRequest
		 */
		 var myRequest;
		if(window.XMLHttpRequest){ 

			// if it Support Chrome - safari - firefox

		 	myRequest = new XMLHttpRequest();

		}else{
			// if not support ie-6
			myRequest = new ActiveXObject("Microsoft.XMLHTTP");
		}
		myRequest.onreadystatechange = function () {
			var myDiv = document.getElementById("myinfo");
			if(this.readyState == 4 && this.status == 200){
				myDiv.innerHTML  = "<p>HI</p>";
				myDiv.innerHTML += this.responseText;

			}else if(this.readyState < 4 && this.readyState > 0 ){
				myDiv.innerHTML = "<img src='img/loading.gif'>";

			}else{
				myDiv.innerHTML="<h1>Your Request is not initialized </h1><br>";
			}
		}
		myRequest.open("GET","myinfo.php",true);
		myRequest.send();

}
function run1 () {
		var myRequest;
		var Fname = document.getElementsByTagName("input")[0].value;
		if(window.XMLHttpRequest){ 
			// if it Support Chrome - safari - firefox
		 	myRequest = new XMLHttpRequest();
		}else{
			// if not support ie-6
			myRequest = new ActiveXObject("Microsoft.XMLHTTP");
		}
		myRequest.onreadystatechange = function () {
			var myDiv = document.getElementById("myinfo");
			if(this.readyState == 4 && this.status == 200){
				myDiv.innerHTML  = "<p>HI form button 2</p>";
				myDiv.innerHTML += this.responseText;

			}else if(this.readyState < 4 && this.readyState > 0 ){
				myDiv.innerHTML = "<img src='img/loading.gif'>";

			}else{
				myDiv.innerHTML="<h1>Your Request is not initialized </h1><br>";
			}
		}
		myRequest.open("POST","Name.php" ,true);
		myRequest.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
		myRequest.send("Fname=" + Fname);
}
/*
// Send My Request Through Link or Form (Method get/post)
// open(method , url ,asynic[Defult = True , false]) Functions
//If Method Get
myRequest.open("GET","info.php?fname=salah&lname=kiro",true);
myRequest.Send();

//If not have Information
myRequest.open("POST","info.php",true);
myRequest.Send();

myRequest.open("GET","info.php",true);
myRequest.Send();



//If Method POST With Information
myRequest.open("POST","info.php",true);
myRequest.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
myRequest.Send("fname=salah&lname=kiro");



// Asyn false stop even load have done
myRequest.open("GET","info.php",false);
myRequest.Send();
var myDive = document.getElementById('MyDiv');
myDive.innerHTML = myRequest.responseText; // Return Text
myDive.innerHTML = myRequest.responseXML; // Return XML file


// Asyn True Continue load have done
myRequest.onreadystatechange = function (){
	var myDive = document.getElementById('MyDiv');
	myDive.innerHTML = myRequest.responseText; // Return Text
	myDive.innerHTML = myRequest.responseXML; // Return XML file	
}

myRequest.open("GET","info.php",true);
myRequest.Send();
*/



// Show Data In Table
function MyMemberInfo () {
	var myRequest;

	if(window.XMLHttpRequest){ 
 		myRequest = new XMLHttpRequest();
	}else{
		myRequest = new ActiveXObject("Microsoft.XMLHTTP");
	} 
	myRequest.onreadystatechange = MyData;
	myRequest.open("GET","mytable.php",true);
	myRequest.send();
}

function MyData () {

	var table = document.getElementById("updateMe");

	if(this.readyState == 4 && this.status == 200){

		table.innerHTML  = this.responseText;

	}else if(this.readyState < 4 && this.readyState > 0 ){

		table.innerHTML = "<img class='center-block' src='img/loading.gif'>";
	}else{
		table.innerHTML="<h1>Your Request is not initialized </h1><br>";
	}
}
document.getElementById("update").onclick = MyMemberInfo;

MyMemberInfo();


function insertMemberInfo(){
	var myRequest;
	var fname = document.getElementById("fname").value;
	var lname = document.getElementById("lname").value;
	var phone = document.getElementById("phone").value;
	var job = document.getElementById("job").value;
	if(window.XMLHttpRequest){ 
 		myRequest = new XMLHttpRequest();
	}else{
		myRequest = new ActiveXObject("Microsoft.XMLHTTP");
	} 
	myRequest.onreadystatechange = function MyData () {

	var table = document.getElementById("updateMe");

	if(this.readyState == 4 && this.status == 200){
		MyMemberInfo();
		document.getElementById("fname").value = "";
		document.getElementById("lname").value ="";
		document.getElementById("phone").value ="";
		document.getElementById("job").value = "";
		table.innerHTML  = this.responseText;

	}else if(this.readyState < 4 && this.readyState > 0 ){

		table.innerHTML = "<img class='center-block' src='img/loading.gif'>";
	}else{
		table.innerHTML="<h1>Your Request is not initialized </h1><br>";
	}
}

	myRequest.open("POST","insert.php",true);
	myRequest.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
	myRequest.send("fname="+ fname +
					"&lname="+ lname +
					"&phone="+ phone +
					"&job="+ job );
	return false;
};
function deleteUser(userid){
	var myRequest;

	if(confirm("Are You Sure To Delete This Member")){

		if(window.XMLHttpRequest){ 
	 		myRequest = new XMLHttpRequest();
		}else{
			myRequest = new ActiveXObject("Microsoft.XMLHTTP");
		} 
		myRequest.onreadystatechange = function MyData () {

		var table = document.getElementById("updateMe");

		if(this.readyState == 4 && this.status == 200){
			MyMemberInfo();//Update For Table
			table.innerHTML  = this.responseText;

		}else if(this.readyState < 4 && this.readyState > 0 ){

			table.innerHTML = "<img class='center-block' src='img/loading.gif'>";
		}else{
			table.innerHTML="<h1>Your Request is not initialized </h1><br>";
		}
	}
	myRequest.open("GET","delete.php?userid="+userid,true);
	myRequest.send();


	}
	return false;
}

//Choose User
function ChooseUser(){

		var user = document.getElementById('ChooseUser');
		var myRequest;
		if(window.XMLHttpRequest){ 
	 		myRequest = new XMLHttpRequest();
		}else{
			myRequest = new ActiveXObject("Microsoft.XMLHTTP");
		} 
		myRequest.onreadystatechange = function MyData () {
		var table = document.getElementById("updateMe");
		if(this.readyState == 4 && this.status == 200){
			user.innerHTML  = this.responseText;
		}
	}

	myRequest.open("GET","SelectUser.php",true);
	myRequest.send();
}
ChooseUser();


function showUserInfo(userid){
	var myRequest;
	var user = document.getElementById('displayUser');
	if(userid == ''){
		return;
	}
	if(window.XMLHttpRequest){ 
 		myRequest = new XMLHttpRequest();
	}else{
		myRequest = new ActiveXObject("Microsoft.XMLHTTP");
	} 
	myRequest.onreadystatechange = function MyData () {
		var table = document.getElementById("updateMe");
		if(this.readyState == 4 && this.status == 200){
			user.innerHTML  = this.responseText;
		}
	}

	myRequest.open("GET","getOneUserData.php?id=" + userid,true);
	myRequest.send();
	}













































