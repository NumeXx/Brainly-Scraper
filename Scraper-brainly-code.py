# Di coding oleh iFanpS
# Module brainly berasal dari sini (https://krypton-byte.github.io/brainly-scraper/)
# BIG Thanks untuk krypton-byte
# Saya disini hanya memperbagus tampilan nya saja


import time, os, sys
try:
    from brainly_scraper import brainly
    from art import *
except ModuleNotFoundError:
    os.system('pip install art')
    time.sleep(1)
    os.system('python -m pip install brainly_scraper')

def utama():
    try:
        tprint('Brainly')
        pertanyaan = input('Masukan pertanyaan mu: ')
        jumlah_pertanyaan = int(input('Jumlah pertanyaan(abaikan jika tidak perlu): '))
    except ValueError:
        jumlah_pertanyaan=1

    os.system('cls')
    tprint('Brainly')
    print('                                            \033[32mPertanyaan : {0}\n                                            \033[32mJumlah pertanyaan : {1}'.format(pertanyaan,jumlah_pertanyaan))
    scrap=brainly("""{0}""".format(pertanyaan), jumlah_pertanyaan)

    for i in scrap:
        type_slowly(f"\033[91mBeberapa pertanyaan yang sama:\n\033[32m{i.question.content}", .03)
        for answer in enumerate(i.answers):
            type_slowly(f"\033[91mJawaban dari pertanyaan mu:\n\033[32m{answer[1].content}", .03)

def type_slowly(text, speed, newLine = True):
    for i in text: 
        print(i, end = "", flush = True) 
        time.sleep(speed) 
    if newLine:
        print() 

utama()
while True:       
    tanya_kembali = input('\nJawab y untuk kembali bertanya jika tidak Tekan saja: ')
    if tanya_kembali == 'y':
        os.system('cls')
        utama()
    else:
        sys.exit()
