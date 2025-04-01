import customtkinter
from tkinter import ttk
import tkinter as tk
import sqlite3


# def frame inicial
def abrir_cadastro():
    frame_entrada.grid_forget()
    frame_saida.grid_forget()
    frame_edicao.grid_forget()
    frame_relatorio.grid_forget()
    frame_relatorio_entrada.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_cadastro.grid(row=0, column=1)
    frame_cadastro.grid_propagate(False)

def abrir_edicao():
    frame_entrada.grid_forget()
    frame_saida.grid_forget()
    frame_cadastro.grid_forget()
    frame_relatorio.grid_forget()
    frame_relatorio_entrada.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_edicao.grid(row=0, column=1)
    frame_edicao.grid_propagate(False)
    ler_dados_editar()

def abrir_saida():
    frame_entrada.grid_forget()
    frame_cadastro.grid_forget()
    frame_relatorio.grid_forget()
    frame_edicao.grid_forget()
    frame_relatorio_entrada.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_saida.grid(row=0, column=1)
    frame_saida.grid_propagate(False)
    ler_dados_saida()

def abrir_entrada():
    frame_edicao.grid_forget()
    frame_saida.grid_forget()
    frame_cadastro.grid_forget()
    frame_relatorio.grid_forget()
    frame_relatorio_entrada.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_entrada.grid(row=0, column=1)
    frame_entrada.grid_propagate(False)
    ler_dados_entrada()

def abrir_relatorio():
    frame_edicao.grid_forget()
    frame_saida.grid_forget()
    frame_cadastro.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio_entrada.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_relatorio.grid(row=0, column=1)
    frame_relatorio.grid_propagate(False)
    ler_dados()


# def relatório
def abrir_relatorio_entrada():
    frame_edicao.grid_forget()
    frame_saida.grid_forget()
    frame_cadastro.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_relatorio_entrada.grid(row=0, column=1)
    frame_relatorio_entrada.grid_propagate(False)

def abrir_relatorio_saida():
    frame_edicao.grid_forget()
    frame_saida.grid_forget()
    frame_cadastro.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio.grid_forget()
    frame_relatorio_entrada.grid_forget()
    frame_relatorio_saida.grid(row=0, column=1)
    frame_relatorio_saida.grid_propagate(False)


# Frame Pop-up Exportar
def exportar():
    exportar = customtkinter.CTk()
    exportar.title("window")
    exportar.geometry("450x250")

    Relatorio = customtkinter.CTkLabel(exportar, text="Escolher Relatório(s):", font=("Arial", 15, "bold"))
    Relatorio.grid(pady=10, column=0, sticky="nw", padx=40, row=0)
    Extensao = customtkinter.CTkLabel(exportar, text="Escolher Extensão:", font=("Arial", 15, "bold"))
    Extensao.grid(pady=10, column=1, sticky="ne", padx=40, row=0)

    Exportar_es = customtkinter.CTkCheckBox(exportar, text="Exportar Estoque:")
    Exportar_es.grid(pady=10, column=0, padx=40, row=1, stick="w")
    Exportar_sa = customtkinter.CTkCheckBox(exportar, text="Exportar Saida:")
    Exportar_sa.grid(pady=10, column=0, padx=40, row=2, stick="w")
    Exportar_en = customtkinter.CTkCheckBox(exportar, text="Exportar Entrada:")
    Exportar_en.grid(pady=10, column=0, padx=40, row=3, stick="w")
    Word = customtkinter.CTkCheckBox(exportar, text="Word:")
    Word.grid(pady=10, column=1, padx=40, row=1, stick="w")
    Excel = customtkinter.CTkCheckBox(exportar, text="Excel:")
    Excel.grid(pady=10, column=1, padx=40, row=2, stick="w")
    pdf = customtkinter.CTkCheckBox(exportar, text="PDF:")
    pdf.grid(pady=10, column=1, padx=40, row=3, stick="w")

    botao_cancelar = customtkinter.CTkButton(exportar, text="Cancelar", width=80, height=30)
    botao_cancelar.grid(pady=10, column=1, padx=15, row=4, stick="w")
    botao_salvar = customtkinter.CTkButton(exportar, text="Salvar", width=80, height=30)
    botao_salvar.grid(pady=10, column=1, padx=15, row=4, stick="e")
    exportar.mainloop()


