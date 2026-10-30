total_gaji = 0
for hari in range (1,8):
    print ("hari ke", hari)

    while True :
        lembur = int(input("Masukkan jam lembur (0, 1, 2, 3, 4, 6, 8): "))
        if lembur > 8 :
            print ("jam lembur melebihi batas yang ditentukan!")
        elif lembur < 0 or lembur == 5 or lembur == 7:
            print ("jam lembur tidak sesuai ketentuan!")
        else :
            break

    if lembur >= 3:
        upah_lembur = lembur * 25000
    elif lembur == 4:
        upah_lembur = 100000
    elif lembur == 6:
        upah_lembur = 200000
    elif lembur == 8:
        upah_lembur = 300000
    else:
        upah_lembur = 0

    shift = input("shift malam? (ya/tidak/YA):")
    gaji_pokok = 100000

    if shift == ("ya/YA"):
        upah_malam = 50000
    else :
        upah_malam = 0

    gaji_harian = gaji_pokok + upah_lembur + upah_malam
    total_gaji = total_gaji + gaji_harian

    print ("Gaji hari ini: Rp", gaji_harian)
    
print ("Total gaji selama 7 hari: Rp", total_gaji)