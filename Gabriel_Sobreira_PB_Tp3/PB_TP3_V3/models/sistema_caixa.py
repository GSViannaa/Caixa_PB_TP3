from models.arquivo_produtos import ArquivoProdutos
from models.caixa import Caixa

class SistemaCaixa:
    def __init__(self):
        self.arquivo = ArquivoProdutos()
        self.produtos = self.arquivo.ler()
        self.caixa = Caixa(self.produtos)

    def executar(self):
        while True:
            print("\n=== MENU PRINCIPAL ===")
            print("[1] Novo atendimento")
            print("[2] Fechar caixa e sair")

            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                self.caixa.atender_cliente()

            elif opcao == 2:
                self.caixa.fechar_caixa()
                self.arquivo.gravar(self.produtos)

                break
            else:
                print("Opção inválida.")
