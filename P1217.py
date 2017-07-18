#Zari McFadden - 2/13/16
#P1217 - Caesar Deciphered
#Write a program that accepts a ciphertext then automatically deciphers it by
#testing every shift value to find the value that yields the highest confidence.

def main():
    word2 = []                          #create empty words list
    
    words = open('words.txt', 'r')      #open words.txt file         

    for word in words:                  #loop through words in file
        word1 = word.upper()            #uppercase the words
        word2.append(word1.rstrip())    #append rstripped the words to list
        
    words.close()                       #close the file

    word3 = word2[:]                    #create a copy of the list
    
    A = []                              #create an empty list for A
    A1 = []                             #create an empty list for A1
    S = []                              #create an empty list for S
    
    for letter in range(65, 91):        #append the letters to A
        A.append(chr(letter))

    e = 1                               #set e to 1
    count = 0                           #set count to 0 
    greatest = 0                        #set greatest to 0
    greatest_word = ''                  #greatest_word is empty string
    
    s = input("Enter a string: ")       #user enters a string
    s1 = s.upper()                      #uppercase letters in string

    while e <= 26:
        
        for i in range(e, len(A)):      #if encrytion key is positive
            A1.append(A[i])             #shift alphabet up
        for x in range(e):
            A1.append(A[x])

            
        A = ''.join(A)                  #turn A into a string
        
        for char in s1:                 #search char in string
            if char in A:               #if char in A
                y = A.find(char)        #find index of char in A
                S.append(A1[y])         #append new letter to S

            else:
                S.append(char)          #append spaces/ other char

        s2 = ''.join(S)                 #turn S into a string
        s3 = s2.split()                 #split string

        for element in s3:              #loop through s3
            for word in word3:          #loop through words3
                if element == word:     #if element == word
                    count += 1          #increment the count
                    
        confidence = count/len(s3)      #find confidence percentage

        if confidence > greatest:       #if confidence > greatest
            greatest = confidence       #set greatest to confidence
            greatest_word = s2          #set greatest word to string equivalent
            count = 0                   #reset the count

            
            
        A1.clear()                      #clear the A1 list
        S.clear()                       #clear the S list

        e += 1                          #increment e

    #print string with greatest confidence and confidence percentage
    #print("Decryption key:", e)
    print(greatest_word)
    print("Confidence:", format(greatest, '.0%'))


main()
