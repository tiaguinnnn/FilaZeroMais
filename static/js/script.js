let contador = 10;
const capacidade = 20;

function atualizarStatus() {
    const status = document.getElementById("status");
    const percentual = contador / capacidade;

    status.className = "status";

    if (percentual < 0.5) {
        status.innerText = "🟢 Livre";
        status.classList.add("verde");
    } else if (percentual < 0.8) {
        status.innerText = "🟡 Moderado";
        status.classList.add("amarelo");
    } else {
        status.innerText = "🔴 Lotado";
        status.classList.add("vermelho");
    }

    document.getElementById("contador").innerText = contador;
}

function entrada() {
    if (contador < capacidade) {
        contador++;
        atualizarStatus();
        // aqui depois entra fetch() pro Django
    }
}

function saida() {
    if (contador > 0) {
        contador--;
        atualizarStatus();
    }
}
