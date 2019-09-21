# This is a Python Program to find the longest common substring between two string's

from difflib import SequenceMatcher

def longestCommonSubsequence(str1, str2):
    seqMatch = SequenceMatcher(None, str1, str2)
    match = seqMatch.find_longest_match(0, len(str1), 0, len(str2))
    if (match.size != 0):
        return str1[match.a:match.a + match.size]
    else:
        print("No common substring between two strings.")

print(longestCommonSubsequence("hamster", "start"))