$(document).ready(function() {
	initializeSendSmsButton();
	sendResponse();
});

function initializeSendSmsButton(){
	$("#send_message").on("click", ({ currentTarget }) => {
		let data = {
			message : "test",
			recipients: [555, 222, 333],
			sender_id: 12,
			site_id: 0,
			is_routine: false
		};
		SOCKET_SERVER.emit("sendSms", {data});
	});
}

function sendResponse(){
	SOCKET_SERVER.on("sendResponse", function( response ) {
        console.log( response );
     });
}