questions=[["Which one among them is a domestic animal?","Dog","Lion","Tiger",   "Leopard","a"],
["In the Wurtz reaction, what type of compound is obtained by treating an alkyl halide with sodium metal?","Alkane","Alkene","Alkyne",   "Alcohol","a"],

["Which of the following haloalkanes is least reactive towards nucleophilic substitution reactions?","Methyl chloride","Isopropyl chloride","Ethyl chloride",   "Tert-butyl chloride","d"],

["Which one among them is a Wild animal?","Donkey","Lion","Rat",   "Mouse","b"],

["Which of the following reagents is commonly used for the conversion of an alcohol to a haloalkane?","H2SO4","PCL5","NaOH",   "KMnO4","b"],

["When a primary haloalkane is treated with a strong base, what is the primary reaction that occurs?","Oxidation","Addition","Elimination",   "Nucleophilic substitution","c"],

["Which of the following haloalkanes is used as a local anesthetic??","Methyl chloride","Chloroform","1-Chlorobutane",   "Ethyl bromide","b"],

["Which one among them is a domestic animal?","Donkey","Lion","Tiger",   "Leopard","a"],
["Which alcohol is commonly used as a disinfectant and antiseptic","Methanol","Ethanol","Propanol",   "Butanol","b"],

["What is the general formula for primary alcohols?","R-OH","R1-OH","R2-OH",   "R3-OH","a"],

["What is the product when an alcohol is dehydrated with concentrated sulfuric acid?","Alkane","Alkene","Alkyne",   "Alcohol","b"],

["When a haloalkane undergoes nucleophilic substitution, what is typically observed in the reaction mechanism?"," An elimination step","Formation of a carbocation intermediate","No change in the carbon skeleton",   "Formation of a double bond","b"],
]

money=0

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000,640000,10000000]
print("Welcome to KBC presented by Swaraj".center(60))
for i in range(0,len(questions)):
    print(f"\n\n **This Question is for Rs-{levels[i]}**")
    print("\n",i+1,".",questions[i][0])
    print(f"      a.{questions[i][1]}")
    print(f"      b.{questions[i][2]}")
    print(f"      c.{questions[i][3]}")
    print(f"      d.{questions[i][4]}")
          
    reply=str(input("\nEnter your answer(a-d) "))
    if reply==f"{questions[i][-1]}":
        if(i==11):
            print("\nSupper!! You cracked the KBC")
        print(f"\nCorrect Answer! You earned Rs- {levels[i]}")
        money=levels[i]
        
    else:
        print(f"\nWrong Answer! The correct answer was {questions[i][-1]}")
        if 0<=i<=4:
            money=0
        elif 4<i<=8:
            money=10000
        elif 8<i<=11:
            money=320000
        elif i>11:
            money=10000000
        break
 
        
print(f"\nYou will take only Rs- {money} to home.")