# SQL do cadastro + banco criado
def create_bank():
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("CREATE TABLE IF NOT EXISTS itens (nome text, preco decimal, descricao text)")
    conexao.commit()
    conexao.close()

def salvar_produto():
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(f"INSERT INTO itens (nome, preco, descricao) VALUES ('{entrada_nome_cadastro.get()}', '{(entrada_preco_cadastro.get())}', '{caixa_texto_cadastro.get('1.0', 'end')}')")
    conexao.commit()
    conexao.close()

def ler_dados():
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("SELECT * FROM itens")
    recebe_dados = terminal_sql.fetchall()
    print(recebe_dados)

    for item in estoque_tree_relatorio.winfo_children():
        estoque_tree_relatorio.delete(item)

    for j in recebe_dados:
        nome = str(j[0])
        quantidade = 0
        preco = (j[1])
        descricao = str(j[2])
        estoque_tree_relatorio.insert('', tk.END, values=(nome, quantidade, preco, descricao))
    conexao.commit()
    conexao.close()


# SQL frame editar
def ler_dados_editar():
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("SELECT nome FROM itens")
    items_editar = terminal_sql.fetchall()
    print(items_editar)

    for item in scrollable_frame_edicao.winfo_children():
        item.destroy()

    for item in items_editar:
        box_editar = customtkinter.CTkCheckBox(scrollable_frame_edicao, text=item, border_width=2)
        box_editar.grid(pady=5, padx=10)
        box_editar.configure(
            command=lambda nome=item[0], cb=box_editar: (selecionar_item(nome) if cb.get() == 1 else desmarcar_item_editar()))

        def selecionar_item(arg_item):
            conexao = sqlite3.connect("dados.db")
            terminal_sql = conexao.cursor()
            terminal_sql.execute(f"SELECT * FROM itens WHERE nome ='{arg_item}'")
            receber_dados_produto = terminal_sql.fetchall()
            print(receber_dados_produto)

            entrada_nome_edicao.insert(0, receber_dados_produto[0][0])
            entrada_preco_edicao.insert(0, receber_dados_produto[0][1])
            caixa_texto_edicao.insert(0.0, receber_dados_produto[0][2])

        def desmarcar_item_editar():
            entrada_nome_edicao.delete(0, "end")
            entrada_preco_edicao.delete(0, "end")
            caixa_texto_edicao.delete(0.0, "end")

# SQL frame saida
def ler_dados_saida():
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("SELECT nome FROM itens")
    items_saida = terminal_sql.fetchall()
    print(items_saida)

    for item in scrollable_frame_saida.winfo_children():
        item.destroy()

    for item in items_saida:
        box_saida = customtkinter.CTkCheckBox(scrollable_frame_saida, text=item, border_width=2)
        box_saida.grid(pady=5, padx=10, sticky="nw")
        box_saida.configure(
            command=lambda nome=item[0], cb=box_saida: (selecionar_item(nome) if cb.get() == 1 else desmarcar_item_saida()))

        def selecionar_item(arg_item):
                    conexao = sqlite3.connect("dados.db")
                    terminal_sql = conexao.cursor()
                    terminal_sql.execute(f"SELECT * FROM itens WHERE nome ='{arg_item}'")
                    receber_dados_produto = terminal_sql.fetchall()
                    print(receber_dados_produto)

                    entrada_nome_saida.insert(0, receber_dados_produto[0][0])

        def desmarcar_item_saida():
            entrada_nome_saida.delete(0, "end")

