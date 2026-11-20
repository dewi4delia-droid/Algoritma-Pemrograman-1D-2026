undangan = set()
webinar_a = set()
webinar_b = set()

print("DATA PESERTA WEBINAR")

jumlah = int(input("Jumlah undangan: "))

for i in range(jumlah):
    nama = input("Nama undangan: ")
    undangan.add(nama)

jumlah = int(input("Jumlah peserta Webinar A: "))

for i in range(jumlah):
    nama = input("Nama peserta A: ")
    webinar_a.add(nama)

jumlah = int(input("Jumlah peserta Webinar B: "))

for i in range(jumlah):
    nama = input("Nama peserta B: ")
    webinar_b.add(nama)

print("HASIL DATA WEBINAR")
print("Semua peserta:", webinar_a | webinar_b)
print("Hadir di kedua webinar:", webinar_a & webinar_b)
print("Hadir di salah satu webinar:",webinar_a ^ webinar_b)
print("Undangan yang tidak hadir:",undangan - (webinar_a | webinar_b))