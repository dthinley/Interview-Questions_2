# Check if s1 and s2 are anagram to each other
def anagram_check(s1, s2):
    # sorted returns a new list and compare
    return sorted(s1) == sorted(s2)

# Check if anagram of t is a substring of s
def question1(s, t):
    for i in range(len(s) - len(t) + 1):
        if anagram_check(s[i: i+len(t)], t):
            return True
    return False

def main():
    print (question1("udacity", "city"))
    print (question1("dorjee", "ee"))
    print (question1("dorjee", "aa"))

if __name__ == '__main__':
    main()  
