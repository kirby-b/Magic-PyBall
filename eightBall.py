import random
import sys

def main():
    question = input("What is your question?\n")
    if not question:
        print("You have to ask a question!")
    else:
        print("Shaking the magic 8 ball!")
        shakeEightBall()

def shakeEightBall():
    answers = ["It is certain", "Reply hazy, try again", "As I see it, yes", "Don't count on it", "Ask someone else",
                "It is decidedly so", "Ask again later", "Most likely", "My reply is no", "Wubba Lubba Dub Dub", 
                "Without a doubt", "Better not tell you now", "Outlook good", "My sources say no", "Outlook awful"
                "Yes definitely", "Cannot predict now", "Yes", "Outlook not so good", "Please wipe the screen, I couldnt hear you"
                "You may rely on it", "Concentrate and ask again", "Signs point to yes", "Very doubtful", "Perhaps therapy"]
    getAns = answers[random.randint(0, len(answers))]
    print(getAns)

if __name__ == "__main__":
    main()