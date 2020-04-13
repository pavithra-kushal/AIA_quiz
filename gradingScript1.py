import hashlib

QUESTIONS = [
        'Question 1) How many vulnerabilities in the project are detected by SonarQube?',
        'Question 2) How many security hotspots in the project are detected by SonarQube?',
        'Question 3) How many bugs in the project are of type severity major?',
        'Question 4) Is it possible to perform SQL injection on the application? Answer (yes/ no) ',
        'Question 5) How many duplicated lines are present in the project? ',
        'Question 6) How difficult is the application is to understand, in terms of cognitive complexity? '
        ]

ANSWERS = [
"3ada92f28b4ceda38562ebf047c6ff05400d4c572352a1142eedfef67d21e662",
"4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce",
"44cb730c420480a0477b505ae68af508fb90f96cf0ec54c6ad16949dd427f13a",
"8a798890fe93817163b10b5f7bd2ca4d25d84c52739a645a889c173eee7d9d3d",
"ad57366865126e55649ecb23ae1d48887544976efea46a48eb5d85a6eeb4d306",
"eb624dbe56eb6620ae62080c10a273cab73ae8eca98ab17b731446a31c79393a"
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
