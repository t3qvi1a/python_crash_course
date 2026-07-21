favorite_languages = {
    'john': ['c', 'cpp'],
    'tina': ['java', 'c'],
    'fave': ['python']
}

for name, languages in favorite_languages.items():
    print(f"{name.title()}'s favorite language are: ")
    for language in languages:
        print(language.title())
