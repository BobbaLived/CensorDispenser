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
#TODO Right now this isn't working as intended.  Is censoring every word, not only after second occurence.  Unsure how to fix at the moment.

#Testing Req 4
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
#print(censor3(email_three,negative_words))

def censor4(email, lst1):
    temp = email.split(" ")
    for n in lst1:
        for i, k in enumerate(temp):
            if n in k:
                temp[i] = "CENSOR"
                if i > 1:
                    temp[i - 1] = ""
                if i < len(temp) - 1:
                    temp[i+1] = ""
    return " ".join(temp)

#Test requirement #5
print(censor4(email_four, proprietary_terms + negative_words))


