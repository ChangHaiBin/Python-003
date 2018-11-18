
print("What is your final exam score?")
input1 = input()
score = int(input1)


if score >= 80:
    print(f"You scored an A. Great job!")

elif score >= 60:
    diff = 80 - score
    print(f"You scored a B. You need {diff} points to reach A.")

elif score >= 40:
    diff = 60 - score
    print(f"You scored a C. You need {diff} points to reach B.")

else:
    diff = 40 - score
    print(f"You scored a D. You need {diff} points to reach C.")



input("Press Enter to continue:")

