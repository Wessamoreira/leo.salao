// Simulação de dados de produtos (em um ambiente real, isso seria buscado via API)
const produtos = [
    { nome: "Shampoo", preco: 30.00, estoque: 50 },
    { nome: "Condicionador", preco: 25.00, estoque: 30 },
    { nome: "Creme para Pentear", preco: 20.00, estoque: 100 },
];

// Função para carregar a lista de produtos na tabela
function carregarProdutos() {
    const productList = document.getElementById('product-list');
    productList.innerHTML = "";  // Limpa a tabela antes de adicionar os novos produtos

    produtos.forEach(produto => {
        const row = document.createElement('tr');
        
        row.innerHTML = `
            <td>${produto.nome}</td>
            <td>R$ ${produto.preco.toFixed(2)}</td>
            <td>${produto.estoque}</td>
            <td>
                <button onclick="editarProduto('${produto.nome}')">Editar</button>
                <button onclick="removerProduto('${produto.nome}')">Remover</button>
            </td>
        `;

        productList.appendChild(row);
    });
}

// Função para editar um produto
function editarProduto(nome) {
    alert("Editar produto: " + nome);
    // Aqui você pode redirecionar para uma página de edição de produto ou mostrar um formulário de edição
}

// Função para remover um produto
function removerProduto(nome) {
    alert("Produto removido: " + nome);
    // Aqui você pode fazer a remoção do produto via API ou manipulando a lista local
}

// Carregar a lista de produtos assim que a página carregar
window.onload = carregarProdutos;