import pygame
import enemy
import hero
import bg


class StarWar(object):
    def __init__(self):
        pygame.init()  # 游戏之前初始化
        print("初始化")
        self.SCREEN_REC = (283, 397)  # 定义常量
        self.FRAME_PER_SEC = 60
        self.CREATE_ENEMY_EVENT = pygame.USEREVENT  # 创建敌机定时器常量
        self.CREATE_FIRE_EVENT = pygame.USEREVENT + 1  # 创建发射子弹常量（用户常量+1）
        self.score = 0

        self.screen = pygame.display.set_mode(self.SCREEN_REC)  # 创建主窗口,缺省值resolution(宽高)，flags(附加选项)，depth(颜色位数)
        self.clock = pygame.time.Clock()  # 游戏时钟
        self.__create_sprites()  # 创建敌人和背景精灵组
        pygame.time.set_timer(self.CREATE_ENEMY_EVENT, 600)  # 事件定时器常量，时间间隔毫秒
        pygame.time.set_timer(self.CREATE_FIRE_EVENT, 500)  # 发射子弹事件

    def __create_sprites(self):
        bg1 = bg.BackGroundSprite(self.SCREEN_REC)
        bg2 = bg.BackGroundSprite(self.SCREEN_REC, True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        self.enemy_group = pygame.sprite.Group()

        self.the_hero = hero.HeroSprite(self.SCREEN_REC)
        self.hero_group = pygame.sprite.Group(self.the_hero)

        self.bullet_group = pygame.sprite.Group()

    def __event_handler(self):
        for event in pygame.event.get():
            # 退出游戏
            if event.type == pygame.QUIT:
                StarWar.__game_over()
            elif event.type == self.CREATE_ENEMY_EVENT:
                # print("敌机！！！")
                the_enemy = enemy.EnemySprite(self.SCREEN_REC)
                self.enemy_group.add(the_enemy)
            elif event.type == self.CREATE_FIRE_EVENT:
                the_bullet = hero.Bullet(self.SCREEN_REC, self.the_hero)
                self.bullet_group.add(the_bullet)
                # self.the_hero.fire()
            """elif event.type == pygame.KEYDOWN:  # 按住不放只触发一次
                if event.key == pygame.K_RIGHT:
                    print("右移")
                elif event.key == pygame.K_LEFT:
                    print("左移")"""
        key_pressed = pygame.key.get_pressed()  # 键盘捕获，返回[0, 0, 0, ...1, 0,  ...],指定的按下的位置1
        if key_pressed[pygame.K_RIGHT]:  # 按住不放触发多次
            self.hero_group.update(True)
        elif key_pressed[pygame.K_LEFT]:
            self.hero_group.update(False)
        else:
            pass

    def __check_collied(self):
        bullet_kill = pygame.sprite.groupcollide(self.bullet_group, self.enemy_group, True, True)  # 精灵组对象与精灵组对象碰撞
        if len(bullet_kill) > 0:
            print("摧毁敌机")
            self.score += 2

        hero_killed = pygame.sprite.spritecollide(self.the_hero, self.enemy_group, True)
        if len(hero_killed) > 0:
            print("GAME OVER!!! 得分 %d" % self.score)
            self.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.bullet_group.update()
        self.bullet_group.draw(self.screen)

        self.hero_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()

    def start_game(self):
        print("游戏开始")
        while True:
            self.clock.tick(self.FRAME_PER_SEC)  # 设置刷新帧率
            self.score += 1/60
            self.__event_handler()  # 事件监听
            self.__check_collied()  # 碰撞检测
            self.__update_sprites()  # 更新绘制精灵组
            pygame.display.update()  # 更新显示


if __name__ == '__main__':
    game = StarWar()
    game.start_game()
