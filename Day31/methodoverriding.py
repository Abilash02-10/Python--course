class Hotstar:
    def __init__(self,name):
        print(f"welcome to the Hotstar,{name}")
    def login(self):
        print("you can login to the Hotstar")
    def dashboard(self):
        print("you can see the dashboard")
    def search(self):
        print("you can search")
    def playcontrollers(self):
        print("pause.resume.play")
    def history(self):
        print("you can see the recent videos")
    def ads(self):
        print("ads will run")
    def access(self):
        print("you can accessto limited things")
    def download(self):
        print('you can download high quality videos')

class premiumHotstar(Hotstar):
    def __init__(self,name):
        self.name = name
        print(f"dear { self.name}, Welcome to the Hotstar")

    def ads(self):
        print("ads will not run")
    def quality(self):
        print("Quality is High")

    def access(self):
        print("you have unlimited access")

    def download(self):
        print("you can download high quality videos")

a = Hotstar("Abhi")
a.login()
a.access()
a.dashboard()
a.search()
a.playcontrollers()
a.history()
a.download()

b = premiumHotstar("sai")
b.ads()
b.quality()
b.access()
b.download()