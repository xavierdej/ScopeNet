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

<div id="bodyblock">
<label>Recent views of <?PHP if ($body=='Moon') { echo 'the '; }; echo($body); ?> :-</label>
<ul id="bodyresults">

<?PHP

// Connect to the database
include_once('lib/database.php');

// Queary the database
$query_result = mysql_query( "SELECT `UploadTime`, `Name`, `FileName`
		FROM `uploads`
		WHERE ( `Name` = '" . $body . "' )
		ORDER BY `UploadTime` DESC
		LIMIT 5" );

// Apologise for no results
if (mysql_num_rows($query_result)==0) {
	echo "<li>No recent views found.</li>";
}

// Loop through the results
while ( $query_row = mysql_fetch_row( $query_result ) ) {
	$theTime = date('D jS M Y g:ia', strtotime($query_row[0]));
	$theFileName = $query_row[2];
	echo '<li><a href="#" onclick="switchImage(' . "'/imagecache/" . $theFileName . "'" . ');">' . $theTime . '</a></li>' . "\n";		
}


?>
</ul>
<input id="requestbutton" value="Request New Image..." type="button" onclick="location.href = 'request.php?b=<?PHP echo($body); ?>';" />
</div>

<a id="previewanchor" href="#"><img id="previewimage" src="holder.png" /></a>

<div id="gazers"> </div>
</body>
</html>
