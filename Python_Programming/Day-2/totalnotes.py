#Print the notes for the amount given.
def notes(x):
    if x>=2000 :
        n=x//2000
        return f"{n} 2000 rupee notes"+"\n"+notes(x-(2000*n))
    elif x>=500 :
        n=x//500
        return f"{n} 500 rupee notes"+"\n "+notes(x-(500*n))
    elif x>=100:
        n=x//100
        return f"{n} 100 rupee notes"+"\n "+notes(x-(100*n))
    elif x>=50:
        n=x//50
        return f"{n} 50 rupee notes"+"\n"+notes(x-(50*n))
    elif x>=20:
        n=x//20
        return f"{n} 20 rupee notes"+"\n"+notes(x-(20*n))
    elif x>=10:
        n=x//10
        return f"{n} 10 rupee notes"+"\n"+notes(x-(10*n))
    elif x>=5:
        n=x//5
        return f"{n} 5 rupee coins"+"\n"+notes(x-(5*n))
    elif x>=2:
        n=x//2
        return f"{n} 2 rupee coins"+"\n"+notes(x-(2*n))
    elif x>=1:
        n=x//1
        return f"{n} 1 rupee coins"+"\n"+notes(x-(1*n))
    elif x==0:
        return ""
    else:
        return "Invalid Input"
y=int(input("Enter the amount : "))
print(notes(y))