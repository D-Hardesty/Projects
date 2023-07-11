import turtle
from quiz_brain import QuizBrain
from draw_states import DrawState

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(height=590, width=720)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

quiz_brain = QuizBrain()
draw_state = DrawState()

score = 0
game_is_on = True
while game_is_on:
    answer_state = turtle.textinput(title=f"Guess a State, {score}/50!", prompt="Type 'end' if you want to give up.")\
        .title()
    if answer_state == "End" or score == 50:
        game_is_on = False
        break
    is_correct = quiz_brain.check_state(answer_state)
    if is_correct:
        draw_state.write_state(is_correct[0], is_correct[1], answer_state)
        score += 1

turtle.write(f"You scored {score} out of 50, that's {score} more than I got!", align="center", font=("Ariel", 20,
                                                                                                     "normal"))
quiz_brain.game_end()
