import random

number_q_picks = int(input("How many quick picks?"))
for line in range(0, number_q_picks):
    for i in range(0, 6):
        calculated_int = random.randint(1, 45)

        if i == 5:
            print(calculated_int, end="\n")

        elif calculated_int < 10 and i < 5:
            print(calculated_int, end="  ")

        else:
            print(calculated_int, end=" ")