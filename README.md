# Verificação de Sintaxe de Código C++

Este projeto contém um script Python que verifica a sintaxe de códigos C++ utilizando ferramentas como `cpplint`, `cppcheck` e `cpp-linter`. O código é lido a partir de um arquivo Excel e os resultados da verificação são salvos em um arquivo CSV.

## Funcionalidades

- Leitura de um arquivo Excel com códigos C++.
- Verificação de sintaxe utilizando as ferramentas:
  - `cpplint`
  - `cppcheck`
  - `cpp-linter`
- Geração de um arquivo CSV com os resultados da verificação.

## Requisitos

Certifique-se de ter os seguintes pacotes Python instalados:

- `pandas`
- `openpyxl` (para ler arquivos Excel)
- `numpy` (dependência do pandas)

Além disso, você precisa instalar as ferramentas externas:

- `cpplint`: uma ferramenta de linting para C++
- `cppcheck`: um analisador estático para C++
- `cpp-linter`: uma ferramenta de linting para C++
- `clang`: necessário para o funcionamento do `cppcheck` e do `cpp-linter`


### Instalação dos Pacotes

Para utilizar as ferramentas de verificação de sintaxe de código C++, você precisará instalar o `clang-tidy` e o `clang-format`. Você pode fazer isso usando o seguinte comando no terminal:

```bash
sudo apt install clang-tidy clang-format


### Instalação dos Pacotes Python

Você pode instalar os pacotes python necessários com o seguinte comando:

```bash
pip install -r requirements.txt
