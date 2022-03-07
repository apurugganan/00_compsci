sHours = input('Enter hours: ')
sRate = input('Enter rate: ')

def computePay(hours, rate):
    fHours = float(hours)
    fRate = float(rate)

    if fHours > 40 :
        regular = fHours * fRate
        overtime = (fHours - 40.0) * fRate * 0.5
        total = regular + overtime
    else:
        total = fHours * fRate
    return total

gtotal = computePay(sHours, sRate)

print('Pay: ', gtotal)
