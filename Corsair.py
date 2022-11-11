import time
import pyautogui as gui
import sys
import os

print("""
                 __/___                 ______                      _     
           _____/______|               / ____/___  ______________ _(_)____
   _______/_____\_______\_____        / /   / __ \/ ___/ ___/ __ `/ / ___/
   \              < < <       |      / /___/ /_/ / /  (__  ) /_/ / / /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   \____/\____/_/  /____/\__,_/_/_/
""")
time.sleep(1)

loading = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(30):
    time.sleep(0.1)
    sys.stdout.write("\rloading.... " + loading[i % len(loading)])
    sys.stdout.flush()    
print("\nDone!")
print("clearing...")
time.sleep(1)
os.system('cls')
# =============================================================================
time.sleep(1)
print('welcome back')
time.sleep(1)
print('loading gui...')
time.sleep(1)
os.system('cls')
# =============================================================================
while True:
    gui_prompt = gui.prompt(text='Enter your username\n (make sure text is all lowercase and no spaces!)', title='username')
    if gui_prompt == 'trentblinux':
    
        gui_password = gui.password(text='Enter your password\n', title='password', mask='*')
        if gui_password == 'amongus':
            print('welcome back ' + gui_prompt)
            break
        else:
            gui.alert(text='password not found try again', title='password', button='OK')
    else:
        gui.alert(text='username not found try again', title='username', button='OK')
