# By Kamran Bigdely Nov. 2020
# Move Field (attribute)
class Gun:
    def __init__(self, name):
        self.name = name
        self.num_cathridge_bullets = []
        # initialize with 10 bullets in each gun's cathridge.
        self.num_cathridge_bullets.append(10)          
    def shoot(self):
        print('shoot')
    def reload(self):
        print('reload')

class Player:
    def __init__(self, guns):        
        self.guns = guns
        
    def fire_once(self):
        for i, gun in enumerate(self.guns):
            if gun.num_cathridge_bullets[i] > 0:
                gun.shoot()
                gun.num_cathridge_bullets[i] -= 1
                break
            
def game_loop():
    while (True):
        player.fire_once()
        # other logic here.
        break

guns = [Gun('pistol'), Gun('rifle')]
player = Player(guns)
game_loop()
