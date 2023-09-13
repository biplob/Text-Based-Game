answer_yes = ["Yes", "Y", "yes", "y"]
answer_no = ["No", "N", "no", "n"]

print("""
WELCOME! LET'S START THE ADVENTURE

You are standing outside of your house and you see a man running towards you and asking for urgent shelter.

Will you provide shilter to him. (Yes / No)
""")

ans1 = input(">>")

if ans1 in answer_yes:
    print("\nAfter 2 minutes, the Police came to your home, and ask you that whether the thief is in your house or not. Will you (Yes / No)\n")

    ans2 = input(">>")

    if ans2 in answer_yes:
        print("\nYou are an honest person. He was a thief and You won the Game")

    elif ans2 in answer_no:
        print("\nYou helped a thief. Now, got to jail. GAME OVER")

    else:
        print("\nYou typed the wrong input. GOODBYE!")

elif ans1 in answer_no:
    print("\nNow, he is trying to kill you. Will, knock him down? (Yes / No)\n")

    ans3 = input(">>")

    if ans3 in answer_yes:
        print("\nCongrats! He was a thief & You helped the police to catch him with you bravery.")

    elif ans3 in answer_no:
        print("\nSorry You are dead. He was a thief & He killed you. GAME OVER")

    else:
        print("\nYou typed the wrong input. GOODBYE!")

else:
    print("\nYou typed the wrong input. GOODBYE!")


