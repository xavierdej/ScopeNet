<?PHP

// Sanity / security check
if (!isset($_GET['q'])) { die(); }

// Get the name to search for
$searchVal = $_GET['q'];

// Connect to the database
include_once('lib/database.php');

// Queary the database
$query_result = mysql_query( "SELECT `Name`
		FROM `bodies`
		WHERE ( `Name` LIKE '" . $searchVal . "%' )
		LIMIT 50" );

// Loop through the results
while ( $query_row = mysql_fetch_row( $query_result ) ) {

	$theName = $query_row[0];
		
	echo '<li><a href="body.php?b=' . $theName . '">' . $theName . '</a></li>' . "\n";
		
}

?>