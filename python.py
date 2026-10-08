def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Pindahkan piringan 1 dari tiang {source} ke tiang {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Pindahkan piringan {n} dari tiang {source} ke tiang {target}")
    hanoi(n - 1, auxiliary, target, source)

if __name__ == "__main__":
    jumlah_piringan = 3
    print(f"--- Langkah-langkah Penyelesaian Menara Hanoi ({jumlah_piringan} Piringan) ---")
    hanoi(jumlah_piringan, 'A', 'C', 'B')
