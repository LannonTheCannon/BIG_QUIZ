# This would be a great program to show the students 
# After the for loop practice section so they have a 
# Good understanding of how to apply their own skills 

import pgzrun
import pygame
import secrets

WIDTH = 950
HEIGHT = 645

main_box = pygame.Rect(0, 0, 700, 210)
timer_box = pygame.Rect(0, 0, 110, 210)
answer_box1 = pygame.Rect(0, 0, 365, 125)
answer_box2 = pygame.Rect(0, 0, 365, 125)
answer_box3 = pygame.Rect(0, 0, 365, 125)
answer_box4 = pygame.Rect(0, 0, 365, 125)

main_box.move_ip(50, 40)
timer_box.move_ip(810, 40)
answer_box1.move_ip(50, 308)
answer_box2.move_ip(555, 308)
answer_box3.move_ip(50, 500)
answer_box4.move_ip(555, 500)

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]
score = 0
time_left = 10
lives = 7

q39 = ["",
 "", "", "", "", 2]
q38 = ["",
 "", "", "", "", 2]
q38 = ["",
 "", "", "", "", 3]
q37 = ["",
 "", "", "", "", 4]
q36 = ["",
 "", "", "", "", 1]
q35 = ["",
 "", "", "", "", 1]
q34 = ["",
 "", "", "", "", 3]
q33 = ["",
 "", "", "", "", 1]
q32 = ["",
 "", "", "", "", 3]
q31 = ["",
 "", "", "", "", 3]
q30 = ["",
 "", "", "", "", 1]
q29 = ['',
'','','','',3]
q28 = ['',
'','','','',2]
q27 = ['',
'','','','',3]
q26 = ['',
'','','','',1]
q25 = ['',
'','','','',4]
q24 = ['',
'','','','',2]
q23 = ["",
 "", "", "", "", 2]
q22 = ["",
 "", "", "", "", 3]
q21 = ["",
 "", "", "", "", 4]
q20 = ["",
 "", "", "", "", 1]
q19 = ["",
 "", "", "", "", 1]
q18 = ["",
 "", "", "", "", 3]
q17 = ["",
 "", "", "", "", 1]
q16 = ["",
 "", "", "", "", 3]
q15 = ["",
 "", "", "", "", 3]
q14 = ["",
 "", "", "", "", 1]
q13 = ['',
'','','','',4]
q12 = ['',
'','','','',2]
q11 = ['',
'','','','',3]
q10 = ['',
'','','','',1]
q9 = ['',
'','','','',4]
q8 = ['',
'','','','',2]
q7 = ['',
'','','','',3]
q6 = ['',
'','','','',2]
q5 = ['',
'','','','',4]
q4 = ['',
'','','','',4]
q3 = ['',
'','','','',2]
q2 = ['',
'','','','',1]
q1 = ['',
'','','','',3]

questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11,
             q12, q13, q14, q15, q16, q17, q18, q19, q20,
             q21, q22, q23, q24, q25, q26, q27, q28, q29,
             q30, q31, q32, q33, q34, q35, q36, q37, q38,
             q39]
             
secrets.SystemRandom().shuffle(questions)

question = questions.pop(0)

def draw():
    screen.fill("dim grey")
    screen.draw.filled_rect(main_box, "sky blue")
    screen.draw.filled_rect(timer_box, "sky blue")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "orange")
        screen.draw.textbox(str(time_left), timer_box, color=("black"))
        screen.draw.textbox(question[0], main_box, color=("black"))
        index = 1

    for box in answer_boxes:
        screen.draw.textbox(question[index], box, color=("black"))
        index = index + 1

def game_over():
    global question, time_left
    message = "Game over. You got %s questions correct" % str(score)
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0

def correct_answer():
    global question, score, time_left
    score = score + 1
    if questions:
        question = questions.pop(0)
        time_left = 20
    else:
        print("End of questions")
        game_over()

def on_mouse_down(pos):
    global lives 
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("Clicked on answer " + str(index))
            if index == question[5]:
                print("You got it correct!")
                correct_answer()
            else:
                print('Sorry, Incorrect.')
                lives = lives - 1
            if lives == 0: 
                game_over()
        index = index + 1

def update_time_left():
    global time_left
    if time_left:
        time_left = time_left - 1
    else:
        game_over()

clock.schedule_interval(update_time_left, 1.5)
pgzrun.go()
