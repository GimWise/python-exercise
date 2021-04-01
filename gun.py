# gun.py

from weapon import Weapon

class Gun(Weapon):
    def __init__(self, name, power,num):
        super().__init__(name,power)
        self.bullet_num=num
    def attack(self):
        if self.bullet_num == 0:
            print("공격 불가!")
            return
        print('%s(으)로 %d의 데미지를 주었습니다' % (self.weapon_name, self.power))
        self.bullet_num -=1
        print("남은 총알 : ",self.bullet_num)
    def reload(self, num):
        self.bullet_num += num




