
class writeTerminal:
    def write(self,texto):
        print("### => [ {0} ]".format(texto))

    def printFormat(self,describe, value, pularLinha):
        formatString = '{0} : {1}'
        print(formatString.format(describe,value))

        if pularLinha:
            self.pularLinha()
    
    def pularLinha(self):
        print("")