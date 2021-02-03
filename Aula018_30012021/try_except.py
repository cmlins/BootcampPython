try: 
    fh = open("./Aula018_30012021/testfile.txt", "w") 
    fh.write("This is my test file for exception handling!!") 
except IOError: 
    print ("Erro: Fofinho, não pode escrever o arquivinho.") 
else: 
    print ("Fofinho, escreveu o arquivinho viu?!") 
    fh.close()


try: 
    fh = open("testfile2.txt", "w") 
    try: 
        fh.write("This is my test file for exception handling!!") 
    finally: 
        print ("Going to close the file") 
        fh.close() 
except IOError: 
    print ("Error: can\'t find file or read data") 