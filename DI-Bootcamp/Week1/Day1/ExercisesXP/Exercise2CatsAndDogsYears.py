humanYears=10
catYears1=15
catYears2=15+9
catYears3andMore=15+9+(4*(humanYears-2))
dogYears1=15
dogYears2=15+9
dogYears3andMore=15+9+(5*(humanYears-2))
if humanYears==1:
    print (humanYears,catYears1,dogYears1)
if humanYears==2:
    print (humanYears,catYears2,dogYears2)
if humanYears>2:
    print (humanYears,catYears3andMore,dogYears3andMore)