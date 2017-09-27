import exercises.solutions.average_solutions as average_solutions


def test(func,input,expected):
    inputStr = str(input)
    expectedStr = str(expected)
    try:
        result = func(input)
        success_or_fail = "SUCCESS!" if result == expected else "***FAILED***"
        print(success_or_fail + " " + func.__name__ + "(" + inputStr + "): got " + str(result) + ", expected " + expectedStr)
    except Exception as error:
        print("***FAILED*** " + func.__name__ + "(" + inputStr + "): exception - " + str(error) + ", expected " + expectedStr)


def run_unit_tests():

    # mean
    list1 = [0,1,2,3,4,5,6,7,8,9,10]
    list2 = [0.3,25,90,1000,3000]

    test(average_solutions.mean, list1, 5)
    test(average_solutions.mean, list2, 823.0600000000001)


    # median
    list3 = [10,20,30]
    list4 = [20, 30]

    test(average_solutions.median, list3, 20)
    test(average_solutions.median, list4, 25)


    # mode
    list5 = [1,2,2,3,3,3]

    test(average_solutions.mode, list5, 3)


    # What other tests could be done?



run_unit_tests()