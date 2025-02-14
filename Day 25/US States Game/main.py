import pandas,turtle
image=r"Day 25\US States Game\blank_states_img.gif"
data=pandas.read_csv(r"Day 25\US States Game\50_states.csv")
state_list=data.state.to_list()
screen=turtle.Screen()
screen.addshape(image)
turtle.shape(image)
gussed_states=[]
while len(gussed_states)<50:
    answer_state=screen.textinput(title=f"{len(gussed_states)}/50 States Correct", prompt="Enter Name:(enter 'Exit' to exit)").title()
    if answer_state == "Exit" :
        missing=[]
        for state in state_list:
            if state not in gussed_states:
                missing.append(state)
        new_data=pandas.DataFrame(missing)
        new_data.to_csv(r"Day 25\US States Game\sates_to_learn.csv")
        break;
    if answer_state in state_list:
        gussed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state == answer_state]
        t.goto(int(state_data.x.item()),int(state_data.y.item()))
        t.write(answer_state)



screen.exitonclick()

