#list of frequencies in alphabetical order
freqs_en = 26*[0] #creating a list of length 26 filled with 0s

with open("secret_files\ch-freq-en.txt", "r") as ch_file:
    for ch_line in ch_file:
        
        ch_line = ch_line.strip() #get rid of the new line \n
        ch_text = ch_line.split("\t") #split the information at the tab \t
        ch_letter = ch_text[0] #take the information at position 0 of text as the letter
        ch_freq = ch_text[1] #take the information at position 1 of text as the frequency

        freqs_en[ord(ch_letter) - 65] = float(ch_freq) #replace the 0 with the frequency at the alphabetical position of the letter

    #loop over all elements and divide by sum
    sum_freqs_en = sum(freqs_en)

    for i in range(len(freqs_en)):
        freqs_en[i] = freqs_en[i] / sum_freqs_en

def getfreq(text):

    freqs = 26*[0] #creating a list of 26 zeros
    text = text.upper()

    for ch in text:
        
        if 'A' <= ch <= 'Z': #ch is indeed a letter
            freqs[ord(ch) - 65] = freqs[ord(ch) - 65] + 1 #adding one to the list at the position of its letter

    #loop over all elements and divide by sum
    sum_freqs = sum(freqs)

    for j in range(len(freqs)):
        freqs[j] = freqs[j] / sum_freqs

    return freqs

def calcdiff(freqs_en, freqs):

    dif = 0 #defining the difference variable

    for k in range(26): #running through the index spot k 26 times
        dif += abs(freqs_en[k] - freqs[k]) #

    return dif

def findshift(txt):

    freqs = getfreq(txt) #defining freqs from before
    dif = 26*[0] #defining empty list for all the differences

    for m in range(26):
        freqs = freqs[1:] + [freqs[0]] #chops off the element at index 0, then adds it at the end

        dif[m] = calcdiff(freqs_en, freqs) #putting the difference at each position in the list 

    optshift = 25 - dif.index(min(dif)) #finding which index the minimum value of the differences list is at

    return optshift

def cipher(text, shift=0):

    deciph = "" #creating an empty string (that will have stuff put into it)
    for ch in text:
        if 'a' <= ch <= 'z':
            deciph += chr(97 + ((ord(ch) + shift - 97) % 26)) #turning the character into ascii, adding the shift and then making sure this stays in the range of the alphabet, then turning it back into a character lol
        elif 'A' <= ch <= 'Z':
            deciph += chr(65 + ((ord(ch) + shift - 65) % 26)) #for capital letters
        else:
            deciph += ch #leaving other characters the same

    print(deciph)

#reading the secret file

secret = input("File name: ") #asking the user which file they want
#raise FileNotFoundError
txt = open(secret, "r").read()

shift = findshift(txt) #getting the variable of what the shift is
cipher(txt, shift) #ciphering the text (from the secret file) and applying the optimal shift

