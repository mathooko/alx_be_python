size=int(input("Enter the size of the pattern: "))
row=0

while row< size:
    # for item in pInt: does not work
    #  for row in range(size):check why this does not work
      for row in range(size):
        x=size*"*"
        print(x)
#i+=1 Does not work
      row+=1
