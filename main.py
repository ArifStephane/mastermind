from random import randint

COLORS = {
    1: "Yellow",
    2: "Blue",
    3: "Violet",
    4: "Black",
    5: "White",
    6: "Red",
}
MAX_ATTEMPTS = 10
CODE_LENGTH = 4

def generate_secret_code(code_length):
    return [randint(1, len(COLORS)) for _ in range(code_length)]

def evaluate_guess(guess, secret_code):
    correct_position = 0
    correct_color_wrong_position = 0
    guess_copy = guess.copy()
    secret_code_copy = secret_code.copy()

    for i in range(len(secret_code)):
        if guess_copy[i] == secret_code_copy[i]:
            correct_position += 1
            guess_copy[i] = secret_code_copy[i] = None

    for i in range(len(secret_code)):
        if guess_copy[i] is not None and guess_copy[i] in secret_code_copy:
            correct_color_wrong_position += 1
            secret_code_copy[secret_code_copy.index(guess_copy[i])] = None

    return f"{correct_position} bien placés, {correct_color_wrong_position} mal placés"

def validate_user_input(user_input):
    """Valide l'entrée utilisateur et retourne un tuple (erreur, message)."""
    user_guess = user_input.split()
    if len(user_guess) != CODE_LENGTH:
        return True, f"Le code doit contenir exactement {CODE_LENGTH} chiffres."
    for color in user_guess:
        if not color.isdigit():
            return True, "Seuls les chiffres sont autorisés."
        elif int(color) not in COLORS:
            return True, f"Les chiffres doivent être entre 1 et {len(COLORS)}."
    return False, ""

def main():
    print("Bienvenue dans le jeu Mastermind !\n")
    print("Les couleurs disponibles sont :")
    for num, color in COLORS.items():
        print(f"{num}: {color}")
    print("\nPour commencer, tapez 'start'. Pour quitter, tapez 'exit'.")

    while True:
        user_input = input("\n> ").strip()
        if user_input == "exit":
            break
        elif user_input == "start":
            secret_code = generate_secret_code(CODE_LENGTH)
            print(f"\nLe jeu commence ! Vous avez {MAX_ATTEMPTS} tentatives pour deviner le code secret.")
            for attempt in range(1, MAX_ATTEMPTS + 1):
                print(f"\nTentative {attempt}/{MAX_ATTEMPTS}")
                user_input = input(f"Entrez votre code (ex: 1 2 3 4) : ")
                error, message = validate_user_input(user_input)
                if error:
                    print(f"Erreur : {message}")
                    continue
                user_guess = [int(color) for color in user_input.split()]
                result = evaluate_guess(user_guess, secret_code)
                print(f"Indice : {result}")
                if result.startswith(f"{CODE_LENGTH} bien placés"):
                    print("\nBravo, vous avez gagné !")
                    return
            else:
                print(f"\nDésolé, vous avez épuisé vos {MAX_ATTEMPTS} tentatives.")
                print(f"Le code secret était : {' '.join(map(str, secret_code))}")
        else:
            print("Pour commencer, tapez 'start'.")

if __name__ == "__main__":
    main()
