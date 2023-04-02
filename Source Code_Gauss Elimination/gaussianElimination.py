def gaussian_elimination():
    # Input ukuran matriks
    n = int(input("Masukkan ukuran matriks: "))

    # Input elemen matriks
    A = []
    for i in range(n):
        row = list(map(float, input(f"Masukkan elemen baris ke-{i+1}: ").split()))
        A.append(row)

    # Input elemen vektor hasil
    b = list(map(float, input("Masukkan elemen vektor hasil: ").split()))

    # Eliminasi Gauss
    for k in range(n-1):
        # Cari baris dengan elemen terbesar pada kolom k
        max_index = k
        for i in range(k+1, n):
            if abs(A[i][k]) > abs(A[max_index][k]):
                max_index = i

        # Tukar baris k dengan baris max_index
        if max_index != k:
            A[k], A[max_index] = A[max_index], A[k]
            b[k], b[max_index] = b[max_index], b[k]
            print(f"Tukar baris {k+1} dengan baris {max_index+1}:")
            print_matrix(A, b)

        # Lakukan operasi elemen baris pada matriks A dan vektor b
        for i in range(k+1, n):
            factor = A[i][k] / A[k][k]
            b[i] -= factor * b[k]
            for j in range(k, n):
                A[i][j] -= factor * A[k][j]
            print(f"Operasi pada baris {i+1}:")
            print_matrix(A, b)

    # Substitusi Mundur
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - sum(A[i][j] * x[j] for j in range(i+1, n))) / A[i][i]

    # Output solusi
    print("\nSolusi:")
    for i in range(n):
        print(f"x_{i+1} = {x[i]}")

def print_matrix(A, b):
    for i in range(len(A)):
        row = ["{0: <8.2f}".format(a) for a in A[i]]
        print("| " + " ".join(row) + " | {0: <8.2f} |".format(b[i]))
    print("")
#Contoh penggunaan
gaussian_elimination()