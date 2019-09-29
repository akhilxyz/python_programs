# ---------------------Program----------------------
print("----------Guess The Number Game-------------")
number=34
count=0
while(True):
    if count>10:
        count+=1
        continue
    user_input = int(input("Enter the number: "))
    if user_input > number:
        print("you Entered Greater number\n")
    elif user_input < number:
        print("you Entered smaller number \n")
    print(f"you have left {9-count} Chances ")
    count += 1
    if user_input==number:
        print("congratulation you guess the right number")
        break




