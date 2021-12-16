from model import Jogador
from controller import GerenciadorDeJogo

jogador1 = Jogador('Alex')
jogador2 = Jogador('Joãozinho')

gerenciadorDeJogo = GerenciadorDeJogo(jogador1, jogador2)

while(True):
    input()
    resultado = gerenciadorDeJogo.apostarRodada()
    print(resultado)
    print()