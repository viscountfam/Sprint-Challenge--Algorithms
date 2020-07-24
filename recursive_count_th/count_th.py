'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    # create a substring of two characters
    # if the substring contains th return 1
    # move the window by one character

    # base case
    if len(word) < 2:
        return 0
    window = word[:2]
    if window.startswith("th" or "TH"):
        return 1 + count_th(word[1:])
    else:
        return 0 + count_th(word[1:])
