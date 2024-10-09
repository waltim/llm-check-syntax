import pandas as pd
import tempfile
import subprocess
import csv
import os

# Caminho do arquivo Excel
input_file = 'tb_function_comparison2.xlsx'
output_file_path = './'

def check_syntax_cpplint(code: str) -> str:
    """Função para verificar a sintaxe de um código C++ utilizando cpplint."""
    try:
        # Cria um arquivo temporário para armazenar o código C++
        with tempfile.NamedTemporaryFile(suffix=".cpp", delete=False) as temp_file:
            temp_file.write(code.encode('utf-8'))
            temp_file.flush()

            # Comando para rodar o cpplint com filtros para runtime, build, e readability
            result = subprocess.run(['cpplint', '--filter=-whitespace,-legal', temp_file.name], 
                                    capture_output=True, text=True)

            # Se não houver erros críticos de sintaxe, o retorno será 0
            if result.returncode == 0:
                return "OK"
            else:
                return result.stderr.strip()

    except Exception as e:
        # Captura qualquer exceção durante o processo
        return str(e)

    finally:
        if os.path.exists(temp_file.name):
            os.remove(temp_file.name)
            
def check_syntax_cppcheck(code: str) -> str:
    """Função para verificar a sintaxe de um código C++ utilizando cppcheck."""
    try:
        # Cria um arquivo temporário para armazenar o código C++
        with tempfile.NamedTemporaryFile(suffix=".cpp", delete=False) as temp_file:
            temp_file.write(code.encode('utf-8'))
            temp_file.flush()

            # Comando para rodar o cppcheck
            result = subprocess.run(['cppcheck', '--enable=all', temp_file.name],
                                    capture_output=True, text=True)

            # Se o retorno for 0, o código está correto
            if result.stderr == '' and result.returncode == 0:
                return "OK"
            else:
                return result.stderr.strip()

    except Exception as e:
        # Captura qualquer exceção durante o processo
        return str(e)

    finally:
        if os.path.exists(temp_file.name):
            os.remove(temp_file.name)
            
def check_syntax_cpp_linter(code: str) -> str:
    """Função para verificar a sintaxe de um código C++ utilizando cpp-linter."""
    try:
        # Cria um arquivo temporário para armazenar o código C++
        with tempfile.NamedTemporaryFile(suffix=".cpp", delete=False) as temp_file:
            temp_file.write(code.encode('utf-8'))
            temp_file.flush()

            # Comando para rodar o cppcheck
            result = subprocess.run(['cpp-linter', '--tidy-checks', temp_file.name],
                                    capture_output=True, text=True, cwd='/tmp')

            # Se o retorno for 0, o código está correto
            if result.stderr == '' and result.returncode == 0:
                return "OK"
            else:
                return result.stderr.strip()

    except Exception as e:
        # Captura qualquer exceção durante o processo
        return str(e)

    finally:
        if os.path.exists(temp_file.name):
            os.remove(temp_file.name)

def check_syntax(code: str, tool: str = 'cpplint') -> str:
    """Função para verificar a sintaxe de um código C++ utilizando a ferramenta especificada."""
    if tool == 'cpplint':
        return check_syntax_cpplint(code)
    elif tool == 'cppcheck':
        return check_syntax_cppcheck(code)
    elif tool == 'cpp-linter':
        return check_syntax_cpp_linter(code)
    else:
        raise ValueError("Ferramenta não suportada. Use 'cpplint', 'cpp-linter' ou 'cppcheck'.")


def process_excel(input_file: str, output_file_path: str, tool: str = 'cppcheck'):
    # Lê o arquivo Excel
    df = pd.read_excel(input_file, sheet_name='Sheet1').fillna('')

    # Abre o arquivo CSV para escrita dos resultados
    with open(output_file_path+'syntax_check_results_'+tool+'.csv', mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        # Escreve o cabeçalho
        header = ['id_function_original', 'code_pre_commit_result',
                  'code_post_commit_result', 'code_model_llama3_result',
                  'code_model_gpt4o_result', 'code_model_geminipro_result',
                  'code_model_claude3opus_result']
        writer.writerow(header)

        # Itera sobre cada linha do dataframe
        for _, row in df.iterrows():
            # Extrai os campos de código
            id_function_original = row['id_function_original']
            code_pre_commit = row['code_pre_commit']
            code_post_commit = row['code_post_commit']
            code_model_llama3 = row['code_model_llama3']
            code_model_gpt4o = row['code_model_gpt4o']
            code_model_geminipro = row['code_model_geminipro']
            code_model_claude3opus = row['code_model_claude3opus']

            # Verifica a sintaxe de cada campo de código
            code_pre_commit_result = check_syntax(code_pre_commit, tool)
            code_post_commit_result = check_syntax(code_post_commit, tool)
            code_model_llama3_result = check_syntax(code_model_llama3, tool)
            code_model_gpt4o_result = check_syntax(code_model_gpt4o, tool)
            code_model_geminipro_result = check_syntax(code_model_geminipro, tool)
            code_model_claude3opus_result = check_syntax(code_model_claude3opus, tool)

            # Escreve a linha com os resultados no arquivo CSV
            writer.writerow([
                id_function_original, code_pre_commit_result,
                code_post_commit_result, code_model_llama3_result,
                code_model_gpt4o_result, code_model_geminipro_result,
                code_model_claude3opus_result
            ])

    print(f"Processamento concluído. Resultados salvos em {output_file_path+'syntax_check_results_'+tool+'.csv'}")


# Executa o processamento
process_excel(input_file, output_file_path)
