from turtle import Screen

class GameScreen(Screen):

    def __init__(self,width=800,height=800):
        super().__init__()
        self.title("Multiplayer Snake Game")
        self.bgcolor("lightblue")
        # min size for multiplayer snake game is 800x800
        if width < 800 or height < 800:
            self.setup(width=800, height=800+200)  #200 is extra space for score display
        else:
            self.setup(width=width, height=height+200)  #200 is extra space for score display
        
        self.tracer(0)