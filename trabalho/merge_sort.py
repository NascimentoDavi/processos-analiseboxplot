# Aplicar duas versões do algoritmo Merge Sort
# -> Versão Sequencial -> Implementação Tradicional
# -> Versão Parelela -> Implementação utilizando processamento paralelo

# Para cada conjunto de dados voce deve executar ambas as versões do algoritmo pelo menos dez vezes

# O tempo de execução de cada rodada deve ser medido e armazenado para posterior analise

# A comparação entre as duas abordagens será feita por meio de diagramas de box plot. Para isso é necessario gerar cinco box plots para cada versao do algoritmo, totalizando dez graficos

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file if line.strip().isdigit()]


def write_numbers_to_file(file_path, numbers):
    with open(file_path, 'w') as file:
        for number in numbers:
            file.write(f"{number}\n")


if __name__ == "__main__":
    input_file = "numeros.txt"  # Nome do arquivo de entrada
    output_file = "numeros_ordenados.txt"  # Nome do arquivo de saída
    
    numbers = read_numbers_from_file(input_file)
    merge_sort(numbers)
    write_numbers_to_file(output_file, numbers)
    
    print("Ordenação concluída! Os números foram salvos em", output_file)
