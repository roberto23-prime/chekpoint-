from datetime import datetime

class Venda:
    def __init__(self, codigo_produto, nome_produto, quantidade, valor_unitario, desconto=0):
        self.codigo_produto = codigo_produto
        self.nome_produto = nome_produto
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario
        self.desconto = desconto
        self.data = datetime.now()

    def calcular_total(self):
        total_bruto = self.quantidade * self.valor_unitario
        return total_bruto - (total_bruto * (self.desconto / 100))

    def gerar_recibo(self):
        total = self.calcular_total()
        return (f"\n=== RECIBO DE VENDA ===\n"
                f"Data: {self.data.strftime('%d/%m/%Y %H:%M:%S')}\n"
                f"Produto: {self.nome_produto}\n"
                f"Quantidade: {self.quantidade}\n"
                f"Valor Unitário: R$ {self.valor_unitario:.2f}\n"
                f"Desconto: {self.desconto}%\n"
                f"Total a Pagar: R$ {total:.2f}\n"
                f"========================\n")


