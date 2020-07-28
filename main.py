@namespace
class SpriteKind:
    Immunity = SpriteKind.create()
    Badge = SpriteKind.create()
def displayDialog(text: str):
    game.set_dialog_frame(img("""
        . . e e e e e e e e e e e e e e e e e e e e . . 
                . e 4 4 e e 4 4 e e 4 4 e e 4 4 e e 4 4 e e e . 
                e e e 4 4 e e 4 4 e e 4 4 e e 4 4 e e 4 4 e 4 e 
                e e 4 e e e e e e e e e e e e e e e e e e 4 4 e 
                e 4 4 e e b b b b b b b b b b b b b b e e 4 e e 
                e 4 e e b b b b b b b b b b b b b b b b e e e e 
                e e e e b b b b b b b b b b b b b b b b e e 4 e 
                e e 4 e b b b b b b b b b b b b b b b b e 4 4 e 
                e 4 4 e b b b b b b b b b b b b b b b b e 4 e e 
                e 4 e e b b b b b b b b b b b b b b b b e e e e 
                e e e e b b b b b b b b b b b b b b b b e e 4 e 
                e e 4 e b b b b b b b b b b b b b b b b e 4 4 e 
                e 4 4 e b b b b b b b b b b b b b b b b e 4 e e 
                e 4 e e b b b b b b b b b b b b b b b b e e e e 
                e e e e b b b b b b b b b b b b b b b b e e 4 e 
                e e 4 e b b b b b b b b b b b b b b b b e 4 4 e 
                e 4 4 e b b b b b b b b b b b b b b b b e 4 e e 
                e 4 e e b b b b b b b b b b b b b b b b e e e e 
                e e e e b b b b b b b b b b b b b b b b e e 4 e 
                e e 4 e e b b b b b b b b b b b b b b e e 4 4 e 
                e 4 4 e e e e e e e e e e e e e e e e e e 4 e e 
                e 4 e 4 4 e e 4 4 e e 4 4 e e 4 4 e e 4 4 e e e 
                . e e e 4 4 e e 4 4 e e 4 4 e e 4 4 e e 4 4 e . 
                . . e e e e e e e e e e e e e e e e e e e e . .
    """))
    game.show_long_text(text, DialogLayout.CENTER)
def subImmuneByStudyingAnimal(num: number):
    global current_immunity
    sub.set_image(immunity_sub_image_list[num])
    current_immunity = num
def displayStartScreen():
    scene.set_background_color(4)
    scene.set_background_image(BIOMIMICRY)
    game.set_dialog_frame(img("""
        . 4 4 4 4 4 4 4 4 4 4 4 4 4 . 
                4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 
                4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 
                4 4 4 e e e e e e e e e 4 4 4 
                4 4 4 e e e e e e e e e 4 4 4 
                4 4 4 e e e e e e e e e 4 4 4 
                4 4 4 e e e e e e e e e 4 4 4 
                4 4 4 e e e e e e e e e 4 4 4 
                4 4 4 e e e e e e e e e 4 4 4 
                4 4 4 e e e e e e e e e 4 4 4 
                4 4 4 e e e e e e e e e 4 4 4 
                4 4 4 e e e e e e e e e 4 4 4 
                4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 
                4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 
                . 4 4 4 4 4 4 4 4 4 4 4 4 4 .
    """))
    game.show_long_text("Venture into the sea, study the animals. Press \"A\" to start.",
        DialogLayout.BOTTOM)
def sharkEncountered(mySprite: Sprite):
    if current_immunity > -1:
        music.magic_wand.play()
        displayDialog("" + immunity_text_list[current_immunity] + " You caught this shark!")
        num_caught_list[current_immunity] = 0
        num_caught_list[9] = num_caught_list[9] + 1
        info.change_score_by(50)
        loseImmunity()
        if num_caught_list[9] == 9:
            music.stop_all_sounds()
            game.over(True, effects.bubbles)
        mySprite.destroy()
    else:
        sub.say("Ack, teeth!", 2000)
        game.over(False)

def on_on_overlap(sprite, otherSprite):
    if sprites.read_data_string(otherSprite, "species") == "Shark":
        sharkEncountered(otherSprite)
    else:
        nonSharkEncountered(otherSprite)
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap)

def loseImmunity():
    global new_badge, current_immunity, level
    sub.set_image(img("""
        . . . . . . . . . . . f f f f f f . . . . . . . . . . . . . . . 
                . . . . . . . . . . f d e d e e e f . . . . . . . . . . . . . . 
                . . . . . . . . . . f d d e e e e f . . . . . . . . . . . . . . 
                . . . . . . . . . . f d e d e e e f . . . . . . . . . . . . . . 
                . . . . . . . . . . f d d e e e e f . . . . . . . . . . . . . . 
                . . f f f f f f f f d d e d e e e e f f f f f f f f f f f f . . 
                . f f c f d e d e e e e e e e e e e e e e e e e d e d f c f f . 
                f f c b f e d e e d d e e e e e e e e e e d d e e d e f b c f f 
                f c b b f d e e d c b d e e e e e e e e d c b d e e d f b b c f 
                f b b b f e e d c b b b d e e e e e e d c b b b d e e f b b b f 
                f f f f f e e d b b b b d e e e e e e d b b b b d e e f f f f f 
                f b b b f e e e d b b d e e e e e e e e d b b d e e e f b b b f 
                f b b b f e d e d d d e d e d e d e d e d d d e d e d f b b b f 
                f f b b f d e d e d e d e d e d e d e d e d e d e d e f b b f f 
                . f f b f d d d d d d d d d d d d d d d d d d d d d d f b f f . 
                . . f f f f f f f f f f f f f f f f f f f f f f f f f f f f . .
    """))
    if immunity_badge_awarded[current_immunity] == 0:
        new_badge = sprites.create(immunity_badge_list[current_immunity], SpriteKind.Badge)
        new_badge.set_position(12 * current_immunity + 4, 4)
        info.change_score_by(300)
    current_immunity = -1
    level += 0.1
    music.change_tempo_by(20)
