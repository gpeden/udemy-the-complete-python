"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# your code starts here:
mqf = []

# Read the questions file
qf = open("questions.txt", "r")

maximum = 0
score = 0

for line in qf.readlines():
    maximum += 1

    # split on the equal sign
    line = line.split("=")

    # ask the question and get the answer
    answer = input("{}=".format(line[0].rstrip()))
    correct = line[1].rstrip()

    # check the answer
    if answer == correct:
        score += 1

qf.close()

results = open("results.txt", "w")
results.write("Your final score is {}/{}".format(score, maximum))
results.close()
