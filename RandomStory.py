#RANDOM_STORY_GENERATOR
# Used import keyword to make the code in random module
# Firstly, should import the Random module to access the functions of choosing.
import random
# Used Lists Concept
# Making Required number of Lists, where we added phrases/lines for the story.
start = ["Once there was a skinny dude,"," In the desert of the Wakanda, prince T'challa.",
        " A young high school clever teen, ",   
        " Son of Brilliant engineer,inventor and founder of Stark Industries."]
verse1 = [" who was passionate and determined to become a Soldier,",
        " Had to take up throne to put up the late father's Pride,",
        " Got bit by a Radioactive spider.",
        " Was as Brilliant as his father was."]
verse2 = [" his Physical inability made him think about his determination.",
        " As to avenge his father's death,",
        " Got Powers to save people and to be a friendly neighbourhood Superhero.",
        " got into business,as he chose to become A Genius, A Billionaire, A philantropist,"]
verse3 = [" A Scientist from Queens experimented on him to give a height,",
        " He bacame a wise and a great peoples' head,",
        " Keepin' up the daily doings by saving lives, protecting people.",
        " Gave lot of expertise in his company to uplift his father's Reputation."]
verse4 = [" Became an ideal being to serve his pride.",
        " Tried to open the portal of his life with the world.",
        " As time came, his identiy became a mystery.",
        " failed to notice the dark things going on in his back."]
verse5 = [" He tried doing what he thought to be,",
        " but failed as it might get dangerous for the outside world.",
        " got his superhero stunt videos on social media,",
        " Thought he can do something good from his industry,"]
verse6 = [" He has been puppetted up for what he became,",
        " but the Superheroes needed the help,",
        " made himself private from the mystery,",
        " made suit out of metal scraps."]
verse7 = [" but finally he served,",
        " he did what he told to do, a king's job",
        " but the master needed his help.",
        " He thought he could make a sheild for the entire planet."]
verse8 = [" Went on a mission, saved many and freezed down for years."," He went down to avenge,",
        " he went on a civil war as to take a positive side."," He started making suits in leisure."]
verse9=[" Once finemen Found the CAP in the Ice."," He Went for the wrong man, and knew what vengeance consumes in you.",
        " He fought to win the battle and made through it."," The man in iron scraps had to chose the path where its needs a protective superhero."]
verse10 = [" Astonished about the days passed, with an awe inside exclaiming about the reality."," Gave his holdings to the superheroes who needed help, made them visit the Secret world of his.",
        " He fell for a nerdy-lame girl, whom he had a crush on."," He has been approached by a director of S.H.I.E.L.D. "]
verse11 = [" Lead all the grief aside, started prepping out to serve again. "," Made the dopest technology using a rare metal element for the people in the kind.",
        " but couldn't let that out as his identity would be revealed out."," And, became the Genius Avenger the world could have."]
verse12 = [" Became the first-Righteous Avenger, known for his vibra-shield."," But the Rare metal has been smuggled down in the wrong hands.",
        " Made through a lot of hard stuff praising himself up."," Yet needed a team to tackle or to protect the mankind,"]
verse13 = [" Did lot of respectful Battles and lost the precious battle,The Love."," Went down with loved one to make the culprit down.",
        " Had to tell his bestfriend about his identity."," Married his personal manager at work, who helped in bringing up the business."]
verse14 = [" Lost his love to the age. but kept himself in the righteous side."," Surprisingly, it went all downside, made him reconsider about the past.",
        " He was not ready for his identity to get public."," Yet His mistakes made the world vulnerable, and Caused Plenty Damages."]
verse15 = [" But in the last he chose to be with the love of his life rather being in a duty of the world."," The time came for him to Disclose every advanced technology that had helped his kingdom.",
        " He chose to be a friendly neighbourhood superhero rather letting or pushing his closed ones in danger."," Sorted out everything advancedly to be a step ahead in time and for the future protection"]        
# Used random.choice(listname) method to select any random phrase in the corresponding List
# Assigning randomly chosen phrases into the variables.
intro = random.choice(start)
ver1 = random.choice(verse1)
ver2 = random.choice(verse2)
ver3= random.choice(verse3)
ver4 = random.choice(verse4)
ver5 = random.choice(verse5)
ver6 = random.choice(verse6)
ver7 = random.choice(verse7)
ver8 = random.choice(verse8)
ver9 = random.choice(verse9)
ver10 = random.choice(verse10)
ver11 = random.choice(verse11)
ver12 = random.choice(verse12)
ver13 = random.choice(verse13)
# Used String Concatenation.
# Concatenating the strings in the variables given.
# To Create a Sensible Story, We Concatenated the phrases from different lists.
story = intro + ver1 + ver2 + ver3 + ver4 + ver5 + ver6 + ver7 + ver8 + ver9 + ver10 + ver11 + ver12 + ver13
# Used print() function to print the concatenated strings, which is the Story, to make sense.
print(story) 