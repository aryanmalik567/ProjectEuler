possibilities = 0

for a in range(2):  # Number of £2 coins that can be used
    for b in range(int((200 - 200*a) / 100) + 1):  # No of £1
        for c in range(int((200 - 200*a - 100*b) / 50) + 1):  # No of 50p
            for d in range(int((200 - 200*a - 100*b - 50*c) / 20) + 1):  # No of 20p
                for e in range(int((200 - 200*a - 100*b - 50*c - 20*d) / 10) + 1):  # No of 10p
                    for f in range(int((200 - 200*a - 100*b - 50*c - 20*d - 10*e) / 5) + 1):  # No of 5p
                        for g in range(int((200 - 200*a - 100*b - 50*c - 20*d - 10*e - 5*f) / 2) + 1):  # No of 2p
                            possibilities += 1  # Only 1 possibility for number of 1ps at this stage

print(possibilities)
