
# Estudo de manipulação de strings em Python

# +-----------------------------------------------+
# | SLICING                                       |
# +-----------------------------------------------+
'''
No slicing a primeira parte indica o INICIO e a segunda FIM e não quantos caracteres será lido.

ex: bom dia

para pegar a palavra 'dia' iniciamos na posição 4 e lemos até a posição 7
'''
msg = "bom dia"
print(msg[4:7]) #dia

msg = "Meu nome é Paulo da Silva Pinheiro"
print(msg[0:2]) #Me
print(msg[:2]) #Me (da posição 0 até o total de caracteres definidos)
print(msg[11:16]) #Paulo
print(msg[11:]) #Paulo (da posição definida (11) até o total de caracteres)

# Negative index
print(msg[-8:-1]) #Pinheir

# +-----------------------------------------------+
# | STRING FORMAT                                 |
# +-----------------------------------------------+

print("Meu nome é {} tenho {} anos de idade e moro em {}".format("Paulo da Silva Pinheiro", 39, "Barueri"))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# +-----------------------------------------------+
# | ESCAPE CHARACTER                              |
# +-----------------------------------------------+

#  Tipos de escape
#     \'		Single Quote	
#     \\		Backslash	
#     \n		New Line	
#     \r		Carriage Return	
#     \t		Tab	
#     \b		Backspace	
#     \f		Form Feed	
#     \ooo	    Octal value	
#     \xhh	    Hex value


print("PAULO DA SILVA PINHEIRO is my \'name\'")
print("PAULO \nDA SILVA \nPINHEIRO is my \'name\'")

# Hex value
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 