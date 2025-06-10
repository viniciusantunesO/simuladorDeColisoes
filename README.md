🧪 Simulador de Colisões Elásticas 2D
Este projeto é um simulador interativo de colisões elásticas bidimensionais entre bolas, desenvolvido com a biblioteca Pygame. Ele permite visualizar como objetos circulares se movem, colidem e reagem fisicamente de maneira realista em um ambiente fechado.

⚠️ Aviso: Este projeto ainda está em desenvolvimento e pode conter comportamentos imperfeitos ou limitações na simulação física.

🎮 Demonstração
O simulador cria bolas com posições, velocidades e cores aleatórias, e simula colisões entre elas e com as bordas da janela. As colisões seguem as leis da física para colisões elásticas (sem perda de energia cinética).

✅ Funcionalidades
-Inicialização com parâmetros customizáveis via terminal:
    -Tamanho da janela (WIDTH e HEIGHT)
    -Número de bolas (NUM_BOLAS)
    -Raio das bolas (raio)
-Detecção e resposta a colisões entre bolas e com as paredes
-Visualização gráfica interativa usando Pygame
-Velocidades e cores aleatórias para diversificar a simulação
 
🧠 Conceitos Envolvidos
-Colisão Elástica: Troca de momento linear entre duas massas iguais, com conservação de energia.
-Vetores normal e tangente: Utilizados para decompor e recompor as velocidades das bolas durante a colisão.
-Reposicionamento pós-colisão: Para evitar sobreposição entre objetos após uma colisão detectada.