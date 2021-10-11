from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
robotArm.speed = 2
# Jouw python instructies zet je vanaf hier:
robotArm.grab()
print(robotArm.scan())
for i in range(10):
    if robotArm.scan() == "red":
        for a in range(9):
            robotArm.moveRight()
        robotArm.drop()
    else:
        robotArm.drop(), robotArm.moveRight(), robotArm.grab(), robotArm.scan()
        if robotArm.scan() == "red":
            for a in range(8):
                robotArm.moveRight()
            robotArm.drop()
        else:
            robotArm.drop(), robotArm.moveRight(), robotArm.grab(), robotArm.scan()
            if robotArm.scan() == "red":
                for a in range(7):
                    robotArm.moveRight()
                robotArm.drop()
            else:
                robotArm.drop(), robotArm.moveRight(), robotArm.grab(), robotArm.scan()
                if robotArm.scan() == "red":
                    for a in range(6):
                        robotArm.moveRight()
                    robotArm.drop()
                else:
                    robotArm.drop(), robotArm.moveRight(), robotArm.grab(), robotArm.scan()
                    if robotArm.scan() == "red":
                        for a in range(5):
                            robotArm.moveRight()
                        robotArm.drop()
                    else:
                        robotArm.drop(), robotArm.moveRight(), robotArm.grab(), robotArm.scan()
                        if robotArm.scan() == "red":
                            for a in range(4):
                                robotArm.moveRight()
                            robotArm.drop()
                        else:
                            robotArm.drop(), robotArm.moveRight(), robotArm.grab(), robotArm.scan()
                            if robotArm.scan() == "red":
                                for a in range(3):
                                    robotArm.moveRight()
                                robotArm.drop()
                            else:
                                robotArm.drop(), robotArm.moveRight(), robotArm.grab(), robotArm.scan()
                                if robotArm.scan() == "red":
                                    for a in range(2):
                                        robotArm.moveRight()
                                    robotArm.drop()
                                else:
                                    robotArm.drop(), robotArm.moveRight(), robotArm.grab(), robotArm.scan()
                                    if robotArm.scan() == "red":
                                        for a in range(1):
                                            robotArm.moveRight()
                                        robotArm.drop()
for b in range(8):
    robotArm.moveLeft()
robotArm.grab()
if robotArm.scan() == "red":
    for a in range(9):
        robotArm.moveRight()
    robotArm.drop()
else:
    robotArm.drop(), robotArm.moveRight(), robotArm.grab(), robotArm.scan()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
