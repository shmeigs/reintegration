

#Hackathon social justice project
#Choose your own adventure on the life of an ex-convict
#With Amelia Otto and Sarah Meigs
#Dec 14 2019


print("You have been released from prison. Every Year, approximately 700,000 people are released from US prisons. ")
print("You are either on parole or have finished serving your sentence.")


a = int(input("\n Where do you go? Enter a number 1-5 and we'll tell you: "))
if a == 1:
    print("You go to a halfway house to try to re-integrate into society.")
    job1 = int(input('Pick a number, 1 or 2, to find out if you leave the halfway house and find a job or not:  '))
    if job1 == 1 and financial_bg == 1:
        print("Congratulations! You have found a job.")
    if job1 == 1 and financial_bg == 2:
        print("Congratulations! You have found a job.")
    if job1 == 1 and financial_bg == 3:
        print("Congratulations! You have found a job.")
    if job1 == 2:
        print("Unfortunately, you have violated the rules of your halfway house.")
        print("You will stay in the halfway house longer or return back to prison.")
        lose1 = int(input("Pick  number, 1 or 2, to see where you will end up:  "))
        if lose1 == 1:
            print("You will get to continue your stay in an halfway house for a little bit longer.")
        if lose1 == 2:
            print("You have been sent back to prison for substance abuse.") 
if a == 2:
    print("You have a home to return to. You probably had money when you were convicted and still do.")
    money1 = int(input("Pick a number, 1 or 2, to see if you are financially stable:  "))
    if money1 == 1:
            print("You are financially stable. You have the opportunity to come re-inegrate yourself in society.")
    if money1 == 2:
        print("Unfortunately, you do not have enough money to live on your own. You may be able to get a job.")
        job2=int(input("Pick a number, 1 or 2, to see if you're able to get a job:  "))
        if job2 == 1:
            print("You can get a job!.")
            print("Only 40 percent of employers surveyed were willing to hire someone who had been in prison.")
        if job2 == 2:
            print("Unfortunately, you were unable to get a job. You will need to move into somewhere you can be taken care of before you can find a living of your own.")
            print("After a few years, you may have found a way to leave your situation.")
            streets1 = int(input("Pick a number, 1-3, to see what happens next:  "))
            if streets1 == 1:
                print("You have found a family member/friend to help you out.")
            if streets1 == 2:
                print("Unfortunately, you have been involved with illegal drugs again. You will sadly return to prison.")
            if streets1 == 3:
                print("Sadly your life has come to an end. You have gotten sick and not recovered.")
if a == 3:
    print("You have a friend or relative you can stay with, at least for now.")
    print("After some time, your friend is no longer able to support you. Will you be able to get a job to support yourself?")
    job3 = int(input("Pick a number, 1 or 2, to see if you can find work:  "))
    if job3 == 1:
        print("You can get a job! You will be able to make a living.")
        print("Only 40 percent of employers surveyed were willing to hire someone who had been in prison.")
    if job3 == 2:
        print("Unfortunately, you were unable to get a job. You will need to move into somewhere you can be taken care of before you can find a living of your own.")
        print("After a few years, you may have found a way to leave your situation.")
        streets2 = int(input("Pick a number, 1-3, to see what happens next:  "))
        if streets2 == 1:
            print("You have found a family member/friend to help you out.")
        if streets2 == 2:
            print("Unfortunately, you have been involved with illegal drugs again. You will sadly return to prison.")
        if streets2 == 3:
            print("Sadly your life has come to an end. You have gotten sick and not recovered.")
if a == 4:
    print("You end up homeless, in either a shelter or on the streets.")
    print("People who have been to prison experience homelessness at a rate nearly 7 times higher than the overall population.")
    streets3 = int(input("Pick a number, 1-3, to see what happens next:  "))
    if streets3 == 1:
        print("You have found a family member/friend to help you out.")
    if streets3 == 2:
        print("Unfortunately, you have been involved with illegal drugs again. You will sadly return to prison.")
    if streets3 == 3:
                    print("Sadly your life has come to an end. You have gotten sick and not recovered.")
if a == 5:
    print("You end up in public housing provided by the government.")
    if job4 == 2:
            print("Unfortunately, you were unable to get a job. You will need to move into somewhere you can be taken care of before you can find a living of your own.")
            print("After a few years, you may have found a way to leave your situation.")
            streets1 = int(input("Pick a number, 1-3, to see what happens next:  "))
            if streets4 == 1:
                print("You have found a family member/friend to help you out.")
            if streets4 == 2:
                print("Unfortunately, you have been involved with illegal drugs again. You will sadly return to prison.")
            if streets4 == 3:
                print("Sadly your life has come to an end. You have gotten sick and not recovered.")

