<?PHP

// Saifty and sanity check
if (!isset($_FILES['file'])) { die(); }
if (!isset($_POST['bodyName'])) { die(); }

// Connect to the database
include_once('../alpha/lib/database.php');

// Build a new filename
$destFilename = time() . '_' .  $_POST['bodyName'] . '.png';

// Move and rename the uploaded image file
move_uploaded_file($_FILES["file"]["tmp_name"], '../imagecache/' . $destFilename);

// Add a record of the image to the database
mysql_query("INSERT INTO `uploads` (`UploadTime`, `Name`, `FileName`) VALUES (CURRENT_TIMESTAMP, '" . $_POST['bodyName'] . "', '" . $destFilename . "');");

?>