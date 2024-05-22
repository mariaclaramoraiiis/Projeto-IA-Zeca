function sendMessage() {
    var userInput = document.getElementById("user-input").value;
    var chatBox = document.getElementById("chat-box");

    // Envia a mensagem do usuário para o servidor Flask
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://localhost:5000/chat", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                // Recebeu a resposta do servidor e adiciona ao chat
                var response = JSON.parse(xhr.responseText);
                chatBox.innerHTML += '<div class="message received">' + response.message + '</div>';
                // Limpa o campo de entrada
                document.getElementById("user-input").value = "";
                // Rola o chat para a parte inferior para mostrar a nova mensagem
                chatBox.scrollTop = chatBox.scrollHeight;
            } else {
                console.error('Erro ao enviar a mensagem:', xhr.status);
            }
        }
    };
    xhr.send(JSON.stringify({message: userInput}));
}

