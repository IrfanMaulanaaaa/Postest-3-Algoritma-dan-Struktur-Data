# Postest 3 Algoritma dan Struktur Data
"Penerapan SinglyLinked List dalam pembuatan mini project pendataan pesanan laundry".

Dibuat oleh: Muhammad Irfan Maulana (2209116036)

## Fungsional dan Cara kerja program

Program ini dibuat khusus untuk mendata pesanan masuk permintaan Laundry. Program ini dibuat dengan menerapkan singlylinked list yang dimana merupaka salah satu dari beberapa linked list yang ada yang dimana singly linked list memiliki paradigma bahwa data dapat dipindahkan, dialihkan ke satu arah saja. Program ini dapat melakukan input user seperti tambah, hapus, dan tampilkan data. Data yang ditambahkan dan dihapus juga akan otomatis masuk ke riwayat data. 

## penjelasan elemen - elemen program dan outputnya

![image](https://user-images.githubusercontent.com/121864328/225942801-0370de1a-9d55-437d-9ccd-6b325948b6c2.png)

output:

![image](https://user-images.githubusercontent.com/121864328/225944930-4b63095b-92c3-47a0-a68d-d0a2463f3e95.png)![image](https://user-images.githubusercontent.com/121864328/225945179-5dd5cae1-4444-4c32-b52c-b87f8591b7d4.png)



1. import prettytable adalah library yang digunakan untuk menampilkan data sesuai yang diinginkan dengan visual tabel
2. x,y, dan z adalah tiga variabel yang di inisialisasi sebagai variabel penampung data berbentuk tabel.
3. field names adalah inisialisasi nama kolom pada tabel.

![image](https://user-images.githubusercontent.com/121864328/225943884-be6827ab-1208-45b2-a08b-0b8d9b124597.png) ![image](https://user-images.githubusercontent.com/121864328/225947147-e8c6bd43-3234-40a8-b3e6-118d1aebe4df.png)


4. class Node: adalah pendefinisian sebuah konstruktor yang mengambil parameter "data" dan menginisialisasi atribut "self.data" dan "self.next" menjadi None. Kemudian didefinisikan sebuah kelas bernama "LinkedList" yang memiliki atribut "self.head" dan "self.history".
5. Class LinkedList memiliki beberapa metode, diantaranya "display", untuk menampilkan data, "addfirst" untuk menambahkan data pada awal linked list, "deletefirst" untuk menghapus data pada awal linked list, dan "print_history" untuk menampilkan riwayat data yang dihapus

![image](https://user-images.githubusercontent.com/121864328/225947829-2fb48bd8-8a35-4b0a-a6ab-3a96b20ccbbf.png)

output: ![image](https://user-images.githubusercontent.com/121864328/225948286-4e540c79-e3b5-412c-83b3-9df8c997bf61.png)


6. terakhir, terdapat fungsi main yang melakukan perulangan while dan menerima input dari pengguna untuk menampilkan, menambahkan, dan menghapus data. 
7. Kemudian, di bawah fungsi "main", dibuat sebuah objek "Laundry" dari kelas "LinkedList" dan menambahkan beberapa data pada awalnya. Setelah itu, fungsi "main" dipanggil untuk memulai program.
output:

![image](https://user-images.githubusercontent.com/121864328/225948989-250ff298-f330-4bff-99f8-e6e10127b09e.png)


