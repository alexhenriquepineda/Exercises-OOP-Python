from gerenciador_de_email import GerenciadorDeEmail
from destinatario import Destinatario

gerenciadorDeEmail = GerenciadorDeEmail('MinhaEmpresa', 'empresa@email.com')

while True:
    titulo = input('Defina o Titulo do Email: ')
    mensagem = input('Defina o assunto: ')
    print()

    gerenciadorDeEmail.criar_email(titulo, mensagem)

    command = 's'

    while command == 's':
        nome = input('Defina o nome do destinatario: ')
        email = input('Defina o e-mail do destinatario: ')
        destinatario = Destinatario(nome, email)
        gerenciadorDeEmail.adicionar_destinatario(destinatario)
        print()

        command = input('Deseja adicionar outro destinatario? s/n')

    gerenciadorDeEmail.enviar_email()
    print()