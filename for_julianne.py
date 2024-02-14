from common import *

# are you who you say you are?
call_next_script('resources/MFA_name.py')
print("MFA_name.py terminated")
call_next_script('resources/MFA_passkey.py')
print("MFA_passkey.py terminated")
call_next_script('resources/game_start.py')
print("game_start.py terminated")

# question block
call_next_script('questions/q1.py')
print("q1.py terminated")
call_next_script('questions/q2.py')
print("q2.py terminated")
call_next_script('questions/q3.py')
print("q3.py terminated")
call_next_script('questions/q4.py')
print("q4.py terminated")


# good girl block
call_next_script('rewards/congratulations.py')
print("congratulations.py terminated")
call_next_script('rewards/my_heart_laid_bare.py')
print("my_heart_laid_bare.py terminated")
call_next_script('rewards/draw.py')
print("draw.py terminated")

placeholder = input("I love you Julianne, more than words can describe")
