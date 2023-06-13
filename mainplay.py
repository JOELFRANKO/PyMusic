from playsound import playsound

print ("Available Songs \n 1. Vaarayo-Vaarayo \n 2. Damakku-Damakku \n 3. Pala-Palakura ")

order = input ("Enter the music name to play :")

if "Vaarayo-Vaarayo" in order:
    playsound('E:\\MUSIC\\TAMIL\\adhavan\\Vaarayo-Vaarayo-MassTamilan.mp3')

elif "Damakku-Damakku" in order:
    playsound('E:\\MUSIC\\TAMIL\\adhavan\\Damakku-Damakku-MassTamilan.mp3')

elif "Pala-Palakura"in order:
    playsound('E:\\MUSIC\TAMIL\\aayan\\Pala-Palakura.mp3')
