from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint


class Paddle(Widget):
    
    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class WortGame(Widget):
    ball = ObjectProperty(None)
    player = ObjectProperty(None)

    def serve_ball(self):
        self.ball.center = self.center
        self.ball.velocity = (1, 4)

    def update(self, dt):
        self.ball.move()

        self.player.bounce_ball(self.ball)

        # bounce off top and bottom
        if self.ball.top > self.height:
            self.ball.velocity_y *= -1

        # bounce off left or right
        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1

        if self.ball.y < 0:
            self.serve_ball()

    def on_touch_move(self, touch):
        self.player.center_x = touch.x


class WortApp(App):
    def build(self):
        game = WortGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)        
        return game


if __name__ == '__main__':
    WortApp().run()

__version__ = '0.0.1'
