import pandas as pd
import flet as ft

tabela_armazem = pd.read_excel("armazem.xlsx")
tabela_kit = pd.read_excel("kit.xlsx")
tabela_vendas = pd.read_excel("Saida dos produtos.xlsx")

#funcao que lista a tabela armazem
def listar_armazem(page, voltar_func):
    global tabela_armazem
    # Limpa a página
    page.clean()
    # Cria as colunas da tabela
    columns = [ft.DataColumn(ft.Text(col)) for col in tabela_armazem.columns]
    # Cria as linhas da tabela
    rows = [ft.DataRow(cells=[ft.DataCell(ft.Text(str(tabela_armazem[col].iloc[i]))) for col in tabela_armazem.columns])
            for i in range(len(tabela_armazem))]
    # Cria a tabela de dados
    data_table = ft.DataTable(columns=columns, rows=rows, border=ft.border.all(1))
    # Adiciona rolagem à tabela usando um contêiner Column
    scrollable_table = ft.Column([data_table], scroll=ft.ScrollMode.ALWAYS, height=300)
    # Cria o botão "Voltar"
    botao_voltar = ft.Container(content=ft.ElevatedButton(text="Voltar", on_click=voltar_func), alignment=ft.alignment.bottom_right, margin=10)
    #Texto que aparece o valor total em estoque
    texto_total = ft.Container(
    content=ft.ElevatedButton(f"Total: R${round(tabela_armazem['valor'].sum(), 2)}"))
    # Adiciona a tabela rolável e o botão "Voltar" na página
    page.add(scrollable_table, botao_voltar, texto_total)
    
#funcao que lista a tabela kit
def listar_kits(page, voltar_func):
    global tabela_armazem
    # Limpa a página
    page.clean()
    # Cria as colunas da tabela
    columns = [ft.DataColumn(ft.Text(col)) for col in tabela_kit.columns]
    # Cria as linhas da tabela
    rows = [ft.DataRow(cells=[ft.DataCell(ft.Text(str(tabela_kit[col].iloc[i]))) for col in tabela_kit.columns]
                       ) for i in range(len(tabela_kit))]
     # Cria a tabela de dados
    data_table = ft.DataTable(columns=columns,rows=rows,border=ft.border.all(1),)
    # Adiciona rolagem à tabela usando um contêiner Column
    scrollable_table = ft.Column([data_table], scroll=ft.ScrollMode.ALWAYS, height=300)
    # Cria o botão "Voltar"
    botao_voltar = ft.Container(content=ft.ElevatedButton(text="Voltar", on_click=voltar_func), alignment=ft.alignment.bottom_right, margin=10 )
    # Adiciona a tabela rolável e o botão "Voltar" na página
    page.add(scrollable_table, botao_voltar)
    
#funcao que lista a tabela vendas
def listar_vendas(page, voltar_func):
    global tabela_vendas

    # Limpa a página
    page.clean()

    # Cria as colunas da tabela
    columns = [ft.DataColumn(ft.Text(col)) for col in tabela_vendas.columns]

     # Cria as linhas da tabela
    rows = [ft.DataRow(cells=[ft.DataCell(ft.Text(str(tabela_vendas[col].iloc[i]))) for col in tabela_vendas.columns]
                       ) for i in range(len(tabela_vendas))]
    
    # Cria a tabela de dados
    data_table = ft.DataTable(columns=columns,rows=rows,border=ft.border.all(1),)

    # Adiciona rolagem à tabela usando um contêiner Column
    scrollable_table = ft.Column([data_table], scroll=ft.ScrollMode.ALWAYS, height=300)

    # Cria o botão "Voltar"
    botao_voltar = ft.Container(content=ft.ElevatedButton(text="Voltar", on_click=voltar_func), alignment=ft.alignment.bottom_right, margin=10)

    # Adiciona a tabela rolável e o botão "Voltar" na página
    page.add(scrollable_table, botao_voltar)
    
#funcao que cadastra o produto
def cadastro_produto(codigo, nome, quantidade, valor):
    global tabela_armazem

    #cria um df inserir e insere as informações recebidas
    inserir = pd.DataFrame({
        "codigo": [codigo],
        "nome": [nome],
        "quantidade": [quantidade],
        "valor": [valor * quantidade]
    })

    #faz uma verificação se ja existe esse item na tebal, caso tenha ele salva em cima desse item 
    #verifica se o codigo recebido ja tem na tabel
    if inserir["codigo"].values[0] in tabela_armazem['codigo'].values:

        #verifica a linha que se localiza esse item
        indice = tabela_armazem[tabela_armazem['codigo'] == inserir["codigo"].values[0]].index[0]
        #soma com a quantidade e o valor atual
        tabela_armazem.loc[indice, 'quantidade'] += inserir["quantidade"].values[0]
        tabela_armazem.loc[indice, 'valor'] += inserir.loc[0, 'valor']
    else:
        #caso não tenha ele apenas concatena com as ultimas informações
        tabela_armazem = pd.concat([tabela_armazem, inserir], ignore_index=True)

    try:
        #tenta salvar, caso ele sava retorna uma mensagem
        tabela_armazem.to_excel('armazem.xlsx', index=False)
        return "Cadastro realizado com sucesso!"
    except Exception as e:
        #caso não tenha, ele retorna uma mensagem com o erro
        return f"Erro ao salvar: {e}"

