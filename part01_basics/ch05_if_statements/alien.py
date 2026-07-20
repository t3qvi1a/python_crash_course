alien_colors = []

for i in range(1, 7):
    alien_colors.append('blue')

for i in range(1, 4):
    alien_colors.append('yellow')

for i in range(1, 3):
    alien_colors.append('red')

alien_colors.append('purple')

total_score = 0
for alien_color in alien_colors:
    if alien_color == 'blue':
        total_score += 1
    elif alien_color == 'yellow':
        total_score += 3
    elif alien_color == 'red':
        total_score += 7
    else:
        total_score += 100


killed_blue = alien_colors.count('blue')
killed_yellow = alien_colors.count('yellow')
killed_red = alien_colors.count('red')
print(f"You killed {killed_blue} blue aliens")
print(f"You killed {killed_yellow} yellow aliens")
print(f"You killed {killed_red} red aliens")
print(total_score)

if alien_colors:
    print('True')




