import sys
import pyautogui
import time
import turtle
password_data = {'Wavewind':1357924680,'visiter':123456}
print("______________________________________________")
print(".                                            .")
print(".                                            .")
print(".                                            .")
print(".Welcome  this  Laboratory project  library! .")
print(".            Nice to meet you!               .")
print(".                                            .")
print(".         First:write your login name：      .")
print(".                                            .")
print("______________________________________________")
while True:
    loginname = input()
    if (loginname in password_data):
        print("please write your password(all number):")
        password = int(input())
        if password_data[loginname] == password:
            print("Welcome!"+loginname)
            break
        else:
            print("password have a mistake!You maybe write the mistake login name.Now,write your login name again!")
        
    else:
        print("Sorry,I can't find your login name!Please write your login name again:")
print("Do you want to open Laboratory projects?(Y/N)")
open_answer = str(input())
while open_answer.upper() != 'Y' or open_answer.upper() != 'N':
    if open_answer.upper() == 'Y':
        print("Let's choose your favorite Laboratory project!")
        break
    elif open_answer.upper() == 'N':
        print("Hope to see you again!")
        sys.exit()
    else:
        print("I can't understand your answer,please write your answer again:")
        open_answer = str(input())

print("1.use the keyboard to write")
print("2.full your from")
print("What's your favorite Laboratory project?Please write Laboratory project's number:")
choose_answer = int(input())
if choose_answer == 1:
    speak_word = ''
    pyautogui.moveTo(700, 700, duration=2)
    pyautogui.PAUSE = 0.2
    print("First,you can give me a word!")
    get_word = str(input())
    pyautogui.press(['w', 'e', 'l', 'c', 'o', 'm', 'e'])
    pyautogui.press(' ')
    pyautogui.press(['t', 'o'])
    pyautogui.press(' ')
    pyautogui.press(['t', 'h', 'i', 's'])
    pyautogui.press(' ')
    pyautogui.press(['g', 'a', 'm', 'e'])
    pyautogui.press(' ')
    pyautogui.press(['n', 'o', 'w', '!'])
    pyautogui.press(' ')
    pyautogui.press(['I', ' ', 'a', 'm'])
    pyautogui.press(' ')
    pyautogui.press(['y', 'o', 'u', 'r'])
    pyautogui.press(' ')
    pyautogui.press(['h', 'e', 'l', 'p', 'e', 'r', '!'])
    pyautogui.press(' ')
    pyautogui.press(['n', 'o', 'w', '!'])
    pyautogui.press(' ')
    pyautogui.press(['I', ' ', 'c', 'a', 'n'])
    pyautogui.press(' ')
    pyautogui.press(['.', '.', '.', '.', '.', '.'])
    pyautogui.moveTo(1270, 0, duration=2)
    pyautogui.click(1270, 0, button='left')
    pyautogui.moveTo(700, 500, duration=2)
    pyautogui.click(700, 500, button='right')
    pyautogui.press(['w'])
    pyautogui.moveTo(950, 415)
    pyautogui.moveTo(950, 630, duration=1)
    pyautogui.click(950, 630, button='left')
    pyautogui.moveTo(730, 615, duration=1)
    pyautogui.press('shift')
    pyautogui.press(['l', 'e', 't', ' ', 'u', 's',
                     ' ', 'p', 'l', 'a', 'y', '!'])
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.click(730, 530, button='left')
    pyautogui.press(['I', ' ', 'c', 'a', 'n', ' ', 's', 'p', 'e', 'a',
                     'k', ' ', 'a', 'l', 'l', ' ', 'w', 'o', 'r', 'd', 's', '!'])
    pyautogui.press('enter')
    pyautogui.press(['D', 'o', 'n', "'", 't', ' ', 'y', 'o',
                     'u', ' ', 'b', 'e', 'l', 'i', 'e', 'v', 'e', '?'])
    pyautogui.press('enter')
    for x in get_word:
        speak_word += x
        speak_word += '-'
    '''a=re.split('[_]',speak_word)'''
    pyautogui.typewrite(speak_word)
    pyautogui.press('backspace')
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.press('Capslock')
    pyautogui.press(['o', 'k'])
    pyautogui.press('Capslock')
    pyautogui.press('enter')
    pyautogui.typewrite('wait three seconds')
    time.sleep(3)
    pyautogui.click(900, 170, button='left')
    pyautogui.press(['s'])
    pyautogui.moveTo(730, 600, duration=1)
    pyautogui.click(730, 600, button='right')
    pyautogui.press(['d'])
    pyautogui.press(['y'])

elif choose_answer == 2:
    pen = turtle.Pen()
    answer_number = turtle.numinput('Quesion', 'hou many grades do you need?')
    pen.penup()
    pen.goto(-200, 150)
    pen.write('what things dou you need:')
    pen.goto(-200, 140)
    pen.write('You need'+str(answer_number)+'grades')
    time.sleep(3)
    answer_number_two = turtle.numinput('Quesion', 'hou many apples do you need?')
    pen.goto(-200, 130)
    pen.write('You need'+str(answer_number_two)+'apples')
    time.sleep(3)
    answer_number_three = turtle.numinput('Quesion', 'hou many computers do you need?')
    pen.goto(-200, 120)
    pen.write('You need'+str(answer_number_three)+'computers')
    time.sleep(3)
    answer_number_four = turtle.numinput('Quesion', 'hou many windows do you need?')
    pen.goto(-200, 110)
    pen.write('You need'+str(answer_number_four)+'windows')
    time.sleep(3)
    pen.goto(-200, 100)
    pen.write('but......')
    time.sleep(0.5)
    pen.pensize(15)
    pen.goto(-200, 85)
    pen.write('You only need me now!')
    time.sleep(3)
