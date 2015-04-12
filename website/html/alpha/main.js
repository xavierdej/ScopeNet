// JavaScript Document

// Get the XMLHttpRequest object
function getXmlHttpRequestObject() {
	if (window.XMLHttpRequest) {
		return new XMLHttpRequest(); //Not IE
	} else if(window.ActiveXObject) {
		return new ActiveXObject("Microsoft.XMLHTTP"); //IE
	} else {
		alert("Error : Your browser doesn't support the XmlHttpRequest object.");
		return false;
	}
}

// Called when something is entered in to the search
function lookupBodyUpdated() {
var receiveReq = getXmlHttpRequestObject();
	if ((receiveReq) && (receiveReq.readyState == 4 || receiveReq.readyState == 0)) {
		receiveReq.open("GET", "bodysearch.php?q=" + document.getElementById('bodysearch').value, true);
		receiveReq.onload = function (e) {
			if ((receiveReq.readyState == 4) && (receiveReq.status == 200)) {
				var responseText = receiveReq.responseText;
				document.getElementById('bodyresults').innerHTML = responseText;
			}	
		}
		receiveReq.send(null);
	}
}

// Called to switch the camera image shown
function switchImage(imageURL) {
	// Speed up the delay if already hidden
	var hideDelay = 400;
	if (previewimage.style.opacity==0) {
		hideDelay = 1;
	}
	// Hide the old image
	previewimage.style.opacity = 0;
	setTimeout(function(){
		// Swap the image
		var previewimage = document.getElementById('previewimage');
		previewimage.src = imageURL;
		// Change what the image links to
		var previewanchor = document.getElementById('previewanchor');
		previewanchor.onclick = function() {
			window.location.href = imageURL; 
		    return false;
		};
		setTimeout(function(){
			// Show the image after it loads
			previewimage.style.opacity = 1;	
		}, 400);
	}, hideDelay);
}
