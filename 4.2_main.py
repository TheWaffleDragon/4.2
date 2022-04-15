def palindrome(word):
    x = True
    for i in range(0,len(word)):
        if word[i]!=word[-(i+1)]:
            x = False
            break
        else:
            continue
    return x
        
 
# print(palindrome("KASZA"))
# print(palindrome("KAJAK"))
# print(palindrome("K"))           
