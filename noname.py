import random
import sys
import time
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.3)
#ubah angka 0.1 sesuai keinginan kamu
#angka terkecil adalah yang paling cepat
#angka terbesar adalah yang paling lambat
mengetik('nazwa,auramu bagaikan embun di pagi hari,indah,alami,dan mempesona.kamu mau sama aku sampe kapan kira-kira,jawab di  whatsapp yaaa ,nazwa,pernah gak kamu di gombalin kaya gini?,sama aku beda yahh,hehe.')