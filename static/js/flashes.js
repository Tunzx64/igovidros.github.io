
// Espera 3 segundos e esconde a mensagem
setTimeout(function() {
const flashMessage = document.querySelector('.flash-message');
if (flashMessage) {
    flashMessage.style.opacity = '0'; // Aplica a transição de fade out
    setTimeout(() => flashMessage.remove(), 500); // Remove do DOM após a transição
}
}, 3000);
