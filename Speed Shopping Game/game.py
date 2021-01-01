# Diksha Jothi (dj6dyz)
"""
This program creates a game that simulates a speed shopping situation, where the player must grab all the items in the
shopping list to get closer to completing the goal. The player must try to finish before time runs out, and without
grabbing the wrong items.
Features:
    user input: through arrow keys and spacebar
    graphics/images: grocery store background
    start screen: appears once program is run
    Window Size: 800 x 600
Optional Features:
    Animation: Running character when arrow keys are pressed
    Collectibles: the products on the store
    Scrolling level: the level scrolls when the player moves left and right
    Timer: shown at the top of the screen, once the timer runs out, the game is over
"""
import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)

# global variables
scroll_speed = 3
timer = 0
score = 0
time_left = 60
gravity = 5
lives = 5
standing = True
left = False
flipped = False
game_started = False
winner = False

# creating all the images in the background
ground = gamebox.from_color(0, 600, 'white', 5000, 75)
ground.bottom = camera.bottom

front_door = gamebox.from_image(0, 0, 'front_door.png')
front_door.scale_by(1.7)
front_door.x = camera.x - 380
front_door.bottom = ground.top

produce_aisle = gamebox.from_image(0, 0, 'empty_aisle.png')
produce_aisle.scale_by(.5)
produce_aisle.left = camera.right - 300
produce_aisle.bottom = ground.top

produce_aisle2 = gamebox.from_image(0, 0, 'empty_aisle.png')
produce_aisle2.scale_by(.5)
produce_aisle2.left = camera.right + 200
produce_aisle2.bottom = ground.top

dairy_aisle = gamebox.from_image(0, 0, 'empty_aisle.png')
dairy_aisle.scale_by(.5)
dairy_aisle.right = camera.left - 400
dairy_aisle.bottom = ground.top

dairy_aisle2 = gamebox.from_image(0, 0, 'empty_aisle.png')
dairy_aisle2.scale_by(.5)
dairy_aisle2.right = camera.left - 1345
dairy_aisle2.bottom = ground.top

produce_sign = gamebox.from_image(330, 200, 'produce_sign.png')
produce_sign.scale_by(.2)
dairy_sign = gamebox.from_image(-300, 200, 'dairy_sign.png')
dairy_sign.scale_by(.2)

# these are the different shopping lists that could appear, they are ranndomly picked
url_list = ['list1.png', 'list2.png', "list3.png", "list4.png", "list5.png", "list6.png"]
list_index = random.randrange(0, 6)

shopping_list = gamebox.from_image(0, 0, url_list[list_index])
shopping_list.scale_by(.3)
shopping_list.right = camera.right
shopping_list.top = camera.top

background = [ground, front_door, produce_sign, dairy_sign, produce_aisle, produce_aisle2, dairy_aisle, dairy_aisle2,
              shopping_list]

# creating all the products on the shelves
apple = gamebox.from_image(700, 285, 'apple.png')
apple.scale_by(.1)
apple2 = gamebox.from_image(800, 285, 'apple.png')
apple2.scale_by(.1)
apple3 = gamebox.from_image(900, 285, 'apple.png')
apple3.scale_by(.1)
banana = gamebox.from_image(1050, 280, 'banana.png')        # image from https://www.freepnglogos.com/search.php?q=banana
banana.scale_by(.06)
banana2 = gamebox.from_image(1200, 280, 'banana.png')       # image from https://www.freepnglogos.com/search.php?q=banana
banana2.scale_by(.06)
orange = gamebox.from_image(1300, 290, 'orange.png')        # image from https://www.freepnglogos.com/search.php?q=orange
orange.scale_by(.025)
orange2 = gamebox.from_image(1400, 290, 'orange.png')       # image from https://www.freepnglogos.com/search.php?q=orange
orange2.scale_by(.025)
strawberry = gamebox.from_image(700, 285, 'strawberry.png')     # image from https://www.freepnglogos.com/images/strawberry-14955.html
strawberry.scale_by(.06)
strawberry2 = gamebox.from_image(700, 285, 'strawberry.png')        # image from https://www.freepnglogos.com/images/strawberry-14955.html
strawberry2.scale_by(.06)
bread = gamebox.from_image(700, 285, 'bread.png')       # image from https://www.freepnglogos.com/search.php?q=bread
bread.scale_by(.08)
bread2 = gamebox.from_image(700, 285, 'bread.png')      # image from https://www.freepnglogos.com/search.php?q=bread
bread2.scale_by(.08)
cookies = gamebox.from_image(700, 285, 'cookies.png')       # image from https://www.freepnglogos.com/search.php?q=cookies
cookies.scale_by(.1)
milk = gamebox.from_image(700, 285, 'milk.png')     # image from https://www.freepnglogos.com/search.php?q=milk
milk.scale_by(.06)
water = gamebox.from_image(700, 285, 'water.png')       # image from https://www.freepnglogos.com/search.php?q=water+bottle
water.scale_by(.2)
water2 = gamebox.from_image(700, 285, 'water.png')      # image from https://www.freepnglogos.com/search.php?q=water+bottle
water2.scale_by(.2)
water3 = gamebox.from_image(700, 285, 'water.png')      # image from https://www.freepnglogos.com/search.php?q=water+bottle
water3.scale_by(.2)
toilet_paper = gamebox.from_image(700, 285, 'toilet_paper.png')     # image from https://www.freepnglogos.com/images/paper-14742.html
toilet_paper.scale_by(.1)
toilet_paper2 = gamebox.from_image(700, 285, 'toilet_paper.png')         # image from https://www.freepnglogos.com/images/paper-14742.html
toilet_paper2.scale_by(.1)
sanitizer = gamebox.from_image(700, 285, 'sanitizer.png')       # from https://www.clipartkey.com/downpng/bmmmmm_germ-clipart-hand-sanitizer-purell-hand-sanitizer/
sanitizer.scale_by(.07)
sanitizer2 = gamebox.from_image(700, 285, 'sanitizer.png')      # from https://www.clipartkey.com/downpng/bmmmmm_germ-clipart-hand-sanitizer-purell-hand-sanitizer/
sanitizer2.scale_by(.07)

