
# Some useful command line commands

## Finding information on files 

**list file info in date order**\
`$ ls -lt`

**pipe file names to csv**\
`$ ls -1 > filenames.csv`

**Number of files in folder**\
`$ ls | wc -l` (-l gives line count) 

**Gets the 10 largest files sorted by size (du -h gives disk usage -h tag for readable format) (sort-nr tags is numeric reverse order)**\
`$ du -h | sort -nr | head -n 10`

**Cleaner file size info top 10**\
`$ du -ha ~ | sort -rh | head -10`

**Lists the file types in a directory labelled dir. Loops through file names, gets the 2nd field and sorts for unique file types**\
`$ for file in dir/*; do file "$file" | cut -d: -f 2; done | sort -u`

**Find the location of all files in the current directory (indicated by . prefix) with a certain extension. In this case txt files**\
`$ find . -type f -name "*.txt"`

**Find a file name containing "file_name" in a folder**
`$ find Folder | grep "file_name"`

**List all files in a folder of a certain size**\
`$ find folder_path -type f -size 0 -exec ls {} \;`\
In this case 0, but c for bytes, k for kilobytes, M for megabytes and G for gigabytes\
e.g. +4M (Greater than 4 Megabytes) -4M (Less than 4 Megabytes)\
-type f means it looks at files only not directories , the -exec ls {} \; generates the output on consecutive lines

**Counts the number of text files in a folder that contain a given word - in this example "test"**\
`$ grep -i -l "test" folder_location/*.txt |  wc -l`\
-i makes the grep case insensitive, -l makes the grep output filenames only. This is then piped to wc -l where the -l gives line count

**Basic grep search of the files in a folder that contains a search term**\
`$ grep -i -rl "search_term" folder_file path`

**Getting the names of text files .txt in a folder that contain a word e.g. covid. ggrep on mac seems to work better than grep**\
**if you want to exclude files e.g tableau workbooks use the flag --exclude="*.twb"**\
`$ ggrep -i -l -r --include="*.txt" "Covid" folder_file_path`

