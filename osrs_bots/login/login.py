import bot_builder as bb 
import pyautogui

def login():
    
    clicker = bb.clicker()
    delayer = bb.delay()

    delayer.countdown()
    
    # Screen 1/2 (Only if DC'd)
    ok_match = bb.screen_matcher("images/ok.png")
    ok_cleaner = bb.match_cleaner(ok_match.get_positions())
    centers = ok_cleaner.get_centers()
    if centers != []:
        clicker.left_click(centers[0])
    else: # May not be on this screen so go on
        print("Didn't find Ok screen so moving on to existing users")

    delayer.fixed(3)

    # Screen 1
    existing_user_match = bb.screen_matcher("images/existing_user.png")
    positions = existing_user_match.get_positions()
    print("Postions: ")
    print(str(positions))
    existing_user_cleaner = bb.match_cleaner(positions)
    centers = existing_user_cleaner.get_centers()
    print("Centers: ")
    print(str(centers))
    if centers != []:
        clicker.left_click(centers[0])
    else: # May not be on this screen so go on
        print("Didn't find existing user screen so moving on to login")

    delayer.fixed(3) # Wait for the next screen in case of lag

    # Screen 2
    login_match = bb.screen_matcher("images/login.png")
    positions = login_match.get_positions()

    login_centers = bb.match_cleaner(positions).get_centers()
    if login_centers == []:
        print("Didn't find login, you're not on the right screen")
        login_match.show_matches()
        return None

    pyautogui.typewrite('<password>', interval=.2) # If you have "remember my username" selected it should automatically prompt you and put you in the box for the password
    clicker.left_click(login_centers[0])

    delayer.fixed_random(8, 2)

    # Screen 3
    play_match = bb.screen_matcher("images/play.png")
    positions = play_match.get_positions()

    play_centers = bb.match_cleaner(positions).get_centers()
    if play_centers == []:
        print("Didn't find play button, you're not on the right screen")
        play_match.show_matches()
        return None
    clicker.left_click(play_centers[0])
    return 1 # Success

    

if __name__ == "__main__":
    login()
