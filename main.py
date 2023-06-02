# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player1 = 'Ruud Gullit'
player2 = 'Marco van Basten' 

goal_0 = 32
goal_1 = 54

scorers = player1 + " " + str (goal_0)+ ", " + player2 + " " + str(goal_1)
# print (scores)

report = f"""{player1} scored in the {goal_0}nd minute\n{player2} scored in the {goal_1}th minute"""
#firstname
player = 'Marco van Basten'
first_name = player
 #first_name = player [:6]
# Zoeken op spatie
## Dit kan met .find
#print("Find", player.find(' ')) 
aantal_letters_first_name = player.find(' ')
# print(aantal_letters_first_name)
 # Zoek op welk karakter in de naam de eerste spatie zit
first_name = player [:aantal_letters_first_name]
print(first_name) 
gras = aantal_letters_first_name + 1
# print (gras)
achternaam = player[gras:]

print(achternaam)
last_name_len = len(achternaam)
print (last_name_len)

# begin stap 4
# voor letter van first_name
voor_letter = first_name [0]
print (voor_letter)

# combineer voorletter + achternaam
name_short = voor_letter + ". " + achternaam 
print (name_short)
# einde stap 4

# Marco ->  5 letters, 5 keer printen -> Marco! Marco! Marco!

chanttijdelijk =  (first_name + "! ") * 5
print("Chanttijdelijk:", chanttijdelijk)
chant = chanttijdelijk [:-1]
print ("chant", chant )

#boolean 

good_chant = chant  [-1] != " "
print (good_chant)















# print (first_name)
# #lastname
# last_name_len =['van Basten']
# print (last_name_len)
# # firstname, M. lastname

# chant =("Marco!" + "" +  "" + "" )*3
# print(chant)
# print ('Marco!')
# print ("Marco! {}". format ("Marco!"))
# print ( f"Marco  {Marco}" )













