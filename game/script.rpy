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
define a0 = Character("Agent 0",        color="#776644")
define a1 = Character("Agent 1",        color="#776644")
define a2 = Character("Agent 2",        color="#776644")
define a3 = Character("Agent 3",        color="#776644")


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
    "Now, what should i wear? I must've prepared that yesterday, but was busy
    with LD all day instead."
    
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
    
    menu:
        "Walk around the fontain":
            "todo"
        "Continue sitting":
            "todo"
    
    "..It's 10:15. I've called her three times already, but her phone is still
    out of network."
    "Christine, where are you? My thoughts are interrupted by another firework
    explosion. What idiot is launching fireworks in the morning anyway?.."
    "I notice some change in sound background. Hmm, that monotonous guy stopped
    talking, but also people are starting to sound more worried."
    "Then somebody runs past me looking very frightend. I look in the direction
    of main stage (which can't be seen from here, but i know exactly where it
    is). There are few more people looking extremly frightend.. Then there are
    two men in uniform, probably from security."
    
    ch "Hey, Jack!"
    "Her voice! She finally came! For a second i even forgot about that weird
    accident."
    me "Hi, Christy.. I'm so glad you came.. I was so worried.."
    "I really was. Was afraid of loosing her."
    ch "Sorry i am late.. But it's not time for that."
    ch "Look there. Something happend, i think it's not quite safe to stay here
    now."
    ch "Let's go back to the subway and then decide where to go."
    "She doesn't look really frightend even though now it's obviously looking
    like a serious situation: people are chaotically running everywhere.
    {p}But she looks only a bit worried and maybe even annoyed."
    "I realize she's totally right about leaving this place. Even if it's not
    dangerous anymore, we don't want to spend date talking to the police as
    witnesses. Especially haven't witnessed anything important or interesting."
    
    "So i grab her hand and we run to the exit."
    
    "When we're entering subway, i hear police siren howling."
    
    "When we're already in the train heading towards city center, i say:"
    me "This all looks like we're running from the police"
    ch "You feel so? Don't tell me you had time to play another of your stupid
    detective games today already."
    me "Well, yeah, i played. There wasn't anything better to do on the way here
    anyway."
    ch "See, it's all your imagination!"
    me "But that accident, i don't even know what was that, but it happend."
    me "And you say such things happen only in fiction!"
    ch "I'm just joking, silly."
    "She slightly pokes me and laughs."
    ch "More importantly, where are we going now?"
    "I start thinking, but she interrupts it."
    ch "What about Transient Cafe? It's quite nice and cozy."
    me "Really? I've never been there before. But lets go."
    
    "By this time the train is already approaching next station."
    
    "When doors opened, a group of four unfriendly looking people in grey suites
    come into the coach. Then everything happens very fast. I catch gaze of one
    of them. I observe his hand coming out of pocket, and then suddenly feel
    something cold by my neck and somebody pulling me back."
    ch "Drop your weapons and get out of here! Our i'll cut his throat!"
    "What?! As i hear this i realize that it's Christine staying behind me and
    pressing dagger's blade on my neck."
    "Passangers are screaming and running out of train to the station somewhere
    in the distant background. My attention is directed solely towards those
    guys in uniform.
    One of them who is looking more confident than others steps forward and
    says:"
    a0 "Really?.. Isn't that your comrade?"
    "He grins and finally takes his gun of the pocket."
    "His collegue is speaking to the transmitter."
    a1 "We have a hostage here, please check if he's civillian. Damn, i hope
    he's not."
    ch "Don't make another step!"
    "Christine pushes blade further and i feel pain and then something wet on my
    neck."
    ch "Or he's dead!"
    a0 "Oy, oy, are you really that serious, bitch?"
    ch "Don't even try to fuck with me, idiot!"
    "At this moment train is starting to leave station. I nearly lost balance
    and blade pricked me again. Finally i regain ability to speak."
    me "What.. what is this all?.. Christy, what is happenning?.."
    "My voice sound distant and weak."
    a1 "She's a terrorist, boy. Don't worry, we'll save you if you won't do
    anything stupid."
    me "Is.. is this true?"
    ch "Not time to babble, Jack! I need to get out of here, Jack so you'll be
    my shield for now. And you - drop your weapon NOW!"
    "Her voice sounds so cold and now i get {i}really{/i} scared of dying."
    "Their leader doesn't obey but doesn't make any jerky movements either. He's
    not even pointing his pistol in our direction."
    ch "I'll count to three and if you don't drop your weapons and hold your
    hands in the air, you'll have a dead body on you!"
    "She starts counting:"
    ch "One... Two..."
    "When she shouts \"Three\" i notice sudden movement by peripheral vision.
    There was latest passenger which haven't escaped coach on station. He was
    looking like a sleeping bum, so nobody was paying attention to him in this
    tough situation."
    "I feel being pushed aside and while falling watch \"agents\" taking out
    their pistols, and \"bum\" shooting at them with submachine gun in the
    jump."
    "When i hit the ground, i see two of agents fell on the ground with blood
    on their bodies. Christine jumped past me and took position behind seats."
    
    $ laying_down = False
