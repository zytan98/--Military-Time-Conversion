def timeconversion(time):
    time = time.split(":")
    H, M, AP = time[0], time[1][:2], time[1][2:]
    AM = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
            11: 'eleven', 12: 'zero'}
    PM = {1: 'thirteen', 2: 'fourteen', 3: 'fifteen', 4: 'sixteen', 5: 'seventeen', 6: 'eighteen',
        7: 'nineteen', 8: 'twenty', 9: 'twenty-one', 10: 'twenty-two', 11: 'twenty-three', 12: 'Twelve'}
    Mins = {1: 'one', 2: 'two'	, 3: 'three'	, 4: 'four'	, 5: 'five'	, 6: 'six', 7: 'seven'	, 8: 'eight'	, 9: 'nine'	, 10: 'ten', 11: 'eleven'	, 12: 'twelve'	, 13: 'thirteen'	, 14: 'fourteen'	, 15: 'fifteen'	, 16: 'sixteen'	, 17: 'seventeen'	, 18: 'eighteen'	, 19: 'nineteen', 20: 'twenty', 21: 'twenty-one', 22: 'twenty-two'	, 23: 'twenty-three'	, 24: 'twenty-four', 25: 'twenty-five', 26: 'twenty-six', 27: 'twenty-seven', 28: 'twenty-eight'	, 29: 'twenty-nine', 30: 'thirty', 31: 'thirty-one'	, 32: 'thirty-two', 33: 'thirty-three', 34: 'thirty-four',
35: 'thirty-five', 36: 'thirty-six', 37: 'thirty-seven'	, 38: 'thirty-eight', 39: 'thirty-nine', 40: 'forty',
41: 'forty-one', 42: 'forty-two'	, 43: 'forty-three', 44: 'forty-four', 45: 'forty-five', 46: 'forty-six', 47: 'forty-seven', 48: 'forty-eight', 49: 'forty-nine', 50: 'fifty', 51: 'fifty-one', 52: 'fifty-two'	, 53: 'fifty-three', 54: 'fifty-four', 55: 'fifty-five', 56: 'fifty-six', 57: 'fifty-seven', 58: 'fifty-eight', 59: 'fifty-nine', 60: 'sixty'
}
    if M == "00":
        if AP == "AM":
            hours = AM[int(H)]
        else:
            hours = PM[int(H)]
        print(hours + " hundred hours")
    else:
        mins = Mins[int(M)]
        if AP == "AM":
            hours = AM[int(H)]
            if int(H) < 10:
                hours = "zero " + hours
        else:
            hours = PM[int(H)]
        if int(M) < 10:
            mins = "zero " + mins
        print(hours + " " + mins)

while(1):
    time = input("Enter the timing:(press q to quit)")
    if time == "q":
        break
    timeconversion(time)
