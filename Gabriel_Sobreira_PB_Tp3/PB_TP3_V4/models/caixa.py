from models.cliente import Cliente
from tabulate import tabulate

class Caixa:
    def __init__(self, produtos):
        self.produtos = produtos
        self.produtos_vendidos = []
        self.numero_cliente = 1

    def buscar_produto(self, id_produto):

        for p in self.produtos:
            if p.id == id_produto:
                return p
        return None

    def atender_cliente(self):

        cliente = Cliente(self.numero_cliente)
        while True:
            opcao = int(input("\n[1] Adicionar produto | [2] Finalizar compra: "))

            if opcao == 1:
                id_produto = int(input("ID do produto: "))
                produto = self.buscar_produto(id_produto)

                if produto:
                    qtd = int(input("Quantidade: "))
                    cliente.adicionar_produto(produto, qtd)

                else:
                    print("Produto não encontrado.")

            elif opcao == 2:
                cliente.imprimir_recibo()
                self.produtos_vendidos.append(cliente)
                self.numero_cliente += 1
                break

    def fechar_caixa(self):

       print("\n=== FECHAMENTO DE CAIXA ===\n")

       if not self.produtos_vendidos:
            print("Nenhum cliente foi atendido.")
            return

       total_caixa = 0
       total_itens = 0
       tabela = []

       
       for cliente in self.produtos_vendidos:
            subtotal = cliente.calcular_total()
            total_caixa += subtotal
            qtd_itens_cliente = sum(item["quantidade"] for item in cliente.itens)
            total_itens += qtd_itens_cliente

            tabela.append([f"Cliente {cliente.numero}", qtd_itens_cliente, f"{subtotal:.2f}"])

     
       print(tabulate(tabela, headers=["Cliente", "Itens Vendidos", "Total ($)"], tablefmt="grid"))

        
       print("\n============================")
       print(f"Total de clientes: {len(self.produtos_vendidos)}")
       print(f"Total de itens vendidos: {total_itens}")
       print(f"Total arrecadado: {total_caixa:.2f}")
       print("============================")

 
       produtos_sem_estoque = [p for p in self.produtos if p.quantidade <= 0]

       if produtos_sem_estoque:
            print("\n========= Produtos sem estoque ==========")
            for p in produtos_sem_estoque:
                print(f"O produto {p.nome} ficou sem estoque")
            print("===========================================\n")
       else:
            print("\nNenhum produto ficou sem estoque.\n")

    