# SQL frame entrada
def ler_dados_entrada():
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("SELECT nome FROM itens")
    items_entrada = terminal_sql.fetchall()
    print(items_entrada)

    for item in scrollable_frame_entrada.winfo_children():
        item.destroy()

    for item in items_entrada:
        box_entrada = customtkinter.CTkCheckBox(scrollable_frame_entrada, text=item, border_width=2)
        box_entrada.grid(pady=5, padx=10, sticky="se")
        box_entrada.configure(command=lambda  nome=item[0],cb=box_entrada:(selecionar_item(nome)if cb.get() == 1 else desmarcar_item_entrada()))

        def selecionar_item(arg_item):
                conexao = sqlite3.connect("dados.db")
                terminal_sql = conexao.cursor()
                terminal_sql.execute(f"SELECT * FROM itens WHERE nome ='{arg_item}'")
                receber_dados_produto = terminal_sql.fetchall()
                print(receber_dados_produto)

                entrada_nome_entrada.insert(0, receber_dados_produto[0][0])

        def desmarcar_item_entrada():
            entrada_nome_entrada.delete(0, "end")

# funcionalidades editar - excluir, cancelar e salvar
def deletar_produto_entrada(nome_produto):
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(f"DELETE FROM itens WHERE nome = '{nome_produto}'")
    conexao.commit()
    conexao.close()
    entrada_nome_edicao.delete(0, "end")
    entrada_preco_edicao.delete(0, "end")
    caixa_texto_edicao.delete(0.0, "end")
    ler_dados()

def editar_produto(nome_produto_edicao, preco_produto_edicao, descricao_produto_edicao):
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(f"UPDATE itens SET nome = '{nome_produto_edicao}', preco = '{preco_produto_edicao}', descricao = '{descricao_produto_edicao}' ")
    conexao.commit()
    conexao.close()
    entrada_nome_edicao.delete(0, "end")
    entrada_preco_edicao.delete(0, "end")
    caixa_texto_edicao.delete(0.0, "end")
    ler_dados()


create_bank()

janela = customtkinter.CTk()
janela.geometry("800x600")
customtkinter.set_appearance_mode("dark")

# Mudança de cor da COLUNA - Frame Relatorio
style = ttk.Style(master=janela)
style.theme_use('clam')
style.configure("Treeview", background="#3484F0", fieldbackground="#393939", foreground="white", rowheight=25,
                bordercolor="white")
style.configure("Treeview.Heading", background="#565b5e", foreground="white", relief="flat")
style.map("Treeview.Heading", background=[('active', '#323232')])

# Frame Menu
frame_menu = customtkinter.CTkFrame(janela, width=190, height=400, corner_radius=0, fg_color="black")
frame_menu.grid(row=0, column=0, padx=10, pady=10)
frame_menu.pack_propagate(False)

frame_cadastro = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=0, fg_color="black")
frame_cadastro.grid(row=0, column=6, padx=10, pady=10)
frame_cadastro.grid_propagate(False)

# Widgets Frame Menu
label_menu = customtkinter.CTkLabel(frame_menu, text="Exemplo 01", font=("Arial", 20, "bold"), text_color="dark gray")
label_menu.pack(pady=50)
cadastro = customtkinter.CTkButton(frame_menu, corner_radius=5, text="Cadastrar", command=abrir_cadastro)
cadastro.pack(pady=5)
edicao = customtkinter.CTkButton(frame_menu, corner_radius=5, text="Editar", command=abrir_edicao)
edicao.pack(pady=5)
saida = customtkinter.CTkButton(frame_menu, corner_radius=5, text="Saída", command=abrir_saida)
saida.pack(pady=5)
entrada = customtkinter.CTkButton(frame_menu, corner_radius=5, text="Entrada", command=abrir_entrada)
entrada.pack(pady=5)
relatorio = customtkinter.CTkButton(frame_menu, corner_radius=5, text="Relatório", command=abrir_relatorio)
relatorio.pack(pady=5)

# Widgets Frame Cadastro
label_cadastro = customtkinter.CTkLabel(frame_cadastro, text="Cadastro", font=("Arial", 20, "bold"),
                                        text_color="dark gray")
label_cadastro.grid(padx=32, row=0, column=1, pady=25, sticky="w")
label_nome = customtkinter.CTkLabel(frame_cadastro, text="Nome do Produto:")
label_nome.grid(row=2, column=0, padx=40, pady=5, sticky="e")
label_preco = customtkinter.CTkLabel(frame_cadastro, text="Preço(R$):")
label_preco.grid(row=3, column=0, padx=40, pady=5, sticky="e")
label_descricao = customtkinter.CTkLabel(frame_cadastro, text="Descrição:")
label_descricao.grid(row=4, column=0, padx=40, pady=5, sticky="ne")

