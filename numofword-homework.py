
import sys


def read_file_content_to_dictionary(file_path):
    with open(file_path) as file: #פותח את הקובץ של הטקסט
        d = {}  #יוצר רשימה בשביל לספור את כמות הפעמים לכל מילה
        for line in file: #רץ על כל שורה בטקסט     
            for word in line.split(): #רץ על כל מילה בשורה ומפצל אותם     
                if word in d:
                    d[word] += 1 #אם המילה כבר נספרה פעם אחת אז הוא מוסיף לה אחד
                else:
                    d[word] = 1 #אחרת המילה לא הופיעה עדיין ברשימה אז מאפס אותה ל1
        return d
    

def sort_words_by_frequency(words_dict, n):
    l = sorted(words_dict.items(), key=lambda item: item[1], reverse=True) #ממיין את כל המילים מהסדר הגבוה לנמוך 
    l = l[:n] #משאיר רק את הטופ של הN  
    sorted_dict = dict(l) # מעביר את הרשימה ל DICTIONARY
    return sorted_dict



if __name__ == "__main__":
    if len(sys.argv) > 1: #בודק שלN יש ערך
        n = int(sys.argv[1]) #N שווה לערך המוזן
    else:
        raise Exception("Please enter N as sys argument") #מחזיר שגיאה אם אין ערך לN


    file_path = "C:/Users/cohen/git/test_words.txt" #יוצר משתנה לקובץ של הטקסט
    d = read_file_content_to_dictionary(file_path)  
    d = sort_words_by_frequency(d, n) 
    for key, value in d.items():
        print("Word: " + key + " Appears " + str(value) + " times") #מדפיס את התוצאה עבור כל אחד מהמילים של הטופ N