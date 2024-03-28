### Starting the EC2 instance and logging in

**1. Select and launch an EC2 instance**\
   You are prompted to select an existing key pair or create a new one

**2. If no previous key pair exists create a new one and download the file with the .pem ending e.g. file.pem**

**3. Move the key pair to the project folder**\
   `$cd /mnt/c/users/Name/Downloads`   cd to Downloads folder\
   `$ mv file.pem /home/projectfolder/` Move the key pair file to the project folder
  
**4. Change the permissions on the .pem file**\
   `$ cd /home/projectfolder/` cd to the project folder\
   `$ chmod 400 file.pem`  Change the permissions on the pem file from -rwxrwxrwx  to  -r--------  Visible with ls -l 
   
**5. Logging into the EC2 instance**\
   Select the DNS information from the instance page, it looks like ec2-y-yy-yy-yyy.compute-1.amazonaws.com Where the ys are numnbers, then\
   `$ ssh -i file.pem  ec2-user@XXXXXX` Where the XXXXXX is replaced by the DNS information from the instance page
   
   **! Don't forget to check the prefix - it is ec2-user@ here as this example is Amazon linux, but it varies according to type for Ubuntu it would be ubuntu**
   
**6.Getting to prompt**
    The terminal will prompt with 'Are you sure you want to continue connecting (yes/no)?' 
     Say yes and you will log into the remote EC2 machine. The command line has the form
 `[ec2-user@ip-x-x-x ~]$`
     
### Transferring data to and from instances

**Copying a folder from home machine to ubuntu cloud machine -r not needed if copying a file**

`$ scp -r -i keypair.pem   /c/users/sss/folder  ubuntu@ec2-xx-xxx-xxx-xxx.eu-west-2.compute.amazonaws.com:folder_location`\
`$ scp -r -i keypair.pem         source                            target`

**The order reverses to copy a folder from cloud to local e.g.**

`$ scp -r -i key_pair.pem ubuntu@ec2-xx-xxx-xxx-xxx.eu-west-2.compute.amazonaws.com:~/folder_in_home_directory/ /c/users/xxxx/documents/target_folder`

### Listing, starting and stopping instances

**lists the ec2 instances**
`$ aws ec2 describe-instances`

**example of launching and stopping ec2 from command line**\
`$ aws ec2 run-instances --image-id ami-xxxxxxxx --count 1 --instance-type t2.micro --key-name MyKeyPair --security-group-ids sg-903004f8 --subnet-id subnet-6e7f829e`

**get instances' public ip addresses**\
`$ aws ec2 describe-instances --query "Reservations[*].Instances[*].PublicIpAddress" --output=text`

**stopping instances**
`$ aws ec2 stop-instances --instance-ids example_id`

**deleting instances**
`$ aws ec2 terminate-instances --instance-ids example_id`

### Logging into a Jupyter notebook

cd to the relevant folder in AWS, then run\

`$ jupyter notebook`
   
and the notebook will show at  https://xxxxxx:portnumber where xxxxxx is replaced by the DNS and the portnumber by that used when setting 
Jupyter up

if the pages does not load change the security settings to allow the portnumber as an inbound rule

Custom TCP Rule, TCP, portno

### Setting up jupyter notebook certificate on an ubuntu ec2

**Create an ssl directory**\
`$ mkdir ssl`\
`$ cd ssl`

**Create a certificate**\
`$ openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout "cert.key" -out "cert.pem" -batch`

**Create a jupyter notebook config file**\
`$ jupyter notebook --generate-config`

**Start Ipython shell**\
`$ ipython ` Then in the shell run\
`from IPython.lib import passwd`\
`passwd()` This will prompt for a password and return a hash\
`exit` 

**Edit the jupyter config file**\
`$ nano ~/.jupyter/jupyter_notebook_config.py`

**and paste the following at the start of the file** 

`c=get_config()`\
`c.NotebookApp.certfile=u'/home/ubuntu/ssl/cert.pem'` \
`c.NotebookApp.keyfile=u'/home/ubuntu/ssl/cert.key'`  
`c.IPKernelApp.pylab='inline'`\
`c.NotebookApp.ip='*'`                                                                                                                                             
`c.NotebookApp.open_browser=False` \
`c.NotebookApp.password=The_hash_that_was_generated_earlier` 





