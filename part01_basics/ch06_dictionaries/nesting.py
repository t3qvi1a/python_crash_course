alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

i = 0
for alien in aliens:
    # print(f"alien {i}: {alien}")
    print(f"alien {i}'s color: {alien['color']}")
    print(f"alien {i}'s points: {alien['points']}")
    print("\n")
    i += 1
