# ((M[r-s].\s[A-Z]\w*)|(Dr.\s[A-Z].\s[A-Z]\w*)|[A-Z]\w*\s[A-Z]\w*)
import re 
namesRegex = re.compile(r'(M[r-s].\s[A-Z]\w*)|(Mrs.\s[A-Z]\w*)|(Dr.\s[A-Z].\s[A-Z]\w*)|([A-Z]\w*\s[A-Z]\w*)')

for i, line in enumerate(open('names.txt')):
    for match in re.finditer(namesRegex, line):
        print('Found name :' + match.group())

#code piece found via stackoverflow: (https://stackoverflow.com/questions/10477294/how-do-i-search-for-a-pattern-within-a-text-file-using-python-combining-regex)
