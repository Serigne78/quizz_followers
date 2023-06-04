import sys 
import random
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""
vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

score = 0
found = True


while found == True:
      print(logo)
      celebrities = ["Messi from argentina", "Mbappe from France", "Selena from usa", "Lebron from usa", "Giannis from Greece", "Morant from usa"]

      celeb_a = random.choice(celebrities)
      celeb_b = random.choice(celebrities)
      if celeb_a == celeb_b:
            print("Nouvelle generation aleatoire")
            celeb_a = random.choice(celebrities)
            celeb_b = random.choice(celebrities)
            if celeb_a == celeb_b:
                  celeb_a = random.choice(celebrities)
                  celeb_b = random.choice(celebrities)
                  if celeb_a == celeb_b:
                        celeb_a = random.choice(celebrities)
                        celeb_b = random.choice(celebrities)



            
      

      def power_a():
            global celeb_a
            if celeb_a  == "Messi from argentina":
                  return 100
            if celeb_a  == "Mbappe from France":
                  return 80
            if celeb_a  == "Selena from usa":
                  return 10
            if celeb_a  == "Lebron from usa":
                  return 70
            if celeb_a  == "Giannis from Greece":
                  return 10
            if celeb_a  == "Morant from usa":
                  return 20

      def power_b():
            global celeb_a
            if celeb_b  == "Messi from argentina":
                  return 100
            if celeb_b  == "Mbappe from France":
                  return 80
            if celeb_b  == "Selena from usa":
                  return 10
            if celeb_b  == "Lebron from usa":
                  return 70
            if celeb_b  == "Giannis from Greece":
                  return 10
            if celeb_b  == "Morant from usa":
                  return 20
            



      followers_a = power_a()

      followers_b = power_b()
     
      if followers_a > followers_b:
            print(f"Compare A :{celeb_a} ")
            print(vs)
            print(f"Compare B :{celeb_b} ")

            question = input(f"Qui a le plus de followers entre {celeb_a} et {celeb_b}: Type 'a' ou Type 'b': ").lower()
            if question == "a":
                  print("succes")
                  score+=1
                  print(f"Ton score actuel est de {score}")
            else:
                  print(f"Tu t'es trompé ton score final est de {score}") 
                  found = False

      if followers_b > followers_a:
            print(f"Compare A :{celeb_a} ")
            print(vs)
            print(f"Compare B :{celeb_b} ")
            question = input(f"Qui a le plus de followers entre {celeb_a} et {celeb_b}: Type 'a' ou Type 'b': ").lower()
            if question == "b":
                  print("succes")
                  score+=1
                  print(f"Ton score actuel est de {score}")
            else:
                  print(f"Tu t'es trompé ton score final est de {score} ")
                  found = False

      
