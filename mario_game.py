import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BROWN = (139, 69, 19)
GRAY = (128, 128, 128)
SKY_BLUE = (135, 206, 235)

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 5
        self.jump_power = -15
        self.gravity = 0.8
        self.on_ground = False
        self.lives = 3
        self.score = 0
        self.coins = 0
        
    def update(self, platforms):
        keys = pygame.key.get_pressed()
        
        # Horizontal movement
        self.vel_x = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vel_x = -self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vel_x = self.speed
            
        # Jumping
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]) and self.on_ground:
            self.vel_y = self.jump_power
            self.on_ground = False
            
        # Apply gravity
        self.vel_y += self.gravity
        
        # Horizontal collision
        self.rect.x += self.vel_x
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_x > 0:
                    self.rect.right = platform.rect.left
                elif self.vel_x < 0:
                    self.rect.left = platform.rect.right
                    
        # Vertical collision
        self.rect.y += self.vel_y
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0:
                    self.rect.top = platform.rect.bottom
                    self.vel_y = 0
                    
        # Screen boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            
        # Fall off screen
        if self.rect.top > SCREEN_HEIGHT:
            self.lives -= 1
            self.rect.x = 50
            self.rect.y = 400
            
    def draw(self, screen):
        # Draw Mario as a simple red rectangle with details
        pygame.draw.rect(screen, RED, self.rect)
        # Hat
        pygame.draw.rect(screen, RED, (self.rect.x + 5, self.rect.y - 5, 30, 10))
        # Eyes
        pygame.draw.circle(screen, WHITE, (self.rect.x + 12, self.rect.y + 10), 3)
        pygame.draw.circle(screen, WHITE, (self.rect.x + 28, self.rect.y + 10), 3)
        pygame.draw.circle(screen, BLACK, (self.rect.x + 12, self.rect.y + 10), 1)
        pygame.draw.circle(screen, BLACK, (self.rect.x + 28, self.rect.y + 10), 1)

class Platform:
    def __init__(self, x, y, width, height, color=BROWN):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)

class Coin:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 20)
        self.collected = False
        
    def update(self, player):
        if not self.collected and self.rect.colliderect(player.rect):
            self.collected = True
            player.coins += 1
            player.score += 100
            
    def draw(self, screen):
        if not self.collected:
            pygame.draw.circle(screen, YELLOW, self.rect.center, 10)
            pygame.draw.circle(screen, BLACK, self.rect.center, 10, 2)

class Enemy:
    def __init__(self, x, y, speed=1):
        self.rect = pygame.Rect(x, y, 30, 30)
        self.speed = speed
        self.direction = 1
        self.alive = True
        
    def update(self, platforms):
        if not self.alive:
            return
            
        self.rect.x += self.speed * self.direction
        
        # Check platform edges and walls
        on_platform = False
        for platform in platforms:
            # Check if enemy is on a platform
            if (self.rect.bottom >= platform.rect.top and 
                self.rect.bottom <= platform.rect.top + 10 and
                self.rect.centerx >= platform.rect.left and 
                self.rect.centerx <= platform.rect.right):
                on_platform = True
                
            # Check wall collision
            if self.rect.colliderect(platform.rect):
                self.direction *= -1
                
        # Turn around at platform edges
        if not on_platform:
            self.direction *= -1
            
    def check_collision(self, player):
        if not self.alive:
            return False
            
        if self.rect.colliderect(player.rect):
            # Check if player is jumping on enemy
            if player.vel_y > 0 and player.rect.bottom < self.rect.centery:
                self.alive = False
                player.score += 200
                player.vel_y = -10  # Bounce
                return False
            else:
                return True  # Player hit enemy
        return False
        
    def draw(self, screen):
        if self.alive:
            pygame.draw.rect(screen, BLACK, self.rect)
            # Eyes
            pygame.draw.circle(screen, RED, (self.rect.x + 8, self.rect.y + 8), 3)
            pygame.draw.circle(screen, RED, (self.rect.x + 22, self.rect.y + 8), 3)

