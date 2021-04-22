import pyinputplus as pyip
import pyinputplus as pyip
import random
import time

number_of_questions = 10
correct_answers = 0

for questionNumber in range(number_of_questions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    prompt = f"#{questionNumber}: {num1} x {num2} = "
    try:
        pyip.inputStr(prompt, allowRegexes=[
                      f'^{num1*num2}$'], blockRegexes=[(".*", "incorrect!")], timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print("Correct!")
        correct_answers += 1
    time.sleep(1)
print(f"Score: {correct_answers} / {number_of_questions}")
