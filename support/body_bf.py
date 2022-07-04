import requests
import time

file1 = open("../wordlists/naughty_strings.txt")

for line in file1:
    title = line
    content = line
    fee = 2
    
    dict = { var: eval(var) for var in ["title", "content", "fee"] }
    print(dict)