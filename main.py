import random

# Statistik permainan
total_menang = 0
total_kalah = 0
total_tebakan_berhasil = 0

while True:
    print("==================================")
    print("🎮 Selamat datang di Tebak Angka!")
    print("Saya telah memilih angka dari 1 sampai 100.")
    print("Bisakah kamu menebaknya? Kamu punya 5 kesempatan!")
    print("==================================\n")

    angka_rahasia = random.randint(1, 100)
    MAX_TEBakan = 5
    berhasil = False  # untuk mendeteksi apakah menang
    for kesempatan in range(1, MAX_TEBakan + 1):
        while True:
            try:
                tebakan = int(input(f"Tebakan ke-{kesempatan} (1–100): "))
                if tebakan < 1 or tebakan > 100:
                    print("🚫 Masukkan angka antara 1 sampai 100!\n")
                    continue
                break
            except ValueError:
                print("🚫 Input tidak valid! Masukkan angka saja.\n")

        if tebakan < angka_rahasia:
            print("Terlalu kecil.\n")
        elif tebakan > angka_rahasia:
            print("Terlalu besar.\n")
        else:
            print(f"🎉 Selamat! Kamu menebak dengan benar di percobaan ke-{kesempatan}.\n")
            berhasil = True
            total_menang += 1
            total_tebakan_berhasil += kesempatan
            break
    else:
        print(f"😞 Game Over! Angka yang benar adalah {angka_rahasia}.\n")
        total_kalah += 1

    # 🔁 Tanya main lagi
    main_lagi = input("Ingin bermain lagi? (y/n): ").lower()
    if main_lagi != 'y':
        print("\n📊 Statistik Permainan:")
        print(f"✔️ Jumlah menang: {total_menang}")
        print(f"❌ Jumlah kalah: {total_kalah}")
        if total_menang > 0:
            rata_rata = total_tebakan_berhasil / total_menang
            print(f"📈 Rata-rata tebakan saat menang: {rata_rata:.2f}")
        print("👋 Terima kasih sudah bermain. Sampai jumpa!")
        break

print("👍 Program selesai.")
