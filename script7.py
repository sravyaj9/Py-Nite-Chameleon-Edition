import pygame
import random
import math

pygame.init()
# Load the pizza image and scale it to fit your game
pizza_img = pygame.image.load("pizza.png")
pizza_img = pygame.transform.scale(pizza_img, (60, 60)) # Adjust 60, 60 to the size you want
# Colors
DARK_BLUE = (10, 10, 30);
RED = (200, 0, 0);
PURPLE = (150, 0, 255)
GREEN = (0, 200, 0);
WHITE = (255, 255, 255);
YELLOW = (255, 215, 0)
GRAY = (100, 100, 100);
ORANGE = (255, 165, 0);
DARK_GREEN = (0, 150, 0)
CYAN = (0, 255, 255);
BROWN = (139, 69, 19)

# Game Constants
sword_stage = 1
damage_values = {1: 25, 2: 40, 3: 60, 4: 90, 5: 130, 6: 200}
range_values = {1: 80, 2: 90, 3: 100, 4: 120, 5: 140, 6: 180}
color_values = {1: CYAN, 2: (100, 255, 255), 3: YELLOW, 4: ORANGE, 5: RED, 6: PURPLE}


class Character:
    def __init__(self, x, y, hp, color, radius):
        self.x, self.y = x, y
        self.hp = hp
        self.max_hp = hp
        self.color = color
        self.radius = radius
        self.hit_timer = 0

    def draw(self, screen):
        color = WHITE if self.hit_timer > 0 else self.color
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.radius)
        pygame.draw.rect(screen, RED, (self.x - 20, self.y - 40, 40, 5))
        pygame.draw.rect(screen, GREEN, (self.x - 20, self.y - 40, max(0, 40 * (self.hp / self.max_hp)), 5))


# Entities
vampire = Character(600, 100, 800, RED, 30)
pizza = Character(100, 500, 300, YELLOW, 20)
guard = Character(300, 300, 200, DARK_GREEN, 25)

# Game Objects
phoenix = {"x": 500, "y": 400, "hp": 0, "stage": 0, "active": True}
cage = {"x": 300, "y": 300, "active": True}
swordfish = None
chests = [{"x": 150, "y": 150, "active": True}, {"x": 650, "y": 500, "active": True}]

# Projectiles & Effects
onions = []
shockwaves = []
slash_timer = 0

clock = pygame.time.Clock()
running = True

