import time
test = ("How much wood could a woodchuck chuck if a woodchuck could chuck wood")

start = time.time()

print(("typing prompt: ") + test)
ans = input("Match the prompt: ") 
if (ans == test):
    print("Correct!")
    end = time.time()
    print(str(end - start))

else:
    print(("typing prompt: ") + test)
    ans = input("Match the prompt: ")
