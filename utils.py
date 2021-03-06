from time import sleep
import pyautogui
import pyclick
from numpy import random
from sympy import E
import os

bankTellerColor = (214, 183, 150)

def move(x,y):
    hc = pyclick.HumanClicker()
    dist = random.normal(loc=2, scale=1, size=(4))
    x = x + abs(dist[0])
    y = y + abs(dist[1])
    x = int(x.item())
    y = int(y.item())
    hc.move((x,y), abs(dist[2]))
    sleep(abs(dist[3]))
    hc.click()

def giveDelay():
    dist = random.normal(loc=3, scale=1, size=(4))
    return abs(dist[0])

def isDragonHideTanned():
    if pyautogui.locateCenterOnScreen('./imgs/tannedHide.png'):
        return True
    else: 
        return False
    
def recordMissingItems():
    checks = {
        "astrals": not isAstralsInInv(), 
        "natures": not isNatureRunesInInv(),
        "hides": isDragonHideTanned()
             }
    return checks

def openMagic():
    if not isMagicOpen():
        magicIcon = pyautogui.locateCenterOnScreen('./imgs/magicUnopened.png')#If the file is not a png file it will not work
        if magicIcon == None:
            print("Magic Icon Not found")
        move(magicIcon.x, magicIcon.y)
    
def isMagicOpen():
    if pyautogui.locateCenterOnScreen('./imgs/magicOpened.png'):
        return True
    else:
        return False
    
def openInventory():
    if not isInventoryOpen():
        magicIcon = pyautogui.locateCenterOnScreen('./imgs/invUnopened.png')#If the file is not a png file it will not work
        move(magicIcon.x, magicIcon.y) 
    
def isInventoryOpen():
    if pyautogui.locateCenterOnScreen('./imgs/invOpened.png'):
        return True
    else:
        return False
    
def openBank():
    if not isBankOpen():
        s = pyautogui.screenshot()
        for x in range(0,1919,5):
            for y in range(0,1079,5):
                if s.getpixel((x, y)) == bankTellerColor: 
                    move(x,y)
                    return
    
def isBankPinPrompt():
    print()
    
def isBankOpen():
    if pyautogui.locateCenterOnScreen('./imgs/bankOpened.png') or pyautogui.locateCenterOnScreen('./imgs/bankTabOpenedText.png'):
        return True
    else:
        return False

def depositHides():
    if isBankOpen():
        move(1477,782)
    
def openBankTab():
  if not isInventoryOpen() and not isBankTabOpen():
    try:
            bankTab = pyautogui.locateCenterOnScreen('./imgs/bankTabUnopened.png')#If the file is not a png file it will not work
            move(bankTab.x, bankTab.y) 
    except AttributeError:
        print("Couldn't find tab")
def isBankTabOpen():
    if pyautogui.locateCenterOnScreen('./imgs/bankTabOpened.png'):
        return True
    else:
        return False
    
def withdrawHides():
    if isHidesInBank():
        hidesInBank = pyautogui.locateCenterOnScreen('./imgs/untannedHideInBank.png')#If the file is not a png file it will not work
        if hidesInBank == None:
            sleep(1)
            hidesInBank = pyautogui.locateCenterOnScreen('./imgs/untannedHideInBank.png')
            if hidesInBank == None:
                print("Cant find hides in bank bro.")
                quit()
        move(hidesInBank.x, hidesInBank.y)
    
def isHidesInBank():
    if pyautogui.locateCenterOnScreen('./imgs/untannedHidesGone.png'):
        return False
    else:
        return True
    
def isAstralsInInv():
    if pyautogui.locateCenterOnScreen('./imgs/astralRune.png'):
        return True
    else:
        return False
    
def isNatureRunesInInv():
    if pyautogui.locateCenterOnScreen('./imgs/natureRune.png'):
        return True
    else:
        return False
    
def closeBank():
    pyautogui.press('escape')
    
def castTanHide():
    hc = pyclick.HumanClicker()
   # spellLocation = pyautogui.locateCenterOnScreen('./imgs/tanHideSpell.png')#If the file is not a png file it will not work
    move(1545,808) ## Meh fix to get working
    while isUntannedHideStillInInv() == True:
        hc.click()
        sleep(3)
        
def isPinUnlockOpen():
    bankPinUnlock = pyautogui.locateCenterOnScreen('./imgs/bankPinUnlock.png')#If the file is not a png file it will not work
    if bankPinUnlock == True:
        return True
    else:
        return False
    
def unlockBank():
    print()
    
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
    
def isUntannedHideStillInInv():
    im = pyautogui.screenshot()
    px = im.getpixel((106, 832))
    if px[0] == 93:
        return False
    if px[0] == 117:
        return True
    else: 
        return "Unknown color - inv prolly empty"