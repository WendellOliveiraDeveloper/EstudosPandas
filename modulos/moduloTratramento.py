import pathlib
import pandas as pd
import datetime
import csv
import re
import os
import numpy as np

hoje = datetime.date.today()
caminhoOutputs = pathlib.Path('./outputs')

def trata_coluna_nome(df, coluna):
    df = df.copy()

    df[coluna] = df[coluna].str.upper()
    df[coluna] = df[coluna].str.strip()

    # Caso o nome tenha menos de 3 letras ficará vazio
    df.loc[(df[coluna].str.len() > 0) & (df[coluna].str.len() <= 3), coluna] = ""

    # Trunca nomes com mais de 90 caracteres sem quebrar palavra
    def truncar_nome(nome, max_len=90):
        if pd.isnull(nome):
            return nome
        if len(nome) <= max_len:
            return nome
        truncado = nome[:max_len]
        if ' ' in truncado:
            truncado = truncado[:truncado.rfind(' ')]
        return truncado

    df[coluna] = df[coluna].apply(truncar_nome)

    # Remove caracteres que quebram o arquivo gerado
    caracteres_remover = ["\'", "\"", ";", "\\\\", "\\/", "\r\n", "\n", "\r"]
    for c in caracteres_remover:
        df[coluna].replace(to_replace=c, value='', regex=True, inplace=True)

    return df

def trata_df_pessoas(df_pessoas, formato_data = '%Y-%m-%d'):
    df_pessoas = df_pessoas.applymap(
        lambda x: x.strip() if isinstance(x, str) else x
    )

    if 'NOME' in df_pessoas.columns:
        df_pessoas['NOME'] = trata_coluna_nome(df_pessoas, 'NOME')
    else:
        df_pessoas['NOME'] = ''

    return df_pessoas