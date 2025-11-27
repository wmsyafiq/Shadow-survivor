import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
FPS = 60

# Colors
BLACK = (10, 10, 20)
DARK_BLUE = (15, 15, 35)
PURPLE = (138, 43, 226)
DARK_PURPLE = (75, 0, 130)
CYAN = (0, 255, 255)
LIGHT_CYAN = (100, 255, 255)
RED = (255, 50, 50)
ORANGE = (255, 140, 0)
YELLOW = (255, 215, 0)
GREEN = (50, 255, 50)
PINK = (255, 105, 180)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)
DARK_GREEN = (34, 139, 34)
BROWN = (139, 69, 19)
GRAY = (128, 128, 128)

def draw_ninja(surface, x, y, size, color=CYAN):
    """Draw a pixel art Sonic the Hedgehog"""
    pixel_size = size // 10
    
    # Quills/Spikes (back)
    pygame.draw.rect(surface, color, (x - pixel_size * 4, y - pixel_size * 3, pixel_size * 2, pixel_size * 4))
    pygame.draw.rect(surface, color, (x - pixel_size * 3, y - pixel_size * 4, pixel_size * 2, pixel_size * 2))
    pygame.draw.rect(surface, color, (x - pixel_size, y - pixel_size * 5, pixel_size * 2, pixel_size * 2))
    
    # Head (blue)
    pygame.draw.rect(surface, color, (x - pixel_size * 3, y - pixel_size * 3, pixel_size * 6, pixel_size * 4))
    
    # Face/muzzle (beige/tan)
    tan = (255, 220, 177)
    pygame.draw.rect(surface, tan, (x - pixel_size * 2, y - pixel_size * 2, pixel_size * 4, pixel_size * 3))
    
    # Eyes (white with black pupils)
    pygame.draw.rect(surface, WHITE, (x - pixel_size * 2, y - pixel_size * 2, pixel_size * 2, pixel_size * 2))
    pygame.draw.rect(surface, WHITE, (x, y - pixel_size * 2, pixel_size * 2, pixel_size * 2))
    # Pupils (green)
    pygame.draw.rect(surface, GREEN, (x - pixel_size, y - pixel_size, pixel_size, pixel_size))
    pygame.draw.rect(surface, GREEN, (x + pixel_size, y - pixel_size, pixel_size, pixel_size))
    
    # Nose (small black)
    pygame.draw.rect(surface, BLACK, (x, y, pixel_size, pixel_size))
    
    # Body (blue)
    pygame.draw.rect(surface, color, (x - pixel_size * 2, y + pixel_size, pixel_size * 4, pixel_size * 3))
    
    # Belly (tan)
    pygame.draw.rect(surface, tan, (x - pixel_size, y + pixel_size, pixel_size * 2, pixel_size * 2))
    
    # Arms (blue)
    pygame.draw.rect(surface, color, (x - pixel_size * 3, y + pixel_size, pixel_size, pixel_size * 2))
    pygame.draw.rect(surface, color, (x + pixel_size * 2, y + pixel_size, pixel_size, pixel_size * 2))
    
    # Gloves (white)
    pygame.draw.rect(surface, WHITE, (x - pixel_size * 3, y + pixel_size * 2, pixel_size, pixel_size))
    pygame.draw.rect(surface, WHITE, (x + pixel_size * 2, y + pixel_size * 2, pixel_size, pixel_size))
    
    # Legs (blue)
    pygame.draw.rect(surface, color, (x - pixel_size * 2, y + pixel_size * 3, pixel_size, pixel_size * 2))
    pygame.draw.rect(surface, color, (x + pixel_size, y + pixel_size * 3, pixel_size, pixel_size * 2))
    
    # Shoes (red with white stripe)
    pygame.draw.rect(surface, RED, (x - pixel_size * 3, y + pixel_size * 4, pixel_size * 2, pixel_size))
    pygame.draw.rect(surface, RED, (x + pixel_size, y + pixel_size * 4, pixel_size * 2, pixel_size))
    pygame.draw.rect(surface, WHITE, (x - pixel_size * 3, y + pixel_size * 4, pixel_size * 2, pixel_size // 2))
    pygame.draw.rect(surface, WHITE, (x + pixel_size, y + pixel_size * 4, pixel_size * 2, pixel_size // 2))

def draw_goblin(surface, x, y, size, color=GREEN):
    """Draw a pixel art goblin"""
    pixel_size = size // 6
    
    # Ears
    pygame.draw.rect(surface, color, (x - pixel_size * 3, y - pixel_size * 2, pixel_size, pixel_size * 2))
    pygame.draw.rect(surface, color, (x + pixel_size * 2, y - pixel_size * 2, pixel_size, pixel_size * 2))
    # Head
    pygame.draw.rect(surface, color, (x - pixel_size * 2, y - pixel_size * 3, pixel_size * 4, pixel_size * 3))
    # Eyes (red)
    pygame.draw.rect(surface, RED, (x - pixel_size * 2, y - pixel_size * 2, pixel_size, pixel_size))
    pygame.draw.rect(surface, RED, (x + pixel_size, y - pixel_size * 2, pixel_size, pixel_size))
    # Body
    pygame.draw.rect(surface, DARK_GREEN, (x - pixel_size * 2, y, pixel_size * 4, pixel_size * 2))
    # Arms
    pygame.draw.rect(surface, color, (x - pixel_size * 3, y, pixel_size, pixel_size * 2))
    pygame.draw.rect(surface, color, (x + pixel_size * 2, y, pixel_size, pixel_size * 2))
    # Legs
    pygame.draw.rect(surface, BROWN, (x - pixel_size * 2, y + pixel_size * 2, pixel_size, pixel_size))
    pygame.draw.rect(surface, BROWN, (x + pixel_size, y + pixel_size * 2, pixel_size, pixel_size))

def draw_orc(surface, x, y, size, color=DARK_GREEN):
    """Draw a pixel art orc"""
    pixel_size = size // 8
    
    # Head (larger)
    pygame.draw.rect(surface, color, (x - pixel_size * 3, y - pixel_size * 4, pixel_size * 6, pixel_size * 4))
    # Tusks
    pygame.draw.rect(surface, WHITE, (x - pixel_size * 3, y - pixel_size, pixel_size, pixel_size * 2))
    pygame.draw.rect(surface, WHITE, (x + pixel_size * 2, y - pixel_size, pixel_size, pixel_size * 2))
    # Eyes (angry red)
    pygame.draw.rect(surface, RED, (x - pixel_size * 2, y - pixel_size * 3, pixel_size, pixel_size))
    pygame.draw.rect(surface, RED, (x + pixel_size, y - pixel_size * 3, pixel_size, pixel_size))
    # Body (muscular)
    pygame.draw.rect(surface, color, (x - pixel_size * 3, y, pixel_size * 6, pixel_size * 4))
    pygame.draw.rect(surface, BROWN, (x - pixel_size * 2, y, pixel_size * 4, pixel_size * 2))
    # Arms (thick)
    pygame.draw.rect(surface, color, (x - pixel_size * 4, y, pixel_size * 2, pixel_size * 3))
    pygame.draw.rect(surface, color, (x + pixel_size * 2, y, pixel_size * 2, pixel_size * 3))

def draw_ogre(surface, x, y, size, color=BROWN):
    """Draw a pixel art ogre boss"""
    pixel_size = size // 10
    
    # Massive head
    pygame.draw.rect(surface, color, (x - pixel_size * 4, y - pixel_size * 5, pixel_size * 8, pixel_size * 5))
    # Horns
    pygame.draw.rect(surface, GRAY, (x - pixel_size * 5, y - pixel_size * 6, pixel_size * 2, pixel_size * 3))
    pygame.draw.rect(surface, GRAY, (x + pixel_size * 3, y - pixel_size * 6, pixel_size * 2, pixel_size * 3))
    # Eyes (glowing)
    pygame.draw.rect(surface, ORANGE, (x - pixel_size * 3, y - pixel_size * 4, pixel_size * 2, pixel_size * 2))
    pygame.draw.rect(surface, ORANGE, (x + pixel_size, y - pixel_size * 4, pixel_size * 2, pixel_size * 2))
    # Teeth
    pygame.draw.rect(surface, WHITE, (x - pixel_size * 2, y - pixel_size, pixel_size, pixel_size * 2))
    pygame.draw.rect(surface, WHITE, (x + pixel_size, y - pixel_size, pixel_size, pixel_size * 2))
    # Body (huge)
    pygame.draw.rect(surface, color, (x - pixel_size * 5, y, pixel_size * 10, pixel_size * 6))
    pygame.draw.rect(surface, (100, 50, 20), (x - pixel_size * 4, y, pixel_size * 8, pixel_size * 4))
    # Arms (massive)
    pygame.draw.rect(surface, color, (x - pixel_size * 7, y, pixel_size * 3, pixel_size * 5))
    pygame.draw.rect(surface, color, (x + pixel_size * 4, y, pixel_size * 3, pixel_size * 5))

class Particle:
    def __init__(self, x, y, color, vx=None, vy=None, life=30, size=3):
        if vx is None:
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(1, 4)
            self.vx = math.cos(angle) * speed
            self.vy = math.sin(angle) * speed
        else:
            self.vx = vx
            self.vy = vy
        self.x = x
        self.y = y
        self.life = life
        self.max_life = life
        self.color = color
        self.size = size
        self.gravity = 0.1
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += self.gravity
        self.life -= 1
    
    def draw(self, screen, camera):
        if self.life > 0:
            alpha = int(255 * (self.life / self.max_life))
            size = int(self.size * (self.life / self.max_life))
            surf = pygame.Surface((size * 2, size * 2), pygame.SRCALPHA)
            color = (*self.color[:3], alpha)
            pygame.draw.circle(surf, color, (size, size), size)
            screen.blit(surf, (int(self.x - camera.x - size), int(self.y - camera.y - size)))

class Pickup:
    def __init__(self, x, y, pickup_type):
        self.x = x
        self.y = y
        self.type = pickup_type  # 'xp' or 'health'
        self.size = 8 if pickup_type == 'xp' else 12
        self.color = CYAN if pickup_type == 'xp' else RED
        self.collected = False
        self.attraction_radius = 100
        self.bob_offset = 0
        self.bob_speed = 0.1
    
    def update(self, player):
        # Bobbing animation
        self.bob_offset = math.sin(pygame.time.get_ticks() * self.bob_speed / 100) * 5
        
        # Attract to player if close
        dist = math.hypot(self.x - player.x, self.y - player.y)
        if dist < self.attraction_radius:
            angle = math.atan2(player.y - self.y, player.x - self.x)
            speed = 4
            self.x += math.cos(angle) * speed
            self.y += math.sin(angle) * speed
        
        # Collect
        if dist < player.size + self.size:
            if self.type == 'xp':
                player.xp += 10
            elif self.type == 'health':
                player.heal(20)
            self.collected = True
    
    def draw(self, screen, camera):
        screen_x = int(self.x - camera.x)
        screen_y = int(self.y - camera.y + self.bob_offset)
        
        # Glow effect
        glow_surf = pygame.Surface((self.size * 4, self.size * 4), pygame.SRCALPHA)
        pygame.draw.circle(glow_surf, (*self.color, 60), (self.size * 2, self.size * 2), self.size * 2)
        screen.blit(glow_surf, (screen_x - self.size * 2, screen_y - self.size * 2))
        
        if self.type == 'xp':
            # Crystal shard
            points = [
                (screen_x, screen_y - self.size),
                (screen_x + self.size // 2, screen_y),
                (screen_x, screen_y + self.size),
                (screen_x - self.size // 2, screen_y)
            ]
            pygame.draw.polygon(screen, self.color, points)
            pygame.draw.polygon(screen, LIGHT_CYAN, points, 2)
        else:
            # Health heart
            pygame.draw.circle(screen, self.color, (screen_x - self.size // 3, screen_y - self.size // 4), self.size // 2)
            pygame.draw.circle(screen, self.color, (screen_x + self.size // 3, screen_y - self.size // 4), self.size // 2)
            pygame.draw.polygon(screen, self.color, [
                (screen_x - self.size, screen_y - self.size // 4),
                (screen_x, screen_y + self.size),
                (screen_x + self.size, screen_y - self.size // 4)
            ])

class Camera:
    def __init__(self, width, height):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
    
    def update(self, target):
        self.x = target.x - SCREEN_WIDTH // 2
        self.y = target.y - SCREEN_HEIGHT // 2

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 24
        self.hp = 100
        self.max_hp = 100
        self.speed = 4.5
        self.xp = 0
        self.level = 1
        self.color = CYAN
        self.angle = 0
        self.invulnerable = 0
        
        # Upgrades
        self.max_projectiles = 1
        self.projectile_damage = 1
        self.projectile_speed = 5
        self.fire_rate = 500
        self.pierce = 0
        self.life_steal = 0
        self.speed_boost = 0
    
    def move(self, keys):
        dx, dy = 0, 0
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dy -= 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dy += 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx -= 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx += 1
        
        if dx != 0 or dy != 0:
            magnitude = math.sqrt(dx * dx + dy * dy)
            actual_speed = self.speed * (1 + self.speed_boost * 0.1)
            self.x += (dx / magnitude) * actual_speed
            self.y += (dy / magnitude) * actual_speed
            self.angle = math.atan2(dy, dx)
        
        if self.invulnerable > 0:
            self.invulnerable -= 1
    
    def take_damage(self, damage):
        if self.invulnerable <= 0:
            self.hp -= damage
            self.invulnerable = 30
            return True
        return False
    
    def heal(self, amount):
        old_hp = self.hp
        self.hp = min(self.hp + amount, self.max_hp)
        return self.hp > old_hp
    
    def gain_xp(self, amount):
        self.xp += amount
        xp_needed = self.level * 100
        if self.xp >= xp_needed:
            self.xp -= xp_needed
            self.level += 1
            return True
        return False
    
    def draw(self, screen, camera, game=None):
      
        if game is None:
            return
        screen_x = int(self.x - camera.x)
        screen_y = int(self.y - camera.y)

        # Optional invulnerability flash
        if self.invulnerable > 0 and self.invulnerable % 6 < 3:
            img = pygame.Surface(game.player_img.get_size(), pygame.SRCALPHA)
            img.fill((255, 255, 255, 150))  # white flash overlay
        else:
            img = game.player_img

        rect = img.get_rect(center=(screen_x, screen_y))
        screen.blit(img, rect.topleft)

class Enemy:
    def __init__(self, x, y, wave):
        self.x = x
        self.y = y
        
        # Enemy types
        types = [
            {'size': 18, 'speed': 1.5, 'hp': 2, 'color': GREEN, 'xp': 8, 'name': 'Goblin', 'draw': 'goblin'},
            {'size': 24, 'speed': 1.0, 'hp': 4, 'color': DARK_GREEN, 'xp': 15, 'name': 'Orc', 'draw': 'orc'},
            {'size': 15, 'speed': 2.5, 'hp': 1, 'color': RED, 'xp': 12, 'name': 'Imp', 'draw': 'goblin'},
            {'size': 30, 'speed': 0.8, 'hp': 8, 'color': BROWN, 'xp': 25, 'name': 'Troll', 'draw': 'orc'}
        ]
        
        enemy_type = min(random.randint(0, wave // 2), len(types) - 1)
        t = types[enemy_type]
        
        self.size = t['size']
        self.speed = t['speed'] * (1 + wave * 0.03)
        self.hp = t['hp'] + wave // 2
        self.max_hp = self.hp
        self.color = t['color']
        self.xp = t['xp']
        self.name = t['name']
        self.draw_type = t['draw']
        self.angle = 0
        self.hit_flash = 0
        self.is_boss = False
        self.damage = 15
    
    def update(self, player):
        self.angle = math.atan2(player.y - self.y, player.x - self.x)
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        
        if self.hit_flash > 0:
            self.hit_flash -= 1
    
    def take_damage(self, damage):
        self.hp -= damage
        self.hit_flash = 5
        return self.hp <= 0
    
    def draw(self, screen, camera, game=None):
        screen_x = int(self.x - camera.x)
        screen_y = int(self.y - camera.y)
        
        
        color = WHITE if self.hit_flash > 0 else self.color
        
        if self.draw_type == 'goblin':
            draw_goblin(screen, screen_x, screen_y, self.size, color)
        elif self.draw_type == 'orc':
            draw_orc(screen, screen_x, screen_y, self.size, color)
        
        # HP bar
        if self.hp < self.max_hp:
            bar_width = self.size * 2
            bar_height = 4
            bar_x = screen_x - bar_width / 2
            bar_y = screen_y - self.size - 10
            
            pygame.draw.rect(screen, (40, 40, 40), (bar_x, bar_y, bar_width, bar_height))
            hp_width = bar_width * (self.hp / self.max_hp)
            pygame.draw.rect(screen, RED, (bar_x, bar_y, hp_width, bar_height))

class Boss(Enemy):
    def __init__(self, x, y, wave):
        super().__init__(x, y, wave)
        self.size = 60
        self.speed = 1.2
        self.hp = 150 + wave * 75
        self.max_hp = self.hp
        self.color = BROWN
        self.xp = 500
        self.name = f"Ogre King (Wave {wave})"
        self.draw_type = 'ogre'
        self.is_boss = True
        self.damage = 30
        self.phase = 0
    
    def update(self, player):
        super().update(player)
        
        # Boss phases - gets faster as HP drops
        hp_percent = self.hp / self.max_hp
        if hp_percent < 0.3:
            self.phase = 2
            self.speed = 2.0
        elif hp_percent < 0.6:
            self.phase = 1
            self.speed = 1.6
    
    def draw(self, screen, camera, game=None):
      if game is None or game.boss_img is None:
          return  # cannot draw without the image

      screen_x = int(self.x - camera.x)
      screen_y = int(self.y - camera.y)

      # Copy boss image for optional flash effect
      img = game.boss_img.copy()
      if getattr(self, 'hit_flash', 0) > 0:
          flash = pygame.Surface(img.get_size(), pygame.SRCALPHA)
          flash.fill((255, 255, 255, 100))
          img.blit(flash, (0, 0))

      # Draw boss
      rect = img.get_rect(center=(screen_x, screen_y))
      screen.blit(img, rect.topleft)

      # Draw HP bar and name
      bar_width = 250
      bar_height = 20
      bar_x = screen_x - bar_width / 2
      bar_y = screen_y - 100

      pygame.draw.rect(screen, (40, 40, 40), (bar_x, bar_y, bar_width, bar_height))
      hp_width = bar_width * (self.hp / self.max_hp)
      pygame.draw.rect(screen, (255, 0, 0), (bar_x, bar_y, hp_width, bar_height))

      font = pygame.font.Font(None, 28)
      name_text = font.render(self.name, True, (255, 215, 0))  # GOLD
      screen.blit(name_text, (screen_x - name_text.get_width() // 2, bar_y - 30))


class Projectile:
    def __init__(self, x, y, target_x, target_y, damage, speed, pierce=0):
        self.x = x
        self.y = y
        self.size = 6
        self.damage = damage
        self.pierce = pierce
        self.pierced = 0
        angle = math.atan2(target_y - y, target_x - x)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.color = CYAN
        self.trail = []
    
    def update(self):
        self.trail.append((self.x, self.y))
        if len(self.trail) > 6:
            self.trail.pop(0)
        self.x += self.vx
        self.y += self.vy
    
    def draw(self, screen, camera):
        for i, (tx, ty) in enumerate(self.trail):
            alpha = int(200 * (i / len(self.trail)))
            size = int(self.size * 0.7 * (i / len(self.trail)))
            surf = pygame.Surface((size * 2, size * 2), pygame.SRCALPHA)
            pygame.draw.circle(surf, (*self.color, alpha), (size, size), size)
            screen.blit(surf, (int(tx - camera.x - size), int(ty - camera.y - size)))
        
        screen_x = int(self.x - camera.x)
        screen_y = int(self.y - camera.y)
        
        # Draw shuriken
        angle = pygame.time.get_ticks() / 50
        points = []
        for i in range(4):
            a = angle + i * math.pi / 2
            points.append((screen_x + math.cos(a) * self.size, screen_y + math.sin(a) * self.size))
        pygame.draw.polygon(screen, WHITE, points)
        pygame.draw.polygon(screen, self.color, points, 2)
        pygame.draw.circle(screen, LIGHT_CYAN, (screen_x, screen_y), self.size // 2)

class UpgradeOption:
    def __init__(self, name, description, effect, rarity="common"):
        self.name = name
        self.description = description
        self.effect = effect
        self.rarity = rarity
        self.colors = {
            "common": (200, 200, 200),
            "rare": (100, 150, 255),
            "epic": (200, 0, 255),
            "legendary": (255, 200, 0)
        }
        self.color = self.colors[rarity]

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Shadow Survivor - Ninja Edition")
        self.clock = pygame.time.Clock()
        self.font_large = pygame.font.Font(None, 56)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)
        
                # Load and resize images
        player_img = pygame.image.load("player.png").convert_alpha()
        boss_img = pygame.image.load("boss.png").convert_alpha()
        
        # Resize: player smaller, boss bigger
        self.player_img = pygame.transform.scale(player_img, (50, 50))  # 50x50 px
        self.boss_img = pygame.transform.scale(boss_img, (200, 200))     # 200x200 px
        
        self.camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.reset()
    
    def reset(self):
        self.player = Player(0, 0)
        self.enemies = []
        self.projectiles = []
        self.particles = []
        self.pickups = []
        
        self.score = 0
        self.wave = 1
        self.enemies_per_wave = 15
        self.enemies_spawned = 0
        self.wave_complete = False
        self.boss_spawned = False
        
        self.last_enemy_spawn = pygame.time.get_ticks()
        self.last_projectile = pygame.time.get_ticks()
        
        self.game_state = 'menu'
        self.upgrade_options = []
        self.selected_upgrade = 0
        
        self.kills = 0
        self.time_survived = 0
        self.start_time = 0
    
    def get_upgrade_options(self):
        all_upgrades = [
            UpgradeOption("Shuriken Storm", "Fire +1 projectile", lambda p: setattr(p, 'max_projectiles', p.max_projectiles + 1), "rare"),
            UpgradeOption("Shadow Strike", "+50% damage", lambda p: setattr(p, 'projectile_damage', p.projectile_damage + 0.5), "common"),
            UpgradeOption("Rapid Assault", "+30% fire rate", lambda p: setattr(p, 'fire_rate', int(p.fire_rate * 0.7)), "common"),
            UpgradeOption("Piercing Blade", "Pierce +1 enemy", lambda p: setattr(p, 'pierce', p.pierce + 1), "epic"),
            UpgradeOption("Blood Drain", "Heal 3 HP on kill", lambda p: setattr(p, 'life_steal', p.life_steal + 3), "rare"),
            UpgradeOption("Iron Body", "+30 max HP", lambda p: (setattr(p, 'max_hp', p.max_hp + 30), p.heal(30)), "common"),
            UpgradeOption("Swift Wind", "+25% speed", lambda p: setattr(p, 'speed_boost', p.speed_boost + 1), "rare"),
            UpgradeOption("Lightning Barrage", "+60% fire rate", lambda p: setattr(p, 'fire_rate', int(p.fire_rate * 0.4)), "epic"),
            UpgradeOption("Full Restore", "Max HP heal", lambda p: setattr(p, 'hp', p.max_hp), "legendary"),
            UpgradeOption("Sonic Shuriken", "+60% projectile speed", lambda p: setattr(p, 'projectile_speed', p.projectile_speed + 3), "common"),
        ]
        
        return random.sample(all_upgrades, min(3, len(all_upgrades)))
    
    def spawn_enemy(self, is_boss=False):
        angle = random.uniform(0, 2 * math.pi)
        distance = random.randint(600, 900)
        x = self.player.x + math.cos(angle) * distance
        y = self.player.y + math.sin(angle) * distance
        
        if is_boss:
            enemy = Boss(x, y, self.wave)
        else:
            enemy = Enemy(x, y, self.wave)
        
        self.enemies.append(enemy)
    
    def create_projectiles(self):
        if not self.enemies:
            return
        
        sorted_enemies = sorted(self.enemies, 
                               key=lambda e: math.hypot(e.x - self.player.x, e.y - self.player.y))
        
        targets = sorted_enemies[:self.player.max_projectiles]
        
        for target in targets:
            proj = Projectile(self.player.x, self.player.y, target.x, target.y,
                            self.player.projectile_damage, self.player.projectile_speed,
                            self.player.pierce)
            self.projectiles.append(proj)
    
    def create_particles(self, x, y, color, count=12):
        for _ in range(count):
            self.particles.append(Particle(x, y, color))
    
    def drop_pickup(self, x, y):
        rand = random.random()
        if rand < 0.15:  # 15% health drop
            self.pickups.append(Pickup(x, y, 'health'))
        # Always drop XP
        for _ in range(random.randint(1, 3)):
            offset_x = random.randint(-20, 20)
            offset_y = random.randint(-20, 20)
            self.pickups.append(Pickup(x + offset_x, y + offset_y, 'xp'))
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.game_state == 'playing':
                        self.game_state = 'paused'
                    elif self.game_state in ['paused', 'upgrade']:
                        self.game_state = 'playing'
                
                if self.game_state == 'menu' or self.game_state == 'game_over':
                    if event.key == pygame.K_SPACE:
                        self.reset()
                        self.game_state = 'playing'
                        self.start_time = pygame.time.get_ticks()
                
                if self.game_state == 'upgrade':
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.selected_upgrade = (self.selected_upgrade - 1) % len(self.upgrade_options)
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.selected_upgrade = (self.selected_upgrade + 1) % len(self.upgrade_options)
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        upgrade = self.upgrade_options[self.selected_upgrade]
                        upgrade.effect(self.player)
                        self.game_state = 'playing'
                
                if self.game_state == 'paused' and event.key == pygame.K_SPACE:
                    self.game_state = 'playing'
        
        return True
    
    def update(self):
        if self.game_state != 'playing':
            return
        
        now = pygame.time.get_ticks()
        self.time_survived = (now - self.start_time) // 1000
        keys = pygame.key.get_pressed()
        
        # Move player
        self.player.move(keys)
        self.camera.update(self.player)
        
        # Wave management - spawn more enemies per wave
        if not self.wave_complete and self.enemies_spawned < self.enemies_per_wave:
            spawn_rate = max(150, 1000 - self.wave * 40)
            if now - self.last_enemy_spawn > spawn_rate:
                self.spawn_enemy()
                self.enemies_spawned += 1
                self.last_enemy_spawn = now
        
        # Check if wave complete
        if self.enemies_spawned >= self.enemies_per_wave and len(self.enemies) == 0:
            if not self.wave_complete:
                self.wave_complete = True
                if self.wave % 5 == 0 and not self.boss_spawned:
                    self.spawn_enemy(is_boss=True)
                    self.boss_spawned = True
                elif self.boss_spawned or self.wave % 5 != 0:
                    self.wave += 1
                    self.enemies_per_wave = 15 + self.wave * 8
                    self.enemies_spawned = 0
                    self.wave_complete = False
                    self.boss_spawned = False
        
        # Auto-shoot
        if now - self.last_projectile > self.player.fire_rate:
            self.create_projectiles()
            self.last_projectile = now
        
        # Update enemies
        for enemy in self.enemies[:]:
            enemy.update(self.player)
            
            dist = math.hypot(enemy.x - self.player.x, enemy.y - self.player.y)
            if dist < self.player.size + enemy.size:
                if self.player.take_damage(enemy.damage):
                    self.create_particles(self.player.x, self.player.y, RED, 20)
                
                if self.player.hp <= 0:
                    self.game_state = 'game_over'
        
        # Update projectiles
        for proj in self.projectiles[:]:
            proj.update()
            
            if abs(proj.x - self.player.x) > 1500 or abs(proj.y - self.player.y) > 1500:
                self.projectiles.remove(proj)
                continue
            
            for enemy in self.enemies[:]:
                dist = math.hypot(enemy.x - proj.x, enemy.y - proj.y)
                
                if dist < enemy.size + proj.size:
                    if enemy.take_damage(proj.damage):
                        self.score += enemy.xp
                        self.kills += 1
                        
                        # Drop pickups
                        self.drop_pickup(enemy.x, enemy.y)
                        
                        self.enemies.remove(enemy)
                        self.create_particles(enemy.x, enemy.y, enemy.color, 20)
                        
                        if self.player.life_steal > 0:
                            if self.player.heal(self.player.life_steal):
                                self.create_particles(self.player.x, self.player.y, GREEN, 5)
                    else:
                        self.create_particles(enemy.x, enemy.y, enemy.color, 5)
                    
                    proj.pierced += 1
                    if proj.pierced > proj.pierce:
                        if proj in self.projectiles:
                            self.projectiles.remove(proj)
                    break
        
        # Update pickups
        for pickup in self.pickups[:]:
            pickup.update(self.player)
            if pickup.collected:
                self.pickups.remove(pickup)
                self.create_particles(pickup.x, pickup.y, pickup.color, 8)
                
                # Check for level up
                xp_needed = self.player.level * 100
                if self.player.xp >= xp_needed:
                    self.player.xp -= xp_needed
                    self.player.level += 1
                    self.upgrade_options = self.get_upgrade_options()
                    self.selected_upgrade = 0
                    self.game_state = 'upgrade'
                    self.create_particles(self.player.x, self.player.y, GOLD, 30)
        
        # Update particles
        for particle in self.particles[:]:
            particle.update()
            if particle.life <= 0:
                self.particles.remove(particle)
    
    def draw_background(self):
        self.screen.fill(BLACK)
        
        grid_size = 50
        offset_x = int(self.camera.x % grid_size)
        offset_y = int(self.camera.y % grid_size)
        
        for x in range(-grid_size, SCREEN_WIDTH + grid_size, grid_size):
            pygame.draw.line(self.screen, DARK_BLUE, (x - offset_x, 0), (x - offset_x, SCREEN_HEIGHT), 1)
        for y in range(-grid_size, SCREEN_HEIGHT + grid_size, grid_size):
            pygame.draw.line(self.screen, DARK_BLUE, (0, y - offset_y), (SCREEN_WIDTH, y - offset_y), 1)
    
    def draw_hud(self):
        hud_height = 80
        hud_surf = pygame.Surface((SCREEN_WIDTH, hud_height), pygame.SRCALPHA)
        pygame.draw.rect(hud_surf, (0, 0, 0, 180), (0, 0, SCREEN_WIDTH, hud_height))
        self.screen.blit(hud_surf, (0, 0))
        
        padding = 15
        y = padding
        
        # Left side
        hp_text = self.font_small.render(f"HP: {int(self.player.hp)}/{self.player.max_hp}", True, GREEN)
        level_text = self.font_small.render(f"Level: {self.player.level}", True, CYAN)
        
        self.screen.blit(hp_text, (padding, y))
        self.screen.blit(level_text, (padding, y + 25))
        
        # XP Bar
        xp_bar_width = 200
        xp_bar_height = 15
        xp_progress = self.player.xp / (self.player.level * 100)
        pygame.draw.rect(self.screen, (40, 40, 40), (padding, y + 50, xp_bar_width, xp_bar_height))
        pygame.draw.rect(self.screen, CYAN, (padding, y + 50, xp_bar_width * xp_progress, xp_bar_height))
        pygame.draw.rect(self.screen, WHITE, (padding, y + 50, xp_bar_width, xp_bar_height), 2)
        
        # Center
        wave_text = self.font_medium.render(f"Wave {self.wave}", True, PURPLE)
        self.screen.blit(wave_text, (SCREEN_WIDTH // 2 - wave_text.get_width() // 2, padding))
        
        enemies_text = self.font_small.render(f"Enemies: {len(self.enemies)}", True, RED)
        self.screen.blit(enemies_text, (SCREEN_WIDTH // 2 - enemies_text.get_width() // 2, padding + 35))
        
        # Right side
        score_text = self.font_small.render(f"Score: {self.score}", True, GOLD)
        kills_text = self.font_small.render(f"Kills: {self.kills}", True, RED)
        time_text = self.font_small.render(f"Time: {self.time_survived}s", True, WHITE)
        
        self.screen.blit(score_text, (SCREEN_WIDTH - score_text.get_width() - padding, y))
        self.screen.blit(kills_text, (SCREEN_WIDTH - kills_text.get_width() - padding, y + 25))
        self.screen.blit(time_text, (SCREEN_WIDTH - time_text.get_width() - padding, y + 50))
    
    def draw_menu(self):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 200))
        self.screen.blit(overlay, (0, 0))
        
        title = self.font_large.render("SHADOW SURVIVOR", True, PURPLE)
        subtitle = self.font_medium.render("Ninja Edition", True, CYAN)
        
        for offset in [(2, 2), (-2, -2), (2, -2), (-2, 2)]:
            glow_title = self.font_large.render("SHADOW SURVIVOR", True, DARK_PURPLE)
            self.screen.blit(glow_title, (SCREEN_WIDTH // 2 - title.get_width() // 2 + offset[0], 120 + offset[1]))
        
        self.screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 120))
        self.screen.blit(subtitle, (SCREEN_WIDTH // 2 - subtitle.get_width() // 2, 180))
        
        instructions = [
            "WASD or Arrow Keys - Move",
            "ESC - Pause",
            "",
            "Features:",
            "⚔ Fight goblins, orcs, and mighty ogres",
            "⚔ Collect XP shards to level up",
            "⚔ Health drops to heal",
            "⚔ Boss battles every 5 waves",
            "⚔ Infinite pixel art world",
            "",
            "Press SPACE to Start"
        ]
        
        y = 250
        for line in instructions:
            color = GOLD if "SPACE" in line else WHITE
            text = self.font_small.render(line, True, color)
            self.screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, y))
            y += 32
        
        alpha = int(128 + 127 * math.sin(pygame.time.get_ticks() / 300))
        prompt_text = self.font_medium.render("Press SPACE", True, (*GOLD, alpha))
        self.screen.blit(prompt_text, (SCREEN_WIDTH // 2 - prompt_text.get_width() // 2, SCREEN_HEIGHT - 80))
    
    def draw_pause(self):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        self.screen.blit(overlay, (0, 0))
        
        pause_text = self.font_large.render("PAUSED", True, WHITE)
        self.screen.blit(pause_text, (SCREEN_WIDTH // 2 - pause_text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))
        
        resume_text = self.font_medium.render("Press ESC or SPACE to resume", True, CYAN)
        self.screen.blit(resume_text, (SCREEN_WIDTH // 2 - resume_text.get_width() // 2, SCREEN_HEIGHT // 2))
        
        stats = [
            f"Wave: {self.wave}",
            f"Score: {self.score}",
            f"Kills: {self.kills}",
            f"Time: {self.time_survived}s"
        ]
        
        y = SCREEN_HEIGHT // 2 + 80
        for stat in stats:
            text = self.font_small.render(stat, True, WHITE)
            self.screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, y))
            y += 35
    
    def draw_upgrade_screen(self):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 200))
        self.screen.blit(overlay, (0, 0))
        
        title = self.font_large.render("LEVEL UP!", True, GOLD)
        self.screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 80))
        
        subtitle = self.font_medium.render("Choose Your Upgrade", True, CYAN)
        self.screen.blit(subtitle, (SCREEN_WIDTH // 2 - subtitle.get_width() // 2, 140))
        
        card_width = 280
        card_height = 180
        spacing = 30
        start_x = (SCREEN_WIDTH - (card_width * 3 + spacing * 2)) // 2
        start_y = 220
        
        for i, upgrade in enumerate(self.upgrade_options):
            x = start_x + i * (card_width + spacing)
            
            if i == self.selected_upgrade:
                glow_surf = pygame.Surface((card_width + 20, card_height + 20), pygame.SRCALPHA)
                pygame.draw.rect(glow_surf, (*upgrade.color, 100), (0, 0, card_width + 20, card_height + 20), border_radius=15)
                self.screen.blit(glow_surf, (x - 10, start_y - 10))
            
            card_surf = pygame.Surface((card_width, card_height), pygame.SRCALPHA)
            pygame.draw.rect(card_surf, (20, 20, 40, 250), (0, 0, card_width, card_height), border_radius=10)
            pygame.draw.rect(card_surf, upgrade.color, (0, 0, card_width, card_height), 3, border_radius=10)
            self.screen.blit(card_surf, (x, start_y))
            
            name_text = self.font_medium.render(upgrade.name, True, upgrade.color)
            name_x = x + card_width // 2 - name_text.get_width() // 2
            self.screen.blit(name_text, (name_x, start_y + 20))
            
            rarity_text = self.font_small.render(upgrade.rarity.upper(), True, upgrade.color)
            self.screen.blit(rarity_text, (x + card_width // 2 - rarity_text.get_width() // 2, start_y + 55))
            
            desc_words = upgrade.description.split()
            lines = []
            current_line = ""
            for word in desc_words:
                test_line = current_line + word + " "
                if self.font_small.size(test_line)[0] < card_width - 30:
                    current_line = test_line
                else:
                    lines.append(current_line)
                    current_line = word + " "
            lines.append(current_line)
            
            desc_y = start_y + 95
            for line in lines:
                desc_text = self.font_small.render(line, True, WHITE)
                self.screen.blit(desc_text, (x + card_width // 2 - desc_text.get_width() // 2, desc_y))
                desc_y += 25
            
            if i == self.selected_upgrade:
                indicator = self.font_small.render("▼", True, upgrade.color)
                self.screen.blit(indicator, (x + card_width // 2 - indicator.get_width() // 2, start_y + card_height + 10))
        
        instructions = self.font_small.render("Use A/D to select • Press SPACE to confirm", True, WHITE)
        self.screen.blit(instructions, (SCREEN_WIDTH // 2 - instructions.get_width() // 2, start_y + card_height + 60))
    
    def draw_game_over(self):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 220))
        self.screen.blit(overlay, (0, 0))
        
        for offset in [(3, 3), (-3, -3), (3, -3), (-3, 3)]:
            glow = self.font_large.render("GAME OVER", True, (100, 0, 0))
            self.screen.blit(glow, (SCREEN_WIDTH // 2 - glow.get_width() // 2 + offset[0], 150 + offset[1]))
        
        game_over_text = self.font_large.render("GAME OVER", True, RED)
        self.screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, 150))
        
        stats = [
            ("Final Score", self.score, GOLD),
            ("Waves Survived", self.wave, PURPLE),
            ("Total Kills", self.kills, RED),
            ("Time Survived", f"{self.time_survived}s", CYAN),
            ("Level Reached", self.player.level, GREEN)
        ]
        
        y = 260
        for label, value, color in stats:
            label_text = self.font_medium.render(f"{label}:", True, WHITE)
            value_text = self.font_medium.render(str(value), True, color)
            
            self.screen.blit(label_text, (SCREEN_WIDTH // 2 - 200, y))
            self.screen.blit(value_text, (SCREEN_WIDTH // 2 + 50, y))
            y += 50
        
        alpha = int(128 + 127 * math.sin(pygame.time.get_ticks() / 300))
        restart_text = self.font_medium.render("Press SPACE to play again", True, (*WHITE, alpha))
        self.screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT - 100))
    
    def draw(self):
        self.draw_background()
        
        self.player.draw(self.screen, self.camera, game=self)
        for enemy in self.enemies:
          enemy.draw(self.screen, self.camera, game=self)
        
        if self.game_state == 'menu':
            self.draw_menu()
        elif self.game_state in ['playing', 'paused', 'upgrade']:
            for particle in self.particles:
                particle.draw(self.screen, self.camera)
            
            for pickup in self.pickups:
                pickup.draw(self.screen, self.camera)
            
            for proj in self.projectiles:
                proj.draw(self.screen, self.camera)
            
            for enemy in self.enemies:
                enemy.draw(self.screen, self.camera)
            
            self.player.draw(self.screen, self.camera)
            
            self.draw_hud()
            
            if self.game_state == 'paused':
                self.draw_pause()
            elif self.game_state == 'upgrade':
                self.draw_upgrade_screen()
        elif self.game_state == 'game_over':
            for particle in self.particles:
                particle.draw(self.screen, self.camera)
            
            for pickup in self.pickups:
                pickup.draw(self.screen, self.camera)
            
            for proj in self.projectiles:
                proj.draw(self.screen, self.camera)
            
            for enemy in self.enemies:
                enemy.draw(self.screen, self.camera)
            
            self.player.draw(self.screen, self.camera)
            
            self.draw_game_over()
        
        pygame.display.flip()
    
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()