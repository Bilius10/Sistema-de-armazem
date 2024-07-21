import flet as ft
import funcoes
import time

# Armazenamento do histórico de navegação
navigation_history = []

#Funcao mãe, basicamente tudo que estiver dentro dela ira ser o aplicativo
def main(page: ft.Page):
    #configurações da tela de principal
    page.title = "SISTEMA DE ARMAZENAMENTO"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme = ft.Theme(color_scheme_seed=ft.colors.GREY)
    
    #função salva o estado atual dos controles da página,
    def salvar_estado_atual():
        #salva em uma lista o que tem naquela pagina ou seja, o estado atual
        estado_atual = {
            'controls': list(page.controls)
        }
        #o que esta dentro da lista estado_atual, sera salvo na lista navigation_history
        navigation_history.append(estado_atual)
        #limpara o que estava na ultima pagina acessada, para não haver sobreposição do novo layout com o antigo 
        page.clean()

    #função que sera usada para voltar para a ultima pagina acessada
    def voltar(evento):
        if navigation_history:
            #dara um pop"retirar" as ultimas informações salvas "sera a pagina que estaremos no exato momento"
            last_state = navigation_history.pop()
            #limpara a pagina
            page.clean()
            #voltara para a ultima pagina salva na lista
            for control in last_state['controls']:
                #adiciona os itens a pagina
                page.add(control)
            
    #funcao que sera chama ao clicar o botao"Cadastrar Produto" localizado no menu
    def cadastro_produto(evento):

        #usa a funcao para salvar as configurações da pagina"spawpoint"
        salvar_estado_atual()

        #cria TextField"caixas de texto flutuantes", para escrevermos nelas 
        codigo = ft.TextField(label="Código do Produto", width=200)
        nome = ft.TextField(label="Nome do Produto", width=200)
        quantidade = ft.TextField(label="Quantidade", width=200)
        valor = ft.TextField(label="Valor Unitário", width=200)

        #funcao aonde inviaremos as informações escritas a uma outra funcao
        def enviar(evento):
            #enviamos as informações recebidas para a funcao cadastro_produto
            mensagem = funcoes.cadastro_produto(int(codigo.value),str(nome.value),int(quantidade.value),float(valor.value))
            #adiciona a mensagem recebida na tela/e apos meio segundo retira ela
            men_tela =ft.Text(mensagem)
            page.add(men_tela)
            time.sleep(0.5)
            page.remove(men_tela)
            

        #parte responsavel por criar os itens que apareceram na tela
        titulo = ft.Container(content=ft.Text("CADASTRO DE PRODUTOS", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.GREY), alignment=ft.alignment.center, margin=10)
        botao_cadastro = ft.ElevatedButton(text="Cadastrar", on_click=enviar)
        #form estara salvando os TextField criados um pouco acima
        form = ft.Column([codigo, nome, quantidade, valor], alignment=ft.MainAxisAlignment.CENTER)
        #aqui adicionamos os itens na tela 
        page.add(titulo, form, botao_voltar, botao_cadastro)
        
    #funcao que sera chama ao clicar o botao"Cadastrar Kit" localizado no menu
    def cadastro_kit(evento):

        #usa a funcao para salvar as configurações da pagina"spawpoint"
        salvar_estado_atual()

        #cria TextField"caixas de texto flutuantes", para escrevermos nelas 
        codigo = ft.TextField(label="Código do Kit", width=300)  
        kit = ft.TextField(label="Nome do Kit", width=300)  
        produto = ft.TextField(label="Nomes dos produtos que estarão no kit", width=300)  
        valor = ft.TextField(label="Valor da cesta", width=300)  

        #funcao aonde inviaremos as informações escritas a uma outra funcao
        def enviar(evento):
                #enviamos as informações recebidas para a funcao cadastro_produto
                mensagem = funcoes.cadastro_kit(int(codigo.value), str(kit.value), str(produto.value), float(valor.value))
                #adiciona a mensagem recebida na tela/e apos meio segundo retira ela
                men_tela =ft.Text(mensagem)
                page.add(men_tela)
                time.sleep(0.5)
                page.remove(men_tela)

        #parte responsavel por criar os itens que apareceram na tela
        titulo = ft.Container(content=ft.Text("CADASTRO DE KITS", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.GREY), alignment=ft.alignment.center, margin=10)
        botao_cadastro = ft.ElevatedButton(text="Cadastrar", on_click=enviar)
        #form estara salvando os TextField criados um pouco acima
        form = ft.Column([codigo, kit, produto, valor], alignment=ft.MainAxisAlignment.CENTER)
        #aqui adicionamos os itens na tela 
        page.add(titulo, form, botao_voltar, botao_cadastro)

    #funcao que sera chama ao clicar o botao"Cadastro Venda" localizado no menu
    def cadastro_venda(evento):

        #usa a funcao para salvar as configurações da pagina"spawpoint"
        salvar_estado_atual()

        #cria TextField"caixas de texto flutuantes", para escrevermos nelas 
        nome = ft.TextField(label="Digite o nome do produto", width=300) 
        quantidade = ft.TextField(label="Quantidade vendida", width=300)  
        valor = ft.TextField(label="Digite o valor unitario do produto", width=300) 
        nome_cliente = ft.TextField(label="Digite o nome do cliente", width=300)  

        #funcao aonde inviaremos as informações escritas a uma outra funcao
        def enviar(evento):
                #enviamos as informações recebidas para a funcao cadastro_produto
                mensagem = funcoes.cadastro_vendas(str(nome.value), int(quantidade.value), float(valor.value), str(nome_cliente.value))
                #adiciona a mensagem recebida na tela/e apos meio segundo retira ela
                men_tela =ft.Text(mensagem)
                page.add(men_tela)
                time.sleep(0.5)
                page.remove(men_tela)
                
        #parte responsavel por criar os itens que apareceram na tela
        titulo = ft.Container(content=ft.Text("CADASTRO DE VENDAS", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.GREY), alignment=ft.alignment.center, margin=10)
        botao_cadastro = ft.ElevatedButton(text="Cadastrar", on_click=enviar)
        #form estara salvando os TextField criados um pouco acima 
        form = ft.Column([nome, quantidade, valor, nome_cliente], alignment=ft.MainAxisAlignment.CENTER)
        #aqui adicionamos os itens na tela 
        page.add(titulo, form, botao_voltar, botao_cadastro)

    #funcao que sera chama ao clicar o botao"Retirar Produto" localizado no menu
    def retirar(evento):

        #usa a funcao para salvar as configurações da pagina"spawpoint"
        salvar_estado_atual()

        #cria TextField"caixas de texto flutuantes", para escrevermos nelas 
        codigo = ft.TextField(label="Código do produto", width=300)

        #funcao aonde inviaremos as informações escritas a uma outra funcao
        def enviar(evento):
                #enviamos as informações recebidas para a funcao cadastro_produto
                mensagem = funcoes.eliminar(int(codigo.value))
                #adiciona a mensagem recebida na tela/e apos meio segundo retira ela
                men_tela =ft.Text(mensagem)
                page.add(men_tela)
                time.sleep(0.5)
                page.remove(men_tela)

        #parte responsavel por criar os itens que apareceram na tela
        titulo = ft.Container(content=ft.Text("RETIRAR PRODUTO", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.GREY), alignment=ft.alignment.center, margin=10)
        botao_retirar = ft.ElevatedButton(text="Retirar", on_click=enviar)
        #aqui adicionamos os itens na tela 
        page.add(titulo, botao_voltar, codigo, botao_retirar)

    #funcao que sera chama ao clicar o botao "Pesquisar Produto" localizado no menu
    def pesquisar(evento):

        #usa a funcao para salvar as configurações da pagina"spawpoint"
        salvar_estado_atual()

        #cria TextField"caixas de texto flutuantes", para escrevermos nelas 
        codigo = ft.TextField(label="Código do produto", width=300)

        #funcao aonde inviaremos as informações escritas a uma outra funcao
        def enviar(evento):
                #enviamos as informações recebidas para a funcao cadastro_produto
                mensagem = funcoes.procurar(int(codigo.value), page, voltar)
                #adiciona a mensagem recebida na tela/e apos meio segundo retira ela
                men_tela =ft.Text(mensagem)
                page.add(men_tela)
                time.sleep(0.5)
                page.remove(men_tela)

        #parte responsavel por criar os itens que apareceram na tela
        titulo = ft.Container(content=ft.Text("LISTAR TABELAS", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.GREY), alignment=ft.alignment.center, margin=10)
        botao_procurar = ft.ElevatedButton(text="Procurar", on_click=enviar)
        #aqui adicionamos os itens na tela 
        page.add(titulo, botao_voltar, codigo, botao_procurar)

    #funcao que sera chama ao clicar o botao "Listar Tabelas" localizado no menu
    def listar(evento):

        #usa a funcao para salvar as configurações da pagina"spawpoint"
        salvar_estado_atual()

        #cria o titulo da pagina 
        titulo = ft.Container(content=ft.Text("LISTAR TABELAS", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.GREY), alignment=ft.alignment.center, margin=10)

        #cria os botoes/ dentro de cada ao clicar eles sera puxado uma funcao
        tabela_1 = ft.Container(content=ft.ElevatedButton(text="Listar Armazem",  on_click=lambda e: funcoes.listar_armazem(page, voltar)), margin=10, alignment=ft.alignment.center,)
        tabela_2 = ft.Container(content=ft.ElevatedButton(text="Listar kits",  on_click=lambda e: funcoes.listar_kits(page, voltar)), margin=10, alignment=ft.alignment.center,)
        tabela_3 = ft.Container(content=ft.ElevatedButton(text="Listar Vendas",  on_click=lambda e: funcoes.listar_vendas(page, voltar)), margin=10, alignment=ft.alignment.center,)

        #adiciona os itens na tela
        page.add(titulo, tabela_1, tabela_2, tabela_3, botao_voltar)
    
    #funcao que sera chama ao clicar o botao "Sair" localizado no menu
    def sair(evento):
        #fecha a pagina
        page.window_close()

    botao_voltar = ft.Container(content=ft.ElevatedButton(text="Voltar", on_click=voltar), alignment=ft.alignment.bottom_right, margin=10)
    #criação do menu
    page.add(
        ft.Column(
            [
                #cricao do titulo
                ft.Container(
                    content=ft.Text("GERENCIADOR DE ARMAZENTO", size=32, weight=ft.FontWeight.BOLD, color=ft.colors.GREY),
                    alignment=ft.alignment.center,
                    margin=10
                ),
                #criação dos botoes, aonde cada um que voce clica sera direcionado ao uma funcao
                ft.Container(content=ft.ElevatedButton(text="Cadastrar Produto", on_click=cadastro_produto), margin=10, alignment=ft.alignment.center,),
                ft.Container(content=ft.ElevatedButton(text="Cadastrar Kit", on_click=cadastro_kit), margin=10, alignment=ft.alignment.center,),
                ft.Container(content=ft.ElevatedButton(text="Cadastrar Venda", on_click=cadastro_venda), margin=10, alignment=ft.alignment.center,),
                ft.Container(content=ft.ElevatedButton(text="Retirar Produto", on_click=retirar), margin=10, alignment=ft.alignment.center,),
                ft.Container(content=ft.ElevatedButton(text="Pesquisar Produto", on_click=pesquisar), margin=10, alignment=ft.alignment.center,),
                ft.Container(content=ft.ElevatedButton(text="Listar Tabelas", on_click=listar), margin=10, alignment=ft.alignment.center,),
                ft.Container(content=ft.ElevatedButton(text="Sair", on_click=sair), margin=10, alignment=ft.alignment.center,)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

#essa parte inicia o app
ft.app(target=main)



