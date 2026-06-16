import pygame
import random
import math
import sys

# --- 1. SETTINGS & CONSTANTS ---
WIDTH, HEIGHT = 800, 600
MAP_SIZE = 2000
FPS = 60

# Colors
DARK_BLUE = (10, 20, 40)
GRASS_GREEN = (34, 139, 34)
PLAYER_COLOR = (0, 128, 255)
BOT_COLOR = (220, 50, 50)
BOSS_COLOR = (255, 215, 0)
BULLET_COLOR = (255, 255, 0)
STORM_COLOR = (150, 0, 200)
SAFE_ZONE_COLOR = (255, 255, 255)
MED_COLOR = (0, 255, 100)
RIFLE_COLOR = (255, 140, 0)
SHOTGUN_COLOR = (255, 0, 0)
MYTHIC_COLOR = (255, 215, 0)
TEXT_COLOR = (255, 255, 255)

# --- 2. INITIALIZE PYGAME & CREATE SCREEN ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Py-Nite: Chameleon Nuke Edition")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)
bold_font = pygame.font.SysFont("Arial", 32, bold=True)


# --- 3. GAME CLASSES ---
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 20
        self.speed = 5
        self.health = 100
        self.weapon = "Pistol"
        self.shoot_cooldown = 0

    def move(self, keys):
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:  self.x -= self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: self.x += self.speed
        if keys[pygame.K_w] or keys[pygame.K_UP]:    self.y -= self.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:  self.y += self.speed

        self.x = max(self.radius, min(MAP_SIZE - self.radius, self.x))
        self.y = max(self.radius, min(MAP_SIZE - self.radius, self.y))


class Bot:
    def __init__(self):
        self.x = random.randint(200, MAP_SIZE - 200)
        self.y = random.randint(200, MAP_SIZE - 200)
        self.radius = 20
        self.speed = 2.5
        self.health = 60
        self.weapon = random.choice(["Pistol", "Assault Rifle", "Shotgun"])
        self.shoot_cooldown = random.randint(20, 60)
        self.aim_angle = 0

    def update(self, player, all_bots, boss, bullet_list):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

        closest_target = player
        min_dist = math.hypot(player.x - self.x, player.y - self.y)

        if boss:
            d_boss = math.hypot(boss.x - self.x, boss.y - self.y)
            if d_boss < min_dist:
                min_dist = d_boss
                closest_target = boss

        for other_bot in all_bots:
            if other_bot is self: continue
            d = math.hypot(other_bot.x - self.x, other_bot.y - self.y)
            if d < min_dist:
                min_dist = d
                closest_target = other_bot

        if min_dist < 350:
            self.aim_angle = math.atan2(closest_target.y - self.y, closest_target.x - self.x)
            self.x += math.cos(self.aim_angle) * self.speed
            self.y += math.sin(self.aim_angle) * self.speed

            if self.shoot_cooldown <= 0:
                fire_bullet(self.x, self.y, self.aim_angle, self.weapon, bullet_list, is_enemy=True)
                self.shoot_cooldown = 45 if self.weapon == "Shotgun" else (12 if self.weapon == "Assault Rifle" else 30)
        else:
            if random.random() < 0.05:
                self.aim_angle += random.uniform(-1, 1)
            self.x += random.choice([-1, 0, 1]) * self.speed * 0.4
            self.y += random.choice([-1, 0, 1]) * self.speed * 0.4

        self.x = max(self.radius, min(MAP_SIZE - self.radius, self.x))
        self.y = max(self.radius, min(MAP_SIZE - self.radius, self.y))


class Boss:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 35
        self.speed = 1.5
        self.health = 350
        self.weapon = "Mythic Minigun"
        self.shoot_cooldown = 0
        self.aim_angle = 0

    def update(self, player, all_bots, bullet_list):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

        closest_target = player
        min_dist = math.hypot(player.x - self.x, player.y - self.y)

        for bot in all_bots:
            d = math.hypot(bot.x - self.x, bot.y - self.y)
            if d < min_dist:
                min_dist = d
                closest_target = bot

        if min_dist < 500:
            self.aim_angle = math.atan2(closest_target.y - self.y, closest_target.x - self.x)
            self.x += math.cos(self.aim_angle) * self.speed
            self.y += math.sin(self.aim_angle) * self.speed

            if self.shoot_cooldown <= 0:
                fire_bullet(self.x, self.y, self.aim_angle, self.weapon, bullet_list, is_enemy=True)
                self.shoot_cooldown = 6


