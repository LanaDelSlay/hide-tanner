## While bank not empty of hides. 

    ## Check if inventory has hides, and both runes store the results so we know wat to grab from bank.

        ## If Yes switch to magic tab.

        ## If No open bank -> Check if bank is on correct tab.

            ## If no click correct bank tab

            ## If Yes Continue to next statement

            ## Grab correct items as stored upon first starting.

            ## Exit bank then go to magic tab.

        ## Cast tan hide until hide is gone.

        ## ^^ Once clicked 5 times (Gets rid of 25/26 of the hides if having the runes in inv w/o rune pouch)

        ## Switch to inventory

        ## Check if any thing is missing

            ## If yes kill the script

            # If no (other than the obvious hides) continue restart 

from utils import *
print('Side bar must be opened.')
sleep(5)
while isHidesInBank():
    itemsNeeded = recordMissingItems()
    print(itemsNeeded)
    outOfAstrals = itemsNeeded.get("astrals")
    outOfNaures = itemsNeeded.get("natures")
    outOfHide = itemsNeeded.get("hides")
    
    if outOfAstrals or outOfNaures:
        print("Ran out of runes")
        quit()
    
    if outOfHide:
        print("No hide")
        openBank()
        sleep(1)
        if isBankOpen():
            if isBankTabOpen():
                continue
            if not isBankTabOpen():
                openBankTab()
            if not isHidesInBank():
                print("NO HIDES, KILLING SCRIPT")
                quit()
            withdrawHides()
            sleep(giveDelay())
            closeBank()
    openMagic()
    print("Magic opened")
    sleep(1)
    castTanHide()
    print("Done tanning")
    openBank()
    print("Depositing")
    sleep(.5)
    if not isBankTabOpen():
        print("Bank tab not open")
        openBankTab()
    print("Attempting to deposit")
    depositHides()
    sleep(.5)
    if not isHidesInBank():
        print("Ran out of hides")
        quit()
    withdrawHides()
    sleep(1)
    closeBank()