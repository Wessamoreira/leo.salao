document.getElementById("form-produto").addEventListener("submit", function(event) {
    event.preventDefault(); // Impede o envio do formulário

    // Captura os dados dos campos
    const nome = document.getElementById("nome").value;
    const preco = parseFloat(document.getElementById("preco").value);
    const estoque = parseInt(document.getElementById("estoque").value);

    // Validação simples
    if (!nome || preco <= 0 || estoque < 0) {
        alert("Por favor, preencha todos os campos corretamente.");
        return;
    }

    // Simula o envio para um banco de dados (aqui você poderia enviar para um backend via API)
    alert(`Produto Adicionado: ${nome}\nPreço: R$ ${preco.toFixed(2)}\nEstoque: ${estoque}`);

    // Limpa os campos do formulário
    document.getElementById("nome").value = '';
    document.getElementById("preco").value = '';
    document.getElementById("estoque").value = '';
});