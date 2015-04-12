<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>ScopeNet</title>
<link href="main.css" rel="stylesheet" type="text/css" />
<script src="main.js"></script>
</head>

<body>
<a href="./"><img id="logoimg" src="logo.png" alt="ScopeNet" /></a>

<div id="bodyblock">
<label>What star or planet do you want to look at today?</label>
<input id="bodysearch" name="bodysearch" type="text" value="" onkeypress="setTimeout(function(){lookupBodyUpdated();}, 100);" autofocus /><br />
<ul id="bodyresults">
</ul>
</div>

<div id="gazers"> </div>
</body>
</html>