products = [apple, apple2, apple3, banana, banana2, orange, orange2, strawberry, strawberry2, bread, bread2, cookies,
            milk, water, water2, water3, toilet_paper, toilet_paper2, sanitizer, sanitizer2]

# the lists of the products in each version of the shopping list
list1 = [bread, bread2, apple, apple2, apple3, water, water2, water3, toilet_paper, toilet_paper2, sanitizer, sanitizer2, orange, orange2]
list2 = [orange, orange2, milk, toilet_paper, toilet_paper2, strawberry, strawberry2, cookies, banana, banana2]
list3 = [apple, apple2, apple3, bread, bread2, sanitizer, sanitizer2, banana, banana2, orange, orange2, toilet_paper, toilet_paper2]
list4 = [sanitizer, sanitizer2, milk, water, water2, water3, banana, banana2, strawberry, strawberry2, cookies]
list5 = [water, water2, water3, toilet_paper, toilet_paper2, strawberry, strawberry2, banana, banana2, bread, bread2, sanitizer, sanitizer2]
list6 = [orange, orange2, apple, apple2, apple3, cookies, water, water2, water3, bread, bread2, milk]
all_lists = [list1, list2, list3, list4, list5, list6]
current_list = all_lists[list_index]

# all the different location to place and replace all the products
possible_locations = [700, 850, 1000, 1150, 1300, 1450, 1600, 1750, -470, -620, -770, -920, -1070, -1220, -1370, -1520, -1670, -1820, -1970, -2120]
product_x_locations = [700, 850, 1000, 1150, 1300, 1450, 1600, 1750, -470, -620, -770, -920, -1070, -1220, -1370, -1520, -1670, -1820, -1970, -2120]


def place_products():
    """This funtion randomly orders all the products on the shelf based on the list on possible product locations"""
    for product in products:
        index = random.randrange(0, len(product_x_locations))
        product.x = product_x_locations[index]
        product_x_locations.remove(product_x_locations[index])


place_products()

# creating the player
# Sprite sheet from https://www.gamedeveloperstudio.com/graphics/viewgraphic.php?item=1l4q737v077s1f8l3t
running_sheet = gamebox.load_sprite_sheet('__stick-man_blank_run_732px_by_733px-per-frame.png', 4, 4)
player = gamebox.from_image(0, 0, running_sheet[0])
player.bottom = ground.top + 15

# creating the shopping cart
cart = gamebox.from_image(0, 0, 'shopping_cart.png')        # image from https://www.freepnglogos.com/images/shopping-cart-20357.html
cart.scale_by(.08)
cart.bottom = ground.top + 15

items_in_cart = []  # starts out as empty shopping cart


