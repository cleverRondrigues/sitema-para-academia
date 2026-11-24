import customtkinter as ctk
from index import cadastrar_aluno as salvar_aluno
from index import listar_alunos, consultar_aluno as buscar_aluno

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("500x400")
app.title("sistema da academia")

def limpar_tela():

    for widget in app.winfo_children(): 
        widget.destroy()

def menu():
    #menu label
    ctk.CTkLabel(app, text="Bem-vindo ao sistema da academia!", font=("Arial", 16)).pack(pady=20)
    #menu buttons
    ctk.CTkButton(app, text="Cadastrar Aluno", command=lambda: cadastrar_aluno()).pack(pady=10)

    ctk.CTkButton(app, text="Lista de Alunos", command=lambda: lista_alunos()).pack(pady=10)

    ctk.CTkButton(app, text="Consultar Aluno", command=lambda: consultar_aluno()).pack(pady=10)

    ctk.CTkButton(app, text="Sair", command=app.quit).pack(pady=10)


def cadastrar_aluno():
    limpar_tela()

    # cadastrar aluno label
    ctk.CTkLabel(app, text="Cadastrar Aluno", font=("Arial", 16)).pack(pady=20)

    # cadastrar aluno inputs
    campo_nome = ctk.CTkEntry(app, placeholder_text="Nome")
    campo_nome.pack(pady=10)

    campo_idade = ctk.CTkEntry(app, placeholder_text="Idade")
    campo_idade.pack(pady=10)

    campo_peso = ctk.CTkEntry(app, placeholder_text="Peso")
    campo_peso.pack(pady=10)

    campo_altura = ctk.CTkEntry(app, placeholder_text="Altura em cm")
    campo_altura.pack(pady=10)

    # função para enviar os dados
    def enviar_cadastro():

        nome = campo_nome.get().strip()
        idade = int(campo_idade.get())
        peso = float(campo_peso.get().replace(",", ""))
        altura = float(campo_altura.get().replace(",", "")) / 100

        salvar_aluno(nome, idade, peso, altura)

        print("Aluno cadastrado com sucesso!")

    # cadastrar aluno button
    ctk.CTkButton(app, text="Cadastrar", command=enviar_cadastro).pack(pady=10)

    ctk.CTkButton(app, text="Voltar", command=lambda: limpar_tela() or menu()).pack(pady=10)


def lista_alunos():
    limpar_tela()

    # lista alunos label
    ctk.CTkLabel(app, text="Lista de Alunos", font=("Arial", 16)).pack(pady=20)

    # buscar alunos no banco
    alunos = listar_alunos()

    # mostrar quantidade
    ctk.CTkLabel(
        app,
        text=f"Total de alunos: {len(alunos)}"
    ).pack(pady=10)

    # mostrar informações dos alunos
    for aluno in alunos:

        id, nome, idade, peso, altura, imc = aluno

        ctk.CTkLabel(
            app,
            text=f"ID: {id} | {nome} | {idade} anos\n"
                 f"Peso: {peso} kg | Altura: {altura} m | IMC: {imc}"
        ).pack(pady=5)

    # lista alunos button
    ctk.CTkButton(app, text="Voltar", command=lambda: limpar_tela() or menu()).pack(pady=10)


def consultar_aluno():
    limpar_tela()

    # consultar aluno label
    ctk.CTkLabel(app, text="Consultar Aluno", font=("Arial", 16)).pack(pady=20)

    # consultar aluno inputs
    campo_nome = ctk.CTkEntry(app, placeholder_text="Nome")
    campo_nome.pack(pady=10)

    # área dos resultados
    resultados = ctk.CTkFrame(app)
    resultados.pack(pady=10, fill="both", expand=True)

    def pesquisar():

        for widget in resultados.winfo_children():
            widget.destroy()

        nome = campo_nome.get().strip()

        alunos = buscar_aluno(nome)

        if not alunos:
            ctk.CTkLabel(
                resultados,
                text="Nenhum aluno encontrado."
            ).pack(pady=10)
            return

        for aluno in alunos:

            id, nome, idade, peso, altura, imc = aluno

            ctk.CTkLabel(
                resultados,
                text=f"ID: {id} | {nome} | {idade} anos\n"
                     f"Peso: {peso} kg | Altura: {altura} m | IMC: {imc}"
            ).pack(pady=5)

    # consultar aluno button
    ctk.CTkButton(app, text="Consultar", command=pesquisar).pack(pady=10)

    ctk.CTkButton(app, text="Voltar", command=lambda: limpar_tela() or menu()).pack(pady=10)

menu()

app.mainloop()