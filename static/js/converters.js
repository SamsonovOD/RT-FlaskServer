function buf2hex(buffer) {
	byteArray = new Uint8Array(buffer);
	hexParts = [];
	for(i = 0; i < byteArray.length; i++) {
		hex = byteArray[i].toString(16);
		if (hex.length == 2) {
			paddedHex = ('\\x' + hex);
		} else {
			paddedHex = ('\\x0' + hex);
		}
		hexParts.push(paddedHex);
	}
	return hexParts.join('');
}

function Uint8ToString(u8a){
	var CHUNK_SZ = 0x8000;
	var c = [];
	for (var i=0; i < u8a.length; i+=CHUNK_SZ) {
		c.push(String.fromCharCode.apply(null, u8a.subarray(i, i+CHUNK_SZ)));
	}
	return c.join("");
}

function retrieveImageFromClipboardAsBlob(pasteEvent, callback){
	if(pasteEvent.clipboardData == false){
		if(typeof(callback) == "function"){
			callback(undefined);
		}
	};
	var items = pasteEvent.clipboardData.items;
	if(items == undefined){
		if(typeof(callback) == "function"){
			callback(undefined);
		}
	};
	for (var i = 0; i < items.length; i++) {
		if (items[i].type.indexOf("image") == -1) continue;
		var blob = items[i].getAsFile();
		if(typeof(callback) == "function"){
			callback(blob);
		}
	}
}