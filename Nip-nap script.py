
#find ud af din skæbne for dagen - hvilke pligter skal løses ?? nip nap!

nip_tal_1 = [1,2,5,6]
nip_tal_2 = [3,4,7,8]

print("Du ser en nipnapper med alle regnbuens farver angivet på toppen.")

farvevalg = input("Skriv navnet på den farve, du ønsker at tage udgangspunkt i: ")
print("Du har valgt farven " + farvevalg + ". Et godt valg!")

n_bogstaver = len(farvevalg)

print("Der er " + str(n_bogstaver) + " bogstaver i din valgte farve.")

#standard nip-napping funktion
def nipnapping(x):
    i = 0

    while i <= x-1:
        if i % 2 == 0:
            print("*nip*: " + str(nip_tal_1))
            i += 1
        elif i % 2 != 0:
            print("*nap*: " + str(nip_tal_2))
            i += 1

nipnapping(n_bogstaver) #lav standard nip-napping svarende til antal bogstaver

talvalg_1 = input("Tast det tal af ovenstående, som du ønsker at nip-nappe igennem: ")

if n_bogstaver % 2 == 0: #lav standard nip-napping svarende til det valgte tal
    nipnapping(int(talvalg_1)) 
elif n_bogstaver % 2 != 0: #lav nip-napping i omvendt rækkefølge svarende til det valgte tal
    i = 1
    while i <= int(talvalg_1):
        if i % 2 == 0:
            print("*nip*: " + str(nip_tal_1))
            i += 1
        elif i % 2 != 0:
            print("*nap*: " + str(nip_tal_2))
            i += 1

talvalg_2 = input("Tast det tal af ovenstående, som du ønsker at se resulatet for: ")

#resultater fra nip-napperen
if int(talvalg_2) == 1:
    print("Dine sko trænger sikkert til at blive pudset. Glem ikke at rengøre agletterne!")
elif int(talvalg_2) == 2:
    print("Tag en fridag og drop pligterne for i dag.")
elif int(talvalg_2) == 3:
    print("Er dit gulv mon beskidt? Tag en runde med støvsugeren.")
elif int(talvalg_2) == 4:
    print("Du burde nok tage et bad ...")
elif int(talvalg_2) == 5:
    print("Vidste du, at man burde rengøre sit køleskab hver tredje måned? Skynd dig at få det gjort.")
elif int(talvalg_2) == 6:
    print("Du har ansvaret for at passe på dine planter. Husk at give dem gødning.")
elif int(talvalg_2) == 7:
    print("Opvasken tager ikke sig selv. Kom i gang og få det overstået.")
elif int(talvalg_2) == 8:
    print("Udnyt det gode vejr og få vasket dit beskidte tøj.")
else:
    print("Du har ikke valgt et relevant tal.") 

    #^teknisk set også muligt at vælge ikke-åbent tal fra 1-8 men det er en venlig nip-napper, der tillader det
