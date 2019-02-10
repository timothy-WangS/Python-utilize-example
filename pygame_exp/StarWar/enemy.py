import random
import pygame


class EnemySprite(pygame.sprite.Sprite):  # 用精灵和精灵组建立大批敌机
    def __init__(self, screen_rect):
        super().__init__()  # 父类不是obj，要调用父类初始化
        image_name = "F:\program\Python\pygame_exp\StarWar\material\Enemy.png"
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.SCREEN_REC = screen_rect
        self.rect.bottom = 0  # y方向上从-height开始
        self.rect.x = random.randint(0, self.SCREEN_REC[0]-self.rect.width)  # 水平位置cong0~屏幕宽度-图片宽度
        self.speed = random.randint(1, 3)  # 随机速度

    def update(self, *args):  # 重写父类update
        if self.rect.y >= self.SCREEN_REC[1]:
            self.kill()  # 销毁对象
            print("飞出 %s" % self.rect)
        self.rect.y += self.speed
