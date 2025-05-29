# Can you see John Cena?
# I wanted to use the famous WWE fighter John Cena with his slogan "You can´t see me" that´s why the image must go fast
# AI Tool chatGPT helped me in understanding the change from procedural to OOP and the structure that was provided
import pygame

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 300
BACKGROUND_COLOR = (60, 255, 170)


class John:
    def __init__(self, x, y, image_path):
        # charge and escalate image
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.x = x
        self.y = y
        self.speed = 15

    def move(self):
        self.x += self.speed #moves the image horizontally
        self.y += self.speed #moves the image vertically
        if self.x > SCREEN_WIDTH: #prevents it from disappearing from the right
            self.x = 0
        if self.y > SCREEN_HEIGHT:
            self.y = 0

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('image')
        self.clock = pygame.time.Clock()
        self.running = True

        # create the character
        self.john = John(100, 100, "ucantcme.png")

    def handle_events(self):
       #game event managing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False #this stops the game from running when we quit, it ends the loop

    def update(self):
        #frame actualization logic
        self.john.move()

    def draw(self):
        # screen coloring
        self.screen.fill(BACKGROUND_COLOR)
        self.john.draw(self.screen)
        pygame.display.flip()

    def run(self):
        # principal loop
        while self.running:
            self.clock.tick(60)
            self.handle_events()
            self.update()
            self.draw()

        pygame.quit()
        exit(0)


if __name__ == "__main__":
    game = Game()
    game.run()
