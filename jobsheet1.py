import random
from guess import TebakAngka

jawaban = random.randint(1, 10)
tebakan = int(input('tebak angka dari 1 sd 10 :'))

hasil = TebakAngka(jawaban, tebakan)


if hasil.process():
    print('Jawaban anda benar!')

else:
    print('Jawaban anda salah!')
