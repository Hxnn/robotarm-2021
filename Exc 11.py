from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
robotArm.speed = 2
# Jouw python instructies zet je vanaf hier:
robotArm.grab()
print(robotArm.scan())
for i in range(9):
    if robotArm.scan() == "white":
        robotArm.moveRight(), robotArm.drop(), robotArm.moveRight(), robotArm.grab(), print(robotArm.scan())

    elif robotArm.scan() != "white":
        robotArm.drop(), robotArm.moveRight(), robotArm.grab(), print(robotArm.scan())
