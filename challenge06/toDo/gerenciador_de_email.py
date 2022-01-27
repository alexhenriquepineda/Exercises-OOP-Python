class GerenciadorDeEmail:

    def __init__(self, nome_remetente, email_remetente) -> None:
        self.__nome_remetente = nome_remetente
        self.__email_remetente = email_remetente
        self.__titulo = None
        self.__mensagem = None
        self.__lista_destinatario = []

    def criar_email(self, titulo, mensagem):
        self.__titulo = titulo
        self.__mensagem = mensagem

    def adicionar_destinatario(self, destinatario):
        self.__lista_destinatario.append(destinatario)

    def enviar_email(self):
        print(
            f'''
            Enviando mensagem . . .
            Remetente: {self.__nome_remetente}
            Email: {self.__email_remetente}
            - Título: {self.__titulo}
            Mensagem: {self.__mensagem}
            '''
        )

        print('Destinatarios: ')

        for destinatario in self.__lista_destinatario:
            print(f'        {destinatario.nome} - {destinatario.email}')

        self.__lista_destinatario = []