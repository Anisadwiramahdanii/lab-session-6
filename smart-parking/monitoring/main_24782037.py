"""
Nama file: main_24782037.py

Deskripsi:
    Program utama Smart Parking dengan menu interaktif untuk menambah slot,
    memarkir kendaraan, mengeluarkan kendaraan, dan mengecek status parkir.

Penulis: Anisa Dwi Ramahdani
Tanggal: 26 Maret 2025
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from simulator.parking_simulator import (
    tambah_slot_parkir,
    parkir_kendaraan,
    kendaraan_keluar,
    cek_status_parkir
)

def main():
    """
    Fungsi utama yang menampilkan menu interaktif dan menjalankan
    fitur-fitur parkir sesuai pilihan pengguna.
    """
    while True:
        print("\n=== SMART PARKING SYSTEM ===")
        print("1. Tambah Slot Parkir")
        print("2. Masuk Parkir")
        print("3. Keluar Parkir")
        print("4. Cek Status Parkir")
        print("5. Keluar Program")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            try:
                jumlah = int(input("Masukkan jumlah slot: "))
                jenis = input("Jenis slot untuk apa? (2/4 roda): ")
                if jenis not in ['2', '4']:
                    raise ValueError("Jenis slot tidak valid.")
                tambah_slot_parkir(jumlah, jenis)
            except ValueError as e:
                print(f"Kesalahan input: {e}")
        elif pilihan == '2':
            nomor = input("Masukkan nomor kendaraan: ")
            jenis = input("Jenis kendaraan? (2/4 roda): ")
            parkir_kendaraan(nomor, jenis)
        elif pilihan == '3':
            nomor = input("Masukkan nomor kendaraan yang akan keluar: ")
            kendaraan_keluar(nomor)
        elif pilihan == '4':
            cek_status_parkir()
        elif pilihan == '5':
            print("Terima kasih telah menggunakan Smart Parking!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
