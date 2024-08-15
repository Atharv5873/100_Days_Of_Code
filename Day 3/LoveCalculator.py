print("The Love Calculator is calculating your score...")
name1 = input() 
name2 = input() 

name1=name1.lower()
name2=name2.lower()
t=name1.count("t")+name2.count("t")
r=name1.count("r")+name2.count("r")
u=name1.count("u")+name2.count("u")
e=name1.count("e")+name2.count("e")
t1=t+r+u+e
l=name1.count("l")+name2.count("l")
o=name1.count("o")+name2.count("o")
v=name1.count("v")+name2.count("v")
e=name1.count("e")+name2.count("e")
t2=l+o+v+e
score=t1*10+t2
if score <10 or score>90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score>40 and score<50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")