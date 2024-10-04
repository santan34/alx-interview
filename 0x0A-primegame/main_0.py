#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

# Test case 1
# Expected output: "Winner: Ben"
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

# Test case 2
# Expected output: "Winner: Maria"
print("Winner: {}".format(isWinner(3, [1, 2, 3])))

# Test case 3
# Expected output: "Winner: Ben"
print("Winner: {}".format(isWinner(4, [4, 5, 6, 7])))

# Test case 4
print("Winner: {}".format(isWinner(1, [10])))  # Expected output: "Winner: Ben"

# Test case 5
# Expected output: "Winner: Ben"
print("Winner: {}".format(isWinner(2, [8, 9])))

# Test case 6
print("Winner: {}".format(isWinner(0, [])))  # Expected output: "Winner: None"

# Test case 7
# Expected output: "Winner: None"
print("Winner: {}".format(isWinner(2, [1, 1])))

# Test case 8
# Expected output: "Winner: Maria"
print("Winner: {}".format(isWinner(3, [11, 13, 17])))
