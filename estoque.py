from produto import Produto
from vendas import Venda

class Estoque:
    def __init__(self):
        self.produtos = {}
        self.vendas_realizadas = []
        self.historico = []

    def cadastrar_produto(self, produto):
        if produto.codigo in self.produtos:
            print("⚠️ Produto com este código já existe.")
        else:
            self.produtos[produto.codigo] = produto
            print("✅ Produto cadastrado com sucesso!")

    def adicionar_estoque(self, codigo, quantidade):
        if codigo in self.produtos:
            self.produtos[codigo].quantidade += quantidade
            self.historico.append(f"Adicionado {quantidade}x {self.produtos[codigo].nome}")
            print("✅ Estoque atualizado.")
        else:
            print("❌ Produto não encontrado.")

    def remover_estoque(self, codigo, quantidade):
        if codigo in self.produtos:
            produto = self.produtos[codigo]
            if produto.quantidade >= quantidade:
                produto.quantidade -= quantidade
                self.historico.append(f"Removido {quantidade}x {produto.nome}")
                print("🗑️ Produto removido do estoque.")
            else:
                print("⚠️ Quantidade insuficiente.")
        else:
            print("❌ Produto não encontrado.")

    def ajustar_estoque(self, codigo, nova_qtd):
        if codigo in self.produtos:
            self.produtos[codigo].quantidade = nova_qtd
            self.historico.append(f"Ajustado estoque de {self.produtos[codigo].nome} para {nova_qtd}")
            print("🔧 Estoque ajustado.")
        else:
            print("❌ Produto não encontrado.")

    def listar_produtos(self):
        if not self.produtos:
            print("📦 Nenhum produto cadastrado.")
            return
        print("\n=== LISTA DE PRODUTOS ===")
        for p in self.produtos.values():
            print(p)
            if p.quantidade < 5:
                print("⚠️ Estoque baixo!\n")

    def registrar_venda(self, codigo, quantidade, desconto=0):
        if codigo not in self.produtos:
            print("❌ Produto não encontrado.")
            return

        produto = self.produtos[codigo]
        if produto.quantidade < quantidade:
            print("⚠️ Estoque insuficiente para esta venda.")
            return

        produto.quantidade -= quantidade
        venda = Venda(codigo, produto.nome, quantidade, produto.preco, desconto)
        self.vendas_realizadas.append(venda)
        self.historico.append(f"Venda - {quantidade}x {produto.nome}")
        print(venda.gerar_recibo())

    def relatorio_vendas(self):
        print("\n=== RELATÓRIO DE VENDAS ===")
        if not self.vendas_realizadas:
            print("Nenhuma venda registrada.")
            return
        for v in self.vendas_realizadas:
            print(f"{v.data.strftime('%d/%m/%Y %H:%M:%S')} | {v.nome_produto} | Qtd: {v.quantidade} | Total: R$ {v.calcular_total():.2f}")

    def relatorio_estoque(self):
        print("\n=== RELATÓRIO DE ESTOQUE ===")
        for p in self.produtos.values():
            print(f"{p.nome} - Qtd: {p.quantidade} - R$ {p.preco:.2f}")

    def historico_movimentacoes(self):
        print("\n=== HISTÓRICO DE MOVIMENTAÇÕES ===")
        for h in self.historico:
            print(h)

