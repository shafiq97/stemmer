#initialize functions for prefixes and suffixes of malay
#use malaysiawordnet.txt for malay dictionary

import re
import nltk
import time
# import malaya
import pandas as pd


with open("malaysiawordnet.txt", "r", encoding="latin-1") as f:
    malaywords = f.read().splitlines()

vowels = ['a','e','i','o','u']

def replace_last(source_string, replace_what, replace_with):
    head, _sep, tail = source_string.rpartition(replace_what)
    return head + replace_with + tail

def b_Prefix(text):
    if text.startswith("ber"):
        if len(text) > 3 and text[3] not in vowels:
            stemmed = text[3:]
        else:
            stemmed = text
    else:
        stemmed = text

    temp = Suffix(stemmed)

    return Verify(temp, text)


def m_Prefix(text):
    if text == 'melanda':
        return 'landa'
    if (text[:6] =='memper'):
        stemmed = text[6:]
    elif (text[:4] =='meny'):
        stemmed = re.sub('meny', 's', text)
    elif (text[:4] =='meng'):
        if (text[4] == 'g' or text[4] == 'k' or text[4] == 'h'):
            stemmed = re.sub('meng', '', text)
        else:
            stemmed = re.sub('meng', 'k', text)   
    elif (text[:3] =='mem'):
        if text[3] == 'b':
            stemmed = re.sub('mem', '', text)
        else:
            stemmed = re.sub('mem', 'p', text)
    elif (text[:3] =='men'):
        if text[3] in vowels:
            stemmed = re.sub('men', 't', text)
        else:
            stemmed = re.sub('men', '', text)
    elif (text[:2] =='me'):
        if text[2] == 'l':
            stemmed = text[2:]
        else:
            stemmed = text
    else:
        stemmed = text
        
    temp = Suffix(stemmed)
    
    return Verify(temp, text)



def p_Prefix(text):
    if text.startswith("peny"):
        stemmed = re.sub("peny", "s", text)
    elif text.startswith("peng"):
        if not text[4] in vowels:
            stemmed = re.sub("peng", "", text)
        else:
            stemmed = re.sub("peng", "k", text)
    elif text.startswith("pem"):
        if text[3] == "b":
            stemmed = re.sub("pem", "", text)
        else:
            stemmed = re.sub("pem", "p", text)
    elif text.startswith("pen"):
        if text[3] in vowels:
            stemmed = re.sub("pen", "t", text)
        elif text[3] in ['d', 'j']:
            stemmed = re.sub("pen", "", text)
        else:
            stemmed = re.sub("pen", "", text)
            stemmed = re.sub("^[cdghjklmnpqrstvwxyz]", "", stemmed)
    elif text.startswith("per"):
        stemmed = re.sub("per", "", text)
    elif text.startswith("pe"):
        stemmed = text[2:]
    else:
        stemmed = text

    temp = Suffix(stemmed)

    return Verify(temp, text)






def di_Prefix(text):
    stemmed = text[2:]
    
    temp = Suffix(stemmed)
    
    return Verify(temp, text)  

def ke_Prefix(text):
    if (text[-2] + text[-1] =='an'):
        stemmed = text[2:-2]
    else:
        stemmed = text[2:]
    
    return Verify(stemmed, text)  

def ter_Prefix(text):
    stemmed = text[3:]
    
    temp = Suffix(stemmed)
    
    return Verify(temp, text) 

def ber_Prefix(text):
    stemmed = text[3:]
    
    temp = Suffix(stemmed)
    
    return Verify(temp, text) 



suffixes = ['kan', 'an', 'i', 'ku', 'mu', 'nya', 'lah']  # Add 'lah' to the list of suffixes

# ...

def Suffix(stemmed):
    try:
        if (stemmed[-3] + stemmed[-2] + stemmed[-1] =='kan'):
            temp = stemmed[:-3]
        elif (stemmed[-3] + stemmed[-2] + stemmed[-1] =='nya'):
            temp = stemmed[:-3]
        elif (stemmed[-2] + stemmed[-1] =='an'):
            temp = stemmed[:-2]
        elif stemmed[-1] == 'i' and len(stemmed)>4:
            temp = replace_last(stemmed, 'i', '')
        elif stemmed[-3:] == 'lah':  # Add case to remove 'lah' suffix
            temp = stemmed[:-3]
        else:
            temp = stemmed
    except:
        temp = stemmed
    
    return temp


#verify whether stemmed word exists in malay dictionary
def Verify(temp, text):
    if (temp in malaywords and len(temp)>3):
        stemmed = temp
    else:
        stemmed = text
        
    return stemmed

