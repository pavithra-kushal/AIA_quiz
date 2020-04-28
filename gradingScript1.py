import hashlib

QUESTIONS = [
        'Question 1) Jenkins is an automation tool used for Continuous Integration (Enter "True" or "False")',
        'Question 2) Which account did you authenticate for ssh login without password?(Enter the account name)',
        'Question 3) Maven is used for version control (Enter "True" or "False")',
        'Question 4) How many types of mechanisms does Jenkins support for SonarQube authentication? (Enter a number)',
        'Question 5) Security Hotspots in SonarQube are the security-sensitive code that require manual review?(Enter "True" or "False") ',
        ]

ANSWERS = [
"b5bea41b6c623f7c09f1bf24dcae58ebab3c0cdd90ad966bc43a45b44867e12b",
"264c8c381bf16c982a4e59b0dd4c6f7808c51a05f64c35db42cc78a2a72875bb",
"fcbcf165908dd18a9e49f7ff27810176db8e9f63b4352213741664245224f8aa",
"e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683",
"b5bea41b6c623f7c09f1bf24dcae58ebab3c0cdd90ad966bc43a45b44867e12b"
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
