def get_cur_hedons():
    '''Returns the current number of hedons'''
    global cur_hedons
    return cur_hedons

def get_cur_health():
    '''Returns the current number of health points'''
    global cur_health
    return cur_health


def offer_star(activity):
    '''The function offers a star for activity activity. If the user takes the star right away, the user gets an additional 3 hedons per minute for at most 10 minutes. Note that the user only gets 3 hedons per minute for the first activity they undertake, and do not get the hedons due to the star if they decide to keep performing the activity'''
    global cur_star, cur_star_activity, bored_with_stars
    if cur_star == None:
        cur_star = activity
        cur_star_activity = activity
    elif cur_star == activity:
        cur_star = activity
        cur_star_activity = activity
    else:
        cur_star = activity
        cur_star_activity = activity
        bored_with_stars = True

    


#The function simulates the user’s performing activity activity for duration minutes. Assume duration
#is a positive int. If activity is not one of "running", "textbooks", or "resting", running the function
#should have no effect.
def perform_activity(activity, duration):
    global cur_hedons, cur_health, cur_time, last_activity, last_activity_duration, last_finished, bored_with_stars

    cur_time = 0

    if activity == "running":
        if duration > 180:
            cur_health += 3 * 180 + (duration - 180)
        else:
            cur_health += duration * 3

        if last_activity == 'running' or last_activity == 'textbooks' and cur_time - last_finished < 120:
            if cur_star_activity == 'running':
                if duration > 10:
                    cur_hedons += 10 + (-2) * (duration - 10)
                else:
                    cur_hedons += duration
            else:
                cur_hedons -= 2 * duration
        else:
            if cur_star_activity == 'running':
                if duration > 10:
                    cur_hedons += 5 * 10 + (-2) * (duration - 10)
                else:
                    cur_hedons += 5 * duration

            else:
                if duration > 10:
                    cur_hedons += 2 * 10 + (-2) * (duration - 10)
                else:
                    cur_hedons += 2 * duration
    
        last_finished = cur_time

    elif activity == "textbooks":
        cur_health += 2 * duration

        if last_activity == 'running' or last_activity == 'textbooks' and cur_time - last_finished < 120:
            cur_hedons -= 2 * duration
        else:
            if duration > 20:
                cur_hedons += 1 * 20 + (-1) * (duration - 20)
            else:
                cur_hedons += 1 * duration
    
        last_finished = cur_time

    elif activity == "resting":
        pass
    
    last_activity = activity
    last_activity_duration = duration
    cur_time += duration
    
    
def star_can_be_taken(activity):
    #The function returns True iff a star can be used to get more hedons for activity activity. A star can only
#be taken if no time passed between the star’s being offered and the activity, and the user is not bored with
#stars, and the star was offered for activity activity.
    global cur_time, bored_with_stars, last_activity, last_activity_duration
    if cur_time == 0 and bored_with_stars == False and activity == cur_star_activity:
        return True

def most_fun_activity_minute():
#The function returns the activity (one of "resting", "running", or "textbooks") which would give the
#most hedons if the person performed it for one minute at the current time.
    global cur_hedons, cur_health, cur_time, last_activity, last_activity_duration, last_finished, bored_with_stars

    running_hedons, textbooks_hedons, resting_hedons = 0, 0, 0

    if last_activity == 'running' or last_activity == 'textbooks' and cur_time - last_finished < 120:
        if cur_star_activity == 'running':
            running_hedons += 1
        else:
            running_hedons -= 2
    else:
        if cur_star_activity == 'running':
            running_hedons += 5
        else:
            running_hedons += 2
        
    if last_activity == 'running' or last_activity == 'textbooks' and cur_time - last_finished < 120:
        textbooks_hedons -= 2
    else:
        textbooks_hedons += 1

    if running_hedons > textbooks_hedons and running_hedons > resting_hedons:
        return "running"
    elif textbooks_hedons > running_hedons and textbooks_hedons > resting_hedons:
        return "textbooks"
    else:
        return "resting"

def initialize():
#The function initialize all the global variables in the program. 
    global cur_hedons, cur_health
    global cur_time
    global last_activity, last_activity_duration
    global last_finished
    global bored_with_stars 
    global cur_star_activity, cur_star
    cur_hedons = 0
    cur_health = 0 
    cur_star = None
    cur_star_activity = None  
    bored_with_stars = False
    last_activity = None
    last_activity_duration = 0
    cur_time = 0
    last_finished = -1000
    num_stars= []

if __name__ == '__main__':
    initialize()
    def test10(self):
        perform_activity("running", 30)
        perform_activity("resting", 30)
        offer_star("running")
        perform_activity("textbooks", 30)
        offer_star("running")
        perform_activity("running", 20)
        perform_activity("running", 170)
        self.assertEqual(get_cur_hedons(), -430)              # Test 10


    def test6(self):
        gamify.perform_activity("running", 30)
        gamify.perform_activity("resting", 30)
        gamify.offer_star("running")
        gamify.perform_activity("textbooks", 30)
        self.assertEqual(gamify.get_cur_hedons(), -80)    

    def test8(self):
        gamify.perform_activity("running", 30)
        gamify.perform_activity("resting", 30)
        gamify.offer_star("running")
        gamify.perform_activity("textbooks", 30)
        gamify.offer_star("running")
        gamify.perform_activity("running", 20)
        self.assertEqual(gamify.get_cur_hedons(), -90)


    def test9(self):
        gamify.perform_activity("running", 30)
        gamify.perform_activity("resting", 30)
        gamify.offer_star("running")
        gamify.perform_activity("textbooks", 30)
        gamify.offer_star("running")
        gamify.perform_activity("running", 20)
        gamify.perform_activity("running", 170)
        self.assertEqual(gamify.get_cur_health(), 700)