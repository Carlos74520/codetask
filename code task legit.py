#declare variables
auctionlist = []
buyerlist= []
counter = 0
itemamount = int(input('how many items are there to auction?'))
itemnumber = 000
buyeradd = True
buyerid = []
counter = 0
bidding = False

#this makes innitial item list for bidders to see
for i in range(itemamount):
    itemindividual = []
    itemnumber += 1
    intemdescription = input('what is the item?')
    reserveprice = str(input('what is the reserve price?'))
#append individual factors into the temporary 1D array
    itemindividual.append(itemnumber)
    itemindividual.append(intemdescription)
    itemindividual.append(0)
    itemindividual.append(reserveprice)
#appends the 1D array into the other 1D array, making it a easier to use 2D array
    auctionlist.append(itemindividual)



#this makes an array for bidders so that I can append to them later on
while buyeradd:
    if counter == 0:
        print('adding bidders, its now or never!')
    counter += 1
    buyerid.append(counter)
    buyerlist.append(buyerid)
    print('there are currently', counter, 'buyer(s).')
    morebuyers = input('Are there more buyers (y/n)?')
    buyerid = []
    if morebuyers == 'n':
        #print(buyerlist)
        print('no more bidders can enter this auction')
        buyeradd = False

bidding = True
print('here are the current items and their information:')
for i in range(itemamount):
    print(auctionlist[i])

while bidding:
    #this is temporary, for the legit one you use full names
    buyeridpick = int(input('please enter buyer id'))
    chose = input('Do you want to search via item number or description (in/d)?')
    if chose == 'in':
        pick = int(input('what item number do you want to bid on?'))
        for i in range(itemamount):
            if list[i][0] == pick:
                print('yes it does')