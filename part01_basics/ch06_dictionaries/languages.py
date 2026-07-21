favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

for name in favorite_languages.keys():
    print(f"{name.title()}")

for language in favorite_languages.values():
    print(f"{language.title()}")

for name in sorted(favorite_languages.keys()):
    print(name.title())

print("\n")
for language in set(sorted(favorite_languages.values())):
    print(language.title())

