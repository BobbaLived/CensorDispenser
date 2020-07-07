# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

#Requirement #2
def censor1(email):
    if "learning algorithms" in email:
        email = email.replace('learning algorithms', 'CENSORED')
    return email
#print(censor1(email_one))
###


#Requirement #3
def censor2(email,lst):
    for n in lst:
        if n in email:
            email = email.replace(n, 'CENSOR')
    return email
#TESTING REQ 3
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
#print(censor2(email_two,proprietary_terms))
#REQ 3 finished

#Requirement #4
def censor3(email, words):
    k = 0
    for n in words:
        if n in email:
            k += email.count(n)
            if k >= 2:
                email = email.replace(n, "*****")
    return email
#Right now this isn't working as intended.  Is censoring every word, not only after second occurence.  Unsure how to fix at the moment.

#Testing Req 4
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
print(censor3(email_three,negative_words))

#Requirement #5
def censor4(email, lst1, lst2):
    for n in lst1:                                              #For each word in lst1
        if n in email:                                          #If that word is in the email
            pos = email.find(n)                                 #Find the position of the first letter in that word in the email
            pos1 = pos - 2                                      #Now, pos1 is the leftward start of my substring.  Go back two from the first letter of the word
            pos2 = pos + len(n) +1                              #pos2 is my rightward bound of my substring.  Go ahead to the end of the word and beyond the space following
            while email[pos1] != " ":                           #Now, whenever I run into a string again, give me that position (leftward here)
                pos1 += -1
            while email[pos2] != " ":
                pos2 += 1
        temp = email[pos1:pos2]                                 #Now, create a temporary string of the substring here
        email = email.replace(temp, " CENSOR")                  #Now censor that substring out of the email

    # NOW DO THE EXACT SAME THING BUT FOR LST2!

    for n in lst2:
        if n in email:                                          #If that word is in the email
            pos = email.find(n)                                 #Find the position of the first letter in that word in the email
            pos1 = pos - 2                                      #Now, pos1 is the leftward start of my substring.  Go back two from the first letter of the word
            pos2 = pos + len(n) +1                              #pos2 is my rightward bound of my substring.  Go ahead to the end of the word and beyond the space following
            while email[pos1] != " ":                           #Now, whenever I run into a string again, give me that position (leftward here)
                pos1 += -1
            while email[pos2] != " ":
                pos2 += 1
        temp = email[pos1:pos2]                                 #Now, create a temporary string of the substring here
        email = email.replace(temp, " CENSOR")

    return email
#Test requirement #5
print(censor4(email_four, proprietary_terms, negative_words))


