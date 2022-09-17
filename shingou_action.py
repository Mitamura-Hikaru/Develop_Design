from enum import Enum
class Shingou(Enum):
    RED = 1
    BLUE = 2
    YELLOW = 3

def act_shingou(color):
    shingou = Shingou(color)

    if shingou is Shindou.RED:
        print("とまれ")
    elif shingou is Shingou.BLUE:
        print("進め")
    elif shingou is Shingou.YELLOW:
        print("注意")
    else:
        raise Exception(
            
        )