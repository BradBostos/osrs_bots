import bot_builder as bb

def varrock_tp():

    clicker = bb.clicker()
    delayer = bb.delay()

    delayer.countdown()

    varrock_tp = bb.screen_matcher("images/varrock_tp.png")
    varrock_tp_center = bb.match_cleaner(varrock_tp.get_positions()).get_centers()[1]

    for i in range(0, 400):
        clicker.left_click(varrock_tp_center)
        delayer.fixed_random(0.5, 0.3)
        delayer.fcrc(20, 10, 200)

    for i in range(0,153):
        clicker.left_click(varrock_tp_center)
        delayer.fixed_random(3.6, 0.9)
        delayer.fcrc(20, 10, 100)

if __name__ == "__main__":
    varrock_tp()
