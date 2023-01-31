<?php session_start(); /* Starts the session */

if(!isset($_SESSION['UserData']['Username'])){
	header("location:login.php");
	exit;
}
echo "Welcome: ".$_SESSION['UserData']['Username']."<br>";
echo "Your credit card:".$_SESSION['UserData']['credit']."<br>";
?>

<a href="logout.php">Click here</a> to Logout.
