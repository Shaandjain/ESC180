def initialize():
    
    global cur_hedons, cur_health

    global cur_time
    global last_activity, last_activity_duration
    
    global last_finished
    global bored_with_stars

    global cur_star, cur_star_activity
    global last_star_time
    global tired
    global star_time
    star_time = -1000
    last_star_time = -180
    cur_hedons = 0
    cur_health = 0
    
    cur_star = None
    cur_star_activity = None
    
    bored_with_stars = False
    
    last_activity = None
    last_activity_duration = 0
    
    cur_time = 0
    
    last_finished = -1000


            

def star_can_be_taken(activity):
    global cur_time, bored_with_stars, last_activity, last_activity_duration, last_star_time, cur_star, star_time, cur_star_activity
#The function returns True if a star can be used to get more hedons for activity. A star can only
#be taken if no time passed between the star’s being offered and the activity, and the user is not bored with
#stars, and the star was offered for activity activity.
    if not bored_with_stars and star_time == cur_time and activity == cur_star_activity:
        return True
    else:
        return False

    
def perform_activity(activity, duration):
    global cur_hedons, cur_health, cur_time, last_activity_duration, last_finished, tired, last_activity, cur_star, cur_star_activity
    global star_num

    star_num = 3 if star_can_be_taken(activity) else 0
    # star_num = 0

    cur_time += duration
    
    tired = 0 < last_activity_duration < 120

#HEALTH POINTS
    if activity == 'running':
        if last_activity != "running":
            last_activity_duration = 0
        if duration > (180- last_activity_duration):
            cur_health += 3 * max(0, 180 - last_activity_duration) + 1 * (duration - max(0, 180 - last_activity_duration))
        else:
            cur_health += 3 * duration
        # print("local", cur_health)
        # print("last", last_activity_duration)
        last_finished = cur_time
        last_activity_duration += duration
        last_activity = "running"

    elif activity == 'textbooks':
        if last_activity != "textbooks":
            last_activity_duration = 0
        if duration > (180- last_activity_duration):
            cur_health += 2 * (180-last_activity_duration) + 1 * (duration - (180-last_activity_duration))
        else:
            cur_health += 2 * duration

        last_finished = cur_time
        last_activity_duration = duration
        last_activity = "textbooks"


    elif activity == 'resting':
        last_activity_duration = duration
        last_activity = "resting"

#HEDONS
    #RUNNING
    if activity == 'running':
        if last_activity != "running":
            last_activity_duration = 0
        if tired:
            if duration > 10:
                cur_hedons += ((star_num-2) * 10) + ((-2) * (duration - 10))
  
            else:
                cur_hedons += (star_num-2) * duration

        else:
            if duration > 10:
                    cur_hedons += ((star_num + 2) * 10) + ((-2) * (duration - 10))

            else:
                cur_hedons += (star_num + 2) * duration
 
        last_activity = "running"
    #the star activity should reset to none after the activity is done
        


    #TEXTBOOKS
    elif activity == 'textbooks':
        if last_activity != "textbooks": #if last activity is not textbooks, reassign the last duration
            last_activity_duration = 0
        if tired:
            if duration > 10:
                cur_hedons += ((star_num - 2) * 10) + ((-2) * (duration - 10))


            else:
                cur_hedons += (star_num - 2) * duration

        else:
            if duration > 20:
                cur_hedons += ((star_num + 1) * 10) + ((1) * 10) + ((-1) * (duration - 20))
            elif duration > 10:
                cur_hedons += (star_num + 1) * 10 + 1 * (duration - 10)
            else:
                cur_hedons += (star_num + 1) * duration
                
        last_activity = "textbooks"

    if star_num == 3:
        cur_star = False
        cur_star_activity = None


def perform_activity_hedon(activity):
    global cur_hedons, cur_health, cur_time, last_activity_duration, last_finished, tired, last_activity, cur_star, cur_star_activity
    global star_num

    result = 0

    star_num = 3 if star_can_be_taken(activity) else 0

    tired = 0< last_activity_duration <= 120


#HEDONS
    #RUNNING
    if activity == 'running':
        if tired:
            result += star_num-2
        else:
            result += star_num + 2
    #the star activity should reset to none after the activity is done
    
    #TEXTBOOKS
    elif activity == 'textbooks':
        if tired:
            result += star_num - 2
        else:
            result += star_num + 1
    #the star activity should reset to none after the activity is done

    return result




def get_cur_hedons():
    global cur_hedons
    return cur_hedons
    
def get_cur_health():
    global cur_health
    return cur_health
    
def offer_star(activity):
    global cur_star, cur_star_activity, bored_with_stars
    global cur_time, last_activity,last_star_time, star_time
    if (cur_time - last_star_time < 120):
        bored_with_stars = True
        
    cur_star_activity = activity
    last_star_time = star_time
    star_time = cur_time
    cur_star = True

        
def most_fun_activity_minute():
    global cur_star, cur_star_activity, last_activity, last_activity_duration, last_finished
    global cur_time, last_star_time
#The function returns the activity (one of "resting", "running", or "textbooks") which would give the
#most hedons if the person performed it for one minute at the current time.

    running_hedons = perform_activity_hedon("running")
    textbooks_hedons = perform_activity_hedon("textbooks")
    resting_hedons = 0

    #return the largest of the three
    if running_hedons > textbooks_hedons and running_hedons > resting_hedons:
        return "running"
    elif textbooks_hedons > running_hedons and textbooks_hedons > resting_hedons:
        return "textbooks"
    else:
        return "resting"

    # print(cur_star, cur_time, last_star_time)
    # if cur_star == True and cur_time == last_star_time:
    #     return cur_star_activity
    # elif 0<= last_activity_duration <= 120:
    #     return "resting"
    # else:
    #     return "running"
    
        
################################################################################
        
if __name__ == '__main__':
    initialize()
    perform_activity('textbooks', 1)
    print(get_cur_hedons())