def nonSharkEncountered(mySprite: Sprite):
    global animal_caught_species_id_number, num_animals_caught
    music.ba_ding.play()
    sub.start_effect(effects.trail, 500)
    animal_caught_species_id_number = sprites.read_data_number(mySprite, "animal_index")
    num_animals_caught = num_caught_list[animal_caught_species_id_number]
    if num_animals_caught < animals_needed_to_learn_immunity - 1:
        num_caught_list[animal_caught_species_id_number] = num_animals_caught + 1
        sub.say("" + sprites.read_data_string(mySprite, "species") + " #" + str((num_animals_caught + 1)),
            500)
    elif num_animals_caught == animals_needed_to_learn_immunity - 1:
        sub.say("" + sprites.read_data_string(mySprite, "species") + " #" + str((num_animals_caught + 1)),
            500)
        num_caught_list[animal_caught_species_id_number] = animals_needed_to_learn_immunity
        subImmuneByStudyingAnimal(animal_caught_species_id_number)
    else:
        sub.say("" + sprites.read_data_string(mySprite, "species"), 500)
    mySprite.destroy()
    # Faster animals are worth more points.
    info.change_score_by(animal_caught_species_id_number)
def fillAnimalArrays():
    global immunity_text_list, immunity_badge_list, immunity_sub_image_list, animal_image_list, animal_names, animal_speed_list, num_caught_list, immunity_badge_awarded
    immunity_text_list = ["Studying the turtle, you learned to harden your shell.",
        "Studying the crab, you learned to use pinchers.",
        "Studying the green fish, you learned to blend into the grass.",
        "Studying the octopus, you learn to change colors, and deploy ink.",
        "Studying the pink fish, you learn to blend into the coral.",
        "Studying the narwhal, you learn to use a horn defensively.",
        "Studying the ray, you learn to use a stinger, and blend into the bottom.",
        "Studying the whale, you learn to use your size to your advantage.",
        "Studying the pufferfish, you learn how spines deter predators from eating you."]
    immunity_badge_list = [img("""
            . . . 9 9 . . . 
                    . . 9 7 8 9 . . 
                    . 9 7 8 7 8 9 . 
                    . 9 8 7 8 7 9 . 
                    . 9 7 8 7 8 9 . 
                    . 9 8 7 8 7 9 . 
                    . . 9 8 7 9 . . 
                    . . . 9 9 . . .
        """),
        img("""
            . . 4 4 . 4 . . 
                    . 4 4 . . . 4 . 
                    . 4 . . . 4 4 . 
                    . 4 4 . . . 4 . 
                    . 4 . . . 4 4 . 
                    . 4 4 . . . 4 . 
                    . 4 4 4 4 4 4 . 
                    . . 4 4 4 4 . .
        """),
        img("""
            . . 9 . . 9 . . 
                    . . 9 . . 9 . . 
                    . 9 . . . . 9 . 
                    . 9 . 9 . . 9 . 
                    . 9 . . 9 . 9 . 
                    . . 9 . 9 . 9 9 
                    . . 9 . 9 . . 9 
                    . . 9 . 9 . . 9
        """),
        img("""
            . . . f f f . . 
                    . . f f f f f f 
                    . . f f f f f f 
                    . f f f f f f f 
                    f f f f f f f . 
                    f f f f f f f . 
                    . f f f f f . . 
                    . . . . f f . .
        """),
        img("""
            . . . . . . . . 
                    . 3 3 . 3 3 . 2 
                    3 3 2 2 2 3 2 . 
                    3 6 b 3 2 3 2 3 
                    3 6 3 2 2 3 6 3 
                    3 6 3 3 6 3 3 6 
                    . 3 2 3 2 6 3 6 
                    . 3 6 . 2 2 3 .
        """),
        img("""
            . . . . 6 . . . 
                    . . . 6 6 . . . 
                    . . . 6 5 . . . 
                    . . . 5 6 . . . 
                    . . . 6 6 . . . 
                    . . . 6 5 . . . 
                    . . . 5 6 . . . 
                    . . . 6 6 . . .
        """),
        img("""
            . . . . . . . b 
                    . . . . . . b . 
                    . . . . . b . . 
                    . . . . b . . . 
                    . . . b . . . . 
                    . . b . . . . . 
                    . b . . . . . . 
                    b . . . . . . .
        """),
        img("""
            2 2 2 2 2 2 2 2 
                    2 2 6 2 6 2 6 2 
                    2 6 b b b b 2 2 
                    2 2 b a a b 2 2 
                    2 2 b a a b 2 2 
                    2 2 b b b b 2 2 
                    2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2
        """),
        img("""
            e . . e . . . e 
                    . e . e . . e . 
                    . . e e e e . . 
                    e e e d d e e e 
                    . . e d d e . . 
                    . . e e e e . . 
                    . e . . e . e . 
                    e . . . e . . e
        """)]
    immunity_sub_image_list = [img("""
            . . . . . . . . . . . 9 9 9 9 9 9 . . . . . . . . . . . . . . . 
                    . . . . . . . . . . 9 7 8 7 8 9 8 9 . . . . . . . . . . . . . . 
                    . . . . . . . . . . 9 7 7 8 9 8 9 9 . . . . . . . . . . . . . . 
                    . . . . . . . . . . 9 7 8 9 8 7 8 9 . . . . . . . . . . . . . . 
                    . . . . . . . . . . 9 7 9 8 7 8 8 9 . . . . . . . . . . . . . . 
                    . . 9 9 9 9 9 9 9 9 7 9 8 7 8 8 8 8 9 9 9 9 9 9 9 9 9 9 9 9 . . 
                    . 9 9 c 9 7 8 7 9 8 9 8 7 8 8 8 8 8 8 8 9 8 9 8 7 8 7 9 c 9 9 . 
                    9 9 c b 9 8 7 9 8 7 7 9 8 8 8 8 8 8 8 9 8 7 7 9 8 7 8 9 b c 9 9 
                    9 c b b 9 7 9 8 7 c b 7 9 8 8 8 8 8 9 8 7 c b 7 9 8 7 9 b b c 9 
                    9 b b b 9 9 8 7 c b b b 7 9 8 8 8 9 8 7 c b b b 7 9 8 9 b b b 9 
                    9 9 9 9 9 9 8 7 b b b b 7 8 9 8 9 8 8 7 b b b b 7 8 9 9 9 9 9 9 
                    9 b b b 9 8 9 8 7 b b 7 8 8 8 9 8 8 8 8 7 b b 7 8 9 8 9 b b b 9 
                    9 b b b 9 7 8 9 7 7 7 8 7 8 9 8 9 8 7 8 7 7 7 8 9 8 7 9 b b b 9 
                    9 9 b b 9 8 8 8 9 7 8 7 8 9 8 8 8 9 8 7 8 7 8 9 8 8 8 9 b b 9 9 
                    . 9 9 b 9 7 8 7 8 9 7 7 9 7 8 7 8 7 9 7 7 7 9 8 7 8 7 9 b 9 9 . 
                    . . 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 . .
        """),
        img("""
            . . . . . . . . . . . f f f f f f . . . . . . . . . . . . . . . 
                    . . . . . . . . . . f d e d e e e f . . . . . . . . . . . . . . 
                    . . . . . . . . . . f d d e e e e f . . . . . . . . . . . . . . 
                    . . . . . . . . . . f d e d e e e f . . . . . . . . . . . . . . 
                    . . . . . . . . . . f d d e e e e f . . . . . . . . . . . . . . 
                    . . f f f f f f f f d d e d e e e e f f f f f f f f f f f f . . 
                    . f f 4 4 4 4 d e e e e e e e e e e e e e e e e d 4 4 4 4 f f . 
                    f f 4 4 4 4 4 4 e d d e e e e e e e e e e d d e 4 4 4 4 4 4 f f 
                    f 4 4 f f 4 4 4 d c b d e e e e e e e e d c b d 4 4 4 f f 4 4 f 
                    f 4 f . . f 4 4 c b b b d e e e e e e d c b b b 4 4 f . . f 4 f 
                    . . . . . f 4 4 b b b b d e e e e e e d b b b b 4 4 f . . . . . 
                    f 4 f . . f 4 4 d b b d e e e e e e e e d b b d 4 4 f . . f 4 f 
                    f 4 4 f f 4 4 4 d d d e d e d e d e d e d d d e 4 4 4 f f 4 4 f 
                    f f 4 4 4 4 4 4 e d e d e d e d e d e d e d e d 4 4 4 4 4 4 f f 
                    . f f 4 4 4 4 d d d d d d d d d d d d d d d d d d 4 4 4 4 f f . 
                    . . f f f f f f f f f f f f f f f f f f f f f f f f f f f f . .
        """),
        img("""
            . . . . . . . . . . . 7 8 7 8 7 8 . . . . . . . . . . . . . . . 
                    . . . . . . . . . . 7 7 7 7 7 7 7 7 . . . . . . . . . . . . . . 
                    . . . . . . . . . . 7 8 8 8 8 8 8 7 . . . . . . . . . . . . . . 
                    . . . . . . . . . . 7 7 7 7 7 7 7 7 . . . . . . . . . . . . . . 
                    . . . . . . . . . . 7 8 8 8 8 8 8 7 . . . . . . . . . . . . . . 
                    . . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 . . 
                    . 7 7 c 7 7 8 7 7 7 7 7 7 8 7 8 7 7 8 7 7 7 7 7 7 8 8 7 c 7 7 . 
                    7 7 c b 7 8 8 7 7 8 8 7 7 8 7 7 8 7 8 7 7 8 8 7 7 8 7 7 b c 7 7 
                    7 c b b 7 7 8 7 8 c b 8 7 8 7 8 7 7 8 7 8 c b 8 7 8 8 7 b b c 7 
                    7 b b b 7 8 8 7 c b b b 7 8 7 7 8 7 8 7 c b b b 7 8 7 7 b b b 7 
                    7 7 7 7 7 7 8 7 b b b b 7 8 7 8 7 7 8 7 b b b b 7 8 8 7 7 7 7 7 
                    7 b b b 7 8 8 7 8 b b 8 7 8 7 7 8 7 8 7 8 b b 8 7 8 7 7 b b b 7 
                    7 b b b 7 7 8 7 7 8 8 7 7 8 7 8 7 7 8 7 7 8 8 7 7 8 8 7 b b b 7 
                    7 7 b b 7 8 8 7 7 7 7 7 7 8 7 7 8 7 8 7 7 7 7 7 7 8 7 7 b b 7 7 
                    . 7 7 b 7 7 7 8 7 8 7 8 7 8 7 8 7 8 7 7 8 7 8 7 8 7 8 7 b 7 7 . 
                    . . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 . .
        """),
        img("""
            . . . f f f f f f f f f f f f f f f f f f f . . . . . . f f f . 
                    . . f f d e d e e e e e d d d e e d e e e f f f f f f f f e e f 
                    . f f e d d e e e e e d e d e e e e e d e d e e e d e e e d e f 
                    f f e d c b d e e d e e e e d f f f f f f f e d e e e d e f f . 
                    f e d c b b b d e e e e e e e f . . . . . f f f f f f f f f . . 
                    f e d b b b b d e e d d e e e f . . . . . . . . . . . . . . . . 
                    f d e d b b d e e e e e e d e f . . f f f f f f f f f f f f f . 
                    f e e d d d e d e e d d e d e f f f f e d e e e d e e e d e e f 
                    f e e e d d e e e e d d e e e e e e d e e e d e e e d e e e d f 
                    f e e d c b d e e e e e e d e e d e f f f f f f f f f f f f f . 
                    f e d c b b b d e e d d e e e f f f f . . . . . . . . . . . . . 
                    f e d b b b b d e e e e e e e f . . . . f f f f f f f f . . . . 
                    f f e d b b d e e e e e e e d f f f f f f e d e e e d f f f f . 
                    . f f d d d e d d d e d e d e e d e e e d e e e d e e e e d e f 
                    . . f f d d d d d d d d d d d e e e d e e f f f f f f d e e e f 
                    . . . f f f f f f f f f f f f f f f f f f f . . . . f f f f f .
        """),
        img("""
            . . . . . . . . . . . 5 5 5 5 5 5 . . . . . . . . . . . . . . . 
                    . . . . . . . . . . 5 6 3 6 3 3 3 5 . . . . . . . . . . . . . . 
                    . . . . . . . . . . 5 6 6 3 3 3 3 5 . . . . . . . . . . . . . . 
                    . . . . . . . . . . 5 6 3 6 3 3 3 5 . . . . . . . . . . . . . . 
                    . . . . . . . . . . 5 6 6 3 3 3 3 5 . . . . . . . . . . . . . . 
                    . . 5 5 5 5 5 5 5 5 6 6 3 6 3 3 3 3 5 5 5 5 5 5 5 5 5 5 5 5 . . 
                    . 5 5 c 5 6 3 6 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 6 3 6 5 c 5 5 . 
                    5 5 c b 5 3 6 3 3 6 6 3 3 3 3 3 3 3 3 3 3 6 6 3 3 6 3 5 b c 5 5 
                    5 c b b 5 6 3 3 6 c b 6 3 3 3 3 3 3 3 3 6 c b 6 3 3 6 5 b b c 5 
                    5 b b b 5 3 3 6 c b b b 6 3 3 3 3 3 3 6 c b b b 6 3 3 5 b b b 5 
                    5 5 5 5 5 3 3 6 b b b b 6 3 3 3 3 3 3 6 b b b b 6 3 3 5 5 5 5 5 
                    5 b b b 5 3 3 3 6 b b 6 3 3 3 3 3 3 3 3 6 b b 6 3 3 3 5 b b b 5 
                    5 b b b 5 3 6 3 6 6 6 3 6 3 6 3 6 3 6 3 6 6 6 3 6 3 6 5 b b b 5 
                    5 5 b b 5 6 3 6 3 6 3 6 3 6 3 6 3 6 3 6 3 6 3 6 3 6 3 5 b b 5 5 
                    . 5 5 b 5 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 5 b 5 5 . 
                    . . 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 . .
        """),
        img("""
            . . . . . . . . . . . . . f f f f f f . . . . . . . . . . . . . 
                    . . . . . . . . . . . . f d e d e e e f . . . . . . . . . . . . 
                    . . . . . . . . . . . . f d d e e e e f . . . . . . . . . . . . 
                    . . . . . . . . . . . . f d e d e e e f . . . . . . . . . . . . 
                    . . . . . . . . . . . . f d d e e e e f . . . . . . . . . . . . 
                    . . . . . . f f f f f f e d e d e e e d f f f f f f . . . . . . 
                    . . . . . f f c f d e d e e e e e e e e e d d f c f f . . . . . 
                    . . . . f f c b f e e e d d e e e e d d e e e f b c f f . . . . 
                    . . . . f c b b f d e d c b d e e d c b d e d f b b c f . . . . 
                    . . . . f b b b f e d c b b b d d c b b b d e f b b b f . . . . 
                    f f f f f f f f f e d b b b b d d b b b b d e f f f f f f f f f 
                    . . . . f b b b f e e d b b d e e d b b d e e f b b b f . . . . 
                    . . . . f b b b f e e d d d e d e d d d e d d f b b b f . . . . 
                    . . . . f f b b f d e d e d e d e d e d e d e f b b f f . . . . 
                    . . . . . f f b f d d d d d d d d d d d d d d f b f f . . . . . 
                    . . . . . . f f f f f f f f f f f f f f f f f f f f . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . . . . f f f f f f . . . . . . . 
                    . . . . . . . . . . . . . . . . . . f c b b b b c f . . . . . . 
                    . . . . . . . . . . . . . . . . . f c b c b b b b c f . . . . . 
                    f f f . . . . . . . . . . . . . f f f f f f f f f f f f . . . . 
                    . . . f f f f . . . . . . . . f e d e e e e e e e e e d f . . . 
                    . . . . . . . f f f f . . . f e d e d e d e d e d e d e d f . . 
                    . . . . . . . . . . . f f f d d d d d d d d d d d d d d d d f . 
                    . . . . . . . . . . . . . f f f f f f f f f f f f f f f f f f f
        """),
        img("""
            . . f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f . . . 
                    . f f c f d e d e e e e e e d d d e e e e e e d d d d e e e e e e d e d f c f f . . 
                    f f c c f e d e e e e e e e e d d d e e e e d d d d e e e e e e e e d e f c c f f . 
                    f c c b f e e e e e e e e e e e d d d d d d d d d e e e e e e e e e e e f b c c f . 
                    f c b b f e e e e d d d d e e e e d d d d d d d e e e e d d d d e e e e f b b c f . 
                    f b b b f d e e d c b c b d e e e e e e e e e e e e e d c b c b d e e d f b b b f . 
                    f b b b f e e d c b c b b b d e e e e d d d e e e e d c b c b b b d e e f b b b f . 
                    f b b b f e e d c b b b b b d e e e e e e e e e e e d c b b b b b d e e f b b b f . 
                    f b b b f e e d b b b b b b d e d d d d d d d d d e d b b b b b b d e e f b b b f . 
                    f b b b f e e d b b b b b b d e e e e e e e e e e e d b b b b b b d e e f b b b f . 
                    f b b b f e e d b b b b b b d e e e e d d d e e e e d b b b b b b d e e f b b b f . 
                    f b b b f e e e d b b b b d e e e e e e e e e e e e e d b b b b d e e e f b b b f . 
                    f b b b f e d e d d d e d e d e e d e d e d e d e d e d e d d d e d e d f b b b f . 
                    f f b b f d e d e d e d e d e d d . d . d . d . d e d e d e d e d e d e f b b f f . 
                    . f f b f d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d f b f f . . 
                    . . f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f f . . .
        """),
        img("""
            f . f . . f . . . . . . . . . . . . . . . . f . . . f . . f . . 
                    f . . f . . f . . . . f f f f f f . . . . f . . . f . . f . . . 
                    . f . . f . . f . . f d e d e e e f . . f . . . f . . f . . . f 
                    . f . . f . . f . . f d d e e e e f . . f . . . f . . f . . f . 
                    . . f . . f . f . . f d e d e e e f . . f . . f . . f . . f . . 
                    . . f . . f . . f . f d d e e e e f . . f . . f . . f . f . . . 
                    f . f f f f f f f f d d e e e e e e f f f f f f f f f f f f . . 
                    . f f c f d e d e e e e e e e e e e e e e e e e d e d f c f f . 
                    f f c b f e d e e d d e e e e e e e e e e d d e e d e f b c f f 
                    f c b b f d e e d c b d e e e e e e e e d c b d e e d f b b c f 
                    f b b b f e e d c b b b d e e e e e e d c b b b d e e f b b b f 
                    f f f f f e e d b b b b d e e e e e e d b b b b d e e f f f f f 
                    f b b b f e e e d b b d e e e e e e e e d b b d e e e f b b b f 
                    f b b b f e d e d d d e e e d e d e e e d d d e d e d f b b b f 
                    f f b b f d e d e d e d e d e d e d e d e d e d e d e f b b f f 
                    . f f b f d d d d d d d d d d d d d d d d d d d d d d f b f f . 
                    . . f f f f f f f f f f f f f f f f f f f f f f f f f f f f . . 
                    . . . . f . . . f . . . f . . f . . . f . . . f . . . f . . . . 
                    . . . f . . . f . . . f f . . f . . . f . . . . f . . . f . . . 
                    . . f . . . f . . . . f . . . f . . . . f . . . . f . . . f . . 
                    . f . . . f . . . . f . . . . f . . . . . f . . . . f . . . f . 
                    f . . . f . . . . f . . . . . f . . . . . f . . . . . f . . . f 
                    . . . f . . . . . f . . . . . f . . . . . . f . . . . . f . . . 
                    . . f . . . . . f . . . . . . f . . . . . . . f . . . . . f . .
        """)]
    animal_image_list = [img("""
            . . . . . 7 7 7 . . . . . . . . 
                    . . . . 7 7 7 . . . . . . . . . 
                    . . . . 7 7 . . . . . 7 7 7 7 . 
                    . . . . 7 8 . . . . . 7 7 7 7 7 
                    . . . . 7 8 8 9 9 8 8 7 7 8 . . 
                    . . . . 8 9 9 8 8 7 7 9 8 . . . 
                    . f 7 7 8 9 9 8 8 7 7 9 9 . . . 
                    7 7 7 7 7 8 7 7 9 9 8 8 7 7 . . 
                    7 7 7 7 7 8 7 7 9 9 8 8 7 7 . . 
                    . f 7 7 8 9 9 8 8 7 7 9 9 . . . 
                    . . . . 8 9 9 8 8 7 7 9 8 . . . 
                    . . . . 7 8 8 9 9 8 8 7 7 8 . . 
                    . . . . 7 8 . . . . . 7 7 7 7 7 
                    . . . . 7 7 . . . . . . 7 7 7 . 
                    . . . . 7 7 7 . . . . . . . . . 
                    . . . . . . 7 7 . . . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                    . . . 4 4 . . . . . . . . . . . 
                    . . 4 4 . . . . . . . 4 4 . . . 
                    . . 4 4 . . 4 . . . . . 4 4 . . 
                    . . 4 4 4 4 4 . . 4 . . 4 4 . . 
                    . 4 4 4 4 4 . . . 4 4 4 4 4 . . 
                    . 4 4 . . . . . . . 4 4 4 4 4 . 
                    . 4 . . . . . . . . . . . . 4 . 
                    . 4 4 4 4 4 4 4 4 4 4 4 4 4 4 . 
                    . . 4 4 4 4 f 4 f 4 4 4 4 4 . . 
                    . . . 4 4 4 4 4 4 4 4 4 4 . . . 
                    . . 4 4 4 4 4 4 4 4 4 4 4 4 . . 
                    . 4 4 . 4 . . . . . . 4 . 4 4 . 
                    . 4 . . 4 . . . . . . 4 . . 4 . 
                    . . 4 . . 4 . . . . 4 . . 4 . . 
                    . . . . . . . . . . . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . 8 . . . . 
                    . . . . . . . . . 9 8 8 . . . . 
                    . . . . . . . 8 8 9 8 8 . . . 9 
                    . . . . . 8 9 8 8 9 8 8 . . 9 9 
                    . . . 8 8 8 9 8 8 9 8 8 . 9 9 9 
                    . 8 8 f 8 f 9 8 8 9 8 8 9 9 9 9 
                    9 8 8 8 8 8 9 8 8 9 8 8 9 9 9 9 
                    . 8 8 8 8 8 9 8 8 9 8 8 9 9 9 9 
                    . . . 8 8 8 9 8 8 9 8 8 . 9 9 9 
                    . . . . . 8 9 8 8 9 8 8 . . 9 9 
                    . . . . . . . 8 8 9 8 8 . . . 9 
                    . . . . . . . . . 9 8 8 . . . . 
                    . . . . . . . . . . . 8 . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        img("""
            . . . . . . 5 5 5 5 . . . . . . 
                    . . . . . 5 4 4 4 4 5 . . . . . 
                    . 4 . . 5 4 4 4 4 4 4 5 . . . . 
                    . 4 . 5 4 4 f 4 f 4 4 4 5 . . 4 
                    4 . . 5 4 4 4 4 4 4 4 4 5 . 4 . 
                    4 . 4 5 4 4 4 4 4 4 4 4 5 . . 4 
                    . 4 . 5 4 4 4 4 4 4 4 4 5 4 . 4 
                    . . . 4 5 4 4 4 4 4 4 5 . 4 4 . 
                    . . 4 4 . 5 4 4 4 4 5 4 4 . . . 
                    . . 4 . . 4 5 5 5 5 4 . . 4 . . 
                    . 4 . . 4 . . 4 . 4 . 4 . . 4 . 
                    4 . . 4 . . 4 . . 4 . 4 . . 4 . 
                    4 . 4 4 . 4 4 . 4 . . . 4 . . 4 
                    4 . 4 . . 4 . . 4 . . . 4 . . 4 
                    . . . 4 . . 4 . . 4 . . . 4 . . 
                    . . . . . . . . . . . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . 2 2 2 2 . . . . . 
                    . . . . . . 2 2 2 2 . . . . . . 
                    . . . . . 1 1 2 2 . . . . . . . 
                    . . . . 1 1 1 1 1 . . . . . . . 
                    . . . 1 1 1 1 2 1 1 1 . . . 2 2 
                    . . 1 1 1 1 2 1 1 1 2 1 . 2 2 2 
                    . . 1 f 1 f 1 2 1 2 1 1 2 2 2 . 
                    . 1 1 1 1 1 2 1 1 1 2 1 2 2 2 . 
                    1 1 1 1 1 1 1 2 1 2 1 1 2 2 2 . 
                    . 1 1 1 1 1 2 1 1 1 2 1 . 2 2 2 
                    . . 1 1 1 1 1 2 1 1 1 . . . 2 2 
                    . . . 1 1 1 1 1 1 2 . . . . . . 
                    . . . . 1 1 1 2 2 2 2 . . . . . 
                    . . . . . . . . . 2 2 2 . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        img("""
            . . . . . . 6 . . . . . . . . . 
                    . . . . . . 6 . . . . . . . . . 
                    . . . . . . 6 . . . . . . . . . 
                    . . . . . . 5 5 . . . . . . . . 
                    . . . . . 5 5 5 5 . . . . . . . 
                    . . . . 5 f 5 f 5 5 . . 5 . . . 
                    . . . . 5 5 5 5 5 5 5 5 5 . . . 
                    . . . 5 5 5 5 5 5 5 5 5 5 . . . 
                    . . 5 5 5 5 6 6 5 5 . . . . . . 
                    . . 5 5 5 6 6 6 6 5 . . . . . . 
                    . . 5 . 5 6 6 6 6 5 . 5 . . . . 
                    . . . . 5 6 6 6 6 5 . 5 5 . . . 
                    . . . . 5 6 6 6 6 5 . 5 5 5 . . 
                    . . . . . 5 6 6 5 5 . 5 5 5 5 . 
                    . . . . . 5 5 5 5 5 5 5 . . . . 
                    . . . . . . . 5 5 5 5 . . . . .
        """),
        img("""
            b b b b b b b b b . . . . . . . 
                    b b b f b c b b b . . . . . . . 
                    b b b b b b c b b . . . . . . . 
                    b f b b b b b c b . . . . . . . 
                    b b b b b b b c b . . . . . . . 
                    b c b b b b b b b b . . . . . . 
                    b b c b b b b b b b b . . . . . 
                    b b b c c b b b b . . . . . . . 
                    b b b b b b b b b b . . . . . . 
                    . . . . . b b . . b . . . . . . 
                    . . . . . . b . . b b . . . . . 
                    . . . . . . . . . . b b . . . . 
                    . . . . . . . . . . . b b b b . 
                    . . . . . . . . . . . . . . b b 
                    . . . . . . . . . . . . . . . b 
                    . . . . . . . . . . . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . 2 . 
                    . . . . . . . . . . . . 2 2 2 . 
                    . . . . . . . . . . . 2 2 2 . . 
                    . . . . . . . . . . . 2 2 2 2 . 
                    . . . . . . . . . . 2 2 . 2 2 2 
                    . . . . . . . . . . . . . 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 f 2 f 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 3 
                    2 2 3 3 3 3 3 3 3 3 3 2 2 3 3 . 
                    3 3 3 3 3 3 3 3 3 3 3 3 3 3 . . 
                    . . . 2 2 . 2 . . . . . . . . . 
                    . . . 2 . . 2 . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . e . e . e . . e . . . . . . . 
                    . e d d e d d e d . e . . . . . 
                    . d d d d d d d d e d . e . . . 
                    d d d d d d d d d d d e . . . d 
                    d d d d d d d d d d d d . d d d 
                    d f d f d d d d d d d d d d d . 
                    d d d d d d d d d d d d d d d d 
                    d d d d d d d d d d d d d d d . 
                    d d d e e e e e e d d d . d d d 
                    . d e e e e e e e e d . . . . d 
                    . . e e e e e e e e . . . . . . 
                    . . . d e e e d e d . . . . . . 
                    . . d . . d . d . . d . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . d d d d . . . . . . 
                    . . . . . d d d d . . . . . . . 
                    d d d d d d d d d d d d d . . . 
                    d d f d f d d d d d d d d d d . 
                    . e e e e e e e d d d d d d d d 
                    . . e c c c e e e e e e e e d d 
                    . . . e e e e e e e e e e e e d 
                    . . . . . d d . d d . . . . e d 
                    . . . . . d . . . d . . . . d d 
                    . . . . . . . . . . . d d d d d 
                    . . . . . . . . . . d d d d d . 
                    . . . . . . . . . . . . . d d . 
                    . . . . . . . . . . . . . d d . 
                    . . . . . . . . . . . . . d . . 
                    . . . . . . . . . . . . . . . .
        """)]
    animal_names = ["Turtle",
        "Crab",
        "Green Fish",
        "Octopus",
        "Pink fish",
        "Narwhal",
        "Ray",
        "Whale",
        "Pufferfish",
        "Shark"]
    animal_speed_list = [-15, -25, -35, -45, -55, -65, -75, -85, -95, -110]
    num_caught_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    immunity_badge_awarded = [0, 0, 0, 0, 0, 0, 0, 0, 0]
animal_sprite: Sprite = None
animal_speed = 0
animal_choice = 0
shark: Sprite = None
animal_speed_list: List[number] = []
animal_names: List[str] = []
animal_image_list: List[Image] = []
num_animals_caught = 0
animal_caught_species_id_number = 0
immunity_badge_list: List[Image] = []
new_badge: Sprite = None
immunity_badge_awarded: List[number] = []
num_caught_list: List[number] = []
immunity_text_list: List[str] = []
immunity_sub_image_list: List[Image] = []
current_immunity = 0
animals_needed_to_learn_immunity = 0
sub: Sprite = None
ScienceSubTitle = None
displayStartScreen()
scene.set_background_image(img("""
    a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 
        a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d d d d a a 
        d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d d d d d d d 
        d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d d d d d d d d 
        d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d d d d d d d d 
        d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d d d d d d d d 
        d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d d d d d d d d d d d d d d d d d 
        d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d 
        d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d 
        d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d 
        d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d 
        d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d d d d d d a a 7 7 7 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d 
        d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d d d d d d d a 7 7 7 7 7 7 7 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d 
        d d d d d d d a a a a a a a a a a a 7 a a a a a a a a a a a a d d d d d d d d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 a a a a a a a a a a a a a a a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d 
        d d d d d d d a a a a a 7 7 7 7 7 7 7 7 a a a a a a a a a a a d d d d d d d d d d d d d d a a a a a a a a a a a a a a a a a a a a a a a a d d a a a a a a a a a d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a d d d a a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d 
        d d d d d d d a a 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a a a d d d d d d d d d d d d d d d a a a a a a a a a a a a a a a a a a a a a a d d d d d d d a a a a d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a d d d a a a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d 
        d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a a d d d d d d d d d d d d d d d d a a a a a a a a a a a a a a a a a a a a a d d d d d d d d d d a a d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a d d d d a a a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d 
        d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a a d d d d d d d d d d d d d d d d a a a a a a a a a a a a a a a a a a a a a d d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d a a a a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d 
        d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a d d d d d d d d d d d d d d d d a a a a a a a a a a a a a a a a a a a a a d d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d a a a a a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d 
        d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a a a a d d d d d d d d d d d d d d d d a a a a a a a a a a a a a a a a a a a a d d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d a a 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d 
        d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 a a a a a a d d d d d d d d d d d d d d d d d d d a a a a a a a a a a a a a a a a a a a a d d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d 
        d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d a a d d d a a a a a a a a a a a a a a a d d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d 
        d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d a a d d d d a a a a a a a a a a a a a a d d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d 
        d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d a a a a a a a a a a a a a d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d 
        d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d a a a a a a a a a a a a d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d 
        d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d a a a a a a a a a a a d d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d 
        d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d a a a a a a a a a a a d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d 7 7 7 7 7 7 7 d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d 
        d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d a a a a a a a a a a a d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d 7 7 7 7 7 7 d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d 
        d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d 7 7 7 7 7 d d d d d d d d d d d d d d d d a a a a a a a a a a a d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d 7 d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d 
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d 7 7 7 7 7 7 7 d d d d d d d d d d d d d d a a a a a a a a a a a d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d 
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d a a a a a a a a a a d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d 
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d a d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 7 
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7 
        7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d 7 7 7 7 7 7 7 7
"""))
sub = sprites.create(img("""
        . . . . . . . . . . . f f f f f f . . . . . . . . . . . . . . . 
            . . . . . . . . . . f d e d e e e f . . . . . . . . . . . . . . 
            . . . . . . . . . . f d d e e e e f . . . . . . . . . . . . . . 
            . . . . . . . . . . f d e d e e e f . . . . . . . . . . . . . . 
            . . . . . . . . . . f d d e e e e f . . . . . . . . . . . . . . 
            . . f f f f f f f f d d e d e e e e f f f f f f f f f f f f . . 
            . f f c f d e d e e e e e e e e e e e e e e e e d e d f c f f . 
            f f c b f e d e e d d e e e e e e e e e e d d e e d e f b c f f 
            f c b b f d e e d c b d e e e e e e e e d c b d e e d f b b c f 
            f b b b f e e d c b b b d e e e e e e d c b b b d e e f b b b f 
            f f f f f e e d b b b b d e e e e e e d b b b b d e e f f f f f 
            f b b b f e e e d b b d e e e e e e e e d b b d e e e f b b b f 
            f b b b f e d e d d d e d e d e d e d e d d d e d e d f b b b f 
            f f b b f d e d e d e d e d e d e d e d e d e d e d e f b b f f 
            . f f b f d d d d d d d d d d d d d d d d d d d d d d f b f f . 
            . . f f f f f f f f f f f f f f f f f f f f f f f f f f f f . .
    """),
    SpriteKind.player)
controller.move_sprite(sub)
sub.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
left_shark_image = img("""
    . . . . . . . . . . . . . . . . 
        . . . . . . d d d d . . . . . . 
        . . . . . d d d d . . . . . . . 
        d d d d d d d d d d d d d . . . 
        d d f d f d d d d d d d d d d . 
        . e e e e e e e d d d d d d d d 
        . . e c c c e e e e e e e e d d 
        . . . e e e e e e e e e e e e d 
        . . . . . d d . d d . . . . e d 
        . . . . . d . . . d . . . . d d 
        . . . . . . . . . . . d d d d d 
        . . . . . . . . . . d d d d d . 
        . . . . . . . . . . . . . d d . 
        . . . . . . . . . . . . . d d . 
        . . . . . . . . . . . . . d . . 
        . . . . . . . . . . . . . . . .
""").clone()
left_shark_image.flip_x()
fillAnimalArrays()
animals_needed_to_learn_immunity = 5
current_immunity = -1
level = 1

def on_update_interval():
    global shark
    shark = sprites.create_projectile_from_side(left_shark_image, level * 90, 0)
    shark.y = randint(10, scene.screen_height() - 10)
    sprites.set_data_string(shark, "species", "Shark")
game.on_update_interval(5000, on_update_interval)

def on_update_interval2():
    global shark
    if level > 1.7:
        shark = sprites.create_projectile_from_side(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . d d d d . . . . . . 
                            . . . . . d d d d . . . . . . . 
                            d d d d d d d d d d d d d . . . 
                            d d f d f d d d d d d d d d d . 
                            . e e e e e e e d d d d d d d d 
                            . . e c c c e e e e e e e e d d 
                            . . . e e e e e e e e e e e e d 
                            . . . . . d d . d d . . . . e d 
                            . . . . . d . . . d . . . . d d 
                            . . . . . . . . . . . d d d d d 
                            . . . . . . . . . . d d d d d . 
                            . . . . . . . . . . . . . d d . 
                            . . . . . . . . . . . . . d d . 
                            . . . . . . . . . . . . . d . . 
                            . . . . . . . . . . . . . . . .
            """),
            level * -90,
            0)
        shark.y = randint(10, scene.screen_height() - 10)
        sprites.set_data_string(shark, "species", "Shark")
game.on_update_interval(9000, on_update_interval2)

def on_update_interval3():
    global animal_choice, animal_speed, animal_sprite
    animal_choice = randint(0, 8)
    animal_speed = animal_speed_list[animal_choice]
    animal_sprite = sprites.create_projectile_from_side(animal_image_list[animal_choice], animal_speed * level, 0)
    # Choose random height for animal.
    animal_sprite.y = randint(10, scene.screen_height() - 10)
    sprites.set_data_string(animal_sprite, "species", animal_names[animal_choice])
    sprites.set_data_number(animal_sprite, "animal_index", animal_choice)
game.on_update_interval(1000, on_update_interval3)

def on_forever():
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.play_tone(523, music.beat(BeatFraction.WHOLE))
    music.play_tone(440, music.beat(BeatFraction.WHOLE))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(294, music.beat(BeatFraction.WHOLE))
forever(on_forever)
