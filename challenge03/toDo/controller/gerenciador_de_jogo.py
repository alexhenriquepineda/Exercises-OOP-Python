class GerenciadorDeJogo:

    def __init__(self, jogador1, jogador2) -> None:
        self.__jogador1 = jogador1
        self.__jogador2 = jogador2

    def __jogada1(self):
        jogador1_jogada = self.__jogador1.fazer_jogada()

        return jogador1_jogada

    def __jogada2(self):
        jogador2_jogada = self.__jogador2.fazer_jogada()

        return jogador2_jogada

    def apostarRodada(self):
        jogador1_jogada = self.__jogada1()  
        jogador2_jogada = self.__jogada2()     
        

        resultado_da_rodada = self.__verificar_jogadas(jogador1_jogada, jogador2_jogada)

        if ( resultado_da_rodada == 1): self.__jogador1.incrementar_vitorias()
        if ( resultado_da_rodada == 2): self.__jogador2.incrementar_vitorias()

        return self.__apresentar_resultados(jogador1_jogada, jogador2_jogada)


    def __verificar_jogadas(self, jogador1_jogada, jogador2_jogada):
        if (jogador1_jogada == jogador2_jogada): return 0

        if (
            (jogador1_jogada == 'pedra' and jogador2_jogada == 'tesoura') 
            or (jogador1_jogada == 'papel' and jogador2_jogada == 'pedra')
            or (jogador1_jogada == 'tesoura' and jogador2_jogada == 'papel')
        ): return 1

        return 2

    def __apresentar_resultados(self, jogador1_jogada, jogador2_jogada):
        return f' {self.__jogador1.apresentar_vitorias()} e jogou {jogador1_jogada} ----- {self.__jogador2.apresentar_vitorias()} e jogou {jogador2_jogada}'