def draw_standing_person():
    """This function iterates through all the images in the spritesheet and reassigns it to the player gamebox.
    It also flips the images depending on whether the person is moving left or right"""
    global player, cart
    if standing:
        standing_sheet = gamebox.load_sprite_sheet('standing_sprite_sheet.png', 4, 4)
        player.image = standing_sheet[(timer // 2) % len(standing_sheet)]
        player.speedx = 0
    if not standing:
        player.image = running_sheet[(timer // 2) % len(running_sheet)]
    if not left:
        cart.x = player.x + 140
    if left:
        cart.x = player.x - 140
    player.move_speed()
    camera.draw(player)
    camera.draw(cart)


def draw_background():
    """This function draws all the elements in the background, including the shelves and the products"""
    ground.right = camera.right
    shopping_list.right = camera.right
    shopping_list.top = camera.top
    for item in background:
        camera.draw(item)
    for item in products:
        camera.draw(item)
    for item in items_in_cart:
        item.x = cart.x
        item.y = cart.y
        camera.draw(item)


def instructions_screen():
    """This function creates the first screen that is viewed when the program starts and explains the instructions"""
    camera.clear('indianred1')
    name = gamebox.from_text(150, 50, "Name: Diksha Jothi (dj6dyz)", 25, 'black')
    title = gamebox.from_text(400, 150, "Welcome to Speed Shopping!", 50, 'black', True)
    instructions1 = gamebox.from_text(400, 250, "Your goal is to collect all the items on the shopping list displayed ", 25, 'black')
    instructions2 = gamebox.from_text(400, 300, "before the time runs out. However, the items on the shelves have been ", 25, 'black')
    instructions3 = gamebox.from_text(400, 350, "scrambled and keep moving around. Collect only the things on the list.", 25, 'black')
    instructions4 = gamebox.from_text(400, 400, "use the left and right arrow keys to move sideways and use the up arrow", 25, 'black')
    instructions5 = gamebox.from_text(400, 450, "to jump to grab an item on the shelf.", 25, 'black')
    instructions6 = gamebox.from_text(400, 500, "Press the spacebar to start!", 35, 'black')
    instructions = [instructions1, instructions2, instructions3, instructions4, instructions5, instructions6]
    for item in instructions:
        camera.draw(item)
    camera.draw(title)
    camera.draw(name)


def game_over_screen():
    """This function creates the screen the shows up when the player loses the game"""
    camera.clear('indianred1')
    title = gamebox.from_text(camera.x, 300, "GAME OVER!", 50, 'black', True)
    camera.draw(title)


def winner_screen():
    """This function creates the screen the shows up when the player wins the game"""
    camera.clear('green')
    title = gamebox.from_text(camera.x, 300, "You Win! Congrats!", 50, 'black', True)
    camera.draw(title)


def level_one(keys):
    """This function creates the game to be played and moves the character and products depending on user input"""
    global player, standing, left, flipped, timer, time_left, cart, products, game_started, product_x_locations, possible_locations, winner, score, lives
    timer += 1
    time_left -= .05
    camera.clear('seashell3')
    draw_background()
    standing = True
    if pygame.K_UP in keys and player.bottom_touches(ground):
        player.speedy = -50
    if pygame.K_RIGHT in keys and player.x < 1900:
        player.x += 15
        standing = False
        left = False
        if flipped:
            player.flip()
            cart.flip()
            flipped = False
    if pygame.K_LEFT in keys and player.x > -2200:
        player.x -= 15
        standing = False
        left = True
        if not flipped:
            player.flip()
            cart.flip()
            flipped = True
    for item in products:
        if player.touches(item, -30, -30):
            items_in_cart.append(item)
            possible_locations = [700, 850, 1000, 1150, 1300, 1450, 1600, 1750, -470, -620, -770, -920, -1070, -1220, -1370, -1520, -1670, -1820, -1970, -2120]
            possible_locations.remove(item.x)
            products.remove(item)
            product_x_locations = possible_locations
            if item in current_list:
                score += 1
            if item not in current_list:
                lives -= 1
            place_products()
    if time_left < 0 or lives < 1:
        game_started = False
    if round(score/(len(current_list)) * 100,) == 100:
        winner = True
    player.speedy += gravity
    time_passed = gamebox.from_text(0, 20, "Time Left: " + str(time_left // 1), 36, 'black')
    time_passed.x = camera.x
    score_display = gamebox.from_text(0, 20, 'Completion: ' + str(round(score/(len(current_list)) * 100,)) + "%", 36, 'black')
    score_display.x = camera.left + 100
    lives_display = gamebox.from_text(0, 50, "Lives Remaining: " + str(lives), 36, 'dark red')
    lives_display.x = camera.left + 120
    camera.draw(time_passed)
    camera.draw(score_display)
    camera.draw(lives_display)
    draw_standing_person()
    player.move_to_stop_overlapping(ground)
    camera.x = player.x


def tick(keys):
    """ This function controls which screen the player sees """
    global game_started, time_left
    if not game_started:
        instructions_screen()
    if not game_started and (time_left < 0 or lives < 1):
        game_over_screen()
    if game_started:
        level_one(keys)
    if not game_started and pygame.K_SPACE in keys:
        print("start")
        game_started = True
    if winner:
        winner_screen()
    camera.display()


gamebox.timer_loop(30, tick)
