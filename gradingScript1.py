import hashlib

QUESTIONS = [
        'Question 1) Jenkins is an automation tool used for Continuous Integration (Enter "True" or "False")',
        'Question 2) Which user account did you authenticate for ssh login without password?(Enter the user name)',
        'Question 3) Maven is used for version control (Enter "True" or "False")',
        'Question 4) How many types of mechanisms does Jenkins support for SonarQube authentication (Hint: You used the "Secret Text" mechanism for this lab)? (Enter a number)',
        'Question 5) Security Hotspots in SonarQube are the security-sensitive code that require manual review?(Enter "True" or "False") ',
        'Question 6) Which one of the recommended fix did you use to fix SQL Injection in the Java code'
        ]

ANSWERS = [
"b5bea41b6c623f7c09f1bf24dcae58ebab3c0cdd90ad966bc43a45b44867e12b",
"424e9661130eeeb05edccfd89125d903eafd4e9f9cdf6d0b88fff6b51df92a69",
"fcbcf165908dd18a9e49f7ff27810176db8e9f63b4352213741664245224f8aa",
"e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683",
"b5bea41b6c623f7c09f1bf24dcae58ebab3c0cdd90ad966bc43a45b44867e12b",
["ef4da95ed347f0bdd0aa94cd3903faf427cef9d8e92fc8137f1222add6b16e96", "fae60eefb2da839840d670d73305614527299eee1270a8500e30eaedf5ad7036"]
]
def check_ans(qno, ans):
    if hashlib.sha256(ans).hexdigest() == ANSWERS[qno] or hashlib.sha256(ans).hexdigest() in ANSWERS[qno]:
        return True
    return False

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