entrada_nome_cadastro = customtkinter.CTkEntry(frame_cadastro, placeholder_text="Digite o nome do produto:", width=300)
entrada_nome_cadastro.grid(pady=5, row=2, column=1, sticky="w")
entrada_preco_cadastro = customtkinter.CTkEntry(frame_cadastro, placeholder_text="0,00:", width=60)
entrada_preco_cadastro.grid(pady=5, row=3, column=1, sticky="w")

caixa_texto_cadastro = customtkinter.CTkTextbox(frame_cadastro, width=300, height=80, corner_radius=0)
caixa_texto_cadastro.grid(pady=12, row=4, column=1)
caixa_texto_cadastro.grid_propagate(False)

botao_salvar_cadastro = customtkinter.CTkButton(frame_cadastro, corner_radius=5, text="Salvar", width=90,
                                                command=salvar_produto)
botao_salvar_cadastro.grid(pady=3, padx=5, row=5, column=1, sticky="e")

# Widgets Frame Edicao
frame_edicao = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=0, fg_color="black")
frame_edicao.grid_propagate(False)

label_editar = customtkinter.CTkLabel(frame_edicao, text="Editar Produto", font=("Arial", 20, "bold"),
                                      text_color="dark gray")
label_editar.grid(padx=60, pady=25, row=0, column=1, sticky="n")
entrada_busca_edicao = customtkinter.CTkEntry(frame_edicao, placeholder_text="Buscar produto:", width=230)
entrada_busca_edicao.grid(padx=20, pady=5, row=2, column=0, sticky="w")

# Box1 frame edicao
scrollable_frame_edicao = customtkinter.CTkScrollableFrame(frame_edicao, width=200)
scrollable_frame_edicao.grid(row=3, column=0, pady=20, padx=20, sticky="we", rowspan=4)

entrada_nome_edicao = customtkinter.CTkEntry(frame_edicao, placeholder_text="Nome do produto:")
entrada_nome_edicao.grid(pady=5, row=2, column=1, sticky="we")
entrada_preco_edicao = customtkinter.CTkEntry(frame_edicao, placeholder_text="0,00:", width=20)
entrada_preco_edicao.grid(pady=5, row=3, column=1, sticky="we")

caixa_texto_edicao = customtkinter.CTkTextbox(frame_edicao, width=300, height=95, corner_radius=0)
caixa_texto_edicao.grid(pady=5, row=4, column=1)
caixa_texto_edicao.grid_propagate(False)

botao_salvar_edicao = customtkinter.CTkButton(frame_edicao, corner_radius=5, text="Salvar", width=80)
botao_salvar_edicao.grid(padx=3, row=5, column=1, sticky="e")
botao_excluir_edicao = customtkinter.CTkButton(frame_edicao, corner_radius=5, text="Excluir", width=80, fg_color="red", command=lambda : deletar_produto_entrada(entrada_nome_edicao.get()))
botao_excluir_edicao.grid(padx=3, row=5, column=1, sticky="w")
botao_cancelar_edicao = customtkinter.CTkButton(frame_edicao, corner_radius=5, text="Cancelar", width=80, command=lambda : editar_produto(entrada_nome_edicao.get(), entrada_preco_edicao.get(), caixa_texto_edicao.get()))
botao_cancelar_edicao.grid(padx=3, row=5, column=1)

# Widgets Frame Saida
frame_saida = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=0, fg_color="black")
frame_saida.grid_propagate(False)

label_saida = customtkinter.CTkLabel(frame_saida, text="Saída", font=("Arial", 20, "bold"), text_color="dark gray")
label_saida.grid(padx=70, pady=10, row=0, column=1, sticky="w")
entrada_busca_saida = customtkinter.CTkEntry(frame_saida, placeholder_text="Campo de Busca:", width=230)
entrada_busca_saida.grid(padx=20, pady=5, row=1, column=0)

