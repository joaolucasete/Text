__doc__ = """

DOCUMENTATION

Aplicação com foco em ler arquivos.
No momento a aplicação pode ler os seguintes tipos arquivos...
    .TXT

"""

from sys import argv
from colorama import Fore

class Text:
    def __init__(self):
        # Cria as configs gerais

        self.on_ready = str()
        self.filename = str()
    @staticmethod
    def config(on_ready: str="", filename: str=""):
        """
        Seta as configurações para a aplicação

        Parametros:
            on_ready: str
                Exibe uma mensagem quando o programa...
                Esta pronto
            filename: str
                Pega o nome do arquivo para ler

        Exemplo de utilização:
            lib.config(on_ready="Ola Mundo!", filename="Ola.txt")
        """

        text.on_ready = on_ready
        file.filename = filename
    @staticmethod
    async def run(app: object) -> None:
        """
        Roda a aplicação
        """
        text.app = app

        if len(argv) == 1:
            print(Fore.GREEN + text.on_ready + Fore.RESET)
        elif len(argv) == 2:
            if argv[1] == "--Help":
                text.__help__()
    @staticmethod
    def __version__():
        print(Fore.RED + "Text version: 0.0.1" + Fore.RESET)
    @staticmethod
    def __help__():
        print("""Funções disponiveis:
    lib.__version__() Exibe a versão do aplicativo.
    lib.__help__() Exibe todos comandos disponiveis.
    lib.config() Cria a config da aplicação""")
class Readfile:
    @staticmethod
    def read_txt():
        """
        Vai ler o parametro filename 
        e exibir
        """
        if len(argv) == 1:
            f = open(file.filename, 'r')
            print(Fore.BLUE + f.read() + Fore.RESET)
            f.close()

file = Readfile()
text = Text()
