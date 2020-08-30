def number2words(n):
    """ works for numbers between 0 and 999999 """
    units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
             "nineteen"]
    tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    dic1 = dict(zip([str(i) for i in range(10)], units))
    dic2 = dict(zip([str(i) for i in range(10)], teens))
    dic3 = dict(zip([str(i) for i in range(10)], tens))
    x = n
    if x.isdigit == False:
        return False
    if x < 100:
        printX = ''
        if x > 19:
            if x / 10 == 0:
                printX = dic1[str(x)]
            elif x % 10 == 0:
                printX = dic3[str(x / 10 - 2)]
            else:
                printX = dic3[str(x / 10 - 2)] + '-' + dic1[str(x % 10)]
        if x < 20:
            if x > 9:
                printX = dic2[str(x % 10)]
            else:
                printX = dic1[str(x)]
        return printX
    if x in range(100, 1000):
        printX = ''
        if x / 10 == 0 and x % 10 == 0:
            printX = dic1[str(x / 10 / 10)]
        elif x / 10 == 0 and x % 10 != 0:
            printX = dic1[str(x / 10 / 10)] + ' hundred ' + dic1[str(x % 10)]
        elif x / 10 != 0:
            if x / 10 % 10 == 1:
                printX = dic1[str(x / 10 / 10)] + ' hundred ' + dic2[str(x / 10 % 10)]
            elif x / 10 % 10 != 1 and x % 10 == 0:
                printX = dic1[str(x / 10 / 10)] + ' hundred ' + dic3[str(x / 10 % 10 - 2)]
            elif x / 10 % 10 != 1 and x % 10 != 0:
                printX = dic1[str(x / 10 / 10)] + ' hundred ' + dic3[str(x / 10 % 10 - 2)] + '-' + dic1[
                    str(x % 10)]
        return printX
    if x > 1000:
        printX1 = ''
        printX2 = ''
        x1 = x % 1000
        if x1 in range(100, 1000):
            if x1 / 10 == 0 and x1 % 10 == 0:
                printX1 = dic1[str(x1 / 10 / 10)]
            elif x1 / 10 == 0 and x1 % 10 != 0:
                printX1 = dic1[str(x1 / 10 / 10)] + ' hundred ' + dic1[str(x1 % 10)]
            elif x1 / 10 != 0:
                if x1 / 10 % 10 == 1:
                    printX1 = dic1[str(x1 / 10 / 10)] + ' hundred ' + dic2[str(x1 / 10 % 10)]
                elif x1 / 10 % 10 != 1 and x1 % 10 == 0:
                    printX1 = dic1[str(x1 / 10 / 10)] + ' hundred ' + dic3[str(x1 / 10 % 10 - 2)]
                elif x1 / 10 % 10 != 1 and x1 % 10 != 0:
                    printX1 = dic1[str(x1 / 10 / 10)] + ' hundred ' + dic3[str(x1 / 10 % 10 - 2)] + '-' + dic1[
                        str(x1 % 10)]
        if x1 < 100:
            if x1 > 19:
                if x1 / 10 == 0:
                    printX1 = dic1[str(x1)]
                elif x1 % 10 == 0:
                    printX1 = dic3[str(x1 / 10 - 2)]
                else:
                    printX1 = dic3[str(x1 / 10 - 2)] + '-' + dic1[str(x1 % 10)]
            if x1 < 20:
                if x1 > 9:
                    printX1 = dic2[str(x1 % 10)]
                else:
                    printX1 = dic1[str(x1)]
        x2 = x / 1000
        if x2 < 100:
            if x2 > 19:
                if x2 / 10 == 0:
                    printX2 = dic1[str(x2)]
                elif x2 % 10 == 0:
                    printX2 = dic3[str(x2 / 10 - 2)]
                else:
                    printX2 = dic3[str(x2 / 10 - 2)] + '-' + dic1[str(x2 % 10)]
            if x2 < 20:
                if x2 > 9:
                    printX2 = dic2[str(x2 % 10)]
                else:
                    printX2 = dic1[str(x2)]

        if x2 in range(100, 1000):
            if x2 / 10 == 0 and x2 % 10 == 0:
                printX2 = dic1[str(x2 / 10 / 10)]
            elif x2 / 10 == 0 and x2 % 10 != 0:
                printX2 = dic1[str(x2 / 10 / 10)] + ' hundred ' + dic1[str(x2 % 10)]
            elif x2 / 10 != 0:
                if x2 / 10 % 10 == 1:
                    printX2 = dic1[str(x2 / 10 / 10)] + ' hundred ' + dic2[str(x2 / 10 % 10)]
                elif x2 / 10 % 10 != 1 and x2 % 10 == 0:
                    printX2 = dic1[str(x2 / 10 / 10)] + ' hundred ' + dic3[str(x2 / 10 % 10 - 2)]
                elif x2 / 10 % 10 != 1 and x2 % 10 != 0:
                    printX2 = dic1[str(x2 / 10 / 10)] + ' hundred ' + dic3[str(x2 / 10 % 10 - 2)] + '-' + dic1[
                        str(x2 % 10)]
        printX = printX2 + ' thousand ' + printX1
        return printX



"""
words = "zero one two three four five six seven eight nine" + \
" ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty" + \
" thirty forty fifty sixty seventy eighty ninety"
words = words.split(" ")

def number2words(n):
    if n < 20:
        return words[n]
    elif n < 100:
        return words[18 + n // 10] + ('' if n % 10 == 0 else '-' + words[n % 10])
    elif n < 1000:
        return number2words(n // 100) + " hundred" + (' ' + number2words(n % 100) if n % 100 > 0 else '')
    elif n < 1000000:
        return number2words(n // 1000) + " thousand" + (' ' + number2words(n % 1000) if n % 1000 > 0 else '')
"""
