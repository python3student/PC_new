import pygame

screen_width = 600
screen_height = 500
BG_COLOR = pygame.Color(255, 255, 0)
T_COLOR = pygame.Color(255, 0, 0)


# 主程序
class MainGame:
    window = None

    # 开始游戏
    def start_game(self):
        # 屏幕显示
        pygame.display.init()
        MainGame.window = pygame.display.set_mode(size=[screen_width, screen_height])
        pygame.display.set_caption("坦克大战1.01")
        MainGame.window.fill(BG_COLOR)
        while True:
            # 文字显示
            MainGame.window.blit(self.text('敌方剩余坦克数量：{}'.format(6)), dest=(200, 10))
            # 获取事件
            self.get_event()
            pygame.display.update()

    # 结束游戏
    def end_game(self):
        print('游戏结束，欢迎下次游玩')
        exit()

    # 绘制文字
    def text(self, text):
        pygame.font.init()
        fort = pygame.font.SysFont('华文仿宋', 20)
        textsurface = fort.render(text, False, T_COLOR)
        return textsurface

    def get_event(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                self.end_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP0:
                    self.end_game()
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    print('坦克开始向左走')
                    MyTank().move()
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    print('坦克开始向右走')
                    MyTank().move()
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    print('坦克开始向上走')
                    MyTank().move()
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    print('坦克开始向下走')
                    MyTank().move()


class Tank:

    def __init__(self):
        pass

    def shot(self):
        pass

    def display(self):
        pass

    def move(self):
        pass


class MyTank(Tank):

    def shot(self):
        pass

    def display(self):
        pass

    def move(self):
        pass


class ETank(Tank):

    def shot(self):
        pass

    def display(self):
        pass

    def move(self):
        pass


class Wall:

    def __init__(self):
        pass

    def display(self):
        pass


class B:

    def display(self):
        pass


class MyB:
    pass


class EB:
    pass


class Music:

    def play(self):
        pass


class Photo():

    def display(self):
        pass


if __name__ == '__main__':
    MainGame().start_game()
