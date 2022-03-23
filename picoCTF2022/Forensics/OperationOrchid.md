# PicoCTF 2022: Operation Orchid
## Description: 
The instructions given were to download a disk image and find the flag.

## Step 1
Since the entity in question is a disk image it is best to open a case in the Sluethkit tool, Autopsy (or Volatility).

## Step 2
After downloading the disk image and opening it in Autopsy, I start my investigation by searching for key phrases such as "flag" and "flag.txt". This method is good to use in CTFs because they are usually labeled like this so that participants can distinguish significant information.

![](/picoCTF2022/images/OpOrchid_images/Operation_Orchid1.png)


After search for these keywords a few important files stand out. The "flag.txt" file doesn't seem to have any useful information in it even though it looks like it should. So I moved on the the "".ash_history" file which presents several commands used in a Linux terminal.

After further examination these commands were used to encrypt and salt the "flag.txt" file using AES-256 and create a new encrypted file, "flag.txt.enc". I can also see that the flag.txt file was shredded with the command: 

'shred -u flag.txt' 

This could be why the flag.txt file that was found did not provide the actual flag.

Another notable piece of information we can gather is that the user used the "-k" switch with a plaintext password.

![](/picoCTF2022/images/OpOrchid_images/Operation_Orchid2.png)

## Step 3

After gathering all the information needed to break into the encrypted file, I download the "flag.txt.enc file", and open a terminal window in my Linux VM.

Since Openssl is used to encrypt the "flag.txt" file I start there and carry out additional research into its decryption functions.

Next, I use what I have learned to put together the terminal command:

'openssl enc -d -aes-256-cbc -in flag.txt.enc -out flag.txt.new'

This command uses the tool Openssl enc and decrypts the input "flag.txt.enc" file and outputs the result to "flag.txt.new".

![](/picoCTF2022/images/OpOrchid_images/Operation_Orchid4.png)

Even though the output in the terminal gives a warning and claims a "bad decrypt" after looking at the input file we can see that they flag has been successfully decrypted.

![](/picoCTF2022/images/OpOrchid_images/Operation_Orchid5.png)


