import os
import sys
import psutil
import time
import pyautogui
import logging
from pywinauto.application import Application

class PbiRefresher:

   def refresh(self):  

      #defs		
      script_path="C:\\PBIRefresher\\"
      images_path=script_path+"\\Images\\"
      log_file=script_path+"\\Logs\\PBIRefresher.log"	
      proc_file="PBIDesktop.exe"
      pbix_file="Sales.pbix"

      #configure log file
      logging.basicConfig(filename=log_file,filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
      logging.info("Started")
      time.sleep(5)

      # Kill running PBI
      for proc in psutil.process_iter():
         # check whether the process name matches
         if proc.name() == proc_file:
            logging.info("The " + proc_file + " is still in memory! Kill " + proc.name())
            time.sleep(5)
            proc.kill()
            time.sleep(5)

      # open file
      os.system('start "" "' + script_path + pbix_file + '"')
      time.sleep(60) #wait 1 minutes
      
      # refresh data 
      coords = pyautogui.locateOnScreen(images_path + "Refresh.png")
      if coords is not None:
         logging.info("Refreshing...")
         time.sleep(5)
         pyautogui.click(coords[0], coords[1])
         time.sleep(240) #wait 4 minutes to refresh all data
      else:
         logging.info("Error Identifyng Refresh! Exit.")
         time.sleep(5)
         sys.exit(1)
         
      #save
      logging.info("Saving ...")
      time.sleep(5)
      pyautogui.hotkey('ctrl', 's')
      time.sleep(60)

      # publish		
      coords = pyautogui.locateOnScreen(images_path + "Publish.png")
      if coords is not None:
         logging.info("Publishing...")
         time.sleep(5)
         pyautogui.click(coords[0], coords[1])
         time.sleep(5)
      else:
         logging.info("Error Identifyng Publish! Exit.")
         time.sleep(5)
         sys.exit(1) 
      #select the workspace
      coords = pyautogui.locateOnScreen(images_path + "Workspace PRD.png")
      if coords is not None:
         logging.info("Workspace...")
         pyautogui.click(coords[0], coords[1])
         time.sleep(1)
         pyautogui.press('tab') #put focus on ok buttom 
         time.sleep(1)
         pyautogui.press('enter') #press select
         time.sleep(5)
         pyautogui.press('enter') #press replace
         time.sleep(180) #wait more 3 minutes for publishing        
      else:
         logging.info("Error Identifyng Workspace! Exit.")
         time.sleep(5)
         sys.exit(1)	
  
      #close
      logging.info("Closing...")
      time.sleep(5)
      pyautogui.hotkey('alt', 'f4')
      time.sleep(5)
      pyautogui.hotkey('alt', 'f4')
      time.sleep(5)
  
      #make sure pwbi is closed
      for proc in psutil.process_iter():
         if proc.name() == proc_file:
            logging.info("The " + proc_file + "was not closed! Kill " + proc.name())
            time.sleep(5)
            proc.kill()
            time.sleep(5)
  
      logging.info("Finished")
      time.sleep(5)      

if __name__ == "__main__":

      pbix = PbiRefresher()
      pbix.refresh()
      sys.exit(1)
