function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    const chatBox = document.getElementById("chat-box");

    if (userInput.trim() === "") return;

    chatBox.innerHTML += `<p class="user-message"><strong>You:</strong> ${userInput}</p>`;

    fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: userInput })
    })
    .then(response => response.json())
    .then(data => {
        chatBox.innerHTML += `<p class="bot-message"><strong>Bot:</strong> ${data.response}</p>`;
        document.getElementById("user-input").value = "";
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(() => {
        chatBox.innerHTML += `<p class="bot-message"><strong>Bot:</strong> Oops! Something went wrong. Please try again.</p>`;
    });
}

function resetChat() {
    const chatBox = document.getElementById("chat-box");
    const userInput = document.getElementById("user-input");

    chatBox.innerHTML = '<p class="bot-message">Hello, welcome to the chatbot! How can I assist you today?</p>';
    userInput.value = "";
    chatBox.scrollTop = 0;
}
