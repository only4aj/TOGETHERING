document.addEventListener('DOMContentLoaded', function () {
    const roomNameElement = document.getElementById('roomName');
    const roomName = roomNameElement.textContent.trim();
    const chatSocket = new WebSocket('ws://' + window.location.host + '/ws/watch/' + roomName + '/');
    
    const chatInput = document.getElementById('chatinput');

    // Define handleKeyUp before attaching it to the event listener
    function handleKeyUp(e) {
        if (e.code === 'Enter') {
            sendMessage();
        }
    }

    chatInput.addEventListener('keyup', handleKeyUp);

    function sendMessage() {
        const message = chatInput.value;
        if (message.trim() !== '') {
            chatSocket.send(JSON.stringify({ 'message': message, 'user': 'Guest' }));
            chatInput.value = '';
        }
    }

    chatSocket.onmessage = function (e) {
        const data = JSON.parse(e.data);
        document.querySelector("#chatarea").value += (data.user + ": " + data.message + '\n');
    };

    chatSocket.onclose = function (e) {
        console.log("chatsocket close");
    };

    document.getElementById('chatinput').focus();
});