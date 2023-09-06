# DOCS

First of all we have to understand what type of NFC or RFID the card is using. In order to get this info, I used [libnfc](https://github.com/nfc-tools/libnfc) with an ACR122U NFC reader.

If we try to analyze the card with nfc-list, we get

```
nfc-list uses libnfc 1.8.0
NFC device: ACS / ACR122U PICC Interface opened
1 ISO14443A passive target(s) found
```

This indicates that we a working with a Mifare 1k 13.56 Mhz NFC tag, also known as "Mifare Classic"

### How to clone the tag:

After some quick attempts we can see that the common keys that [mfoc](https://github.com/nfc-tools/mfoc) and [miLazyCracker](https://github.com/nfc-tools/miLazyCracker) use won't work with this card, this means that Ecozona is using a "custom" key (at least).

This is not a big problem, since we can crack the key by ourselves. In order to crack this NFC tag (at least in Arch Linux) we need

- libnfc (git version) from AUR
- build this patched version of mfcuk https://github.com/DrSchottky/mfcuk

After installing everything, we need to run the following commands (with the reader and the card connected to the PC)

```
mfcuk -C -R 0:A -v 2
```

This command will return a key, this is the key A of your card. Now we can run mfoc in order to dump the content of the card, providing the key that we've just found

```
mfoc -O dump.mfd -k KEYFOUNDBYMFCUK
```

In this repo you WON'T find the key in order to avoid the misuse of this PoC.

### How to add money:

- READ THE [DISCLAIMER](https://github.com/sh4tteredd/EcoZonaCharge#big-disclaimer)

- open the dump with an hex editor (ImHex for Windows, HexFiend for Mac or GHex for Linux)

- We will need to focus only to the sector 0, go to the block 2 (offset 0x20), you will see the balance in hex format, for example if you see C8000000 you have to take the C8 part, convert it to decimal and it will return 200 (cents), that is 2€.

- change the value to the amount you want to add, for example if you want to change it to 2,50€ you will change the value to FA000000 with FA that stands for 250 (cents) in hex.

- now the bytes right after (offset 0x24) are a sort of "checksum", that is the result of FFFFFFFF-YOURBALANCE, so if you have 2€ you will have FFFFFFFF-C8000000=37FFFFFF, if you change it to 2.5€ you should write FFFFFFFF-FA000000=05FFFFFF

example of a dump with a balance 0,32€

![example](https://github.com/sh4tteredd/EcoZonaHacking/assets/55893559/f0352a0d-9e3b-4e95-806e-3f8a68ad794c)


- write the dump with 

```
nfc-mfclassic w a u dump.mfd dump.mfd
```
  
  

#### NOTES:

- Remember that the digit of the byte MUST be everytime 8 for example if you change C8000000 to 1F4000000 that has 9 digits, the file won't work.

- There is no check of the UID afaik, so you tecnically clone the original dump to any mifare card even if it doesn't support changeable UID.

- I've a few ecozona cards and the all use the same A and B key.

- The B key has a "secret" meaning, probably also the A card but I can't get it.

- Use these website [Hex Calculator](https://www.calculator.net/hex-calculator.html) [Hexadecimal to Decimal Converter](https://www.rapidtables.com/convert/number/hex-to-decimal.html) for all the conversions and stuff.
