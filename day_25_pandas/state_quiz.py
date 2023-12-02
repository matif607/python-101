import turtle as t
import pandas as pd

states_list = pd.read_csv('50_states.csv')
all_states = states_list.state.to_list()

print(all_states)

screen = t.Screen()
tim = t.Turtle()
screen.title('U.S. States Game')

image = 'blank_states_img.gif'
screen.addshape(image)

t.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# t.onscreenclick(get_mouse_click_coor)
# t.mainloop()


guessed_state = []
missed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_state)} guessed', prompt="guess the next state").title()
    if answer_state == 'Exit':
        for state in all_states:
            if state not in guessed_state:
                missed_state.append(state)
        break
    if answer_state in all_states:
        if answer_state not in guessed_state:
            guessed_state.append(answer_state)
            state_data = states_list[states_list.state == answer_state]
            tim.hideturtle()
            tim.penup()
            tim.goto(int(state_data.x), int(state_data.y))
            tim.write(answer_state)

missing_states = pd.DataFrame(missed_state)
missing_states.to_csv('missing_states.csv')

screen.exitonclick()
