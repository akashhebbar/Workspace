<html>
<form name="f1" method="POST">
name<input type="text" name="name">
<input type="submit" name="sub">

</form>
<?php
if(isset($_POST["sub"]))
{
	$a=$_POST['name'];
	
	
	echo $a;
}
?>