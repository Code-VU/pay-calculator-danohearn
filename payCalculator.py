def calculatePay():
    # Implement your solution in between the two comment blocks
    print("calculating pay")
    # This first line is provided for you
    rate = input("Enter Rate: ")
    hrs = input("Enter Hours: ")
    if hrs > 40 :
        otp = (hrs - 40)*(rate*1.5)
        reg_rate = 40*rate
        grossPay = otp + reg_rate
    else:
        grossPay = float(hrs)*float(rate)

    print(grossPay)

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
## calculatePay()
