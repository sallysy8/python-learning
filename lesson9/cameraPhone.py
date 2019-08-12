'''
camera Phone
'''

class CameraPhone:
    def __init__(self):
        print("This is a new combination!")
    def makePhonecall(self):
        print("Please press the numbers that you want to call.")
    def take_pics(self):
        print("Smile!")


class Camera(CameraPhone):
    def __init__(self):
        print("Take a photo")
        super().__init__()
    def take_pics(self):
        super().take_pics()


class Phone(CameraPhone):
    def __init__(self):
        print("Call 911!")
        super().__init__()

    def makePhonecall(self):
        #print("Please make a phone call!")
        super().makePhonecall()


d = Phone().makePhonecall()
d = Camera().take_pics()






