
class GuessingGame: 
  """ This is the main class for our program. It will store different 
  functions """ 
  
   def __init__(self) -> None:
      self.actors = self.read_dict()
  
   def actors_dict():
    """ name = str, name of the actor would be the value, Brad Pitt 
        genre = str, genre of the actor's movie, Action
        ethnicity = str, ethnicity of the actor, White 
        Args: 0
        Only used for storing values, not going to take any arguments 
    """
      ans = {i for i in self.actors if self.actors[i] == value}
      return str(ans).replace("{","").replace("}","").replace("'","")
    
   def user_input():
      
      """ Takes user input based on the question printed in the output.
         Args: 0
         Side Effects: 
         Print(f”Please answer the following question: {question}”)
        """
      age = input("Enter age: ")

      race = input("Enter Ethnicity: ")

      sex = input("Enter sex: ")

      ans = {'age':age, 'race/ethnicity':race, 'sex':sex}

      return ans
    
  def read_dict(self):
    """ Uses with statements to open and read python file with dictionaries
        Args: 0 
        Returns: dictionary """
    d = {}
    with open("dict.json") as f:
      d = json.load(f)
    return d
    
  def guess_input(self, name):
        """ Conditional expressions that ask user to confirm whether the actor
        is the same one the dictionary resulted in
        Args: 1
        name = str
        Returns: str confirming name of actor """
    if name in self.actors:
      if name == "Jake Gyllenhaal":
        q1 = input("Were they in Brokeback Mountain?")
        if q1 == "yes" or q1 == "Yes":
          print("It's Jake Gyllenhaal!")
        else:
          print("I don't know this person...")
      elif name == "Tom Hardy":
        q2 = input("Were they in Venom?")
        if q2 == "yes" or q2 == "Yes":
          print("It's Tom Hardy!")
        else:
          print("I don't know who this is...")
      elif name == "Margot Robbie":
        q3 = input("Were they in Harley Quinn: Birds of Prey?")
        if q3 == "yes" or q3 == "Yes":
          print("It's Margot Robbie!")
        else:
          print("It's a shame I don't know who this is!")
      elif name == "Shah Rukh Khan":
        q4 = input("Were they in Om Shanti Om?")
        if q4 == "yes" or q4 == "Yes":
          print("It's Shah Rukh Khan!")
        else:
          print("Maybe I should learn more about Bollywood...")
      elif name == "Angelina Jolie":
        q5 = input("Were they in Maleficent?")
        if q5 == "yes" or q5 == "Yes":
          print("It's Angelina Jolie!")
        else:
          print("I don't know this person...")
      elif name == "Will Smith":
        q6 = input("Were they in Men in Black?")
        if q6 == "yes" or q6 == "Yes":
          print("It's Will Smith!")
        else:
          print("I don't know them...")
      elif name == "Andrew Garfield":
        q7 = input("Were they in Spiderman?")
        if q7 == "yes" or q7 == "Yes":
          print("It's Andrew Garfield")
        else:
          print("Who could this be...I wouldn't know")
      elif name == "Priyanka Chopra":
        q8 = input("Were they in Gunday?")
        if q8 == "yes" or q8 == "Yes":
          print("It's Priyanka Chopra!")
        else:
          print("It's not who I think it is...")
      elif name == "Leonardio DiCaprio":
        q9 = input("Were they in Titanic?")
        if q9 == "yes" or q9 == "Yes":
          print("It's Leonardio Dicaprio")
        else:
          print("So I don't know who you're thinking of...")
      elif name == "Henry Golding":
        q10 = input("Were they in in Crazy Rich Asians?")
        if q10 == "yes" or q10 == "Yes":
          print("It's Henry Golding!")
        else:
          print("I wish I knew who this is...")
      elif name == "Ryan Reynolds":
        q1 = input("Were they in Deadpool?")
        if q1 == "yes" or q1 == "Yes":
          print("It's Ryan Reynolds!")
        else:
          print("I don't know this person...")
      elif name == "Matthew McConaughey":
        q2 = input("Were they in How to Lose a Guy in 10 Days?")
        if q2 == "yes" or q2 == "Yes":
          print("It's Matthew McConaughey!")
        else:
          print("I don't know who this is...")
      elif name == "Dakota Johnson":
        q3 = input("Were they in Fifty Shades of Grey?")
        if q3 == "yes" or q3 == "Yes":
          print("It's Dakota Johnson!")
        else:
          print("It's a shame I don't know who this is!")
      elif name == "Ranveer Singh":
        q4 = input("Were they in Ram-Leela?")
        if q4 == "yes" or q4 == "Yes":
          print("It's Ranveer Singh!")
        else:
          print("Maybe I should learn more about Bollywood...")
      elif name == "Jackie Chan":
        q5 = input("Were they in Rush Hour?")
        if q5 == "yes" or q5 == "Yes":
          print("It's Jackie Chan!")
        else:
          print("I don't know this person...")
      elif name == "Florence Pugh":
        q6 = input("Were they in Midsommar?")
        if q6 == "yes" or q6 == "Yes":
          print("It's Florence Pugh!")
        else:
          print("I don't know them...")
      elif name == "Zendaya":
        q7 = input("Were they in Dune?")
        if q7 == "yes" or q7 == "Yes":
          print("It's Zendaya!")
        else:
          print("Who could this be...I wouldn't know")
      elif name == "Ana de Armas":
        q8 = input("Were they in Blonde?")
        if q8 == "yes" or q8 == "Yes":
          print("It's Ana de Armas!")
        else:
          print("It's not who I think it is...")
      elif name == "Miles Teller":
        q9 = input("Were they in Whiplash?")
        if q9 == "yes" or q9 == "Yes":
          print("It's Miles Teller")
        else:
          print("So I don't know who you're thinking of...")
      elif name == "Oscar Isaac":
        q10 = input("Were they in Ex Machina?")
        if q10 == "yes" or q10 == "Yes":
          print("It's Oscar Isaac!")
        else:
          print("I wish I knew who this is...")
    else:
      print("Oops:( I don't know who this could be...")

      
def main():
  """ Executes all class functions """
  game = GuessWho()
  ans = game.user_input()
  actor = game.actors_dict(ans)
  game.guess_input(actor)
      

if __name__ == "__main__":
   main()
  


def parse_args(argslist): 
    """ Parse command line arguments. 
        Expect 5 mandatory arguments: 
        str: dictionary of ethnicity entered by users 
        str: dictionary containing gender entered by users 
        int: dict containing age entered by users 
        str: dict containing answers to a specific question
        regarding a specific actor from the user input 
        str: dict containing answers to a specific question 
        regarding a specific actor from the user input
        int: dict containing birthday entered by users 
        str: dict containing genre of movies entered by users 
        Args: 
        argslist (list of str/int): arguments from the command line
        Returns: 
        user inputs: the parsed arguments """ 
    
        
        
        
        
