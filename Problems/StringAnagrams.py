# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
"""
Write a function that will take 2 strings, decide which characters that it will delete from both strings
to make they anagrams
"""
import math;
string1 = "abccbbd"
def makeAnagram(a, b):
    result = 0
    dict1 = dict()
    dict2 = dict()
    for elem in a:
        if elem not in dict1:
            dict1[elem] = 0
        dict1[elem] +=1
    for elem in b:
        if elem not in dict2:
            dict2[elem] = 0
        dict2[elem]+=1
    unionKeys = dict1.keys() & dict2.keys()
    allKeys = dict1.keys() | dict2.keys()
    deleteKeys = allKeys - unionKeys
    # Delete keys from both dict
    for item in deleteKeys:
        if item in dict1:
            result += dict1[item]
        if item in dict2:
            result += dict2[item]
    for item in unionKeys:
        result += abs(dict1[item] - dict2[item])
    return result
# Complete the isValid function below.
def isValid(s):
    mySet = set(s)
    countList = []
    for item in mySet:
        countList.append(s.count(item))
    print ("Count List: ", countList)
    set2 = set(countList)
    print ("Set2: ", set2)
    if (len(set2)>2): return "NO"
    elif len(set2)==1: return "YES"
    else:
        print ("Testing")
        list2 = list(set2)
        list2 = sorted(list2)
        print ("List2" , list2)
        a= list2[1] - list2[0]
        if (a>1 & (a != list2[1]-1)) | (list2[0]>1):
            print ("Inside1")
            return "NO"
        elif (countList.count(list2[0])>1):
            print ("Inside 2")
            return "NO"
        else:
            return "YES"
s= "ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd"
print(isValid(s))
s1= "aabbcd"
print(isValid(s1))