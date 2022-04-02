import hashlib

counter = 0
flag = 0

print(r"""\

               ___     ___
             .i .-'   `-. i.
           .'   `/     \'  _`.
           |,-../ o   o \.' `|
        (| |   /  _\ /_  \   | |)
         \\\  (_.'.'"`.`._)  ///
          \\`._(..:   :..)_.'//
           \`.__\ .:-:. /__.'/
            `-i-->.___.<--i-'
            .'.-'/.=^=.\`-.`.
           /.'  //     \\  `.\
          ||   ||       ||   ||
          \)   ||       ||  (/
               \)       (/
      
Yb        dP       8                                w            888b.                                         8                        8               
 Yb  db  dP  .d88b 8 .d8b .d8b. 8d8b.d8b. .d88b    w8ww .d8b.    8  .8 .d88 d88b d88b Yb  db  dP .d8b. 8d8b .d88    .d8b 8d8b .d88 .d8b 8.dP .d88b 8d8b 
  YbdPYbdP   8.dP' 8 8    8' .8 8P Y8P Y8 8.dP'     8   8' .8    8wwP' 8  8 `Yb. `Yb.  YbdPYbdP  8' .8 8P   8  8    8    8P   8  8 8    88b  8.dP' 8P   
   YP  YP    `Y88P 8 `Y8P `Y8P' 8   8   8 `Y88P     Y8P `Y8P'    8     `Y88 Y88P Y88P   YP  YP   `Y8P' 8    `Y88    `Y8P 8    `Y88 `Y8P 8 Yb `Y88P 8    
   
                     ,__,
                (/__/\oo/\__(/
                  _/\/__\/\_
                   _/    \_
      """)

passwordHash = input("PLEASE enter md5 hash: ")

wordList = input("ENTER file name|path: ")
      
try:
     passwordFile = open(wordList, "r")
except:
      print("no file found")
      quit()
      
for words in passwordFile:
      encryptedWord = word.encode('utf-8')
      hexConvert = hashlib.md5(encryptedWord.strip()).hexdigest()
      counter += 1
      
      #print(words)
      #print(hexConvert)
      #print(passwordHash)
if hexConvert == passwordHash:print(r"""\ 
  ___                              _    ___             _          _   _ 
 | _ \__ _ _______ __ _____ _ _ __| |  / __|_ _ __ _ __| |_____ __| | | |
 |  _/ _` (_-(_-\ V  V / _ | '_/ _` | | (__| '_/ _` / _| / / -_/ _` | |_|
 |_| \__,_/__/__/\_/\_/\___|_| \__,_|  \___|_| \__,_\__|_\_\___\__,_| (_)
                                                                         
""")
print("Password is " + word)
print("I tried" + counter + "times !")
flag = 1
break

if flag == 0:
print("Password NOT found in the list you provided above")
print("I tried" + counter + "times !")
