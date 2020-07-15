import os
import sys
import psutil
import time
import pyautogui
import logging
import logging.handlers
from logging.handlers import TimedRotatingFileHandler

class PbiRefresher:

   def refresh(self):  

      #defs		
      report_path="C:\\PBIRefresher\\"
      images_path=report_path+"Images\\"
      log_file=report_path+"Logs\\Sales.log"	
      proc_file="PBIDesktop.exe"
      pbix_file="Sales.pbix"

      # create logger
      logger = logging.getLogger(__name__)   
      logger.setLevel(logging.INFO)
      handler = TimedRotatingFileHandler(log_file,when="d",interval=1,backupCount=10)
      formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
      handler.setFormatter(formatter)
      logger.addHandler(handler)
      
      logger.info("Started")
      time.sleep(5)

      # Kill running PBI
      for proc in psutil.process_iter():
         # check whether the process name matches
         if proc.name() == proc_file:
            logger.info("The " + proc_file + " is still in memory! Kill " + proc.name())
            time.sleep(5)
            proc.kill()
            time.sleep(5)

      # open file
      os.system('start "" "' + report_path + pbix_file + '"')
      time.sleep(60) #wait 1 minutes
      
      # check if pwbi desktop is logged
      coords = pyautogui.locateOnScreen(images_path + "Is Signed In.png")
      if coords is not None:
         logger.info("Log in...")
         time.sleep(5)
         pyautogui.click(coords[0], coords[1])
         time.sleep(5)
         coords = pyautogui.locateOnScreen(images_path + "Sign In.png")
         if coords is not None:
            pyautogui.typewrite("everaldo.pessoa@ehpessoa.com")
            time.sleep(5)
            pyautogui.click(coords[0], coords[1])
            time.sleep(30)      
      
      # refresh data 
      coords = pyautogui.locateOnScreen(images_path + "Refresh.png")
      if coords is not None:
         logger.info("Refreshing...")
         time.sleep(5)
         pyautogui.click(coords[0], coords[1])
         time.sleep(240) #wait 4 minutes to refresh all data
      else:
         logger.info("Error Identifyng Refresh! Exit.")
         time.sleep(5)
         sys.exit(1)
         
      #save
      logger.info("Saving ...")
      time.sleep(5)
      pyautogui.hotkey('ctrl', 's')
      time.sleep(60)

      # publish		
      coords = pyautogui.locateOnScreen(images_path + "Publish.png")
      if coords is not None:
         logger.info("Publishing...")
         time.sleep(5)
         pyautogui.click(coords[0], coords[1])
         time.sleep(5)
      else:
         logger.info("Error Identifyng Publish! Exit.")
         time.sleep(5)
         sys.exit(1) 
      #select the workspace
      coords = pyautogui.locateOnScreen(images_path + "Workspace PRD.png")
      if coords is not None:
         logger.info("Workspace...")
         pyautogui.click(coords[0], coords[1])
         time.sleep(1)
         pyautogui.press('tab') #put focus on ok buttom 
         time.sleep(1)
         pyautogui.press('enter') #press select
         time.sleep(5)
         pyautogui.press('enter') #press replace
         time.sleep(180) #wait more 3 minutes for publishing        
      else:
         logger.info("Error Identifyng Workspace! Exit.")
         time.sleep(5)
         sys.exit(1)	
  
      #close
      logger.info("Closing...")
      time.sleep(5)
      pyautogui.hotkey('alt', 'f4')
      time.sleep(5)
      pyautogui.hotkey('alt', 'f4')
      time.sleep(5)
  
      #make sure pwbi is closed
      for proc in psutil.process_iter():
         if proc.name() == proc_file:
            logger.info("The " + proc_file + " was not closed! Kill " + proc.name())
            time.sleep(5)
            proc.kill()
            time.sleep(5)
  
      logger.info("Finished")
      time.sleep(5)      

if __name__ == "__main__":

      pbix = PbiRefresher()
      pbix.refresh()
      sys.exit(1)
