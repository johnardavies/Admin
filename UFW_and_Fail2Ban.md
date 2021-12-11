## Commands for Ultimate Firewall (UFW) and Fail2Ban and others relating to security

### General commands

**Lists failed logins (-a flag adds the hostname). Piping to more give pagination**\
`$ lastb -a | more`

**Getting information on an ip address**\
`$ whois ip_address`

**Piping failed logins to awk to extract the ip address and write to file**\
`$lastb -a | awk -F " " '{print $NF}' | uniq > failed_login_ips.txt` 

**Shell script to send the logins to whois and write to text file**\
#!/bin/bash\
for domain in \`cat failed_login_ips.txt\`\
do\
   echo $domain\
   \`whois $domain >> failed_ips_info.txt\`\
done


### UFW commands
**Installing ufw**\
`$ sudo apt install ufw`

**Enable ufw to run. The default is to deny all incoming and allow all outgoing**\
`$ sudo ufw enable`

**Check to see if ufw is running**\
`$ sudo ufw status`

**Allow ssh connections**\
`$ sudo ufw allow ssh`

**Allow incoming connections from a specific ip address**\
`$ sudo ufw allow from ip_address  proto tcp to any port 22`

### Fail2ban commands

**Install Fail2Ban**\
`$ sudo apt install fail2ban`

**Check status of Fail2Ban (Note the conf file has to be changed to use UFW**\
`$ sudo systemctl status fail2ban`

**Edit the conditions for blocking an ip address**\
`$ sudo nano /etc/fail2ban/jail.d/ssh.conf`

**See the Fail2Bban jails**\
`$ sudo fail2ban-client status`

**Check the banning status of ssh**\
`$ sudo fail2ban-client status ssh`

**See the list of banned ips**\
`$ sudo tail -f /var/log/fail2ban.log`