#funcao que cadastra o kit
def cadastro_kit(codigo, nome, produto, valor):
    global tabela_kit

    # Criação do DataFrame com os dados do novo kit
    inserir = pd.DataFrame({
        "codigo": [codigo],
        "kit": [nome],
        "produto": [produto],
        "valor": [valor]
    })

    # Concatena com a tabela existente
    tabela_kit = pd.concat([tabela_kit, inserir], ignore_index=True)

    try:
        # Salvar a tabela atualizada em um arquivo Excel, e retorna uma mensagem
        tabela_kit.to_excel('kit.xlsx', index=False)
        return "Cadastro realizado com sucesso!"
    except Exception as e:
        #caso de erro, retorna o erro
        return f"Erro ao salvar: {e}"

#Funcao que cadastra as vendas
def cadastro_vendas(nome, quantidade, valor, nome_cliente):
    global tabela_armazem, tabela_vendas

    from datetime import datetime
    #inserção das informaões dentro do df
    inserir = pd.DataFrame({"nome": [nome],
                            "quantidade": [quantidade],
                            "valor": [valor*quantidade],
                            "nome_cliente": [nome_cliente],
                            "data": [datetime.now().strftime('%d/%m/%Y')]})   
    
    #concatenar com as ultimas informações
    tabela_vendas = pd.concat([tabela_vendas, inserir], ignore_index=True) 

    #procura a a linha que se localiza o produto na tebela armazem
    indice = tabela_armazem[tabela_armazem['nome'] == inserir.loc[0,'nome']].index[0]

    #Atualize a quantidade e o valor no DataFrame tabelaArmazem
    retirar = tabela_armazem.loc[indice, 'valor'].astype(float)
    retirar -= inserir.loc[0, 'valor'].astype(float)
    tabela_armazem.loc[indice, 'valor'] = retirar.astype(float)
    tabela_armazem.loc[indice, 'quantidade'] -= inserir.loc[0, 'quantidade'].astype(float)

    #verificação de salvamento
    try:
        # Salvar a tabela atualizada em um arquivo Excel, e retorna uma mensagem
        tabela_vendas.to_excel('Saida dos produtos.xlsx', index=False)
        tabela_armazem.to_excel('armazem.xlsx', index=False)
        return "Cadastro realizado com sucesso!"
    except Exception as e:
        #retorna uma mensagem de erro, que retorna o erro
        return f"Erro ao salvar: {e}"

#funcao que retira itens da tabela armazen
def eliminar(codigo):
    global tabela_armazem

    #verifica se o codigo esta no df
    if codigo in tabela_armazem['codigo'].values:
        #procura a posição desse valor dentro
        indice = tabela_armazem[tabela_armazem['codigo'] == codigo].index[0]
        #retira o item do dataframe
        tabela_armazem = tabela_armazem.drop(indice)

        #verificação de salvamento no excel
        try:
            #salva e retorna uma mensagem
            tabela_armazem.to_excel('armazem.xlsx', index=False)
            return "Produto retirado"
        except Exception as e:
            #retorna uma mensagem de erro, que retorna o erro
            return f"Erro ao salvar: {e}"

    #caso não exista, retorna essa mensagem         
    else:
        return "Produto não existente"
    
#funcao que procura itens dentro da tabela armazen
def procurar(codigo, page, voltar_func):
    global tabela_armazem

    # Busca o item dentro da coluna codigo do df
    if codigo in tabela_armazem['codigo'].values:
        # Localiza a posição do item
        indice = tabela_armazem[tabela_armazem['codigo'] == codigo].index[0]
        
        # Obtém os dados do item encontrado
        item = tabela_armazem.loc[indice]

        # Cria a tabela para exibir o item encontrado
        columns = [
            ft.DataColumn(ft.Text('codigo')),
            ft.DataColumn(ft.Text('nome')),
            ft.DataColumn(ft.Text('quantidade')),
            ft.DataColumn(ft.Text('valor'))
        ]

        rows = [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(item['codigo']))),
                    ft.DataCell(ft.Text(item['nome'])),
                    ft.DataCell(ft.Text(str(item['quantidade']))),
                    ft.DataCell(ft.Text(str(item['valor'])))
                ]
            )
        ]

        # Limpa a página e adiciona a nova tabela e botão de voltar
        page.controls.clear()
        botao_voltar = ft.Container(content=ft.ElevatedButton(text="Voltar", on_click=voltar_func), alignment=ft.alignment.bottom_right, margin=10)
        page.add(ft.DataTable(columns=columns, rows=rows), botao_voltar)

    else:
        return "Produto não existe"
        
        