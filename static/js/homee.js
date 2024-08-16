var roomName = "{{ room_name }}";
var wsPath = '/ws/watch/' + encodeURIComponent(roomName) + '/';
var chatSocket = new WebSocket('ws://' + window.location.host + wsPath);



var btn = document.getElementById("submit");
btn.onclick = function(e){
    var roomname = document.getElementById("link").value;
    window.location.pathname = "/watch/" + roomname + "/";
}