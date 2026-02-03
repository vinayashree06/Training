def toi(n,s,aux,d):
    if n==1:
        print(f"Move disk 1 from {s} to {d}")
        return
    toi(n-1,s,d, aux)
    print(f"Move disk {n} from {s} to {d}")
    toi(n-1,aux, s, d)
n = int(input("Enter number of disks:"))
toi(n, 'A', 'B', 'C')
