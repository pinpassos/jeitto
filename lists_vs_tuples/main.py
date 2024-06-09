""""
Em Python, há um conceito chamado coleção.
Coleções são estruturas de dados que nos permitem armazenar múltiplos valores em uma única variável.
Neste contexto, abordaremos a principal diferença entre duas coleções amplamente utilizadas:
listas e tuplas.

Listas são coleções mutáveis, o que significa que podemos adicionar, remover e alterar
seus elementos após sua criação.

Por exemplo, se tivermos uma lista de números, podemos adicionar um novo número,
remover um existente ou modificar qualquer valor presente na lista.

Por outro lado, tuplas são coleções imutáveis. Uma vez que uma tupla é criada e seus elementos
são definidos, eles não podem ser alterados. Isso significa que, após sua definição inicial,
a estrutura e os valores da tupla permanecem os os mesmos durante todo o tempo de execução
do programa.

A mutabilidade das listas proporciona flexibilidade quando precisamos de uma coleção dinâmica,
enquanto a imutabilidade das tuplas oferece segurança e integridade dos dados quando desejamos
garantir que a coleção não seja modificada por algum motivo.
"""

if __name__ == "__main__":
    morning_tasks = ["Acordar", "Tomar banho", "Beber café"]
    coordinates_of_christ_the_redeemer = (-22.951944, -43.210556)

    # A lista pode sofrer alterações já que as tarefas são dinâmicas,
    # podendo ser modificadas, removidas ou adicionadas mais tarefas.
    morning_tasks[2] = "Arrumar a casa"
    morning_tasks.append("Dormir")
    assert morning_tasks == ["Acordar", "Tomar banho", "Arrumar a casa", "Dormir"]

    # Exceção TypeError: 'tuple' object does not support item assignment é subida,
    # dado que as coordenadas geográficas de um local são estáticas.
    # Utilizamos uma tupla neste cenário para garantir que não haja a possibilidade
    # de alteração.
    try:
        coordinates_of_christ_the_redeemer[0] = -22.4234
    except TypeError as err:
        print("TypeError correctly raised and captured.", err)
