class Produto:
    def __init__(self, id_produto, nome, quantidade, preco):
        
        self.id = id_produto
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def reduzir_estoque(self, quantidade):

        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
        else:
            raise ValueError(f"Estoque insuficiente para o produto {self.nome}.")

    def __repr__(self):
        return f"{self.id} - {self.nome} (Qtd: {self.quantidade}, Preço: {self.preco:.2f})"