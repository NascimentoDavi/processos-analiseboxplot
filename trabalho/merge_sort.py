import os
import time
import multiprocessing
import matplotlib.pyplot as plt
import csv




# MERGE SORT SEQUENCIAL
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        left_half = merge_sort(left_half)
        right_half = merge_sort(right_half)

        return merge(left_half, right_half)
    return arr




# MERGE SORT PARALELO
def parallel_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    with multiprocessing.Pool(processes=2) as pool:
        left_sorted, right_sorted = pool.map(merge_sort, [left_half, right_half])
    
    return merge(left_sorted, right_sorted)




# MESCLA DUAS LISTAS ORDENADAS
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result




# LE OS NUMEROS DO ARQUIVO
def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file if line.strip().isdigit()]




# ESCREVE OS NUMEROS DO ARQUIVO
def write_numbers_to_file(file_path, numbers):
    with open(file_path, 'w') as file:
        for number in numbers:
            file.write(f"{number}\n")




# MEDIR TEMPO DE EXECUÇÃO
def benchmark_sorting(sorting_function, numbers, iterations=10):
    times = []
    for _ in range(iterations):
        numbers_copy = numbers[:]
        start_time = time.perf_counter()
        sorting_function(numbers_copy)
        end_time = time.perf_counter()
        times.append((end_time - start_time) * 1000)  # Convertendo para milissegundos
    return times




# SALVAR EM PDF
def save_times_to_csv(file_name, seq_times, par_times):
    with open(file_name, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Sequencial"] + seq_times)
        writer.writerow(["Paralelo"] + par_times)




# GERAR GRAFICO COMPARATIVO
def plot_results(seq_times_dict, par_times_dict, title, save_path):
    plt.figure(figsize=(12, 6))

    # Extraindo os dados para cada tamanho de arquivo
    seq_data = [seq_times_dict[key] for key in sorted(seq_times_dict.keys())]
    par_data = [par_times_dict[key] for key in sorted(par_times_dict.keys())]

    # Número de conjuntos de dados para cada método
    num_seq_data = len(seq_data)
    num_par_data = len(par_data)

    # Adicionando os boxplots com os dados
    plt.boxplot(seq_data, positions=range(1, num_seq_data + 1), widths=0.4, patch_artist=True, labels=[f"Sequencial {key}" for key in sorted(seq_times_dict.keys())])
    plt.boxplot(par_data, positions=range(num_seq_data + 1, num_seq_data + num_par_data + 1), widths=0.4, patch_artist=True, labels=[f"Paralelo {key}" for key in sorted(par_times_dict.keys())])

    plt.ylabel("Tempo (ms)")
    plt.title(title)
    plt.grid(True)

    # Ajustando os rótulos do eixo X para ficarem na vertical
    plt.xticks(rotation=90)

    # Salvando o gráfico no diretório especificado
    plt.savefig(save_path, bbox_inches='tight')
    print(f"Gráfico salvo em: {save_path}")
    plt.show()




if __name__ == "__main__":
    # Diretórios contendo os arquivos
    input_dirs = ["Listas/listas/listas_pequenas", "Listas/listas/listas_grandes"]
    output_csv = "trabalho/tempo_csv/resultados_tempos.csv"
    output_graph_dir = "trabalho/graficos"  # Diretório onde o gráfico será salvo
    os.makedirs(output_graph_dir, exist_ok=True)

    # Criando diretório de saída se não existir
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)

    # Cria o arquivo CSV e escreve o cabeçalho
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Método"] + [f"Execução {i+1}" for i in range(10)])

    # Dicionários para armazenar os tempos de execução para diferentes tamanhos de arquivos
    seq_times_dict = {}
    par_times_dict = {}

    # Obtém a lista de arquivos em ambos os diretórios
    files = []
    for input_dir in input_dirs:
        files.extend([os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith('.txt')])

    for input_file in sorted(files):  # Ordena os arquivos por nome
        print(f"Processando arquivo: {input_file}")

        numbers = read_numbers_from_file(input_file)

        # Medindo tempos de execução de cada método
        seq_times = benchmark_sorting(merge_sort, numbers)
        par_times = benchmark_sorting(parallel_merge_sort, numbers)

        # Determina o tamanho do arquivo baseado no nome
        file_size = os.path.basename(input_file).split('.')[0]  # Pega o nome do arquivo, por exemplo "100.txt" => "100"

        # Armazenando os tempos no dicionário para o gráfico
        seq_times_dict[file_size] = seq_times
        par_times_dict[file_size] = par_times

        # Salvando tempos no CSV
        save_times_to_csv(output_csv, seq_times, par_times)

        # Criando diretório de saída para números ordenados
        output_sorted_dir = "./trabalho/numeros_ordenados/"
        os.makedirs(output_sorted_dir, exist_ok=True)

        # Salvando os números ordenados
        output_file = os.path.join(output_sorted_dir, os.path.basename(input_file))
        sorted_numbers = merge_sort(numbers[:])
        write_numbers_to_file(output_file, sorted_numbers)

        print(f"Ordenação concluída para {input_file}! Comparando tempos...")

    # Gerando o gráfico para as listas pequenas e grandes e salvando no diretório
    output_graph_path = os.path.join(output_graph_dir, "comparacao_merge_sort.png")
    plot_results(seq_times_dict, par_times_dict, "Comparação de Tempo - Merge Sort Sequencial vs Paralelo", output_graph_path)

    print("Processamento de todos os arquivos concluído!")
    