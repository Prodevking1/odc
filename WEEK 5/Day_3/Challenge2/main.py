import translate

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
translations = {}

for word in french_words:
    translation = translate.translate(word, "en")
    translations[word] = translation

print(translations)