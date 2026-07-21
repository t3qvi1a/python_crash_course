aliens = []

for alien_index in range(30):
    new_alien = {}
    new_alien['color'] = 'green'
    new_alien['speed'] = 'slow'
    new_alien['points'] = 5
    aliens.append(new_alien)
#
# for alien in aliens[:5]:
#     print(alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:6]:
    print(alien)
