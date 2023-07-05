import random

play_again = True

while play_again:
    num_faces = int(input("Introduceți numărul de fețe al zarului: "))
    num_dice = int(input("Introduceți numărul de zaruri: "))


    total_value = 0

    for _ in range(num_dice):
        dice_value = random.randint(1, num_faces)
        total_value += dice_value
        print("Zar:", dice_value)

    print("Valoare totală:", total_value)

    play_again_input = input("Doriți să mai jucați? (da/nu): ")
    play_again = play_again_input.lower() == "da"