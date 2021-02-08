import bot_builder as bb

def wizard_tower():

    # Start by clicking the compass and zooming out as far as you can on osbuddy
    delayer = bb.delay()
    clicker = bb.clicker()

    # Killing Demon Loop


    lesser_demon_match = bb.screen_matcher("images/lesser_demon.png", 0.75)
    lesser_demon_centers = bb.match_cleaner(lesser_demon_match.get_positions()).get_centers()
    correct_center = None
    for _ in range(0,8):
        for center in lesser_demon_centers:
            if center[0] > 750 and center[0] < 950 and center[1] > 550 and center[1] < 590:
                correct_center = center
                break
        if correct_center is not None:
            break
        print("Didn't find a lesser demon")
        delayer.fixed_random(15, 3)
    if correct_center is None:
        print("Could never find a lesser demon")
        return None

    clicker.left_click(correct_center)

    # Killing Demon Loop
    for _ in range(0,1000):
        dead_sm = bb.screen_matcher("images/dead_demon.png")
        click_here_sm = bb.screen_matcher("images/click_here.png")
        while dead_sm.get_positions() == [] and click_here_sm == []:
            dead_sm.rematch()
            click_here_sm.rematch()
            delayer.fixed_random(1, 0.6)
        if click_here_sm.get_positions() != []:
            lesser_demon_match = bb.screen_matcher("images/lesser_demon.png", 0.75)
            lesser_demon_centers = bb.match_cleaner(lesser_demon_match.get_positions()).get_centers()
            correct_center = None
            for _ in range(0,8):
                for center in lesser_demon_centers:
                    if center[0] > 750 and center[0] < 950 and center[1] > 550 and center[1] < 590:
                        correct_center = center
                        break
                if correct_center is not None:
                    break
                print("Didn't find a lesser demon")
                delayer.fixed_random(15, 3)
            if correct_center is None:
                print("Could never find a lesser demon")
                return None

            clicker.left_click(correct_center)
        else:


    



    

