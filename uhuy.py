def tambah (x,y):
    return x + y

while True :
    
    depan = input ("Nama Depan :")
    belakang = input ("Nama Belakang :")

    gabung = " ".join ([depan, belakang])
    panjang = len (gabung)

    print ("Panjang Teks =", panjang)

    if panjang <=13 :
        print ("\nSelamat Datang!", gabung, "Silahkan Pergi!")
        print ("\nSILAHKAN JAWAB PERTANYAAN BERIKUT!")
        print ("\nBagaimana cara anda memakan bubur?")
        A = print ("A. Diaduk")
        B = print ("B. Tidak Diaduk")
        C = print ("C. Dibuang")

        jawaban = input ("\nJAWABAN ANDA:")

        if jawaban .upper() == "A":
            print ("\nSelamat anda mendapatkan uang tunai Rp.1.000.000 dipotong pajak 100%")
            print ("\nSELANJUTNYA")
            print ("Gunakan Kalkulator Penjumlahan dibawah!")
            x = float (input ("Angka ke-1 :"))
            y = float (input ("Angka ke-2 :"))
            print (tambah (x,y))

        elif jawaban .upper() == "B":
            print ("\nANDA KURANG BERUNTUNG")
            print ("\nSELANJUTNYA")
            print ("Gunakan Kalkulator Penjumlahan dibawah!")
            x = float (input ("Angka ke-1 :"))
            y = float (input ("Angka ke-2 :"))
            print (tambah (x,y))

        elif jawaban .upper() == "C":
            print ("\nASTAGFIRULLAH! BAYANGKAN ADA BANYAK SAUDARA KITA YANG KELAPARAN.")
            print ("SEMENTARA ANDA MALAH BUANG-BUANG MAKANAN.")
            print ("\nSELANJUTNYA")
            print ("Gunakan Kalkulator Penjumlahan dibawah!")
            x = float (input ("Angka ke-1 :"))
            y = float (input ("Angka ke-2 :"))
            print (tambah (x,y))

        else :
            print ("\nJAWABANNYA 1,2, SAMA 3 DOANG!") 

    else :
        print ("\nNAMA ANDA KEPANJANG! PANJANG MAKSIMAL 13 Karakter!")
    
    lanjut = input ("\nulang? (y/t) :") 
    
    if lanjut .lower() != "y" :
        break