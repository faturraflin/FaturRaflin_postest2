````
data = [{"nomor": 1, "nama karpet": "karpet aladin", "harga": 10000 }]

def tambah():
    nama_karpet = input("Masukan nama karpet :")
    harga = int(input("Masukan harga :"))
    nomor_terbaru = len(data) + 1
    baju_baru = {"nomor": nomor_terbaru, "nama karpet": nama_karpet, "harga": harga}
    data.append(baju_baru)

    print("Data sudah ditambahkan")
    baca()
    print("-"*25)

def baca():
    for item in data:
        print(f"{item['nomor']}. Nama Karpet: {item['nama karpet']}, Harga: {item['harga']}")
    print("-"*25)

def update():
    baca()
    produk = int(input("Pilih Nomor Produk yang mau di update :"))
    for item in data:
        if item['nomor'] == produk:
            namabaru = input("Masukan nama baru :")
            hargabaru = int(input("Masukan harga baru :"))
            item['nama karpet'] = namabaru
            item['harga'] = hargabaru
            print("Berhasil diupdate")
            break

        else:
            print("Produk yang ingin diubah tidak valid")

def delete():
    baca()
    produk = int(input("Pilih Nomor Produk yang mau dihapus :"))
    for item in data:
        if item['nomor'] == produk:
            data.remove(item)
            print("Data telah dihapus")
            break

        else: 
            print("Produk yang ingin dihapus tidak valid")

def menu_admin():
    while True:
        print("1. Tambah karpet")
        print("2. Tampilkan karpet")
        print("3. Update")
        print("4. Delete")
        print("5. Keluar")
        pilih = input("Pilih: ")

        if pilih == "1":
            tambah()
        elif pilih == "2":
            baca()
        elif pilih == "3":
            update()
        elif pilih == "4":
            delete()
        elif pilih == "5":
            break
        else:
            print("Pilihan tidak valid")

def transaksi():
    while True:
        baca()
        produk = int(input("Pilih Nomor Produk yang mau dibeli :"))
        for item in data:
            harga_item = int(item['harga'])
            if item['nomor'] == produk:
                qty = int(input("Masukan qty :"))
                harga_total = harga_item * qty
                print("Total semuanya adalah Rp.", harga_total)
                return
            else:
                print("Produk tidak ada")

    


def menu_user():
    while True:
        print("1. beli")
        print("2. keluar")
        pilih2 = input("Pilih: ")

        if pilih2 == "1":
            transaksi()
        elif pilih2 == "2":
            break


while True:
    print("Selamat Datang Di Toko Karpet")
    username = input("Masukkan Username Anda: ")
    password = input("Masukkan Kata Sandi Anda: ")

    if password == "admin":
        menu_admin()
    else:
        menu_user()
````
