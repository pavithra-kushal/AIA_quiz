import hashlib

QUESTIONS = [
        'Question 1) What is the "Maintainability" rating given by SonarQube? (Enter "A" or "B" or "C" or "D" or "E" or "F" ) ',
        'Question 2) Are there any Code Smells that are Blockers? (Enter "Yes" or "No")',
        'Question 3) Is the code prone to SQL injection? (Enter "Yes" or "No")',
        'Question 4) How many duplicated lines are present in the project? ',
        'Question 5) How difficult is the application to understand, in terms of cognitive complexity? ',
        'Question 6) Does SonarQube give information about test coverages? (Enter "Yes" or "No") ',
        'Question 7) What is the "Review priority" of SQL Injection detected by SonarQube? (Enter "High" or "Medium" or "Low")'
        ]

ANSWERS = [
"284d1e8c4918248233df17642bbb940c001e1fa856c18aab86ba6dbe7813eb13",
"ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb",
"8a798890fe93817163b10b5f7bd2ca4d25d84c52739a645a889c173eee7d9d3d",
"8a798890fe93817163b10b5f7bd2ca4d25d84c52739a645a889c173eee7d9d3d",
"ad57366865126e55649ecb23ae1d48887544976efea46a48eb5d85a6eeb4d306",
"eb624dbe56eb6620ae62080c10a273cab73ae8eca98ab17b731446a31c79393a",
"8a798890fe93817163b10b5f7bd2ca4d25d84c52739a645a889c173eee7d9d3d",
"6ef7c9b15ecdd69083724b84cfdc2100351963488b51b4ea2fcbddf493fbec94"
]
def check_ans(qno, ans):
    return hashlib.sha256(ans).hexdigest() == ANSWERS[qno]

def askQuestion(qno):
    print("\n" +QUESTIONS[qno])
    ans = raw_input(">").strip().lower()

    return check_ans(qno, ans)

def getScore(qno):
    return qno * 10

if __name__=="__main__":
    qno = 0
    while qno != len(QUESTIONS):
        if askQuestion(qno):
            print("That's correct!")
            qno += 1
            print "Your score is ", getScore(qno)
        else:
            print("Wrong answer :(")
            print "Your score is ", getScore(qno)
            exit()
    print("Congrats. You have completed the quiz!!!")