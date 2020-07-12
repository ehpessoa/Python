import os
import psutil
import time
import pyautogui
import logging

class PbiRefresher:

    def refresh(self):  

        # Kill running PBI
        for proc in psutil.process_iter():
           # check whether the process name matches
           if proc.name() == "PBIDesktop.exe":
              logging.info("PBIDesktop.exe is still in memory, killing " + proc.name())
              time.sleep(5)
              proc.kill()
              time.sleep(5)

        # open file
        pbixfile="C:\\Users\\ehpessoa\\ehpessoa.pbix"
        os.system('start "" "' + pbixfile + '"')
        time.sleep(60) #wait 1 minutes

        # refresh data
        logging.info("Refreshing ...")    
        time.sleep(5)  
        pyautogui.click(x=534, y=100) #click on refresh buttom (should be maximized)
        time.sleep(180) #wait 3 minutes to refresh all data

        #save the file
        logging.info("Saving ...")
        time.sleep(5)
        pyautogui.hotkey('ctrl', 's')
        time.sleep(60)

        # publish 
        logging.info("Publishing ...")
        time.sleep(5)
        pyautogui.click(x=852, y=100) #click on publish buttom
        time.sleep(30)
        pyautogui.press('tab')
        pyautogui.press('tab') 
        pyautogui.press('down')  
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('tab') #put focus on ok buttom 
        pyautogui.press('enter') #press ok
        time.sleep(15)
        pyautogui.press('enter') #press replace
        time.sleep(120) #wait more 2 minutes for publishing

        #close the file and program
        logging.info("Closing ...")
        time.sleep(5)
        pyautogui.hotkey('alt', 'f4')
        time.sleep(5)
        pyautogui.hotkey('alt', 'f4')
        time.sleep(5)
        pyautogui.press('enter') #force an enter to save file before exit
        time.sleep(5)

        for proc in psutil.process_iter():
           # check whether the process name matches
           if proc.name() == "PBIDesktop.exe":
              logging.info("PBIDesktop.exe wasnt properly closed, killing " + proc.name())
              time.sleep(5)
              proc.kill()
              time.sleep(5)

if __name__ == "__main__":

    logging.basicConfig(filename='C:\\Users\\ehpessoa\\PBIRefresher\\PBIRefresher.log',filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
    logging.info('Started !')
    time.sleep(5)

    pbix = PbiRefresher()
    pbix.refresh()

    logging.info('Finished !')
    time.sleep(5)
