from PIL import Image, ImageFilter

img:Image.Image = None

def run():
    global img
    fp = input("Enter the location of the file: ")
    isTrue = True
    try:
        img = Image.open(fp)
        print(img.size, img.mode)
        while(isTrue):
            printChoices()
            value:int = int(input("Enter the value: "))
            if runChoice(value) == 1:
                isTrue = False
        save()
        img.close()
        del img
    except Exception as e:
        print("Please enter valid input ",e)


def printChoices():
    print("Please choose what you want to do with the image.")
    print("1. Rotate the image")
    print("2. Scale it down in size")
    print("3. Display the image")
    

def rotate():
    global img
    angle:float = float(input("Enter the angle (in degrees): "))
    img = img.rotate(angle)


def scale():
    global img
    size:tuple = tuple(input("Enter the size seperated by comma").split(','))
    img = img.resize(size)

def display():
    global img
    img.show()

def runChoice(i:int):
    if i == 1:
        rotate()
    elif i == 2:
        scale()
    elif i == 3:
        display()
    else:
        print("You have entered a wrong choice")
        return 0
    return 1


def save():
    print("Inside save")
    anw:str = input("Do you want to save the file?")
    if anw.capitalize() == 'Yes':
        loc:str = input("Enter the location")
        img.save(loc)


run()
