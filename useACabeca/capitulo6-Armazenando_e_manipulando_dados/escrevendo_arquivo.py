# [todos.tx] não é um arquivo existente ele foi criado durante a execução destes comandos

todos = open('todos.txt','a')

print('Put out the trash.',file=todos)
print('Feed the cat.', file=todos)
print('Prepare tax return.',file=todos)

todos.close()