# Box1 frame saida
scrollable_frame_saida = customtkinter.CTkScrollableFrame(frame_saida, width=200)
scrollable_frame_saida.grid(row=1, column=0, pady=20, padx=20, sticky="we", rowspan=4)

entrada_nome_saida = customtkinter.CTkEntry(frame_saida, width=230, placeholder_text="Nome e qtd no estoque:")
entrada_nome_saida.grid(pady=5, row=1, column=1, sticky="we")
entrada_qtd_saida = customtkinter.CTkEntry(frame_saida, width=130, placeholder_text="Quantidade:")
entrada_qtd_saida.grid(pady=2, padx=2, row=2, column=1, sticky="w")
botao_add_saida = customtkinter.CTkButton(frame_saida, corner_radius=5, text="Add pdt", width=100)
botao_add_saida.grid(pady=2, padx=2, row=2, column=1, sticky="e")

# Box2 frame saida
scrollable_frame_saida1 = customtkinter.CTkScrollableFrame(frame_saida, width=230, height=200)
scrollable_frame_saida1.grid(row=3, column=1, pady=5, padx=20, sticky="w", rowspan=2)
items_saida1 = ["Produto 1", "Produto 2", "Produto 3", "Produto 4", "Produto 5", "Produto 6", "Produto 7", "Produto 8"]
for item in items_saida1:
    box = customtkinter.CTkCheckBox(scrollable_frame_saida1, text=item)
    box.pack(pady=5, padx=10)

botao_salvar_saida = customtkinter.CTkButton(frame_saida, corner_radius=5, text="Salvar", width=90)
botao_salvar_saida.grid(pady=4, padx=6, row=5, rowspan=2, column=1, sticky="e")
botao_cancelar_saida = customtkinter.CTkButton(frame_saida, fg_color="red", corner_radius=5, text="Cancelar", width=90)
botao_cancelar_saida.grid(pady=4, padx=6, row=5, rowspan=2, column=1, sticky="w")

# Widgets Frame Entrada
frame_entrada = customtkinter.CTkFrame(janela, width=590, height=400, corner_radius=20, fg_color="black")
frame_entrada.grid_propagate(False)

label_entrada = customtkinter.CTkLabel(frame_entrada, text="Entrada", font=("Arial", 20, "bold"),
                                       text_color="dark gray")
label_entrada.grid(padx=100, pady=10, row=0, column=0, sticky="w")
entrada_busca_entrada = customtkinter.CTkEntry(frame_entrada, placeholder_text="Campo de Busca:", width=230)
entrada_busca_entrada.grid(padx=20, pady=5, row=1, column=0)

# box1 frame entrada
scrollable_frame_entrada = customtkinter.CTkScrollableFrame(frame_entrada, width=200)
scrollable_frame_entrada.grid(row=2, column=0, pady=20, padx=20, sticky="we", rowspan=4)

entrada_nome_entrada = customtkinter.CTkEntry(frame_entrada, width=230, placeholder_text="Nome e qtd no estoque:")
entrada_nome_entrada.grid(pady=2, row=1, column=1, sticky="we")
entrada_qtd_entrada = customtkinter.CTkEntry(frame_entrada, width=130, placeholder_text="Qtd tirada:")
entrada_qtd_entrada.grid(pady=2, padx=2, row=2, column=1, sticky="w")
botao_add_entrada = customtkinter.CTkButton(frame_entrada, corner_radius=5, text="Add ítem", width=100)
botao_add_entrada.grid(pady=2, padx=2, row=2, column=1, sticky="e")

# box2 frame entrada
scrollable_frame_entrada1 = customtkinter.CTkScrollableFrame(frame_entrada, width=230)
scrollable_frame_entrada1.grid(row=3, column=1, pady=10, padx=20, sticky="we", rowspan=3)
items_entrada1 = []
for item in items_entrada1:
    box = customtkinter.CTkCheckBox(scrollable_frame_entrada1, text=item)
    box.pack(pady=5, padx=10)