**Searches a sql script for text strings that have "scratch" in them, returning just those strings**\
`$ grep -o "scratch\S*" script.sql`
The S keeps matching non-whitespace till you hit the end of the string`

**Gets all the text after hashtags in a file (the_file.py) and sends it to a file the_comments.txt i.e. extracts comments in R and Python files**\
`$ sed -n -e 's/^.*# //p' the_file.py |sed 's/}//'  >> the_comments.txt`

**Gets all the text between the tags < and > in a text file and outputs this to a text file with separating semi-colons**\
`$ grep -oE "<([^>]*)>" input.txt| sed 's/<\(.*\)>/\1;/' > output.txt`

**Get all the text after a standard delimeter given by the -d flag (here '|'). In this example we are extracting the 2nd element after |**\
 `$ cut -d '|' -f2  outputs.tx`

**Showing the unique lines in a file**\
`$ sort file.txt | xargs -n 1| uniq`\
Piping sort to uniq can do this, but may fail with whitespace. Piping the sort to xargs -n 1 first strips out trailing and leading whitespace

**Get x lines after a match (switch -A flag to -B to get x lines before)**\
`$ grep -A x "text_to_match"  file_name`

**To look at a large file, type q to exit**\
`$  less file` 

***Get the first line and line 206 from usage.csv***\
`sed -n -e 1p  -e  206p usage.csv`

## Moving files

**copy all the files in the folder copy_folder to the dest_folder**\
`cp -a /copy_folder/. /dest_folder/`

**copies all the files in one folder with a .doc extension to a new directory labelled backup**\
`$ cp *.doc /filepath/backup`

**copies the results from a grep search of text files for a word (Liverpool in this exampl) to a new directory using ``` ` ` ``` to pass to cp**
```$ cp `ggrep -i -l  -r  --include="*.txt" "Liverpool"` filepath_for_where_files_are_to_go```

## Changing files

**Remove blank lines from a file**\
`$ sed '/^$/d'  file.txt >  file_noblanks.txt`

**Extracting text from pdf files in a folder (requires sudo apt install poppler-utils and sudo apt install calibre)**\
`$ for file in *.pdf; do pdftotext -layout "$file"; done`

**Get the first column of a space separated file.txt**\
`$ awk '{print $1}' file.txt`

## Converting logfile to csv
Converts a logfile writen out to a test file to a csv by extracting columns. Last 3 columns ($5,$6,$7) kept together as they are a datetime\
`$ cat logfile.txt | awk '{print $1 " ,  " $2 " , " $3 " , " $4 ",  " $5 ,$6 ,$7}' > log_test.csv`\
If there are missing values columns may get mixed up. In this case find the columnwidths and set manually e.g.\
awk 'BEGIN{FIELDWIDTHS="9 13 17 4 22"} {print $1 " ,  " $2 " , " $3 " , " $4 ",  " $5 ,$6 ,$7}'

## Viewing files in the terminal 

**For xml**/
`$ xmllint --format file.xml (To output file.xml in nicely printed format add -o pretty_file.xml)`

**For json (For mac install through brew install jq)**
`$ jq '.' file.json`\
`$ jq '.car.color' file.json` extracts the values for the json field car.color if just .car would return the car json
 
## Setting file permissions

`$ chmod (user|group|other) file`

add the numbers below to get permissions
4 stands for "read", 2 stands for "write",1 stands for "execute", and 0 stands for "no permission\
e.g. chmod 700 file gives read, write, execute for the user. No permissions for anyone else

## Linking files 

**Creating a folder called external drive in the home folder that is linked to a mounted external drive called mydisk**\
`$ ln -s /mnt/mydisk/ /home/external_drive`

## Cron jobs 

**Accessing the cron tab to edit the jobs**\
`$ crontab -e`

**Cronjob**\
 `***** /path/to/script.sh`  This version runs every minute\
The order of times is Minute, Hour, Day of Month, Month of Year, Day of week
 
**List cronjobs**
`$ crontab -l`

**Check when the jobs have been run by searching syslog**
`$ grep CRON /var/log/syslog`

## Zipping and Unzipping files 

**unzip a compressed .gz file**\
`$ gunzip archive.gz`

**unzip a tar file**\
`$ tar -xvf file.tar`

**unzip a Winzip file**\
`$ unzip file.zip (To unzip all files in a folder $ unzip "*.zip" )`

**Copies a zipped music file that you have just downloaded to the music folder and unzips**\
`$ cd /c/users/user_name/downloads`\
`$ latest_album=$(ls -Art | tail -n 1)`\
`$ mv $latest_album /c/users/user_name/music`\
`$ cd /c/users/user_name/music`\
`$ unzip $latest_album`\

## Encrypting (and decrypting) files

**encrypt a file with gpg**\
`$ gpg -e -r username file`
 
**and decrypt**\
`$ gpg -o outputfile encryptedfile`

## Backing up 

**Backs up the text file text.txt to the pi external drive. -avz stands for archive (a), verbose (v), z (compress)**\
`$ rsync -avz text.txt pi@ip_address:/mnt/my_external_drive`


## Remote logins 

**Sets up a key for passwordless login**\
(The public key having already been installed on a remote machine with ssh-copy-id)\
`local_machine:~$ ssh-agent $SHELL`\
`local_machine:~$ ssh-add ` Prompts for the password of the SSH key that you want to add\
`local_machine:~$ ssh-agent`\
`local_machine:~$ ssh-add -L`Checks it has been added

## API calls 

**API call returned in nicely formatted json**
`$ curl -s http_request | jq '.'`

## Some programme specific commands 

**Creates a 50 by 50 sprite image from the jpegs in a folder the command is run in, requires ImageMagick to be installed**\
`$ montage "*.jpg" -tile 50x50 -geometry 50x50! sprite.jpg`

**Updating additions to data folder in opencloud from the command line**\
`$ sudo -u www-data php occ files:scan --all`

**Resetting the password of a dockerised nextcloud installation for the user The_user_name** The nextcloud container id is found by running $ docker ps\
`$ docker exec -it docker_container_id  sudo -u abc php /config/www/nextcloud/occ user:resetpassword The_user_name`

**Writing an openstreetmap query to a separate file query.osm and running it from the command line**  
`$ echo "data=node[name=\"Gielgen\"];out;" >query.osm`
`$ wget -O target.osm --post-file=query.osm "http://overpass-api.de/api/interpreter"`

**Command line to inspect sqlite database (Ctrl d to exit)**
`$ sqlite3 database.db`
`sqlite> .tables`  List the tables in the database\
`sqlite> .schema table_name`  List the schema for a table\
`sqlite> .mode line` Viewing mode, others are column and list\
`sqlite> select * from table ;` selects the data in a table\

**Check integrity of jpegs in folder and write details of images that are not ok**\
(i.e. files not containing [OK], using grep -v which returns non matches) to results.txt file\
`$ jpeginfo -c *.jpg | grep -v "[OK]"   >  results.txt`

**Download YouTube videos using youtube-dl which can be installed with homebrew**\
`$ youtube-dl  hyperlink_to_video`

## Logs and logins 

**Most recent log data**
`$ tail /var/log/auth.log`

**Failed password logins**
`$ grep "Failed password" /var/log/auth.log`

## Splitting terminal screen to run two sessions with tmux 

**To get started**
`$ tmux`  

**To split the screen vertically**\
`Type Ctrl and b at the same time, then type %`

**To move betwween the screens** \
`Type Ctrl and b at the same time, and then the arrow key in the direction of the screen you want to move to`

**To close a screen**\
`Type exit or Ctrl and d (If you exit all the screens you will exit tmux`

## Mounting a new drive 
**Create a directory for drive D and mount the drive to directory**
`$ sudo mkdir /mnt/d`\
`$ sudo mount -t drvfs D: /mnt/d`

**and then to access**
`$ cd /mnt/d && ls`

## Cleaning up memory 
**Clean the cache**\
`$ sudo apt-get clean`

**Remove unused dependencies**\
`$ sudo apt-get autoremove -y`

**Finds files taking up a lot of space, pipes the disc usage tool to grep, gets the gigabyte "G" size files**\
`$ sudo du -xh / | grep -P "G\t"`

## Networking
**Gets the details of the devices that are connected to an ip (Need to install nmap)**\
**-sn pings all the addresses on subnet but does not scan open ports**\
`$ nmap -sn xxx.xxx.x.x/24`

**Get the details of the device's internet configuration e.g. what is the ip thw wifi is connected to**\
`$ ifconfig`

**The wifi config for a pi**\
`$ sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`

**Config file to set up a static ip address**\
`$ sudo nano /etc/dhcpcd.conf`

