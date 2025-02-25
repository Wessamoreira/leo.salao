$(document).ready(function () {
    $("#menu-btn").click(function () {
        $("#menu").toggleClass("show");
    });
});

$(document).ready(function () {
    $("#menu-btn").click(function () {
        $("#menu").toggleClass("show");
    });

    $("#booking-form").submit(function (event) {
        event.preventDefault();
        
        let name = $("#name").val();
        let service = $("#service").val();
        let date = $("#date").val();
        let phone = "55062992724650";  // Número do WhatsApp do salão

        let message = `Olá, gostaria de agendar um serviço no Salão Elegance.\n\nNome: ${name}\nServiço: ${service}\nData e Hora: ${date}`;
        let whatsappURL = `https://wa.me/${phone}?text=${encodeURIComponent(message)}`;

        window.open(whatsappURL, "_blank");
    });
});

// script.js

document.addEventListener('DOMContentLoaded', function () {
    // Aplica a animação de "flip" aos cartões de serviços e produtos quando a página carrega
    const serviceCards = document.querySelectorAll('.card');
    const productCards = document.querySelectorAll('.product-card');
  
    // Função para aplicar animação ao carregar
    function addFlipAnimation(cards) {
      cards.forEach((card, index) => {
        setTimeout(() => {
          card.classList.add('animate-flip');
        }, index * 200); // Delay entre as animações
      });
    }
  
    // Adicionando animação aos cartões de serviços
    addFlipAnimation(serviceCards);
  
    // Adicionando animação aos cartões de produtos
    addFlipAnimation(productCards);
  });

  // Função para carregar os agendamentos da API
function carregarHorarios() {
    fetch('http://localhost:8000/horarios')
        .then(response => response.json())
        .then(data => {
            const tabelaHorarios = document.getElementById('horarios-table');
            tabelaHorarios.innerHTML = ''; // Limpa a tabela antes de preencher
            data.forEach(agendamento => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${agendamento.nome_cliente}</td>
                    <td>${agendamento.servico}</td>
                    <td>${agendamento.data_hora}</td>
                `;
                tabelaHorarios.appendChild(row);
            });
        })
        .catch(error => {
            console.error('Erro ao carregar os horários:', error);
        });
}

// Carregar os horários assim que a página carregar
document.addEventListener('DOMContentLoaded', carregarHorarios);

