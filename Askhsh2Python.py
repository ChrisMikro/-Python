#Xrhshmopoih8hke python 2.7
par=raw_input("Dwse akolouthia parenthesewn:")
plhthos=len(par)
i=1
p=0
pl1=par.count("(")
pl2=par.count(")")
if ((par[0]== "(") and (par[plhthos-1]==")") and (pl1==pl2)):
    while i<=plhthos:
        pl3=par.count('(')
        pl4=par.count(')')
        if (pl4<=pl3):
            i=i+1
            p=p+1
        else:
            i=i+1
            break

    if (p==(i-1)):
        print ("Mporei na xhsimopoihthei se ma8hmatikh parastash")
    else:
        print ("Den mporei na xrhsimopoihthei se ma8hmatikh parastash") 



else:
    print ("Den mporei na xrhsimopoihthei se ma8hmatikh parastash")
    
    