botao_salvar_entrada = customtkinter.CTkButton(frame_entrada, corner_radius=5, text="Salvar", width=90)
botao_salvar_entrada.grid(pady=4, padx=6, row=6, column=1, sticky="e")
botao_cancelar_entrada = customtkinter.CTkButton(frame_entrada, fg_color="red", corner_radius=5, text="Cancelar",
                                                 width=90)
botao_cancelar_entrada.grid(pady=4, padx=6, row=6, column=1, sticky="w")

# Widgets Frame Relatório
frame_relatorio = customtkinter.CTkFrame(janela, width=590, height=400, fg_color="black")
frame_relatorio.grid_propagate(False)

label_relatorio = customtkinter.CTkLabel(frame_relatorio, text="Estoque", font=("Arial", 20, "bold"),
                                         text_color="dark gray")
label_relatorio.grid(pady=10, row=0, column=0, columnspan=3)
entrada_busca_relatorio = customtkinter.CTkEntry(frame_relatorio, placeholder_text="Barra de pesquisa:", width=250)
entrada_busca_relatorio.grid(padx=40, pady=5, row=1, column=0, sticky="w")
botao_exportar_relatorio = customtkinter.CTkButton(frame_relatorio, corner_radius=5, text="Exportar", width=90,
                                                   command=exportar)
botao_exportar_relatorio.grid(pady=10, padx=40, row=1, column=0, sticky="e")

# Colunas Relatorio
columns_relatorio = ("nome", "quantidade", "preço", "descrição")
estoque_tree_relatorio = ttk.Treeview(frame_relatorio, columns=columns_relatorio, show='headings', height=8)
estoque_tree_relatorio.grid(row=2, column=0, padx=30, pady=10, sticky="w")

estoque_tree_relatorio.heading("nome", text="nome")
estoque_tree_relatorio.heading("quantidade", text="quantidade")
estoque_tree_relatorio.heading("preço", text="preço")
estoque_tree_relatorio.heading("descrição", text="descrição")
estoque_tree_relatorio.column("nome", width=128, anchor="center")
estoque_tree_relatorio.column("quantidade", width=127, anchor="center")
estoque_tree_relatorio.column("preço", width=127, anchor="center")
estoque_tree_relatorio.column("descrição", width=128, anchor="center")

botao_estoque_relatorio = customtkinter.CTkButton(frame_relatorio, corner_radius=5, text="Estoque", width=90,
                                                  command=abrir_relatorio)
botao_estoque_relatorio.grid(pady=5, padx=40, row=3, column=0, sticky="w")
botao_entrada_relatorio = customtkinter.CTkButton(frame_relatorio, corner_radius=5, text="Entrada", width=90,
                                                  command=abrir_relatorio_entrada)
botao_entrada_relatorio.grid(pady=5, padx=40, row=3, column=0, )
botao_saida_relatorio = customtkinter.CTkButton(frame_relatorio, corner_radius=5, text="Saída", width=90,
                                                command=abrir_relatorio_saida)
botao_saida_relatorio.grid(pady=5, padx=40, row=3, column=0, sticky="e")

# Frame Relatório Entrada
frame_relatorio_entrada = customtkinter.CTkFrame(janela, width=590, height=400, fg_color="black")
frame_relatorio_entrada.grid_propagate(False)

label_relatorio_entrada = customtkinter.CTkLabel(frame_relatorio_entrada, text="Entrada", font=("Arial", 20, "bold"),
                                                 text_color="dark gray")
label_relatorio_entrada.grid(pady=10, row=0, column=0, columnspan=3)
entrada_pesquisa_re = customtkinter.CTkEntry(frame_relatorio_entrada, placeholder_text="Barra de pesquisa", width=250)
entrada_pesquisa_re.grid(padx=40, pady=5, row=1, column=0, sticky="w")
botao_exportar_re = customtkinter.CTkButton(frame_relatorio_entrada, corner_radius=5, text="Exportar", width=90,
                                            command=exportar)
botao_exportar_re.grid(pady=10, padx=40, row=1, column=0, sticky="e")

