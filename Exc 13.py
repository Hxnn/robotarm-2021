from RobotArm import RobotArm

# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1, 7)
robotArm.speed = 3
# Jouw python instructies zet je vanaf hier:
robotArm.grab(), robotArm.scan()
if robotArm.scan():
    robotArm.moveRight(), robotArm.drop()
    robotArm.moveLeft(), robotArm.grab(), robotArm.scan()
else:
    robotArm.drop()
if robotArm.scan():
    robotArm.moveRight(), robotArm.moveRight(), robotArm.drop()
    robotArm.moveLeft(), robotArm.moveLeft(), robotArm.grab(), robotArm.scan()
else:
    robotArm.drop()
if robotArm.scan():
    robotArm.moveRight(), robotArm.moveRight(), robotArm.moveRight(), robotArm.drop()
    robotArm.moveLeft(), robotArm.moveLeft(), robotArm.moveLeft(), robotArm.grab(), robotArm.scan()
else:
    robotArm.drop()
if robotArm.scan():
    robotArm.moveRight(), robotArm.moveRight(), robotArm.moveRight(), robotArm.moveRight(), robotArm.drop()
    robotArm.moveLeft(), robotArm.moveLeft(), robotArm.moveLeft(), robotArm.moveLeft(), robotArm.grab(), robotArm.scan()
else:
    robotArm.drop()
if robotArm.scan():
    robotArm.moveRight(), robotArm.moveRight(), robotArm.moveRight(), robotArm.moveRight(), robotArm.moveRight(), robotArm.drop()
    robotArm.moveLeft(), robotArm.moveLeft(), robotArm.moveLeft(), robotArm.moveLeft(), robotArm.moveLeft(), robotArm.grab(), robotArm.scan()
else:
    robotArm.drop()
if robotArm.scan():
    robotArm.moveRight(), robotArm.moveRight(), robotArm.moveRight(), robotArm.moveRight(), robotArm.moveRight(), robotArm.moveRight(), robotArm.drop()
    robotArm.moveLeft(), robotArm.moveLeft(), robotArm.moveLeft(), robotArm.moveLeft(), robotArm.moveLeft(), robotArm.moveLeft(), robotArm.grab(), robotArm.scan()
else:
    robotArm.drop()
if robotArm.scan():
    robotArm.moveRight(), robotArm.moveRight(), robotArm.moveRight(), robotArm.moveRight(), robotArm.moveRight(), robotArm.moveRight(), robotArm.moveRight(), robotArm.drop()
    robotArm.moveLeft(), robotArm.moveLeft(), robotArm.moveLeft(), robotArm.moveLeft(), robotArm.moveLeft(), robotArm.moveLeft(), robotArm.moveLeft(), robotArm.grab(), robotArm.scan()
else:
    robotArm.drop()
if robotArm.scan():
    robotArm.moveRight(), robotArm.moveRight(), robotArm.moveRight(), robotArm.moveRight(), robotArm.moveRight(), robotArm.moveRight(), robotArm.moveRight(), robotArm.moveRight(), robotArm.drop()
    robotArm.moveLeft(), robotArm.moveLeft(), robotArm.moveLeft(), robotArm.moveLeft(), robotArm.moveLeft(), robotArm.moveLeft(), robotArm.moveLeft(), robotArm.moveLeft(), robotArm.grab(), robotArm.scan()
else:
    robotArm.drop()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
