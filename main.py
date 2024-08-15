import os
from book import pdf_text
from audio import book_audio

list = []

if os.path.exists("book/book.txt"):
    os.remove("book/book.txt")

arquivos = os.listdir("book")
for i, arquivo in enumerate(arquivos):
        list.insert(i, arquivo)

def selectBook():
    opt = input("Digite sua opção: ")
    return int(opt)

print("Escolha um livro da nossa estante para transformá-lo em audiobook.")
print("------------------------------------------------------------------")
for i, item in enumerate(list):
        print(i, " - ", item.replace(".pdf", ""))
print("------------------------------------------------------------------")
opt = selectBook()

try: 
    pdf_text(list[opt])
    book_audio(list[opt].replace(".pdf", ""))
    print("Audiobook foi gerado com sucesso!!")
except:
    print("Opção escolhida inválida. Por favor, insira um opção válida.")
    selectBook()