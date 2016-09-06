# sqlcipher-bruteforcer
Grab a big server and decrypt that Database - only python 2.7

## How it works
You write all chars you want, then the script generates all the avaliable options and loops them all until it find's the right key, or sadly end with them all wrong

Just you to know, more that 9 chars will take weeks to decrypt, keep that in mind

## Speed
I Tested it in a t2.micro at AWS with 1 vcpu and 1GB of RAM, it reached about 100 trys per second, in 1 hour it tried around 450 000 key options

## Requirements
This script is only compatible with python2.7 because pysqlcipher is only avaliable for it

1. Run "pip2 install pysqlcipher" to be able to run the script

## Usage
1. Clone this repo into a good server, and by a good server i mean a f*cking fast cpu and 2GB or more of RAM
2. Open the file decrypter.py and modify the 3 configurations at the top
3. Run the scripy with "python2.7 decrypter.py"
4. You will know the corrent key when the script finishes, if the last line of the consoles says "key is 'actual key here'" you had luck if not, try again with a bigger string

## Known Issues
If you get the error "Segmentation fault (core dumped)" it means you don't have enough RAM to run that string lenght, decrease your max_chars values