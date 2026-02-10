// Contador de pacientes
let contador = parseInt(document.getElementById('contador').innerText);
const statusEl = document.getElementById('status');

function atualizarStatus() {
    if (contador === 0) {
        statusEl.innerText = '🟢 Livre';
        statusEl.className = 'status verde';
    } else if (contador < 5) {
        statusEl.innerText = '🟡 Parcial';
        statusEl.className = 'status amarelo';
    } else {
        statusEl.innerText = '🔴 Cheio';
        statusEl.className = 'status vermelho';
    }
}

function entrada() {
    contador++;
    document.getElementById('contador').innerText = contador;
    atualizarStatus();
}

function saida() {
    if (contador > 0) {
        contador--;
        document.getElementById('contador').innerText = contador;
        atualizarStatus();
    }
}

// Inicializa o status
atualizarStatus();
