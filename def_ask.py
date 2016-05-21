def ask_ok(prompt="Enter a yes or No", retry=4, complain='yes or no'):
  print ("something will be done here")
while 1:
        ok = input(prompt)
        if ok in ('yes','y'):
                print("true")
        if ok in ('no','n'):
                print(" false")
                retry = retry - 1
        if retry < 0:
                raise OSError('No User')
        print(complain)

asking = ask_ok
asking
