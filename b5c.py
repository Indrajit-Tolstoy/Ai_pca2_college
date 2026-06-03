def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return 1

    moves = 0
    moves += tower_of_hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    moves += 1
    moves += tower_of_hanoi(n - 1, auxiliary, source, destination)

    return moves

n = 3
total_moves = tower_of_hanoi(n, 'A', 'B', 'C')
print("Total moves:", total_moves)