#1 
from pygame import * 


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_y, player_speed,width,height):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x , self.rect.y))
#2
class Player(GameSprite):
    def update_r(self):
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <win_height - 80:
            self.rect.y += self.speed
            
#3
while game:
    for e in event.get():
        if e.type = QUIT:
        game = False 
    if finish != True:
        window.fill(back)
        racket1.update_1()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed y
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect (racket2, ball):
            speed_x *= -1
            speed_y *= 1
#4


#5
if ball.rect.y > win_height-50 or ball.rect.y < 0:
    speed_y *= -1


    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))
        game_over = True


    if ball.rect.x > win_width:
        finish = True
        window.blit(lose2,(200,200))
        game_over = True
    racket1.reset()
    racket2.reset()
    ball.reset()
display.update()
clock.tick(FPS)
