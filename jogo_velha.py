
import random
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# --- CORES ---
CO_BRANCO = "#FFFFFF"
CO_ESCURO = "#333333"
CO_LARANJA = "#fcc058"
CO_AZUL = "#3297a8"
CO_FUNDO = "#3b3b3b"

# --- JANELA PRINCIPAL ---
janela = tk.Tk()
janela.title("Jo-Ken-Pô")
janela.geometry("260x280")
janela.configure(bg=CO_FUNDO)
janela.resizable(False, False)

estilo = ttk.Style(janela)
estilo.theme_use("clam")

# --- VARIÁVEIS DE PLACAR ---
pontos_voce = 0
pontos_pc = 0

# --- FRAMES ---
frame_cima = tk.Frame(janela, width=260, height=100, bg=CO_ESCURO, relief="raised")
frame_cima.grid(row=0, column=0, sticky="NW")

frame_baixo = tk.Frame(janela, width=260, height=180, bg=CO_FUNDO, relief="flat")
frame_baixo.grid(row=1, column=0, sticky="NW")

# --- PLACAR E RÓTULOS (FRAME CIMA) ---
app_ponto_voce = tk.Label(frame_cima, text="0", font=("Ivy 30 bold"), bg=CO_ESCURO, fg=CO_BRANCO)
app_ponto_voce.place(x=40, y=15)

app_voce = tk.Label(frame_cima, text="Você", font=("Ivy 10 bold"), bg=CO_ESCURO, fg=CO_BRANCO)
app_voce.place(x=38, y=70)

app_dois_pontos = tk.Label(frame_cima, text=":", font=("Ivy 30 bold"), bg=CO_ESCURO, fg=CO_BRANCO)
app_dois_pontos.place(x=118, y=15)

app_ponto_pc = tk.Label(frame_cima, text="0", font=("Ivy 30 bold"), bg=CO_ESCURO, fg=CO_BRANCO)
app_ponto_pc.place(x=180, y=15)

app_pc = tk.Label(frame_cima, text="PC", font=("Ivy 10 bold"), bg=CO_ESCURO, fg=CO_BRANCO)
app_pc.place(x=185, y=70)

app_linha = tk.Label(frame_cima, text="", width=260, height=1, bg=CO_LARANJA)
app_linha.place(x=0, y=95)

# --- MENSAGEM DE RESULTADO (FRAME BAIXO) ---
app_resultado = tk.Label(
    frame_baixo,
    text="Escolha uma opção abaixo",
    width=28,
    font=("Ivy 9 bold"),
    bg=CO_FUNDO,
    fg=CO_BRANCO,
    anchor="center",
)
app_resultado.place(x=10, y=15)


# --- LÓGICA DO JOGO ---
def jogar(escolha_voce):
    global pontos_voce, pontos_pc

    opcoes = ["Pedra", "Papel", "Tesoura"]
    escolha_pc = random.choice(opcoes)

    if escolha_voce == escolha_pc:
        resultado = "Empate!"
    elif (
        (escolha_voce == "Pedra" and escolha_pc == "Tesoura")
        or (escolha_voce == "Papel" and escolha_pc == "Pedra")
        or (escolha_voce == "Tesoura" and escolha_pc == "Papel")
    ):
        resultado = "Você ganhou!"
        pontos_voce += 1
    else:
        resultado = "PC ganhou!"
        pontos_pc += 1

    app_ponto_voce.config(text=str(pontos_voce))
    app_ponto_pc.config(text=str(pontos_pc))
    app_resultado.config(text=f"PC: {escolha_pc} | {resultado}")


# --- CARREGAR IMAGENS ---
def carregar_imagem(caminho):
    try:
        img = Image.open(caminho)
        img = img.resize((50, 50), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception:
        return None


img_pedra = carregar_imagem("pedra.png") or carregar_imagem("pedra.avif")
img_papel = carregar_imagem("papel.png") or carregar_imagem("papel.avif")
img_tesoura = carregar_imagem("tesoura.png") or carregar_imagem("tesoura.avif")

# --- BOTÕES DE ESCOLHA ---
largura_botao = 65
altura_botao = 50

b_pedra = tk.Button(
    frame_baixo,
    text="Pedra" if not img_pedra else "",
    image=img_pedra,
    width=largura_botao,
    height=altura_botao,
    bg=CO_AZUL,
    fg=CO_BRANCO,
    relief="raised",
    overrelief="ridge",
    command=lambda: jogar("Pedra"),
)
b_pedra.place(x=20, y=60)

b_papel = tk.Button(
    frame_baixo,
    text="Papel" if not img_papel else "",
    image=img_papel,
    width=largura_botao,
    height=altura_botao,
    bg=CO_AZUL,
    fg=CO_BRANCO,
    relief="raised",
    overrelief="ridge",
    command=lambda: jogar("Papel"),
)
b_papel.place(x=95, y=60)

b_tesoura = tk.Button(
    frame_baixo,
    text="Tesoura" if not img_tesoura else "",
    image=img_tesoura,
    width=largura_botao,
    height=altura_botao,
    bg=CO_AZUL,
    fg=CO_BRANCO,
    relief="raised",
    overrelief="ridge",
    command=lambda: jogar("Tesoura"),
)
b_tesoura.place(x=170, y=60)

janela.mainloop()

