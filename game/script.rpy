# IMAGES
# eg. image eileen happy = "eileen_happy.png"

# CHARACTERS
define me = Character("Me",             color="#888888")
define ch = Character("Christine",      color="#BB3366")
define fe = Character("Fyodor",         color="#2244CC")
define n0 = Character("Neightbour",     color="#000000")
define n1 = Character("Neightbour",     color="#000000")
define n2 = Character("Neightbour",     color="#000000")
define s0 = Character("Stranger",       color="#000000")


# The game starts here.
label start:
    $ attitude = 0
    
    "Sound of alarm wakes me up early in the morning.
    {p}Damn! it's only 8:00, why can't i sleep a bit more?.."
    
    "I almost decided to ignore annoying beeping, but then remembered why i set
    it up despite having gone to bed very late yesterday. That's right, i have a
    date with Christine today!"
    
    "..But maybe i still can get a bit more sleep?"
    
    menu:
        "Yeah, just a bit..":
            jump wake_up_late
        "No, i don't want to be late!":
            jump wake_up_early
    
label wake_up_early:
    "That's right. I would feel so awful if i will be late for another date.
    What if she won't wait for me?! Oh no, i must totally hurry and get up."
    "In fifteen minutes i'm already finishing my small breakfast."
    "Now, what should i wear? I must've prepared that yesterday, but was busy with LD all day instead."
    
    "Ok, that should do."
    "I glance at the mirror and run to the exit."
    
    "Elevator is closing!.."
    
    menu:
        "Run faster!":
            jump elevator_run
        "I don't want to ruin my clothes!":
            jump elevator_early
    
label wake_up_late:
    "I set alarm to wake me up in five minutes and dived into the blanket"
    "todo"
    jump elevator_late
    
label elevator_run:
    "I've made it! Doors closes behind me and i almost bumped into somebody."
    me "Excuse me.."
    n0 "Oh, hey, aren't you Jack?"
    me "Emm.. Yeah."
    "I struggle to remember who was that.."
    n0 "You must've forgotten me, right? Don't worry about it. Oh, sorry,
    someone's calling me."
    "He turned to the wall and started talking on the phone."
    n0 "coi la blekus. mi ..."
    "..But in some exotic language i've never heard before."
    
    jump subway_1
    
label elevator_early:
    "todo"
    jump subway_1
    
label elevator_late:
    "todo"
    jump subway_1
    
label subway_1:
    "We part our ways after we exit the building. I guess i'll never find out
    who was that."
    "But i must hurry.. I almost run to the subway."
    
    "Since i live in suburb, it's a long way underground for me. To not waste
    time, i return to playing \"Mystery of Magenta II\", which i haven't played
    since LD started and thus had slight withdrawl syndrome."
    me "Woah, John turned out to be villain! Now that's really tough moral
    choice for detective.."
    "I'm so excited that i even said it out loud. But it's so noisy here,
    nobody should've heard that"
    
    menu:
        "I can't forgive him!":
            "todo"
            $ attitude -= 1
        "He's my friend, but i must stop him.":
            "todo"
        "He's my friend, he may have reasons to do that..":
            "todo"
            $ attitude += 1
    
    "Finally! I exit this technological dungeon and breath open air."
    "I even have seven minutes left. Still i'm rushing to the amusement park."
    "Even though it's quite early, a lot of people are already here. I dive into
    crowd near the entrance and after a minute of crushing in it, i'm near the
    fontain which is our meeting point."
    "Four minutes till ten. She's not here yet. Well, that's not unusual. She
    doesn't want to wait me like previous time.."
    "I'm sitting on fontain edge, nervously looking at clock on the gates and at
    the people entering."
    
    "The minute hand hits \"12\" mark and starts a new circle. Another two
    minutes passing. I'm starting to think about calling her."
    
    s0 "Hey!"
    "Suddenly, someone calls out to me. I turn around and see the stranger."
    "At first glance he seems to be somehow familiar to me, but i can't even
    determine why."
    "His look is definitly out of place though."
    s0 "Excuse me, can you tell me where is shooting range here?"
    
    menu:
        "Answer him":
            $ attitude += 1
            jump show_the_way
        "I don't know":
            $ attitude -= 1
            jump dont_know
    
label show_the_way:
    me "Hmm, shooting range?.."
    "I remember our previous date and park map emerges in my head. I show him
    the way."
    s0 "Thank you so much"
    "Despite his look, he bows ceremoniously and then disappears in the crowd."
    
    jump weird_people_day
    
label dont_know:
    "todo"
    jump weird_people_day
    
label weird_people_day:
    "Is this day of meeting weird people?.. I want to meet Christine, not them!"
    
    "After waiting another two minutes, i finally decide to call. Her phone is
    out of reach. She's probably in subway now."
    "I hope so. But what if she just decided to dump me?!
    {p}This world is so unfair."
    
    "I'm starting to be even more nervous."
    
    ".."
    
    return
