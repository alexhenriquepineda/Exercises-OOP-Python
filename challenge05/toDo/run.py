from planejador_de_viagem import PlanejadorDeViagem
from destinos.belo_horizonte import BeloHorizonte
from destinos.fortaleza import Fortaleza
from destinos.niteroi import Niteroi

planejadorDeViagem = PlanejadorDeViagem()

while(True):

    destino = None

    destino_da_viagem = input('Selecione o destino da viagem: ')

    if (destino_da_viagem == '1'): destino = Niteroi()
    elif (destino_da_viagem == '2'): destino = BeloHorizonte()
    elif (destino_da_viagem == '3'): destino = Fortaleza()
    else: destino = BeloHorizonte()

    atividade = planejadorDeViagem.viajar(destino)

    print(atividade)
    print()