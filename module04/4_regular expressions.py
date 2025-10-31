import re  # importregular expressions module regex regexp

s = "123++4 Asd1234 2323dFdf++ 1234+++ 1231 123asDasd+"

pat1 = "[0-9]{1,}"  # pattern, matches the preceding element [0-9] one or more numbers
res1 = re.findall(pat1, s)  # return list of all matches of pattern "[0-9]{1,}"
print("scans and returns list of matches of pattern '[0-9]{1,}':", res1)

pat2 = r"\d+"  # matches the preceding element d - digit, "+" or (1 or more) numbers
res2 = re.findall(pat2, s)  # scans and returns list of matches of pattern r"\d+"
print("scans and returns list of matches of pattern r'\d+':", res2)

pat3 = r"[0-9]{1,3}"  # r"" (raw string change color),  matches the preceding element [0-9], {1-3} numbers
res3 = re.findall(pat3, s)  # scans and returns list of matches of pattern r"[0-9]{1,3}"
print("scans and returns list of matches of pattern r'[0-9]{1,3}':", res3)

pat4 = r"\d{1,3}"  # matches the preceding element d - digit, {1-3} numbers
res4 = re.findall(pat4, s)  # scans and returns list of matches of pattern r"\d{1,3}"
print("scans and returns list of matches of pattern r'\d{1,3}':", res4)

pat5 = r"[a-zA-Z]{1,3}"  # matches the preceding element [a-zA-Z], {1-3} numbers
res5 = re.findall(pat5, s)  # returns list of matches of pattern r"[a-zA-Z]{1,3}"
print("scans and returns list of matches of pattern r'[a-zA-Z]{1,3}':", res5)

pat6 = r"\++"  # matches the preceding element "\+", "+" or (1 or more) numbers
res6 = re.findall(pat6, s)  # scans and returns list of matches of pattern r"\++"
print("scans and returns list of matches of pattern r'\++':", res6)

pat7 = r"\++"  # matches the preceding element "\+", "+" or (1 or more) numbers
res7 = re.search(pat7, s)  # return match object first elem "\+", or None if not found
print("scans and returns matches of pattern r'\++' re.search(pat7, s):", res7)
print("scans and returns matches of pattern r'\++' res7.group():", res7.group())  # ++
print("scans and returns matches of pattern r'\++' res7.span():", res7.span())  # (3,5)

pat8 = r"\w+"  # matches the preceding [a-zA-Z0-9_], "+" or (1 or more) numbers
res8 = re.search(pat8, s)  # return match object first elem "\w+", or None if not found
print("scans and returns list of matches of pattern r'\w+':", res8)  # (0,3) "123"

"""
scans and returns list of matches of pattern '[0-9]{1,}': ['123', '4', '1234', '2323', '1234', '1231', '123']
scans and returns list of matches of pattern r'\d+': ['123', '4', '1234', '2323', '1234', '1231', '123']
scans and returns list of matches of pattern r'[0-9]{1,3}': ['123', '4', '123', '4', '232', '3', '123', '4', '123', '1', '123']
scans and returns list of matches of pattern r'\d{1,3}': ['123', '4', '123', '4', '232', '3', '123', '4', '123', '1', '123']
scans and returns list of matches of pattern r'[a-zA-Z]{1,3}': ['Asd', 'dFd', 'f', 'asD', 'asd']
scans and returns list of matches of pattern r'\++': ['++', '++', '+++', '+']
scans and returns list of matches of pattern r'\++': <re.Match object; span=(3, 5), match='++'>
scans and returns list of matches of pattern r'\++': ++
scans and returns list of matches of pattern r'\++': (3,5)

"""

s1 = "pi is 3.14 and it's a constant"
pat9 = r"\d+.\d+"  # matches the preceding [0-9.0-9], "+" or (1 or more) numbers
res9 = re.search(pat9, s1)
print("scans and returns list of matches of pattern r'\d+.\d+'", res9)


# The re Module Functions
# Function	                    Description

# re.match(pattern, string)	    Checks for a match only at the beginning of the string. Returns a match object or None.
# re.search(pattern, string)	Scans the entire string for the first match. Returns a match object or None.
# re.findall(pattern, string)	Finds all non-overlapping matches and returns them as a list of strings.
# re.sub(pattern, repl, string)	Substitutes occurrences of a pattern with a replacement string (repl).
# re.split(pattern, string)	    Splits a string by the occurrences of the pattern.
# re.compile(pattern)	        Compiles a regex into a pattern object (useful for reuse or performance).

# Basic Metacharacters
# Pattern	       Description	                                                  Example

# .	     Matches any single character (except newline, by default).	         a.b matches acb, axb
# ^	     Matches the start of the string.	                                 ^Start matches "Start of..."
# $	     Matches the end of the string.	                                     End$ matches "...the End"
# |	     OR operator (alternation).	                                         cat|dog matches "cat" or "dog"
# (...)	 A group. Groups characters together for quantifiers or extraction.	 (abc)+ matches abcabc
# \	     Escapes a special character or starts a special sequence.	         \. matches a literal dot .

# Character Classes
# Pattern  Description	                                    Example

# [abc]	   Matches a, b, or c.	                            [aeiou] matches any vowel
# [a-z]	   Matches any lowercase letter from a to z.	    [A-Za-z] matches any letter
# [0-9]	   Matches any digit from 0 to 9.	                [0-9]{3} matches "123"
# [^abc]   Matches any character not in the set (negation).	[^0-9] matches any non-digit

# Quantifiers (How many times?)
# Quantifier Description	                            Example

# *	         Zero or more occurrences.	                a* matches "", a, aaa
# +	         One or more occurrences.	                a+ matches a, aaa
# ?	         Zero or one occurrence.	                a? matches "" or a
# {n}	     Exactly n occurrences.	                    a{3} matches aaa
# {n,}	     n or more occurrences.                 	a{2,} matches aa, aaa, etc.
# {n,m}	     Between n and m occurrences (inclusive).	a{1,3} matches a, aa, aaa

# Special Sequences (Shorthands)
# Use Raw Strings (r"...") in Python to avoid conflicts with Python's own escape sequences (\n, \t, etc.).

# Sequence	Description	                                                    Equivalent
# \d	    Matches any digit (0-9).	                                    [0-9]
# \D	    Matches any non-digit character.	                            [^0-9]
# \w	    Matches any word character (letter, digit, or underscore).	    [a-zA-Z0-9_]
# \W	    Matches any non-word character.	                                [^a-zA-Z0-9_]
# \s	    Matches any whitespace character (space, tab, newline, etc.).	[\t\n\r\f\v]
# \S	    Matches any non-whitespace character.	                        [^\t\n\r\f\v]
# \b	    Matches a word boundary (start/end of a word).
# \B	    Matches a non-word boundary.
