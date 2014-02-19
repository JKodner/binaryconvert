def dash():
    print "-" * 127
def sep():
    print "*" * 12
mylist = []
bin_code = 3.5
num = ' '
jobs = ["1", "2"]
job = 8
sep()
print "Welcome to the Binary Code Converter!"
dash()
print "Type [1] if you want a number converted into Binary Code."
print "Type [2] if you want a binary code converted into a number."
dash()
while job not in jobs:
    job = raw_input("What task do you want (1 or 2)?")
    dash()
    if job in jobs:
        if job == "1":
            while type(num) != int:
                try:
                    num = int(raw_input("What number do you want converted into Binary Code?"))
                    dash()
                    num = int(num)
                except ValueError:
                    dash()
                    print "Please clarify your input."
                    dash()
                    mylist.append("i")
                try:
                    value = bin(num)
                    print str(num) + " converted into a binary code is: " + str(value) + "."
                except TypeError:
                    if "i" not in mylist:
                        print "Please clarify your input."
                        dash()
        elif job == "2":
            while type(bin_code) != int:
                bin_code = str(raw_input("What binary code do you want converted into a number?"))
                dash()
                try:
                    int(bin_code, 2)
                    value = int(bin_code, 2)
                except ValueError:
                    print "Please clarify your input."
                    dash()
                try:
                    value = int(bin_code, 2)
                    print str(bin_code) + " converted into a number is: " + str(value) + "."
                    break
                except ValueError:
                    None
    else:
        print "Please clarify your input."
        dash()
sep()