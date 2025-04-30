"""
Nama file: main_24782037.py

Deskripsi:
    Program utama Smart Parking dengan menu interaktif untuk menambah slot,
    memarkir kendaraan, mengeluarkan kendaraan, mengecek status parkir, dan
    menampilkan riwayat parkir menggunakan generator.

Penulis: Anisa Dwi Ramahdani
Tanggal: 26 Maret 2025
"""

import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from simulator.parking_simulator import (
    tambah_slot_parkir,
    parkir_kendaraan,
    kendaraan_keluar,
    cek_status_parkir
)

# Riwayat parkir kendaraan
riwayat = []


class Vehicle:
    def __init__(self, nomor, entry_time):
        self.nomor = nomor
        self.entry_time = entry_time
        self.exit_time = None

    def keluar(self, exit_time):
        self.exit_time = exit_time

    def __str__(self):
        keluar = self.exit_time.strftime("%Y-%m-%d %H:%M:%S") if self.exit_time else "Belum keluar"
        return f"{self.nomor} | Masuk: {self.entry_time.strftime('%Y-%m-%d %H:%M:%S')} | Keluar: {keluar}"


# Generator untuk riwayat
def generate_riwayat(riwayat_list):
    for kendaraan in riwayat_list:
        yield kendaraan


def tampilkan_riwayat_parkir():
    print("\n=== Riwayat Parkir ===")
    if not riwayat:
        print("Belum ada kendaraan yang masuk.")
    else:
        print("Generate Riwayat Parkir:")
        generator = generate_riwayat(riwayat)
        for kendaraan in generator:
            print(kendaraan)


def main():
    """
    Fungsi utama yang menampilkan menu interaktif dan menjalankan
    fitur-fitur parkir sesuai pilihan pengguna.
    """
    while True:
        print("\n========== SMART PARKING SYSTEM ==========")
        print("1. Tambah Slot Parkir")
        print("2. Masuk Parkir")
        print("3. Keluar Parkir")
        print("4. Cek Status Parkir")
        print("5. Tampilkan Riwayat Parkir")
        print("6. Keluar Program")
        pilihan = input("Pilih menu (1–6): ")

        if pilihan == '1':
            try:
                jumlah = int(input("Masukkan jumlah slot: "))
                jenis = input("Jenis slot untuk apa? (motor/mobil): ")
                if jenis not in ['motor', 'mobil']:
                    raise ValueError("Jenis slot tidak valid.")
                tambah_slot_parkir(jumlah, jenis)
            except ValueError as e:
                print(f"Kesalahan input: {e}")

        elif pilihan == '2':
            nomor = input("Masukkan nomor kendaraan: ")
            jenis = input("Jenis kendaraan? (motor/mobil): ")
            tahun = input("Masukkan tahun masuk (YYYY): ")
            bulan = input("Masukkan bulan masuk (MM): ")
            tanggal = input("Masukkan tanggal masuk (DD): ")

            now = datetime.now()
            try:
                entry = datetime(int(tahun), int(bulan), int(tanggal), now.hour, now.minute, now.second)
            except ValueError:
                print("Format tanggal tidak valid. Menggunakan waktu sekarang.")
                entry = datetime.now()

            print(f"Kendaraan masuk pada: {entry.strftime('%Y-%m-%d %H:%M:%S')}")
            vehicle = Vehicle(nomor, entry)
            parkir_kendaraan(nomor, jenis)
            riwayat.append(vehicle)

        elif pilihan == '3':
            nomor = input("Masukkan nomor kendaraan yang akan keluar: ")
            exit_time = datetime.now()
            for kendaraan in riwayat:
                if kendaraan.nomor == nomor and kendaraan.exit_time is None:
                    kendaraan.keluar(exit_time)
                    break
            kendaraan_keluar(nomor)

        elif pilihan == '4':
            cek_status_parkir()

        elif pilihan == '5':
            tampilkan_riwayat_parkir()

        elif pilihan == '6':
            print("Terima kasih telah menggunakan Smart Parking!")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
