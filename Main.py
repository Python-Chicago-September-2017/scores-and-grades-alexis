import random
random_num = random.randint(60,100)
print random_num

def robot_grader():
    for i in range(10):
        random_num = random.randint(60,100)

        if random_num >= 90:
            print "Score: {}; Your grade is A".format(random_num)
        elif random_num >= 80:
            print "Score: {}; Your grade is B".format(random_num)
        elif random_num >= 70:
            print "Score: {}; Your grade is C".format(random_num)
        else:
            print "Score: {}; Your grade is D".format(random_num)

    print "End of the program. Bye!"       

robot_grader() 