# Colunas Relatorio Entrada
columns_relatorio_entrada = ("nome", "quantidade", "data/hora")
estoque_tree_relatorio_entrada = ttk.Treeview(frame_relatorio_entrada, columns=columns_relatorio_entrada,
                                              show='headings', height=8)
estoque_tree_relatorio_entrada.grid(row=2, column=0, padx=30, pady=10, sticky="w")

estoque_tree_relatorio_entrada.heading("nome", text="nome")
estoque_tree_relatorio_entrada.heading("quantidade", text="quantidade")
estoque_tree_relatorio_entrada.heading("data/hora", text="data/hora")
estoque_tree_relatorio_entrada.column("nome", width=170)
estoque_tree_relatorio_entrada.column("quantidade", width=170)
estoque_tree_relatorio_entrada.column("data/hora", width=170)

botao_estoque_re = customtkinter.CTkButton(frame_relatorio_entrada, corner_radius=5, text="Estoque", width=90,
                                           command=abrir_relatorio)
botao_estoque_re.grid(pady=5, padx=40, row=3, column=0, sticky="w")
botao_entrada_re = customtkinter.CTkButton(frame_relatorio_entrada, corner_radius=5, text="Entrada", width=90,
                                           command=abrir_relatorio_entrada)
botao_entrada_re.grid(pady=5, padx=4, row=3, column=0)
botao_saida_re = customtkinter.CTkButton(frame_relatorio_entrada, corner_radius=5, text="Saída", width=90,
                                         command=abrir_relatorio_saida)
botao_saida_re.grid(pady=5, row=3, column=0, padx=40, sticky="e")

# Frame Relatório Saída
frame_relatorio_saida = customtkinter.CTkFrame(janela, width=590, height=400, fg_color="black")
frame_relatorio_saida.grid_propagate(False)

label_relatorio_saida = customtkinter.CTkLabel(frame_relatorio_saida, text="Saída", font=("Arial", 20, "bold"),
                                               text_color="dark gray")
label_relatorio_saida.grid(pady=10, row=0, column=0, columnspan=3)
entrada_pesquisa_rs = customtkinter.CTkEntry(frame_relatorio_saida, placeholder_text="Barra de pesquisa", width=250)
entrada_pesquisa_rs.grid(padx=40, pady=5, row=1, column=0, sticky="w")
botao_exportar_rs = customtkinter.CTkButton(frame_relatorio_saida, corner_radius=5, text="Exportar", width=90,
                                            command=exportar)
botao_exportar_rs.grid(pady=10, padx=40, row=1, column=0, sticky="e")

# Colunas Relatorio Saída
columns_relatorio_saida = ("nome", "quantidade", "data/hora")
estoque_tree_relatorio_saida = ttk.Treeview(frame_relatorio_saida, columns=columns_relatorio_saida, show='headings',
                                            height=8)
estoque_tree_relatorio_saida.grid(row=2, column=0, padx=30, pady=10, sticky="w")

estoque_tree_relatorio_saida.heading("nome", text="nome")
estoque_tree_relatorio_saida.heading("quantidade", text="quantidade")
estoque_tree_relatorio_saida.heading("data/hora", text="data/hora")
estoque_tree_relatorio_saida.column("nome", width=170)
estoque_tree_relatorio_saida.column("quantidade", width=170)
estoque_tree_relatorio_saida.column("data/hora", width=170)

botao_estoque_rs = customtkinter.CTkButton(frame_relatorio_saida, corner_radius=5, text="Estoque", width=9,
                                           command=abrir_relatorio)
botao_estoque_rs.grid(pady=5, padx=40, row=3, column=0, sticky="w")
botao_entrada_rs = customtkinter.CTkButton(frame_relatorio_saida, corner_radius=5, text="Entrada", width=90,
                                           command=abrir_relatorio_entrada)
botao_entrada_rs.grid(pady=5, padx=4, row=3, column=0)
botao_saida_rs = customtkinter.CTkButton(frame_relatorio_saida, corner_radius=5, text="Saída", width=90,
                                         command=abrir_relatorio_saida)
botao_saida_rs.grid(pady=5, row=3, column=0, padx=40, sticky="e")

janela.mainloop()
