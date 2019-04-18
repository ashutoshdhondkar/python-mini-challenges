# --------------
#Code starts here

def palindrome(num):
    " function that calculates the next palindrome "
    
    num += 1
    while(True):
        string = str(num)
        flag = 0
        for i in range(len(string)):
            if(string[i] != string[len(string) - i - 1]):
                flag = 1
                break
        if(flag == 0 ):
            return num
        else:
            num += 1

print(palindrome(123))
print(palindrome(1331))


# --------------
def a_scramble(str_1,str_2):
    
    str_1 = str_1.replace(" ","").lower()
    str_2 = str_2.replace(" ","").lower()
    
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    dict_1 = dict.fromkeys(list(alphabets),0)
    dict_2 = dict.fromkeys(list(alphabets),0)
    
    if(len(str_1) < len(str_2)):
        min_length = str_1
    else:
        min_length = str_2
    
    flag = True
    for i in str_1:
        dict_1[i] += 1
    
    for i in str_2:
        dict_2[i] += 1
    
    for i in min_length:
        print(i,dict_1[i],dict_2[i])
        if(dict_1[i] < dict_2[i]):
            
            flag = False
            break
    return flag


print(a_scramble("Tom Marvolo Riddle","Voldemort"))
print(a_scramble("ticket","chat"))



# --------------
#Code starts here
def check_fib(num):
    " checks if the specified number is a part of fibonacci sequence "
    
    num1 = 0
    num2 = 1
    fib = []
    fib.append(num1)
    fib.append(num2)
    while(True):
        num3 = num1 + num2
        fib.append(num3)
        num1 = num2
        num2 = num3
        
        if(num3 >= num):
            break
    return num in fib


print(check_fib(145))
print(check_fib(377))


# --------------
#Code starts here
def compress(word):
    " occurences of each word "
    
    word = list(word.lower())
    word.append('0')
    
    string = ""
    i = 0
    while(True):
        count = 1
        
        while(word[i] == word[i+1]):
            count += 1
            i += 1
        string += str(word[i]) + str(count)
        i += 1
        
        if(word[i] == '0'):
            break
    
    return string
    
        
        
        
    

print(compress("abbs"))
print(compress("xxcccdex"))


# --------------
#Code starts here
def k_distinct(string,k):
    string = string.lower()
    
    distinct = list()
    
    for i in string:
        if(i not in distinct):
            distinct.append(i)

            
#     print(distinct)
    
    return (len(distinct) == k)

print(k_distinct('Messoptamia',8))
print(k_distinct('banana',4))


