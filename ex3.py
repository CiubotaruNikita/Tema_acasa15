import random

play_again = True

while play_again:
    dice1_value = random.randint(1, 6)
    dice2_value = random.randint(1, 6)
    total_value = dice1_value + dice2_value
    print("Zar 1:", dice1_value)
    print("Zar 2:", dice2_value)
    print("Valoare totală:", total_value)

    play_again_input = input("Doriți să mai jucați? (da/nu): ")
    play_again = play_again_input.lower() == "da"
