import pygame


class HeroSprite(pygame.sprite.Sprite):  # 用精灵和精灵组建立大批敌机
    def __init__(self, screen_rect, speed=2):
        super().__init__()  # 父类不是obj，要调用父类初始化
        image_name = "F:\program\Python\pygame_exp\StarWar\material\Hero.png"
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.SCREEN_REC = screen_rect
        self.SPEED = speed
        self.speed = self.SPEED
        self.rect.centerx = screen_rect[0]/2  # centerx为中轴线位置
        self.rect.bottom = screen_rect[1] - 30  # 距离底部30px

        self.bullet_group = pygame.sprite.Group()

    def update(self, direction, *args):  # 重写父类update
        if self.rect.left < 0:  # 主角的左边线
            if direction:
                self.speed = self.SPEED
            else:
                self.speed = 0
        elif self.rect.right > self.SCREEN_REC[0]:  # 主角的右边线
            if direction:
                self.speed = 0
            else:
                self.speed = -self.SPEED
        else:
            if direction:
                self.speed = self.SPEED
            else:
                self.speed = -self.SPEED
        self.rect.x += self.speed


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen_rect, hero, speed=2):
        super().__init__()  # 父类不是obj，要调用父类初始化
        image_name = "F:\program\Python\pygame_exp\StarWar\material\Bullet.png"
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.rect.centerx = hero.rect.centerx
        self.rect.bottom = hero.rect.top
        self.SCREEN_REC = screen_rect
        self.speed = speed

    def update(self, *args):  # 重写父类update
        if self.rect.y <= 0:
            self.kill()  # 销毁对象
        self.rect.y -= self.speed

    """背景与元素叠加绘制原理
    self.bg = pygame.image.load("F:\program\Python\pygame_exp\StarWar\material\BG.png")  # 加载图像
    self.b_x = 0
    self.b_y = 0
    self.B_W = 283
    self.B_H = 397
    self.bg_rect = pygame.Rect(b_x, b_y, B_W, B_H)  # 设置主角元素方块位置(x, y);大小size(width, height)
    self.screen.blit(bg, (bg_rect.x, bg_rect.y))  # 让背景调用图像,设置初始位置
    
    //******************所有元素绘制完成
    
    # pygame.display.update()  # 统一刷新背景"""

    """动态绘制原理
    hero, hero_rect = hero_move.move_hero(hero, hero_rect, bg_rect, self.event_list)  # 更新改变主角位置
     self.screen.blit(bg, bg_rect)  # 更新绘制背景，覆盖上一个绘制的飞机
    self.screen.blit(hero, hero_rect)  # 绘制新的飞机"""