label crawl_to:
    
    menu:
        "Crawl towards her":
            $ attitude += 1
            jump crawl_to_her
        "Lay down" if not laying_down:
            $ laying_down = True
            jump lay_down
        "Crawl towards agents":
            $ attitude -= 1
            jump crawl_to_agents
    
label lay_down:
    "Bullet hits floor just near my head and i decide that i should move
    somewhere else."
    jump crawl_to
    
label crawl_to_her:
    "Even though Christine does look so scary now and is certanly a different
    person than i knew for so long, i still feel safer with her than these
    \"agents\"."
    "She catches a pistol flying from the bum side and starts shooting as well."
    
    a2 "Damned boy! He's her mate in the end! We should've shoot him ealier."
    
    "After this words i suddenly stumble and feel weak. Voices and shooting
    sounds becomes distant and muted.. My mind slowly collapses into the
    darkness."
    
    
    
    me "Am i dying now?.. Damn, i won't even know how well my LD project is
    received... And.. what happend to detective and John.."
    
label blackout:
    "..."
    "..."
    "..."
    
label real_wakeup:
    "..That was my last thoughts before i wake up in cold sweat. I open my eyes
    and realize it was only a dream.. Then i realize i'm still wheezing in
    attempt to scream."
    "I stop and get up smashing tin can with my foot. Probably beer can.. Yeah,
    we were drinking yesterday.. Then i see Christine and Fyodor standing in the
    doorway. Oh, how good to see her without that cold fire in glance.."
    fe "Are you okay?.."
    ch "Had a bad dream, honey?"
    me "..Oh yeah.. A nasty dream.. But i'm ok"
    fe "Then get ready for LD!"
    me "Wha- oh right, we haven't made it yet.."
    fe "Have you dreamed of us failing LD?" 
    me "Nah.."
    "Fyodor giggles and exits the room leaving us alone."
    "Christine comes to me and sits on my bed and comforts me."
    ch "Relax, Jack.. It's only a dream."
    
    "..."

    "We all gather in the living room and after a short breakfast start
    brainstorming our project."
    fe "Eeh, why \"Beneath the surface\"? I was so hoping to do \"Break the
    rules\"! I've got so cool concept"
    ch "What about we finally make a platformer?"
    me "Do you have code for that? Last time we were doing action game, you've
    spent most of jam to get things move smoothly!"
    fe "..And everybody is going to make platformer with this theme!"
    ch "Hey, you are understimating me! I've made all the required enchancements
    to the engine.. And we've got enough booze to keep me productive"
    
    "..."
    
    "So we ended up deciding to make a sidescrolling realtime strategy."
    
    "..."
    
    
    return
