import random

print("===================================================")
print("🎮 Selamat datang di Tebak Angka!")
print("Saya telah memilih angka dari 1 sampai 100.")
print("Bisakah kamu menebaknya? Kamu punya 5 kesempatan!")
print("===================================================\n")

angka_rahasia = random.randint(1, 100)
MAX_TEBakan = 5

for kesempatan in range(1, MAX_TEBakan + 1):
    tebakan = int(input(f"Tebakan ke-{kesempatan}: "))
    
    if tebakan < angka_rahasia:
        print("Terlalu kecil.\n")
    elif tebakan > angka_rahasia:
        print("Terlalu besar.\n")
    else:
        print(f"🎉 Selamat! Kamu menebak dengan benar di percobaan ke-{kesempatan}.")
        break
else:
    print(f"😞 Game Over! Angka yang benar adalah {angka_rahasia}.")
