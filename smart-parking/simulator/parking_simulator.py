"""
Modul simulasi smart parking dengan dukungan untuk kendaraan roda dua dan roda empat.

Menangani:
- Penambahan slot parkir berdasarkan jenis kendaraan
- Parkir dan keluar kendaraan
- Validasi input dan penanganan kesalahan

Penulis: Anisa Dwi Ramahdani
"""

class Vehicle:
    def __init__(self, nomor):
        self.nomor = nomor

    def __str__(self):
        return self.nomor

class TwoWheeled(Vehicle):
    def __str__(self):
        return f"2R-{self.nomor}"

class FourWheeled(Vehicle):
    def __str__(self):
        return f"4R-{self.nomor}"

class ParkingSlot:
    def __init__(self, purpose):
        self.parking_purpose = purpose  # '2' untuk roda dua, '4' untuk roda empat
        self.occupied = False
        self.vehicle = None

    def is_empty(self):
        return self.vehicle is None

    def park(self, vehicle):
        self.vehicle = vehicle

    def remove_vehicle(self):
        vehicle = self.vehicle
        self.vehicle = None
        return vehicle

# Daftar semua slot parkir
parkiran = []

def tambah_slot_parkir(jumlah, jenis):
    """
    Menambahkan slot parkir berdasarkan jenis kendaraan.
    """
    global parkiran
    if jenis not in ['2', '4']:
        raise ValueError("Jenis slot harus '2' untuk roda dua atau '4' untuk roda empat.")
    for _ in range(jumlah):
        parkiran.append(ParkingSlot(purpose=jenis))
    print(f"{jumlah} slot parkir untuk kendaraan roda {jenis} berhasil ditambahkan.")

def parkir_kendaraan(nomor, jenis):
    """
    Memarkir kendaraan ke slot yang sesuai.
    """
    if jenis == '2':
        kendaraan = TwoWheeled(nomor)
    elif jenis == '4':
        kendaraan = FourWheeled(nomor)
    else:
        print("Jenis kendaraan tidak valid. Gunakan '2' atau '4'.")
        return

    for slot in parkiran:
        if slot.is_empty() and slot.parking_purpose == jenis:
            slot.park(kendaraan)
            print(f"Kendaraan {kendaraan} diparkir di slot {parkiran.index(slot) + 1}.")
            return

    print("Maaf, tidak ada slot kosong yang sesuai.")

def kendaraan_keluar(nomor):
    """
    Mengeluarkan kendaraan dari slot jika ditemukan.
    """
    for slot in parkiran:
        if slot.vehicle and slot.vehicle.nomor == nomor:
            slot.remove_vehicle()
            print(f"Kendaraan {nomor} telah keluar dari slot {parkiran.index(slot) + 1}.")
            return
    print(f"Kendaraan dengan nomor {nomor} tidak ditemukan.")

def cek_status_parkir():
    """
    Menampilkan status semua slot parkir.
    """
    print("\nStatus Parkir:")
    for i, slot in enumerate(parkiran):
        status = str(slot.vehicle) if slot.vehicle else f"Kosong (untuk {slot.parking_purpose} roda)"
        print(f"Slot {i + 1}: {status}")
