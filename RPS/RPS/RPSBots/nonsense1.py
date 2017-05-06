outputs = ["R", "P", "S"]

words = '''Your program will receive input through a global variable called input. input will be a string containing the last move of the opponent ("R", "P", or "S"). In the first round of a match the string will be empty (since the opponent hasn't made any previous moves). Your program will be expected to store its next move in a global variable called output. output should be set to one of the following strings: "R", "P", or "S". Since a RPS match consists of multiple rounds, your program can store local and global variables and use them in subsequent rounds.
Your code must pass system tests before the submission is accepted. The system tests involve compiling the code and testing it on two trial matches. Each trial match consists of 1,000 rounds. System test feedback will be displayed in the console output. Using too much memory or CPU will cause the submission to fail. The CPU limit for a match is five seconds.
By submitting, you agree to release your code into the public domain and waive all copyright. Do not submit copyrighted code that does not belong to you.'''

if input == "" or count == len(words):
    count = 0
else:
    count += 1

output = outputs[ord(words[count])%3]