class Powerup:
    def __init__(self, x, y, type="mushroom"):
        self.rect = pygame.Rect(x, y, 25, 25)
        self.type = type
        self.collected = False
        
    def update(self, player):
        if not self.collected and self.rect.colliderect(player.rect):
            self.collected = True
            if self.type == "mushroom":
                player.score += 500
                player.lives += 1
            elif self.type == "star":
                player.score += 1000
                
    def draw(self, screen):
        if not self.collected:
            if self.type == "mushroom":
                pygame.draw.rect(screen, RED, self.rect)
                pygame.draw.circle(screen, WHITE, (self.rect.x + 6, self.rect.y + 6), 3)
                pygame.draw.circle(screen, WHITE, (self.rect.x + 19, self.rect.y + 6), 3)
            elif self.type == "star":
                points = [
                    (self.rect.centerx, self.rect.top),
                    (self.rect.centerx + 8, self.rect.centery),
                    (self.rect.right, self.rect.centery),
                    (self.rect.centerx + 5, self.rect.bottom - 5),
                    (self.rect.centerx, self.rect.bottom),
                    (self.rect.centerx - 5, self.rect.bottom - 5),
                    (self.rect.left, self.rect.centery),
                    (self.rect.centerx - 8, self.rect.centery)
                ]
                pygame.draw.polygon(screen, YELLOW, points)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Super Mario Python")
        self.clock = pygame.time.Clock()
        self.level = 1
        self.game_over = False
        self.won = False
        
        self.reset_level()
        
    def reset_level(self):
        self.player = Player(50, 400)
        self.platforms = []
        self.coins = []
        self.enemies = []
        self.powerups = []
        
        self.create_level()
        
    def create_level(self):
        if self.level == 1:
            # Ground platforms
            self.platforms.extend([
                Platform(0, 550, 400, 50),
                Platform(500, 550, 500, 50),
                Platform(200, 450, 100, 20),
                Platform(400, 350, 100, 20),
                Platform(600, 400, 150, 20),
                Platform(800, 300, 100, 20),
                Platform(300, 250, 80, 20),
                Platform(700, 200, 120, 20)
            ])
            
            # Coins
            self.coins.extend([
                Coin(220, 420), Coin(250, 420), Coin(280, 420),
                Coin(420, 320), Coin(450, 320),
                Coin(620, 370), Coin(650, 370), Coin(680, 370),
                Coin(820, 270), Coin(320, 220), Coin(740, 170)
            ])
            
            # Enemies
            self.enemies.extend([
                Enemy(250, 420), Enemy(650, 370), Enemy(750, 170)
            ])
            
            # Powerups
            self.powerups.extend([
                Powerup(470, 320, "mushroom"),
                Powerup(850, 270, "star")
            ])
            
        elif self.level == 2:
            # More challenging level
            self.platforms.extend([
                Platform(0, 550, 200, 50),
                Platform(300, 550, 200, 50),
                Platform(600, 550, 400, 50),
                Platform(150, 450, 80, 20),
                Platform(350, 400, 80, 20),
                Platform(500, 350, 80, 20),
                Platform(700, 300, 80, 20),
                Platform(250, 300, 60, 20),
                Platform(450, 250, 60, 20),
                Platform(650, 200, 60, 20),
                Platform(850, 150, 100, 20)
            ])
            
            # More coins
            self.coins.extend([
                Coin(170, 420), Coin(370, 370), Coin(520, 320),
                Coin(720, 270), Coin(270, 270), Coin(470, 220),
                Coin(670, 170), Coin(880, 120), Coin(910, 120)
            ])
            
            # More enemies
            self.enemies.extend([
                Enemy(380, 370), Enemy(530, 320), Enemy(730, 270),
                Enemy(280, 270), Enemy(480, 220), Enemy(680, 170)
            ])
            
            # Powerups
            self.powerups.extend([
                Powerup(190, 420, "mushroom"),
                Powerup(550, 320, "star"),
                Powerup(900, 120, "mushroom")
            ])
    
    def check_level_complete(self):
        coins_collected = sum(1 for coin in self.coins if coin.collected)
        total_coins = len(self.coins)
        
        if coins_collected == total_coins and self.player.rect.x > SCREEN_WIDTH - 100:
            if self.level < 2:
                self.level += 1
                self.reset_level()
            else:
                self.won = True
    
    def update(self):
        if self.game_over or self.won:
            return
            
        self.player.update(self.platforms)
        
        for coin in self.coins:
            coin.update(self.player)
            
        for enemy in self.enemies:
            enemy.update(self.platforms)
            if enemy.check_collision(self.player):
                self.player.lives -= 1
                # Respawn player
                self.player.rect.x = 50
                self.player.rect.y = 400
                
        for powerup in self.powerups:
            powerup.update(self.player)
            
        if self.player.lives <= 0:
            self.game_over = True
            
        self.check_level_complete()
    
    def draw(self):
        self.screen.fill(SKY_BLUE)
        
        # Draw clouds
        for i in range(3):
            x = 200 + i * 300
            y = 50 + i * 30
            pygame.draw.circle(self.screen, WHITE, (x, y), 30)
            pygame.draw.circle(self.screen, WHITE, (x + 25, y), 35)
            pygame.draw.circle(self.screen, WHITE, (x + 50, y), 30)
        
        # Draw game objects
        for platform in self.platforms:
            platform.draw(self.screen)
            
        for coin in self.coins:
            coin.draw(self.screen)
            
        for enemy in self.enemies:
            enemy.draw(self.screen)
            
        for powerup in self.powerups:
            powerup.draw(self.screen)
            
        self.player.draw(self.screen)
        
        # Draw UI
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.player.score}", True, BLACK)
        lives_text = font.render(f"Lives: {self.player.lives}", True, BLACK)
        coins_text = font.render(f"Coins: {self.player.coins}", True, BLACK)
        level_text = font.render(f"Level: {self.level}", True, BLACK)
        
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(lives_text, (10, 50))
        self.screen.blit(coins_text, (10, 90))
        self.screen.blit(level_text, (10, 130))
        
        # Instructions
        if self.level == 1 and self.player.score == 0:
            inst_font = pygame.font.Font(None, 24)
            inst_text = inst_font.render("Use ARROW KEYS or WASD to move, SPACE/UP/W to jump", True, BLACK)
            inst_text2 = inst_font.render("Collect all coins and reach the right side to complete level", True, BLACK)
            self.screen.blit(inst_text, (SCREEN_WIDTH//2 - 250, SCREEN_HEIGHT - 40))
            self.screen.blit(inst_text2, (SCREEN_WIDTH//2 - 230, SCREEN_HEIGHT - 20))
        
        # Game over screen
        if self.game_over:
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            overlay.set_alpha(128)
            overlay.fill(BLACK)
            self.screen.blit(overlay, (0, 0))
            
            font = pygame.font.Font(None, 72)
            game_over_text = font.render("GAME OVER", True, RED)
            score_text = font.render(f"Final Score: {self.player.score}", True, WHITE)
            restart_text = font.render("Press R to Restart or Q to Quit", True, WHITE)
            
            self.screen.blit(game_over_text, (SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT//2 - 100))
            self.screen.blit(score_text, (SCREEN_WIDTH//2 - 120, SCREEN_HEIGHT//2 - 20))
            self.screen.blit(restart_text, (SCREEN_WIDTH//2 - 200, SCREEN_HEIGHT//2 + 40))
            
        # Victory screen
        if self.won:
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            overlay.set_alpha(128)
            overlay.fill(BLACK)
            self.screen.blit(overlay, (0, 0))
            
            font = pygame.font.Font(None, 72)
            win_text = font.render("YOU WON!", True, GREEN)
            score_text = font.render(f"Final Score: {self.player.score}", True, WHITE)
            restart_text = font.render("Press R to Restart or Q to Quit", True, WHITE)
            
            self.screen.blit(win_text, (SCREEN_WIDTH//2 - 120, SCREEN_HEIGHT//2 - 100))
            self.screen.blit(score_text, (SCREEN_WIDTH//2 - 120, SCREEN_HEIGHT//2 - 20))
            self.screen.blit(restart_text, (SCREEN_WIDTH//2 - 200, SCREEN_HEIGHT//2 + 40))
        
        pygame.display.flip()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return False
                elif event.key == pygame.K_r and (self.game_over or self.won):
                    self.level = 1
                    self.game_over = False
                    self.won = False
                    self.reset_level()
        return True
    
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

# Run the game
if __name__ == "__main__":
    game = Game()
    game.run()