class Chameleon:
    def __init__(self):
        self.x = random.randint(300, MAP_SIZE - 300)
        self.y = random.randint(300, MAP_SIZE - 300)
        self.radius = 38
        self.speed = 4.2
        self.health = 200
        self.color = (0, 255, 0)

    def update(self, player, all_bots):
        self.color = (random.randint(50, 255), random.randint(150, 255), random.randint(50, 150))

        closest_target = player
        min_dist = math.hypot(player.x - self.x, player.y - self.y)

        for bot in all_bots:
            d = math.hypot(bot.x - self.x, bot.y - self.y)
            if d < min_dist:
                min_dist = d
                closest_target = bot

        angle = math.atan2(closest_target.y - self.y, closest_target.x - self.x)
        self.x += math.cos(angle) * self.speed
        self.y += math.sin(angle) * self.speed

        if min_dist < (self.radius + closest_target.radius):
            closest_target.health = 0


class Bullet:
    def __init__(self, x, y, angle, damage, is_enemy=False):
        self.x = x
        self.y = y
        self.radius = 5
        self.speed = 15
        self.dx = math.cos(angle) * self.speed
        self.dy = math.sin(angle) * self.speed
        self.damage = damage
        self.is_enemy = is_enemy
        self.lifetime = 50

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.lifetime -= 1


class Loot:
    def __init__(self, x=None, y=None, loot_type=None):
        self.x = x if x is not None else random.randint(100, MAP_SIZE - 100)
        self.y = y if y is not None else random.randint(100, MAP_SIZE - 100)
        self.size = 24
        self.type = loot_type if loot_type is not None else random.choice(["Medkit", "Assault Rifle", "Shotgun"])


def fire_bullet(x, y, angle, weapon_type, bullet_list, is_enemy):
    if weapon_type == "Shotgun":
        fire_bullet_raw(x, y, angle - 0.15, 25, bullet_list, is_enemy)
        fire_bullet_raw(x, y, angle, 25, bullet_list, is_enemy)
        fire_bullet_raw(x, y, angle + 0.15, 25, bullet_list, is_enemy)
    elif weapon_type == "Assault Rifle":
        fire_bullet_raw(x, y, angle, 18, bullet_list, is_enemy)
    elif weapon_type == "Mythic Minigun":
        bloom = random.uniform(-0.1, 0.1)
        fire_bullet_raw(x, y, angle + bloom, 15, bullet_list, is_enemy)
    else:
        fire_bullet_raw(x, y, angle, 34, bullet_list, is_enemy)


def fire_bullet_raw(x, y, angle, damage, bullet_list, is_enemy):
    spawn_x = x + math.cos(angle) * 25
    spawn_y = y + math.sin(angle) * 25
    bullet_list.append(Bullet(spawn_x, spawn_y, angle, damage, is_enemy))


