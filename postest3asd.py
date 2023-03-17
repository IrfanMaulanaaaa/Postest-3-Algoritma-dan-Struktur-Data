from prettytable import PrettyTable
import os
x = PrettyTable()
y = PrettyTable()
x.field_names = ["data masuk"]
y.field_names = ["Riwayat data masuk"]
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.history = []

    def display(self):
        if self.head is None:
            os.system('cls')
            print("Datanya Masih Kosong Bang!")
        else:
            n = self.head
            x.clear_rows() 
            y.clear_rows()
            while n is not None:
                os.system('cls')
                x.add_row([n.data]) 
                y.add_row([n.data])
                print(x)
                n = n.next

    def addfirst(self, data):
        data_baru = Node(data)
        if self.head is None:
            self.head = data_baru
        else:
            data_baru.next = self.head
            self.head = data_baru
            

    def deleteFirst(self):
        current_node = self.head
        if self.head is not None:
            self.head = self.head.next
            self.history.append(current_node.data)
    def print_history(self):
        if len(self.history) == 0:
            os.system('cls')
            print("data kosong")
        else:
            os.system('cls')
            print(self.history)
def main():
    while True:
        try:
            print('''Input Data Laundry
            1. Tampil Data
            2. Tambah Data
            3. Hapus Data
            4. Tampilkan Riwayat Data Masuk
            5. Tampilkan Riwayat Data yang dihapus''')
            x = int(input("Masukkan Pilihan (1/2/3/4/5) :"))
            if x == 1:
                Laundry.display()
            elif x == 2:
                a = input("Masukkan Data: ")
                Laundry.addfirst(a)
                y.add_row([a])
            elif x == 3:
                Laundry.deleteFirst()
            elif x == 4:
                print(y)
            elif x == 5:
                Laundry.print_history()
        except:
            print("I N V A L I D")
        
Laundry = LinkedList()
Laundry.addfirst("Muhammad Irfan Maulana: selimut dan Sprei")
Laundry.addfirst("Abdul Rahman: Bantal dan Guling ")
Laundry.addfirst("Muhammad Nabil: Jaket")
Laundry.addfirst("Fauzan Ghifari: Karpet")
main()
