import pyautogui
import random
import dis


def move(pause=2):
    """ This function will move the cursor until user will move it by himself or herself """
    pyautogui.PAUSE = pause
    width, height = pyautogui.size()
    c_w, c_h = width/2, height/2
    random.seed(0)
    while True:
        d_w = random.randint(-width/10, width/10)
        d_h = random.randint(-height/10, height/10)
        center_p_delta = (c_w+d_w, c_h+d_h)
        pyautogui.moveTo(center_p_delta, duration=0.2)
        if center_p_delta != pyautogui.position():
            print(center_p_delta, pyautogui.position(), center_p_delta == pyautogui.position())
            break


if __name__ == '__main__':
    # print(dis.dis(move))
    move()
