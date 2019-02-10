import pygame


class BackGroundSprite(pygame.sprite.Sprite):  # 用精灵和精灵组建立背景
    def __init__(self, screen_rect, is_alt=False, speed=1):  # speed只支持整数
        super().__init__()  # 父类不是obj，要调用父类初始化
        image_name = "F:\program\Python\pygame_exp\StarWar\material\BG.png"  # 背景图片路径
        self.image = pygame.image.load(image_name)  # 加载图像
        self.rect = self.image.get_rect()
        self.speed = speed
        self.SCREEN_REC = screen_rect
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self, *args):  # 重写父类update
        if self.rect.y >= self.SCREEN_REC[1]:  # 背景移出
            self.rect.y = -self.rect.height  # 回滚到上方拼贴
        self.rect.y += self.speed  # 向下移动
