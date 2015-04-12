<?PHP

// Connect to the database
include_once('../alpha/lib/database.php');

// Queary the database
$query_result = mysql_query( "SELECT `Name`
		FROM `requests`
		LIMIT 1" );

// Loop through the results
if ( $query_row = mysql_fetch_row( $query_result ) ) {
	$theName = $query_row[0];
	$theData = array('jobid' => time(), 'body' => $theName);
	// Remove the record returned
	mysql_query("DELETE FROM `requests` WHERE `Name` = '" . $theName . "'");
}
else {
	$theData = array('jobid' => '0', 'delay' => '20');
}

echo json_encode($theData);

?>