#!/usr/bin/python
import os,time,subprocess


#Warn User to prep dssd with correct volume.
print("Plese login to D5 and create a volume named fio_test before proceeding")
time.sleep(2)
print("is the volume fio_test created")
yes_no = raw_input()

if yes_no == str("no"):
  exit()
else:
  blk_list = subprocess.check_output ("flood ls -V fio_test -hil", shell=True)
  blk_uid = subprocess.check_output ("flood ls -V fio_test -hil | awk '{print $5}'", shell=True)

  print(blk_list)
  print(blk_uid)
  
  print (" ")
