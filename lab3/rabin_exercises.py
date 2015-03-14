from lab3.ex4 import Rabin

__author__ = 'Olexandr'


def main():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    exercises = {
        'WEEK': {"p": 67, "q": 71, "enc": '07191605'},
        'WALL': {"p": 53, "q": 67, "enc": '35382124'},
        'FREE': {"p": 53, "q": 71, "enc": '01161407'},
        'SOFT': {"p": 59, "q": 67, "enc": '17000557'},
        'LOST': {"p": 71, "q": 31, "enc": '18330658'},
        'SKIN': {"p": 71, "q": 67, "enc": '32844503'},
        'STEP': {"p": 83, "q": 37, "enc": '12940249'},
        'IRON': {"p": 23, "q": 67, "enc": '02360974'},
        'COPY': {"p": 47, "q": 83, "enc": '28851481'},
        'CASE': {"p": 83, "q": 23, "enc": '18201480'}
    }

    for word in exercises.keys():
        obj = exercises[word]
        rabin = Rabin(obj["p"], obj["q"], alphabet)
        print(word + "(" + str(obj["enc"]) + ") = " + str(rabin.decode(obj["enc"])))


if __name__ == '__main__':
    main()