# Program code for tower of honoi

def tower_of_honoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_honoi(n-1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_honoi(n - 1, auxiliary, source, destination)

# Example
n = 3 #number of disk
tower_of_honoi(n,'A','B', 'C')