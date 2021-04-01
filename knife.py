from weapon import Weapon

class Knife(Weapon):
    def __init__(self, name, power, num):
        super().__init__(name,power)
        self.durability=num
    def attack(self):
        if self.durability == 0:
            print("공격불가!")
            return
        self.durability -=1
        print('%s(으)로 %d의 데미지를 주었습니다' % (self.weapon_name, self.power))
        print("내구성 : ",self.durability)
