#Import of functionallity (Importação de funcionalidades)
import os
import pyaes

fileName = "foto.jpg.nsom"
file = open(fileName, "rb")
fileData = file.read()
file.close()

key = "DeusNoComand0"
aes = pyaes.AESModeOfOperationCTR(key)
decryptData = aes.decrypt(fileData)

#Remove the file (Remover o arquivo)
os.remove(fileName)

newFileName = "foto.jpg"
newFile = open(newFileName, "wb")
newFile.write(decryptData)
newFile.close()
