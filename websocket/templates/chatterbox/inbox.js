$(document).ready(function() {
	loadQuickInbox();
	quickInboxResponse();
	loadUnregisteredInbox();
	unregisteredInboxResponse();
	loadEventInbox();
	eventInboxResponse();
	loadBlockedInbox();
	blockedInboxResponse();
});

function loadQuickInbox(){
	$("#quick_inbox").on("click", ({ currentTarget }) => {
		SOCKET_SERVER.emit("loadQuickInbox");
	});
}

function quickInboxResponse(){
	SOCKET_SERVER.on("quickInboxResponse", function( response ) {
        console.log( response );
     });
}

function loadUnregisteredInbox(){
	$("#unregistered_inbox").on("click", ({ currentTarget }) => {
		SOCKET_SERVER.emit("loadUnregisteredInbox");
	});
}

function unregisteredInboxResponse(){
	SOCKET_SERVER.on("unregisteredInboxResponse", function( response ) {
        console.log( response );
     });
}

function loadEventInbox(){
	$("#event_inbox").on("click", ({ currentTarget }) => {
		SOCKET_SERVER.emit("loadEventInbox");
	});
}

function eventInboxResponse(){
	SOCKET_SERVER.on("eventInboxResponse", function( response ) {
        console.log( response );
     });
}

function loadBlockedInbox(){
	$("#blocked_inbox").on("click", ({ currentTarget }) => {
		SOCKET_SERVER.emit("loadBlockedInbox");
	});
}

function blockedInboxResponse(){
	SOCKET_SERVER.on("blockedInboxResponse", function( response ) {
        console.log( response );
     });
}