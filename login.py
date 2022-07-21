from selenium import webdriver
import time

# create a new Chrome session
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

# arahkan ke halaman beranda aplikasi
sopir . dapatkan ( "https://yuhofactory@gmail.com/" )

#dapatkan kotak teks nama pengguna
login_field  =  driver . find_element_by_name ( "yuhofactory@gmail.com" )
login_field . jelas ()

#Masukkan nama pengguna
login_field . send_keys ( "yuhofactory@gmail.com " )
login_field . send_keys ( u' \ue007 ' ) #unicode untuk memasukkan kunci
waktu . tidur ( 2 )

#dapatkan kotak teks kata sandi
password_field  =  driver . find_element_by_name ( "Mr008800." )
kata sandi_bidang . jelas ()

#Masukkan kata kunci
kata sandi_bidang . send_keys ( "Mr008800." )
kata sandi_bidang . send_keys ( u' \ue007 ' ) #unicode untuk memasukkan kunci
waktu . tidur ( 10 )

#navigasi ke gmail
