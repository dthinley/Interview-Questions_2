### Question 2 main function and helper functions.
"""Given a string a, find the longest palindromic substring contained in a.
Your function definition should look like question2(a), and return a string."""
# Gives substrings of s in decending order.
def substrings(s):

    # Declare local variable for the length of s.
    l = len(s)

    # choose range over x-range for python version compatibility.
    for end in range(l, 0, -1):
        for i in range(l-end+1):
            yield s[i: i+end]

# Define palindrome.
def palindrome(s):
    return s == s[::-1]

# Main function.
def Question2(a):
    for l in substrings(a):
        if palindrome(l):
            return l

# Test case.
print (Question2("racecar"))