# --- 4. POPULATE GAME WORLD ---
player = Player(MAP_SIZE // 4, MAP_SIZE // 4)
bots = [Bot() for _ in range(18)]
boss = Boss(MAP_SIZE // 2, MAP_SIZE // 2)
chameleon = Chameleon()
bullets = []
loots = [Loot() for _ in range(25)]

# Storm Setup
safe_zone_x, safe_zone_y = random.randint(600, MAP_SIZE - 600), random.randint(600, MAP_SIZE - 600)
safe_zone_radius = 250
storm_x, storm_y = MAP_SIZE // 2, MAP_SIZE // 2
storm_radius = MAP_SIZE * 0.75
storm_shrink_speed = 0.35

# Nuke Variables
nuke_triggered = False
nuke_radius = 0

game_over = False
victory = False
running = True

# --- 5. MAIN GAME LOOP ---
while running:
    clock.tick(FPS)
    if player.shoot_cooldown > 0:
        player.shoot_cooldown -= 1

    mouse_x, mouse_y = pygame.mouse.get_pos()
    cam_x = player.x - WIDTH // 2
    cam_y = player.y - HEIGHT // 2
    world_mouse_x = mouse_x + cam_x
    world_mouse_y = mouse_y + cam_y
    player_aim_angle = math.atan2(world_mouse_y - player.y, world_mouse_x - player.x)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    click_state = pygame.mouse.get_pressed()
    if click_state[0] and not game_over and player.shoot_cooldown <= 0:
        fire_bullet(player.x, player.y, player_aim_angle, player.weapon, bullets, is_enemy=False)
        if player.weapon == "Assault Rifle":
            player.shoot_cooldown = 10
        elif player.weapon == "Shotgun":
            player.shoot_cooldown = 45
        elif player.weapon == "Mythic Minigun":
            player.shoot_cooldown = 5
        else:
            player.shoot_cooldown = 25

    if not game_over:
        keys = pygame.key.get_pressed()
        player.move(keys)

        # Storm movement
        dx, dy = safe_zone_x - storm_x, safe_zone_y - storm_y
        dist_to_safe = math.hypot(dx, dy)
        if dist_to_safe > 2:
            storm_x += (dx / dist_to_safe) * 0.1
            storm_y += (dy / dist_to_safe) * 0.1
        if storm_radius > safe_zone_radius:
            storm_radius -= storm_shrink_speed

        # Storm ticks
        if math.hypot(player.x - storm_x, player.y - storm_y) > storm_radius:
            player.health -= 0.3
        if boss and math.hypot(boss.x - storm_x, boss.y - storm_y) > storm_radius:
            boss.health -= 0.3
            if boss.health <= 0:
                loots.append(Loot(boss.x, boss.y, "Mythic Minigun"))
                boss = None
        for bot in bots[:]:
            if math.hypot(bot.x - storm_x, bot.y - storm_y) > storm_radius:
                bot.health -= 0.3
                if bot.health <= 0: bots.remove(bot)

        # Updates
        if boss: boss.update(player, bots, bullets)
        for bot in bots[:]: bot.update(player, bots, boss, bullets)

        # Chameleon Loop processing
        if chameleon:
            chameleon.update(player, bots)
            if player.health <= 0:
                game_over = True
                victory = False
            for bot in bots[:]:
                if bot.health <= 0: bots.remove(bot)
            if boss and boss.health <= 0: boss = None

        # Hit logic
        for bullet in bullets[:]:
            bullet.update()
            if bullet.lifetime <= 0:
                if bullet in bullets: bullets.remove(bullet)
                continue

            if not bullet.is_enemy:
                # Player shoots CHAMELEON -> Triggers NUKE
                if chameleon and math.hypot(bullet.x - chameleon.x, bullet.y - chameleon.y) < chameleon.radius:
                    chameleon.health -= bullet.damage
                    if bullet in bullets: bullets.remove(bullet)
                    if chameleon.health <= 0:
                        chameleon = None
                        nuke_triggered = True

                        # Player shoots Boss
                elif boss and math.hypot(bullet.x - boss.x, bullet.y - boss.y) < boss.radius:
                    boss.health -= bullet.damage
                    if bullet in bullets: bullets.remove(bullet)
                    if boss.health <= 0:
                        loots.append(Loot(boss.x, boss.y, "Mythic Minigun"))
                        boss = None
                # Player shoots bots
                else:
                    for bot in bots[:]:
                        if math.hypot(bullet.x - bot.x, bullet.y - bot.y) < bot.radius:
                            bot.health -= bullet.damage
                            if bullet in bullets: bullets.remove(bullet)
                            if bot.health <= 0: bots.remove(bot)
            else:
                # Enemy hits player
                if math.hypot(bullet.x - player.x, bullet.y - player.y) < player.radius:
                    player.health -= bullet.damage
                    if bullet in bullets: bullets.remove(bullet)
                # Enemy hits bot
                else:
                    for bot in bots[:]:
                        if bullet.lifetime < 48 and math.hypot(bullet.x - bot.x, bullet.y - bot.y) < bot.radius:
                            bot.health -= bullet.damage
                            if bullet in bullets: bullets.remove(bullet)
                            if bot.health <= 0: bots.remove(bot)

        # Loot Processing
        for loot in loots[:]:
            if math.hypot(player.x - loot.x, player.y - loot.y) < player.radius + loot.size:
                if loot.type == "Medkit":
                    player.health = min(100, player.health + 40)
                else:
                    player.weapon = loot.type
                loots.remove(loot)

        if player.health <= 0:
            game_over = True
            victory = False
        elif len(bots) == 0 and boss is None and chameleon is None:
            game_over = True
            victory = True

    # --- NUKE SEQUENCE ANIMATION MECHANISM ---
    if nuke_triggered:
        nuke_radius += 45
        bots.clear()
        boss = None
        if nuke_radius >= MAP_SIZE:
            game_over = True
            victory = True

    # --- 6. RENDER WORLD ---
    screen.fill(DARK_BLUE)
    pygame.draw.rect(screen, GRASS_GREEN, (0 - cam_x, 0 - cam_y, MAP_SIZE, MAP_SIZE))

    # Items
    for loot in loots:
        box_color = MED_COLOR if loot.type == "Medkit" else (RIFLE_COLOR if loot.type == "Assault Rifle" else (
            SHOTGUN_COLOR if loot.type == "Shotgun" else MYTHIC_COLOR))
        pygame.draw.rect(screen, box_color, (loot.x - cam_x, loot.y - cam_y, loot.size, loot.size))

    # Render Chameleon Monster
    if chameleon:
        ch_cx, ch_cy = int(chameleon.x - cam_x), int(chameleon.y - cam_y)
        pygame.draw.circle(screen, chameleon.color, (ch_cx, ch_cy), chameleon.radius)
        pygame.draw.circle(screen, (255, 255, 255), (ch_cx - 12, ch_cy - 10), 8)
        pygame.draw.circle(screen, (0, 0, 0), (ch_cx - 12, ch_cy - 10), 3)
        pygame.draw.circle(screen, (255, 255, 255), (ch_cx + 12, ch_cy - 10), 8)
        pygame.draw.circle(screen, (0, 0, 0), (ch_cx + 12, ch_cy - 10), 3)

    # Render Boss
    if boss:
        b_cx, b_cy = int(boss.x - cam_x), int(boss.y - cam_y)
        pygame.draw.circle(screen, BOSS_COLOR, (b_cx, b_cy), boss.radius)
        pygame.draw.line(screen, (30, 30, 30), (b_cx, b_cy),
                         (int(b_cx + math.cos(boss.aim_angle) * 50), int(b_cy + math.sin(boss.aim_angle) * 50)), 10)

    # Render Bots
    for bot in bots:
        bt_cx, bt_cy = int(bot.x - cam_x), int(bot.y - cam_y)
        pygame.draw.circle(screen, BOT_COLOR, (bt_cx, bt_cy), bot.radius)
        pygame.draw.line(screen, (50, 50, 50), (bt_cx, bt_cy),
                         (int(bt_cx + math.cos(bot.aim_angle) * 32), int(bt_cy + math.sin(bot.aim_angle) * 32)), 6)

    # Render Player
    p_cx, p_cy = int(player.x - cam_x), int(player.y - cam_y)
    pygame.draw.circle(screen, PLAYER_COLOR, (p_cx, p_cy), player.radius)
    pygame.draw.line(screen, (0, 0, 0), (p_cx, p_cy),
                     (int(p_cx + math.cos(player_aim_angle) * 32), int(p_cy + math.sin(player_aim_angle) * 32)), 6)

    # Bullets
    for bullet in bullets:
        pygame.draw.circle(screen, BULLET_COLOR, (int(bullet.x - cam_x), int(bullet.y - cam_y)), bullet.radius)

    # Zones
    pygame.draw.circle(screen, SAFE_ZONE_COLOR, (int(safe_zone_x - cam_x), int(safe_zone_y - cam_y)),
                       int(safe_zone_radius), 2)
    pygame.draw.circle(screen, STORM_COLOR, (int(storm_x - cam_x), int(storm_y - cam_y)), int(storm_radius), 6)

    # Tactical nuke shockwave animation
    if nuke_triggered:
        pygame.draw.circle(screen, (255, 100, 0), (p_cx, p_cy), int(nuke_radius), 40)
        pygame.draw.circle(screen, (255, 230, 100), (p_cx, p_cy), max(0, int(nuke_radius - 60)), 20)

    # --- 7. HUD ---
    health_ui = bold_font.render(f"HP: {max(0, int(player.health))}%", True,
                                 (0, 255, 100) if player.health > 30 else (255, 50, 50))
    weapon_ui = font.render(f"WEAPON: {player.weapon}", True,
                            MYTHIC_COLOR if player.weapon == "Mythic Minigun" else (255, 215, 0))

    total_alive = len(bots) + (1 if boss else 0) + 1
    alive_ui = font.render(f"LOBBY ALIVE: {total_alive}", True, TEXT_COLOR)
    screen.blit(health_ui, (20, 20))
    screen.blit(weapon_ui, (20, 60))
    screen.blit(alive_ui, (20, 90))

    if chameleon:
        cham_dist = math.hypot(player.x - chameleon.x, chameleon.y - chameleon.y)
        if cham_dist < 500:
            lbl_c = font.render(f"🦎 CHAMELEON HP: {int(chameleon.health)}", True, (255, 0, 200))
            screen.blit(lbl_c, (WIDTH // 2 - 110, 30))

    if game_over:
        if nuke_triggered and victory:
            msg = "💥 TACTICAL NUKE VICTORY Royale! 💥"
            msg_color = (255, 69, 0)
        else:
            msg = "#1 VICTORY ROYALE!" if victory else f"ELIMINATED! Placed #{total_alive}"
            msg_color = (255, 215, 0) if victory else (255, 50, 50)

        end_message = bold_font.render(msg, True, msg_color)
        screen.blit(end_message, (WIDTH // 2 - 220, HEIGHT // 2 - 20))

    pygame.display.flip()

pygame.quit()
sys.exit()