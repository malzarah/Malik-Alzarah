from pip._vendor.distlib.compat import raw_input

print("ISQA 3900 Lumber Price Calculator")
print()
condition=True
finalTotal=0.00
while condition:
    print("You will be asked the  number of board feet for purchase and the type of lumber (common or select)")
    board=raw_input('Enter number of board feet:')
    lumber=raw_input('Enter a 1 for select lumber or a 2 for common lumber')
    if(int(lumber)==1):
       total=int(board)*2
    else:
        total=int(board)*1

    if(int(total)<10000):
        finalTotal=total
    if(int(total)>10000 and int(total)<50000):
        finalTotal=int(total)-(int(total)*10/100)
    if( int(total)>50000):
        finalTotal = int(total) - (int(total) * 20 / 100)

    print('Total price for the lumber is {.2f} '.format(finalTotal))
    print('')
    cond=raw_input(' Continue (y/n)?:')
    if (cond=='n'):
        condition= False