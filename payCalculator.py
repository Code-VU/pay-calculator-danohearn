def calculatePay():
    # Implement your solution in between the two comment blocks
    print("calculating pay")
    # This first line is provided for you
    rate = input("Enter Rate: ")
    hrs = input("Enter Hours: ")
    try:
        frate = float(rate)
        fhrs = float(hrs)
    except:
        print("Error, please enter numeric input")
        quit()

    if fhrs > 40.0 :
        otp = (fhrs - 40) * (frate * 1.5)
        reg_rate = 40 * frate
        grossPay = otp + reg_rate
    else:
        grossPay = frate * fhrs
    print(grossPay)
       

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
## calculatePay()
