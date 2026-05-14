# =============================================================
#  🎮 JOGO DA FORCA
#  Autor: Rosário Dutra
#  GitHub: github.com/rosariodutra
#  Descrição: Jogo da forca clássico no terminal com categorias,
#             dificuldades e placar de recordes.
# =============================================================

import random
import os

# ── Palcos da forca ──────────────────────────────────────────

FORCA = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ========="""
]

# ── Banco de palavras por categoria ──────────────────────────

PALAVRAS = {
    "Tecnologia": [
        ("python", "Linguagem de programação muito usada em dados"),
        ("dashboard", "Painel visual com indicadores e gráficos"),
        ("automacao", "Processo de executar tarefas sem intervenção manual"),
        ("algoritmo", "Sequência de passos para resolver um problema"),
        ("banco", "Local onde dados são armazenados e consultados"),
        ("pipeline", "Fluxo de processamento de dados em etapas"),
        ("variavel", "Elemento que armazena um valor em programação"),
        ("funcao", "Bloco de código reutilizável com uma finalidade"),
    ],
    "Análise de Dados": [
        ("dataset", "Conjunto de dados estruturados para análise"),
        ("grafico", "Representação visual de dados"),
        ("insight", "Descoberta relevante obtida a partir dos dados"),
        ("media", "Soma dos valores dividida pela quantidade"),
        ("tendencia", "Direção geral que os dados apontam ao longo do tempo"),
        ("correlacao", "Relação entre duas variáveis nos dados"),
        ("outlier", "Valor muito distante dos demais em um conjunto"),
        ("filtro", "Critério para selecionar parte dos dados"),
    ],
    "Finanças": [
        ("receita", "Total de entradas financeiras de uma empresa"),
        ("despesa", "Custo ou gasto registrado no financeiro"),
        ("lucro", "Diferença positiva entre receita e despesa"),
        ("fluxo", "Movimentação de entradas e saídas de dinheiro"),
        ("balanco", "Demonstrativo do patrimônio em determinada data"),
        ("orcamento", "Planejamento financeiro para um período"),
        ("conciliacao", "Verificação entre saldos de diferentes fontes"),
        ("inadimplencia", "Situação de não pagamento de uma dívida no prazo"),
    ],
}

# ── Dificuldades ─────────────────────────────────────────────

DIFICULDADES = {
    "1": {"nome": "Fácil",   "tentativas": 6, "dica": True},
    "2": {"nome": "Médio",   "tentativas": 5, "dica": False},
    "3": {"nome": "Difícil", "tentativas": 4, "dica": False},
}

# ── Utilitários ───────────────────────────────────────────────

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def cabecalho():
    print("\033[35m")
    print("╔══════════════════════════════════════╗")
    print("║         🎮  JOGO DA FORCA  🎮         ║")
    print("║      github.com/rosariodutra          ║")
    print("╚══════════════════════════════════════╝")
    print("\033[0m")

def exibir_palavra(palavra, letras_certas):
    return " ".join(l if l in letras_certas else "_" for l in palavra)

def exibir_status(forca_idx, palavra, letras_certas, letras_erradas, tentativas_max):
    print(FORCA[forca_idx])
    print(f"\n  Palavra: {exibir_palavra(palavra, letras_certas)}")
    print(f"  Erros  : {', '.join(sorted(letras_erradas)) or '-'}")
    print(f"  Chances: {tentativas_max - forca_idx} restante(s)\n")

# ── Lógica principal do jogo ──────────────────────────────────

def jogar(palavra, dica, tentativas_max):
    letras_certas = set()
    letras_erradas = set()
    erros = 0

    while True:
        limpar()
        cabecalho()
        exibir_status(erros, palavra, letras_certas, letras_erradas, tentativas_max)

        if dica:
            print(f"  💡 Dica: {dica}\n")

        # Vitória
        if all(l in letras_certas for l in palavra):
            print(f"\033[32m  ✅ Parabéns! A palavra era: {palavra.upper()}\033[0m\n")
            return True

        # Derrota
        if erros >= tentativas_max:
            print(FORCA[-1])
            print(f"\033[31m  ❌ Você perdeu! A palavra era: {palavra.upper()}\033[0m\n")
            return False

        chute = input("  Digite uma letra: ").strip().lower()

        if not chute.isalpha() or len(chute) != 1:
            print("  ⚠️  Digite apenas uma letra!")
            input("  [Enter para continuar]")
            continue

        if chute in letras_certas or chute in letras_erradas:
            print("  ⚠️  Você já tentou essa letra!")
            input("  [Enter para continuar]")
            continue

        if chute in palavra:
            letras_certas.add(chute)
        else:
            letras_erradas.add(chute)
            erros += 1

# ── Menu principal ────────────────────────────────────────────

def menu_categoria():
    categorias = list(PALAVRAS.keys())
    print("  Escolha uma categoria:\n")
    for i, cat in enumerate(categorias, 1):
        print(f"    {i}. {cat}")
    print(f"    {len(categorias)+1}. Aleatória\n")

    while True:
        escolha = input("  Opção: ").strip()
        if escolha.isdigit():
            idx = int(escolha)
            if 1 <= idx <= len(categorias):
                return categorias[idx - 1]
            elif idx == len(categorias) + 1:
                return random.choice(categorias)
        print("  ⚠️  Opção inválida!")

def menu_dificuldade():
    print("\n  Escolha a dificuldade:\n")
    for k, v in DIFICULDADES.items():
        dica_info = "com dica" if v["dica"] else "sem dica"
        print(f"    {k}. {v['nome']} — {v['tentativas']} tentativas, {dica_info}")
    print()

    while True:
        escolha = input("  Opção: ").strip()
        if escolha in DIFICULDADES:
            return DIFICULDADES[escolha]
        print("  ⚠️  Opção inválida!")

def main():
    vitorias, derrotas = 0, 0

    while True:
        limpar()
        cabecalho()
        print(f"  Placar: ✅ {vitorias} vitória(s)  ❌ {derrotas} derrota(s)\n")
        print("  1. Jogar")
        print("  2. Sair\n")

        opcao = input("  Opção: ").strip()

        if opcao == "2":
            limpar()
            cabecalho()
            print(f"  Obrigada por jogar! Placar final: {vitorias}V / {derrotas}D\n")
            break

        if opcao != "1":
            continue

        limpar()
        cabecalho()
        categoria = menu_categoria()

        limpar()
        cabecalho()
        dificuldade = menu_dificuldade()

        palavra, dica_texto = random.choice(PALAVRAS[categoria])
        dica = dica_texto if dificuldade["dica"] else None

        resultado = jogar(palavra, dica, dificuldade["tentativas"])

        if resultado:
            vitorias += 1
        else:
            derrotas += 1

        input("  [Enter para continuar]")

if __name__ == "__main__":
    main()
