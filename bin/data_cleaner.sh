#!/bin/bash
# Descrição: Este script limpa os arquivos de reastreamento das imagens no diretório de validação.
# Uso: ./bin/data_cleaner.sh

# Diretório base
base_dir="$(pwd)/data/validation"

# Loop para percorrer todas as letras do alfabeto
for letter  in {A..Z}; do
    # Diretório onde estão as imagens
    dir="$base_dir/$letter "

    # Verificar se o diretório existe
    if [ -d "$dir" ]; then
        # Navegar até o diretório
        cd "$dir" || exit

        # Loop para iterar sobre todas as imagens no diretório
        for image in *.png; do
            # Verificar se o arquivo é uma imagem
            if [[ -f "$image" ]]; então
                # Remover qualquer arquivo de reastreamento associado à imagem
                rm -f "${image}:Zone.Identifier"
                echo "Arquivo de reastreamento removido para $image"
            fi
        done

        echo "Limpeza concluída para o diretório $dir!"
    else
        echo "Diretório não encontrado para a letra $letter "
    fi
done
