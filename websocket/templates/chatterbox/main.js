let SOCKET_SERVER = null;
$(document).ready(function() {
	SOCKET_SERVER = io.connect('http://localhost:5000');
});