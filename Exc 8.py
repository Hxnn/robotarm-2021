from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')
robotArm.speed = 3
# Jouw python instructies zet je vanaf hier:
robotArm.moveRight(), robotArm.grab()
for i in range(8):
    robotArm.moveRight()
robotArm.drop(), robotArm.moveLeft(), robotArm.moveLeft(), robotArm.moveLeft(), robotArm.moveLeft(), robotArm.moveLeft(), robotArm.moveLeft(), robotArm.moveLeft(), robotArm.moveLeft(),

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
# robotArm.moveRight()
# robotArm.grab()
# robotArm.moveLeft()
# robotArm.drop()
