# IMAGES
image bg black          = "black-1.png"
image bg red            = "red-1.png"

image bg room           = "room-1.png"
image bg elevator       = "elevator-1.png"
image bg street         = "street-1.png"
image bg subway_stairs  = "subway-stairs-1.png"
image bg subway         = "subway-1.png"
image bg fontain        = "fontain-1.png"

image christine normal  = "christine-1.png"

# CHARACTERS
define me = Character("Me",             color="#888888")
define ch = Character("Christine",      color="#BB3366", image="christine")
define fe = Character("Fyodor",         color="#2244CC")
define n0 = Character("Neightbour",     color="#000000")
define n1 = Character("Neightbour",     color="#000000")
define n2 = Character("Neightbour",     color="#000000")
define s0 = Character("Stranger",       color="#000000")
define a0 = Character("Agent 0",        color="#776644")
define a1 = Character("Agent 1",        color="#776644")
define a2 = Character("Agent 2",        color="#776644")
define a3 = Character("Agent 3",        color="#776644")

# TRANSFORMS
define close = Transform(yoffset=240)

# The game starts here.
label start:
    $ attitude = 0
    
    scene bg black
    with dissolve
    
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
    scene bg room
    with dissolve
    
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
    
    scene bg room
    with dissolve
    
    "todo"
    jump elevator_late
    
label elevator_run:
    scene bg elevator
    with fade
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
    scene bg elevator
    with fade
    "todo"
    jump subway_1
    
label elevator_late:
    scene bg elevator
    with fade
    "todo"
    jump subway_1
    
label subway_1:
    scene bg street
    with fade
    
    "We part our ways after we exit the building. I guess i'll never find out
    who was that."
    "But i must hurry.. I almost run to the subway."
    
    scene bg subway_stairs
    with fade
    
    scene bg subway
    with fade
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
    
    "todo"
    
    scene bg subway_stairs
    with fade
    
    scene bg street
    with fade
    
    "Finally! I exit this technological dungeon and breath open air."
    "I even have seven minutes left. Still i'm rushing to the amusement park."
    "Even though it's quite early, a lot of people are already here. I dive into
    crowd near the entrance and after a minute of crushing in it, i'm near the
    fontain which is our meeting point."
    
    scene bg fontain
    with fade
    
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
    
    show christine normal at center, close
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
    
    scene bg street
    show christine normal at center, close
    with fade
    
    scene bg subway_stairs
    show christine normal at center, close
    with fade
    
    "When we're entering subway, i hear police siren howling."
    
    scene bg subway
    show christine normal at center, close
    with fade
    
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
    
    scene bg red
    with dissolve
    
    me "Am i dying now?.. Damn, i won't even know how well my LD project is
    received... And.. what happend to detective and John.."
    
label crawl_to_agents:
    "todo"
    jump blackout
    
label blackout:
    scene black
    with dissolve
    
    "..."
    "..."
    "..."
    
label real_wakeup:
    scene bg room
    with Fade(0.5, 0.0, 0.5, color="#FFFFFF")
    
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
    
    "Three days of intense work resulted in producing \"reasonably good\" game
    as we all considered. Of course, it lacked proper balance, nearly half of
    graphics was placeholder, there was only one sound track and game run not
    without glitches. But overally, our entry was way better than previous one."
    
    "..."
    
    "Tuesday morning. I wake up early in the morning to see Christine off
    (Fyodor has already left yesterday)."
    
    "Looks like she's taking shower. I lazily do some excercices."
    
    "As i enter living room, my attention is grabbed by an unfamiliar package
    laying near the door."

    menu:
        "look at it":
            jump look_at_package
        "[doesn't matter":
            jump uncurious_ending
    
label look_at_package:
    "I shouldn't really be doing this, but i'll take a brief look at it."
    
    "Well, not much to see. Just a box with label \"T-08\" on it. What can that be?"
    
    menu:
        "Ask about it":
            jump box_ask
        "Open it":
            jump bloody_ending
    
label box_ask:
    "I'll ask Christine later."
    
    if attitude < 0:
        jump bad_ending
    elif attitude < 2:
        jump normal_ending
    else:
        jump true_ending
    
label true_ending:
    ch "That... {w=1}Jack, can i trust you?"
    me "Yeah?.."
    ch "Can you keep a dangerous secret?"
    me "Yeah, sure. I won't tell anybody.."
    ch "Don't take it that lightly! This can put you in dager! And you certainly
    must not tell this to {i}anybody{/i} including police."
    "..Something like that was in my dream two days ago, wasn't it?.."
    me "If you're in any danger, i'll be glad to share it with you!"
    "Thre is a small pause before she answers."
    ch "..Okay then. I'm a member of underground revolutionary organization. And
    we're making an execution of goverment official today. That box contains
    bomb for him."
    "..Now that definitely sounds like my dream.. Only this time it's not.."
    
    scene bg black
    with fade
    
    ":: True Ending ::"
    return
    
label bloody_ending:
    "They say \"Don't touch suspiciuos objects\", but who really listen to that.
    At least not me.."
    "I open the box and than..."
    
    scene bg red
    with fade
    
    "BOOM!"
    
    ":: Bloody Ending ::"
    return
    
label normal_ending:
    ch "That..."
    "She hesitates"
    ch "Sorry, i can't really tell you now.."
    me "Okay, don't worry about it.."
    
    $ ending = "normal"
    jump common_ending
    
label normal_ending_end:
    "When Christine left, i felt extreme withdrawl effect from not playing
    \"Mystery of Magenta II\" for three days in a row."
    
    "So i grab some fast food from kitchen and comfortly lie on the bed with my
    phone."
    
    ":: Normal Ending ::"
    return

label bad_ending:
    ch "That's a secret! Give it to me."
    "She is quite annoyed."
    me "Sorry.."
    
    $ ending = "bad"
    jump common_ending
    
label bad_ending_end:
    "When Christine left, i returned to my room, layed in bed and turned TV on."
    "I'm really too lazy to even play \"Mystery of Magenta II\" so i'm trying to
    relax by watching stupid shows for next two hours."
    
    "When i was almost sleeping, the show was over and news started."
    
    tv "..at the amusement park.. ..explosion.. ..was killed.."
    
    "I wasn't paying attention initially and missed some words, but general
    meaning struck me like a lighting.. WHAT THE HELL?!"
    
    "My messed up thoughts are interrupted when i hear somebody is ringing on my
    door.."
    
    scene bg black
    with fade
    
    ":: Bad Ending ::"
    return

label uncurious_ending:
    "Why bother?.. Let's prepare some breakfast instead!"
    
    $ ending = "uncurious"
    jump common_ending
    
label uncurious_ending_end:
    "When Christine left, i realize i'm really tired from this LD. I'm even too
    lazy to play \"Mystery of Magenta II\", which i haven't played for last
    three days.."
    
    "I just lay on the bed and take a nap.."
    
    scene bg black
    with fade
    
    ":: Bed Ending ::"
    return
    
label common_ending:
    "..."
    
    "We have a breakfast and then she leaves taking that package with her."
    
    "..."
    
    if ending == "normal":
        jump normal_ending_end
    elif ending == "bad":
        jump bad_ending_end
    else:
        jump uncurious_ending_end
