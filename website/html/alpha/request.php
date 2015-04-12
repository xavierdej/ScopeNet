<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>ScopeNet</title>
<link href="main.css" rel="stylesheet" type="text/css" />
<script src="main.js"></script>
</head>
<?PHP
	$body = isset($_GET['b']) ? $_GET['b'] : '';
?>
<body>
<a href="./"><img id="logoimg" src="logo.png" alt="ScopeNet" /></a>

<?PHP

// Connect to the database
include_once('lib/database.php');
// Add the request to the database
$query_result = mysql_query( "INSERT INTO `requests` (`Name`) VALUES ('" . $body . "') " );

?>

<div id="bodyblock">
<div id="bigmessage">A new image of <?PHP if ($body=='Moon') { echo 'the '; }; echo($body); ?> has been requested and will appear here soon.</div><br />
<div id="bigmessage">Why not <a href="./">look for another body</a> while waiting.</div>
</div>

<div id="gazers"> </div>
</body>
</html>
