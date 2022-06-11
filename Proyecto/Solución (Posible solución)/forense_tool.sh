#!/bin/bash
clear
echo "Hello $USER. Welcome to Forense Tool."
read -p "Type your suspicious file: " file 
sleep 1
read -sp "Type password encrypted: " password
sleep 1
echo "\n"
read -p "Type your decode file (.cpp,.py,.sh,.java): " dcode
echo "READING CODE AND SCRIPT"
sleep 1
echo "Check if you have the right software..."
sleep 2
sudo apt install steghide -y
echo "Wait a minute..."
sleep 2
clear
echo "OK... Everything is OK..."
sleep 1 
clear
echo "Reading you .jpg file suspicious...$file"
sleep 1
echo "Reading your script...$dcode"
steghide extract -sf $file -p $password
echo "Printing your hidden file..."
sleep 1 
echo "\n"
cat binary.txt
python3 $dcode
sleep 3
clear
echo "Your hidden message; "
rm roma.txt
sleep 1
cat japon.txt
echo "\n"
sleep 3
rm binary.txt
rm japon.txt
exit