#  a terminar

def remove(task_iteravel, task=None):
    if task is None:
        task = []
    task.extend(task_iteravel)
    return task


def desfazer(l1, l2):


def adicionar(noav_tarefa, add_list):
    add_list.append(nova_tarefa)


def show_list(list_task):
    print(list_task)


v = True
tarefa = []
refaz = []
c = 0
while (v):
    x = input('O que deseja fazer? Listar(1), Refazer(2), Adicionar(3), Desfazer(4)')

    if x == 1:
        show_list(tarefa)

    v = input('Continuar? s/n')
    if v == 'n':
        break
