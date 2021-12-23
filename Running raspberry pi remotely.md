### How to run programmes remotely on the raspberry pi controlled from a home machine, for example for running API calls

To do this the pi should have (secure shell) ssh enabled and screen installed
The pi is controlled from the home machine via the bash shell (Windows 10 has a Linux subsystem that can be installed that will give this)

In the following:

- ip_address = the ip adress of the raspberry pi which is attached to a router
- prog.py = the file you want to transfer to the pi and run, in this case a python programme
- store.db = the database the results of the programme are stored to
- $ is the command prompt cursor of the home machine
- pi $ is the raspberry pi command prompt when logged in via ssh from bash on the home machine


**1. To transfer files that you want to run to the pi using secure copy (scp) from the home machine to the raspberry pi**

`$ scp /mnt/c/Users/file_path_on_homemachine/prog.py  pi@ip_address:destination_file_path_for_file`

The pi will prompt for its ssh password

**2. Log into the pi via ssh**

`$ ssh pi@ip_address`
  input password

**3. From the pi command line install screen if not alrady installed**\
`pi $ sudo apt-get install screen`

Start a screen session which we'll call apicall

`pi $ screen -S apicall`

**4. Change directory to where the programme you want to run is**\
`pi $ cd destination_file_path_for_file`

**5. Run the programme**\
`pi $ python prog.py`

If you want to edit the programme pi $ nano prog.py will allow this

Then log out of/detach from the session using crtl+a and then d

You can now log out of the raspberry pi by typing exit and the programme will keep running in the screen session

**6. To get back into the session from the home machine command line ssh back into the pi**

`$ ssh pi@ip_address and input password`

`pi $ screen -list` To list the processes that have been left running, example of session name  10439.apicall.raspberrypi

`pi $ screen -r 10439.apicall.raspberrypi` will take you back into the session that is running the programme

If you want to end the session Ctrl+a and then :quit will end the session


**7. To retrieve the outputs from the programme which are being stored, in this case a database called store.db on the usb drive on the pi.**
The usb drive may need to be set up on the pi for this to work

`$ scp pi@ip_address:/media/usb/store.db   /mnt/c/Users/filepath_for_database/store.db`

This run from the command line of the home machine will send a copy of the database from the pi back to the home computer
