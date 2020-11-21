print('fbfr')
i=0
while i<10000000:
    file = open(str(i)+'tam'+'.txt', "w")
    print(i)
    print('fbfr')
    file.write('darova \n')
    i+=1