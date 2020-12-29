from robot.robot import Robot

robot = Robot()
try:
    robot.open()
    robot.send_line('2 + 2')
    robot.send_line('2 + 3')
    robot.send_line('positive ← {⍵/⍨⍵>0}')
    robot.send_line('positive ¯3 + ⍳5')
    robot.send_line(')ed positive')
    robot.screenshot('ed.png')
    robot.close_editor()
    robot.send_line(')off')
finally:
    robot.close()