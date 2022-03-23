# PicoCTF 2022: Operation Oni
## Description: 
Instructions were to download a disk image, find the key, and login to a remote machine to find the flag.

## Step 1
Since this challenged presents a disk image the best way for me to approach it would be to take a forensic look by installing the tool, Autopsy.

## Step 2
Next, after Autopsy was finished analyzing I searched for all files on the disk that contained the "*.pub" extension.

![[Pasted image 20220315162649.png]]


After getting a few hits on .pub files I found one called "id_ed25519" which is a common public key signature system. 

Next, I looked for its original directory and from there could see that it was in the systems root directory under the folder "ssh". 

## Step 3

After downloading the key, I opened my command prompt and took the given command:

'ssh -i key_file -p 57690 ctf-player@saturn.picoctf.net'

and inserted the key I found in the Autopsy analysis like so,

'ssh -i id_ed25519 -p 57690 ctf-player@saturn.picoctf.net'

and get the following:

![[Pasted image 20220315163549.png]]

Now that I have remote access to the machine I search the directory, find a text file that holds the flag, and submit it.

![[Pasted image 20220315163712.png]]


