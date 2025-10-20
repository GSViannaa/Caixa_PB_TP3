from datetime import datetime
from tabulate import tabulate


class Cliente: 

    def __init__(self, numero):
        self.numero = numero
        self.data = datetime.now()
        self.itens = []

    def adicionar_produto(self, produto, quantidade):
        total = produto.preco * quantidade
        self.itens.append({
            "nome": produto.nome,
            "preco": produto.preco,
            "quantidade": quantidade,
            "total": total
        })
        produto.reduzir_estoque(quantidade)

    def calcular_total(self):
        return sum(item["total"] for item in self.itens)

    def imprimir_recibo(self):
       
       print(f"\nCliente {self.numero}")
       print(f"Data: {self.data.strftime('%d/%m/%Y %H:%M')}\n")

       tabela = []
       for i, item in enumerate(self.itens, start=1):
        tabela.append([
            i,
            item["nome"],
            item["quantidade"],
            f"{item['preco']:.2f}",
            f"{item['total']:.2f}"
        ])

       headers = ["Item", "Produto", "Quant.", "Preço", "Total"]
       print(tabulate(tabela, headers=headers, tablefmt="grid", stralign="left", numalign="right"))

       total_geral = self.calcular_total()
       print(f"\nTotal: {total_geral:.2f}")
       print(f"Atendimento ao cliente {self.numero} finalizado.\n")