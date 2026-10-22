#!/usr/bin/env python3
# Abre o arquivo multi-FASTA
with open("Python_08.fasta", "r") as arquivo:

    nome = ""
    seq = ""

    for linha in arquivo:
        linha = linha.strip()

        # Verifica se a linha é um cabeçalho
        if linha.startswith(">"):

            # Se já existe uma sequência armazenada, conta seus nucleotídeos
            if nome != "":
                nt_comp = {"A": 0, "T": 0, "G": 0, "C": 0}

                for nt in seq:
                    if nt in nt_comp:
                        nt_comp[nt] += 1

                print(nome, nt_comp["A"], nt_comp["T"],
                      nt_comp["G"], nt_comp["C"], sep="\t")

            # Guarda o nome da nova sequência
            nome = linha[1:].split()[0]

            # Começa a armazenar a nova sequência
            seq = ""

        else:
            # Junta as linhas que pertencem à mesma sequência
            seq += linha

    # Conta também a última sequência do arquivo
    nt_comp = {"A": 0, "T": 0, "G": 0, "C": 0}

    for nt in seq:
        if nt in nt_comp:
            nt_comp[nt] += 1

    print(nome, nt_comp["A"], nt_comp["T"],
          nt_comp["G"], nt_comp["C"], sep="\t")
