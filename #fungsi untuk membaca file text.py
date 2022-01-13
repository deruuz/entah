#fungsi untuk membaca file text
dict_tabungan = dict()

def baca(namafile):
    file_text = open("Tabungan.txt")
    file = file_text.readlines()
    
#list tabungan yang menggunakan dictionary         
    for i in file:
        nama, harga, tabungan1, tabungan2, var1, var2 = i.split(" ")
        dict_tabungan[nama] = [int(harga), int(tabungan1) + int(tabungan2)]
    print(dict_tabungan)
    file_text.close()
    return baca

#fungsi terbanyak       
def terbanyak(data):
    terbanyak = 0
    key_terbanyak = ""
    for ar_key in dict_tabungan:
        a = dict_tabungan[ar_key][1]
        if a > terbanyak:
            terbanyak = a
            key_terbanyak = ar_key
    print ("Mahasiswa dengan Tabungan Terbanyak :", key_terbanyak)
    return key_terbanyak

#fungsi juara
def juara(data):
    juara = 0
    key_juara = ""
    for ar_key in dict_tabungan:
        a = dict_tabungan[ar_key][0] - dict_tabungan[ar_key][1]
        if a > juara:
            juara = a
            key_juara = ar_key
    print ("Mahasiswa dengan Nominal Tabungan Paling Mendekati Harga Laptop Adalah :", key_juara)
    return key_juara

#main program
main = baca("Tabungan.txt")
juara(main)
terbanyak(main)