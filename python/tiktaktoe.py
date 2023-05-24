XO={"A":["","",""],"B":["","",""],"C":["","",""]}
import pandas as pd
game=pd.DataFrame(XO, index=[1,2,3])
def check_equalizations(x):
      if (game[x][3]!="" and game[x][1]!="" and game[x][2]!="" and game[x][1]==game[x][2] and game[x][1]==game[x][3] and game[x][2]==game[x][3]):
            print(f'{game[x][j]} won')

print(game)
print("\n\n")
for i in range(1,50):
    target=input("which box:")
    if target=="A1" or target=="A2" or target=="A3" or target=="B1" or target=="B2" or target=="B3" or target=="C1" or target=="C2" or target=="C3" or target=="a1" or target=="a2" or target=="a3" or target=="b1" or target=="b2" or target=="b3" or target=="c1" or target=="c2" or target=="c3":
        if i%2==0:
            for k in range(9):
                if game[target[0].upper()][int(target[1])]=="":
                    game[target[0].upper()][int(target[1])]="O"
                    break
                else: 
                    print("it is full, choose another one")
                    i=i+1
        else:
            for k in range(9):
                if game[target[0].upper()][int(target[1])]=="":
                    game[target[0].upper()][int(target[1])]="X"
                    break
                else: 
                    print("it is full, choose another one")
                    i=i+1
        print(game)
        print("\n\n")
        for j in range(1,4):
            if(game["A"][j]!="" and game["B"][j]!="" and game["C"][j]!="" and game["A"][j]==game["B"][j] and game["B"][j]==game["C"][j] and game["A"][j]==game["C"][j]):
                print(f'{game["A"][j]} won')
                break
            break
        check_equalizations("A")
        check_equalizations("B")
        check_equalizations("C")
        if(game["A"][1]!="" and game["B"][2]!="" and game["C"][3]!="" and game["A"][1]==game["B"][2] and game["A"][1]==game["C"][3] and game["B"][2]==game["C"][3]):
            print(f'{game["A"][1]} won')
            break
        elif(game["A"][3]!="" and game["B"][2]!="" and game["C"][1]!="" and game["A"][3]==game["B"][2] and game["A"][3]==game["C"][1] and game["B"][2]==game["C"][1]):
            print(f'{game["A"][1]} won')
            break
    else:
        print("you don't choose right box")

