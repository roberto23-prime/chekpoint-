from produto import Produto
from estoque import Estoque

estoque = Estoque()

def menu():
    while True:
        print("\n=== SISTEMA DE GESTÃO DE ESTOQUE ===")
        print("1. Cadastrar Produto")
        print("2. Adicionar Estoque")
        print("3. Remover Estoque")
        print("4. Ajustar Estoque")
        print("5. Listar Produtos")
        print("6. Registrar Venda")
        print("7. Relatório de Vendas")
        print("8. Relatório de Estoque")
        print("9. Histórico de Movimentações")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            codigo = input("Código: ")
            nome = input("Nome: ")
            categoria = input("Categoria: ")
            quantidade = int(input("Quantidade inicial: "))
            preco = float(input("Preço: "))
            descricao = input("Descrição: ")
            fornecedor = input("Fornecedor: ")
            produto = Produto(codigo, nome, categoria, quantidade, preco, descricao, fornecedor)
            estoque.cadastrar_produto(produto)

        elif opcao == "2":
            codigo = input("Código: ")
            qtd = int(input("Quantidade a adicionar: "))
            estoque.adicionar_estoque(codigo, qtd)

        elif opcao == "3":
            codigo = input("Código: ")
            qtd = int(input("Quantidade a remover: "))
            estoque.remover_estoque(codigo, qtd)

        elif opcao == "4":
            codigo = input("Código: ")
            nova_qtd = int(input("Nova quantidade: "))
            estoque.ajustar_estoque(codigo, nova_qtd)

        elif opcao == "5":
            estoque.listar_produtos()

        elif opcao == "6":
            codigo = input("Código do produto: ")
            qtd = int(input("Quantidade vendida: "))
            desconto = float(input("Desconto (%): "))
            estoque.registrar_venda(codigo, qtd, desconto)

        elif opcao == "7":
            estoque.relatorio_vendas()

        elif opcao == "8":
            estoque.relatorio_estoque()

        elif opcao == "9":
            estoque.historico_movimentacoes()

        elif opcao == "0":
            print("👋 Encerrando o sistema.")
            break

        else:
            print("❌ Opção inválida!")

if __name__ == "__main__":
    menu()

