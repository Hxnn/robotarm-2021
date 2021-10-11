from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
robotArm.speed = 2

# Jouw python instructies zet je vanaf hier:
robotArm.grab()
print(robotArm.scan())
if robotArm.scan() == "red":
    for a in range(9):
        robotArm.moveRight()
        robotArm.drop()

    for b in range(8):
        robotArm.moveLeft()

else:
    robotArm.drop(), robotArm.moveRight(), robotArm.grab(), robotArm.scan()
robotArm.wait()