while running:
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        # Shoot Onions (Right Click)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            mx, my = pygame.mouse.get_pos()
            angle = math.atan2(my - pizza.y, mx - pizza.x)
            onions.append({"x": pizza.x, "y": pizza.y, "vx": 10 * math.cos(angle), "vy": 10 * math.sin(angle)})

    # 2. Timers
    if slash_timer > 0: slash_timer -= 1
    for char in [pizza, vampire, guard]:
        if char.hit_timer > 0: char.hit_timer -= 1

    # 3. Input & Player Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: pizza.x -= 5
    if keys[pygame.K_RIGHT]: pizza.x += 5
    if keys[pygame.K_UP]: pizza.y -= 5
    if keys[pygame.K_DOWN]: pizza.y += 5

    # 4. Sword Attack Logic (Spacebar)
    if keys[pygame.K_SPACE] and slash_timer == 0:
        slash_timer = 20
        current_dmg = damage_values[sword_stage]
        current_range = range_values[sword_stage]

        # Hit Enemies
        for target in [guard, vampire]:
            if target.hp > 0 and math.hypot(pizza.x - target.x, pizza.y - target.y) < current_range:
                target.hp -= current_dmg;
                target.hit_timer = 10

        # Hit Chests
        for chest in chests:
            if chest["active"] and math.hypot(pizza.x - chest["x"], pizza.y - chest["y"]) < current_range:
                chest["active"] = False
                if sword_stage < 6: sword_stage += 1  # Upgrade sword!

        # Break Cage (Only if guard is dead)
        if cage["active"] and guard.hp <= 0 and math.hypot(pizza.x - cage["x"], pizza.y - cage["y"]) < current_range:
            cage["active"] = False
            swordfish = {"x": cage["x"], "y": cage["y"]}  # Spawn Swordfish!

    # 5. Onion Physics & Collisions
    for o in onions[:]:
        o["x"] += o["vx"];
        o["y"] += o["vy"]
        # Hit Vampire
        if vampire.hp > 0 and math.hypot(o["x"] - vampire.x, o["y"] - vampire.y) < 30:
            vampire.hp -= 20;
            vampire.hit_timer = 5
            if o in onions: onions.remove(o)
        # Feed Phoenix
        elif phoenix["active"] and phoenix["stage"] == 0 and math.hypot(o["x"] - phoenix["x"],
                                                                        o["y"] - phoenix["y"]) < 40:
            phoenix["hp"] += 25
            if o in onions: onions.remove(o)
        # Off-screen remove
        elif o["x"] < 0 or o["x"] > WIDTH or o["y"] < 0 or o["y"] > HEIGHT:
            if o in onions: onions.remove(o)

    # 6. Phoenix Growth & Attack
    if phoenix["hp"] >= 100 and phoenix["stage"] == 0:
        phoenix["stage"] = 1  # Evolve to adult
    if phoenix["stage"] == 1 and vampire.hp > 0:
        if random.random() < 0.05: vampire.hp -= 5  # Fire breath damage

    # 7. Swordfish AI
    if swordfish and vampire.hp > 0:
        angle = math.atan2(vampire.y - swordfish["y"], vampire.x - swordfish["x"])
        swordfish["x"] += math.cos(angle) * 3;
        swordfish["y"] += math.sin(angle) * 3
        if math.hypot(vampire.x - swordfish["x"], vampire.y - swordfish["y"]) < 40:
            vampire.hp -= 2;
            vampire.hit_timer = 2

    # 8. Enemy AI (Vampire & Guard)
    if vampire.hp > 0:
        angle = math.atan2(pizza.y - vampire.y, pizza.x - vampire.x)
        vampire.x += math.cos(angle) * 1.2;
        vampire.y += math.sin(angle) * 1.2
        if math.hypot(pizza.x - vampire.x, pizza.y - vampire.y) < 40 and pizza.hit_timer == 0:
            pizza.hp -= 10;
            pizza.hit_timer = 30

        # Vampire Shockwave Generator
        if random.random() < 0.015:  # 1.5% chance per frame
            shockwaves.append({"x": vampire.x, "y": vampire.y, "radius": 10})

    if guard.hp > 0:
        angle = math.atan2(pizza.y - guard.y, pizza.x - guard.x)
        guard.x += math.cos(angle) * 1.5;
        guard.y += math.sin(angle) * 1.5
        if math.hypot(pizza.x - guard.x, pizza.y - guard.y) < 40 and pizza.hit_timer == 0:
            pizza.hp -= 15;
            pizza.hit_timer = 30

    # 9. Shockwave Physics
    for s in shockwaves[:]:
        s["radius"] += 3
        if math.hypot(pizza.x - s["x"], pizza.y - s["y"]) < s["radius"] and pizza.hit_timer == 0:
            pizza.hp -= 15;
            pizza.hit_timer = 30
        if s["radius"] > 150:
            if s in shockwaves: shockwaves.remove(s)

    # 10. Drawing Section
    screen.fill(DARK_BLUE)

    # Draw Chests
    for chest in chests:
        if chest["active"]: pygame.draw.rect(screen, BROWN, (chest["x"] - 15, chest["y"] - 15, 30, 30))

    # Draw Cage
    if cage["active"]: pygame.draw.rect(screen, GRAY, (cage["x"] - 30, cage["y"] - 30, 60, 60), 5)

    # Draw Projectiles & Effects
    for o in onions: pygame.draw.circle(screen, WHITE, (int(o["x"]), int(o["y"])), 8)
    for s in shockwaves: pygame.draw.circle(screen, PURPLE, (int(s["x"]), int(s["y"])), int(s["radius"]), 3)
    if phoenix["stage"] == 1 and vampire.hp > 0:
        pygame.draw.line(screen, ORANGE, (phoenix["x"], phoenix["y"]), (vampire.x, vampire.y), 5)

    # Draw Sword Visual
    if slash_timer > 15:
        dx = 1 if keys[pygame.K_RIGHT] else (-1 if keys[pygame.K_LEFT] else 0)
        dy = 1 if keys[pygame.K_DOWN] else (-1 if keys[pygame.K_UP] else 0)
        if dx == 0 and dy == 0: dx = 1
        pygame.draw.line(screen, color_values[sword_stage], (pizza.x, pizza.y),
                         (pizza.x + dx * range_values[sword_stage], pizza.y + dy * range_values[sword_stage]), 5)

    # Draw Characters
    if guard.hp > 0: guard.draw(screen)
    if swordfish: pygame.draw.circle(screen, CYAN, (int(swordfish["x"]), int(swordfish["y"])), 15)

    # Draw Phoenix
    color = YELLOW if phoenix["stage"] == 0 else RED
    size = 15 if phoenix["stage"] == 0 else 25
    pygame.draw.circle(screen, color, (int(phoenix["x"]), int(phoenix["y"])), size)

    vampire.draw(screen)
    pizza.draw(screen)  # Draw player last so they appear on top

    pygame.display.flip()
    clock.tick(60)

pygame.quit()