
# +-----------------------------------------------+
# | STRING METHODS                                |
# +-----------------------------------------------+

msg = '   paULo da siLVa Pinheiro    '
formatString = '{0} : {1}'
print(formatString.format('Original',msg))


# | Upper case                                |
print(formatString.format('Upper case',msg.upper()))

# | Lower case                                |
print(formatString.format('Lower case',msg.lower()))

# | Remove whitespace                         |
print(formatString.format('Strip',msg.strip()))

# | Replace string                            |
print(formatString.format('Replace',msg.replace('a','$')))

# | Split   string                            |
print(formatString.format('Split',msg.split(' ')))

# | Capitalize   string                       |
print(formatString.format('Capitalize',msg.strip().capitalize()))

# | Count numero de vezes que uma string aparece dentro da sentença  string                            |
print(formatString.format('Count',msg.count("a")))

# | Enconding                                 |
print(formatString.format('Encode',msg.replace("a","ã").encode(encoding="utf-8")))

# | Find                                      |
print(formatString.format('Find',msg.find("paULo")))

# | Index                                      |
print(formatString.format('Index',msg.index("paULo")))

