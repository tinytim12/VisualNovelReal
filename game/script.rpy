# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define n = nvl_narrator
define na = Character("Zack")
define a = Character("Alexis", color ="#db03fc")
define q = Character("???", color="#4e4e54")
define p = Character("Police")

define i = Character("Intercom",  color="#4e4e54")

define crash = "sound/crash.wav"
define footstepsGravel = "sound/footstepsGravel.wav"
define footsteps = "sound/footsteps.wav"
define thud = "sound/thud.wav"
define doorCloseTrain = "sound/doorCloseTrain.wav"
define pageTurn = "sound/pageTurn.wav"
define static = "sound/static.wav"
define trainComing = "sound/trainComing.wav"
define beep = "sound/beep.wav"
define footstepsFast = "sound/footstepsFast.wav"
define footstepsGravelFast = "sound/footstepsGravelFast.wav"

define ambientTrain = "sound/ambientTrain.wav"
define wind = "sound/wind.wav"
define stopTrain = "sound/stopTrain.wav"
define ambientStation = "sound/ambientStation.wav"
define loFi = "sound/loFi.wav"
define cupNoodles = "sound/cupNoodles.wav"
define dread = "sound/dread.wav"
define horror = "sound/horror.wav"

image alexis surprised = "Alexis/alexis_surprised.png"
image alexis angry = "Alexis/alexis_angry.png"
image alexis determined = "Alexis/alexis_determined.png"
image alexis sad = "Alexis/alexis_sad.png"
image alexis smiling = "Alexis/alexis_smiling.png"
image alexis thinking = "Alexis/alexis_thinking.png"
image alexis worried = "Alexis/alexis_worried.png"

image howard close1 = "Howard/HowardClose1.png"
image howard close2 = "Howard/HowardClose2.png"
image howard close3 = "Howard/HowardClose3.png"
image howard close4 = "Howard/HowardClose4.png"
image howard close5 = "Howard/HowardClose5.png"

image stationSide = "Bg/stationSide.jpg"
image trainSide = "Bg/trainSide.jpg"
image trainSideDreamy = "Bg/trainSideDreamy.jpg"
image trainSideHorror = "Bg/trainSideHorror.jpg"
image trainMiddleHorror = "Bg/trainMiddleHorror.jpg"
image trainMiddle = "Bg/trainMiddle.jpg"
image trainMiddleHoward = "Bg/trainMiddleHoward.jpg"
image tunnel = "Bg/tunnel.jpg"
image trainDoor ="Bg/trainDoor.jpg"
image trainDoorHoward = "Bg/trainDoorHoward.jpg"
image stationGantry ="Bg/stationGantry.jpg"
image vending ="Bg/vending.jpg"
image detention ="Bg/detention.jpg"
image office ="Bg/office.jpg"
define emergency ="Bg/emergency.jpg"

define flash = Fade(1, 1, 1, color="#fff")
define redFlash = Fade(0.25, 0.25, 0.25, color="#8a0303")
define quickFlash = Fade(0.25, 0.25, 0.25, color="#fff")
define wipe  = ComposeTransition(Dissolve(3.0), before=wipeleft)

image black = "#000"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
        
    scene black 
    
    play looper wind fadein 1
    
    

    n "It is not in the nature of trains to rebel." 
    
    nvl clear
    
    n "{vspace=50}After all, they are just machines."
    
    n "{vspace=50}Programmed to bring you from point A to point B."
    
    nvl clear
    
    n "{vspace=15}Could you imagine what would happen to our city if they strayed off the rails?"

    n "{vspace=15}If the levers controlling its engine no longer worked?"
    
    n "{vspace=15}Could you even fathom the thought if them clambering out of the platform and out into the streets?"
    
    nvl clear 
    
    n "{vspace=15}Never mind the property damage."
    
    n "{vspace=15}People would no longer be able to go where they needed to go."
    
    n "{vspace=15}Boxed in their carriages, floating in a singular point in space."
    
    n "{vspace=15}Eyes searching desperately for the road ahead."
    
    nvl clear
    
    n "{vspace=15}That's why there are laws in place."
    
    n "{vspace=15}The train can only move forward."
    
    n "{vspace=15}It cannot move left or right."
    
    n "{vspace=15}It cannot go past the end of the track."

    n "{vspace=15}It cannot remain in place or go too fast."
    
    nvl clear
    
    #slow fade out
    
    n "{vspace=50}This is the fundamental truth of our society."
    
    n "{vspace=50}Without trains, humanity would cease to exist."
    
    n "{vspace=50}And yet, we still plant explosives on the tracks."
    
    nvl clear
   
    n "{vspace=50}This is the result."
    
    nvl clear
    
    #scene of the devestation
    
    scene trainMiddleHorror with fade
    
    n "I am inside the carcass of a rebel."
    
    n "A once proud warrior stripped bare."
    
    n "Already, it's organs are failing."
    
    n "The occupants have long since descended into madness."
        
    nvl clear
   
    n "My tongue comes out dry and my head like brass."
 
    n "Behind me, a man succumbs."
    
    n "His limbs distort and he convulses to the ground."

    n "In front of me, the rest are trying to get the door open."
    
    n "Their hands pull until their fingers split, but the train denies them."
    
    n "A foot crushes my collarbone as someone throws himself against the windows."
    
    nvl clear
    
    n "Shocked by the pain, I remember how to move my leg again."
    
    n "My instinct alone plants me back on my feet."
    
    n "From here, I have a full view of the carnage before me."
    
    n "The dying and the desperate broiling against each other."
    
    n "The fire stroking out from beneath the ceiling."
    
    n "I have a full view of the carriage which dared fly too close to the sun."
        
    nvl clear 
    
    n "I can see her."
    
    n "Just the shape, hovering above the sea of corpses."
    
    n "She might have already left this world, but still."
    
    n "My legs turn, and they shuffle..."
    
    n "...and instead of fleeing I approach the carnage."
    
    n "The darkness begins to lift and I start to make out her dress."
    
    nvl clear
    
    n "Again, the two of us had arrived."
    
    n "{vspace=20}On the same road on the same track on the same route."
    
    n "{vspace=20}The beginning of the journey, and the end."
    
    n "{vspace=20}Point A..."
    
    nvl clear
    
    n "{vspace=50}...to Point B"
    
    stop looper
    
    nvl clear
    
    scene stationGantry with flash
    #change scene 
    
    play music loFi fadeout 1.0 fadein 1.0 loop
    
    $ renpy.pause(2.5, hard=True)
    
    scene stationSide with dissolve
    
    $ renpy.pause(2.5, hard=True)
    
    scene vending with dissolve
    
    $ renpy.pause(2, hard=True)
    
    n "Alright, what will it be today?"
    
    
    nvl clear
    
    n "That's the thing about the vending machine."
    
    n "It's cursed."
    
    n "Well, cursed only to me. Darren tried it the other day and it worked fine for him."
    
    n "But no matter how many times I push the button, I always end up with avocado flavour."
    
    nvl clear
    
    n "Avocado of all things was never meant to exist on a candy!"
    
    n "There are like, five, six other flavours with are much better."
    
    n "Problem is, this vending machine has a gimmick."
    
    n "There's only one button for selection. That's because the flavour of the candy it gives you is entirely random."
    
    nvl clear
    
    n "So one out of six times, you'd be stuck with the avocado."
    
    n "I've tried at least twelve times and it always spits out the worst one."
    
    n "As if it's been programmed to taunt me."
    
    n "Which is ridiculous, because no vending machine could be sentient enough to enact a personal vendetta."
    
    n "Not as if I treated it badly or anything."
    
    n "I've always stroked the buttons with the utmost care."
    
    nvl clear
    
    na "Alright..."
    
    na "Lucky number thirteen, here we go..."
    
    na "..."
    
    na "{color=#10a0e3}(Maybe if I try a different technique, it won't give me the avocado again.){/color}"
    
    menu: 
    
        "Just press the button normally":
            
            na "{color=#10a0e33}(After all, there's only one way to use a vending machine.){/color}"
        
        "Press the button three times within one second!":
        
            na "{color=#10a0e3}(Come on, that's ridiculous!){/color}"
            
            na "{color=#10a0e3}(As if that would do anything.){/color}"
            
        "Kick it in the stomach!":
        
            na "{color=#10a0e3}(Come on, I'm not going to hurt it!){/color}"
            
            na "{color=#10a0e3}(Plus, if the station staff sees me do that, I'm bound to get arrested.){/color}"
    
    na "{color=#10a0e3}(In the end, the old ways are the best.){/color}"
    
    play sound beep
    
    na "{color=#10a0e3}(Just press the button...){/color}"
    
    play sound thud
    
    na "..."
    
    n "Avocado..."
    
    nvl clear
    
    q "Do you want to swap?" 
    
    n "...?"
    
    n "Someone noticed what I was doing?"
    
    nvl clear
    
    show alexis worried with dissolve
    
    q "..."
    
    n "It's a girl."
    
    n "Hey, I've seen her around before. She's one of the girls who usually sit at the back row of the canteen."
    
    n "The one with purple eyes."
    
    nvl clear
    
    na "Um..."
    
    na "Hi...?"
    
    show alexis surprised
    
    q "Oh! I'm sorry."
    
    q "But if you like Orange..."
    
    q "I don't mind swapping it for Avocado."
    
    na "{color=#10a0e3}(She unfurled her hand to reveal the orange counterpart of the candy I had received.){/color}"
    
    na "{color=#10a0e3}(So...she wanted to swap candies?){/color}"
    
    na "{color=#10a0e3}(What..?){/color}"
    
    na "S-sure..."
    
    na "Here you go."
    
    show alexis worried 
    
    q "Thanks."
    
    q "Well..."
    
    q "See you in school."
    
    na "Yeah..."
    
    hide alexis with dissolve
    
    na "...."
    
    n "What..."
    
    scene vending with hpunch
    
    n "What the hell did I just do?"
    
    n "They never taught you to talk to girls in school!"
    
    n "And it was the one with purple eyes, as well!" 
    
    n "What could have said to her anyway?"

    n "Not as if I could quiz her on her top five favourite foods right off the bat!"
    
    n "What a missed chance..."
    
    nvl clear
    
    scene stationSide with wipeleft
    
    n "This must be some sort of cruel fate."
    
    n "She's waiting at the platform."
    
    n "Don't tell me she's taking the same train as me."
    
    nvl clear
    
    n "Would it be weird if I went up and tried to talk to her again?"
    
    n "Yes, it would most definitely be."
    
    n "But destiny has already handed me a chance on a silver platter!"
    
    n "I have no choice but to take it."
    
    play sound trainComing fadein 1.0 fadeout 1.0
        
    n "The train's coming!"
    
    n "I don't know which station she gets off."
    
    n "It could be a long journey, or she could be gone by next stop."
    
    n "No, never mind that, she's already moving inside."
    
    n "I have to follow her..."
    
    nvl clear
    
    stop sound
    
    show trainSideDreamy with fade
    
    show screen borders with dissolve
    
    play looper ambientTrain  fadein 1.0
    
    n "...The train's empty."
    
    n "It's in the middle of the afternoon, after all, and all the adults are away."
    
    n "That means, of course, that I have to stand far away from her so I don't look weird."
    
    n "Did she notice me come in? Is she freaked out?"
    
    n "As far as I can see, she's still staring out the window."
    
    nvl clear
    
    n "This is driving me crazy."
    
    n "The next station's only three minutes, and she might get off!"
    
    n "Here we go..."
    
    nvl clear
    
    play sound footsteps
    
    #approach alexis
    
    $ renpy.pause(1.5, hard=True)
    
    show alexis thinking with fade
    
    na "..."
    
    $ renpy.pause(1.5, hard=True)
    
    show alexis surprised
    
    q "..."
    
    na "..."
    
    na "{color=#10a0e3}(She's inching away...){/color}"
    
    na "Don't try the Avocado!" 
    

    
    q "..."
    
    na "It tastes like shit!"
    
    show alexis worried
    
    na "{color=#10a0e3}(That was a horrible opener...){/color}"
    
    na "Which stop are you getting off at!"
    
    show alexis worried
    
    q "..."
    
    q "N-newton station."
    
    na "{color=#10a0e3}(That's an obvious lie, Newton's in the complete opposite direction...){/color}"
    
    nvl clear
    
    na "Sorry, I don't mean to shout so loud, my voice is just like that, and the train's really echoey underground, so that adds to the volume, you know what I mean?"
    
    q "..."
    
    q "Yes."
       
    na "I'm think I'm going to faint."
    
    show alexis surprised
    
    na "This...this...carriage is too hot..."
    
    na "I need water..."
    
    q "I have some water in my bag!"
    
    show alexis worried
    
    na "Ugh...could I please have some?"
    
    q "S-sure!"
    
    q "Sit down here..."
    
    n "Buried in half truths of course, but my act seems to be working."
    
    n "I'd better end it soon though, or I'm not going to live with myself."
    
    n "Conversation, conversation..."
    
    n "What's that poking out of her bag?"
    
    nvl clear
    
    na "Hey, what's that?"
    
    show alexis worried
    
    q "This? It's just a book."
    
    na "Mind if I have a look inside?"
    
    na "Sorry, I'm just trying to keep myself from passing out here..."
    
    q "Should I call an ambulance?"
    
    na "No, no, just reading something is okay. It's called a grounding technique, my doctor taught me that."
    
    na "Even if you have just doodles written down, just looking at them will help."
    
    show alexis thinking
    
    q "Sure."
    
    n "She actually believed that?!"
    
    n "I'm definitely inching closer and closer to Hell by now..."
    
    n "But is it really my fault? I didn't expect it, but she's just so naively cute."
    
    nvl clear
    
    #flips through sketchbook
    
    play sound pageTurn
    
    q "Erm...is it okay if you only see the first few pages?"
    
    n "Is she embarrassed?"
    
    n "These drawings of her's are really, really good though."
    
    play sound pageTurn
    
    play sound pageTurn
    
    n "I don't know how many flavours of 'punk' there are apart from steampunk or cyberpunk, but she's all the science fiction styles down."
    
    n "Buildings, cities, skyscrapers, a few rough sketches of characters, all dressed up in their own unique style."
    
    n "There's no way anyone I know would even think of drawing something like this."
    
    nvl clear
    
    na "Hey, these are amazing!"
        
    show alexis smiling
    
    na "{color=#10a0e3}(She's smiling!){/color}"
    
    na "Where did you learn all this?"
    
    q "I'm happy you like it."
    
    q "My dad was a painter, so I just learned from him."
    
    na "This is seriously Picasso tier."
    
    na "You could earn millions from this!"
    
    show alexis surprised
    
    q "Nononono, no one would buy these!"
    
    na "{color=#10a0e3}(I was exaggerating, of course, but I'd heard overcompliments are my best weapon right now.){/color}"
        
    na "And what are these?"
    
    hide alexis with fade
    
    n "A few pages on, the fantastical drawings ceased, and more mundane everyday sketches emerged."
    
    n "Most of them were random places around the city."
    
    na "Isn't this the train we're in now!"
    
    q "Yeah! I spend an hour everyday on a train, so I couldn't help but sketch it."
       
    scene trainSideDreamy with fade
    
    #background 
    play sound pageTurn
    
    na "{color=#10a0e3}(*flip){/color}"

    #background 2 
    play sound pageTurn
    
    na "{color=#10a0e3}(*flip){/color}"
    
    
    show alexis worried with fade
    
    q "Do you dislike any of them?"
    
    q "I'm not good at the realistic stuff."
    
    q "My father always said that I needed to branch out into other styles, so I can find something I'm can really specialize in."
    
    na "If you want my take on it, anybody can draw anything from real life."
    
    na "But it takes true talent to draw from imagination."
    
    na "Your first few drawings are the best ones, you should focus on those."
    
    show alexis smiling
    
    n "She looked at me as if she would a lighthouse in the middle of a stormy sea."
    
    n "And to think I made that piece of advice up on the spot!"
    
    nvl clear 
    
    #time passes
    
    hide alexis with fade
    
    n "The train cruised on."
    
    nvl clear
    
    #background
    
    n "The windows turned black, which meant we were going underground."
    
    #background
    nvl clear
    
    n "How many stations had it been already?"
    
    n "It felt like we had passed ten by now."
    
    nvl clear
    
    show alexis smiling with fade
    
    q "...A concept artist would be really hard. Everyone wants to be one. Some people work for ten years before they finally get that position."
    
    na "A concept artist? You mean, like for a movie?"
    
    q "Movies are great, but they're too competitive. I'm thinking maybe for a video game studio."
    
    na "Ubisoft! Or Blizzard!"
    
    show alexis worried
    
    q "Those companies are competitive too! I won't get in."
    
    show alexis thinking
    
    q "Maybe in a small studio..."
    
    na "Let me tell you something."
    
    na "You should drop out of school and send your drawings to Ubisoft right now."
    
    show alexis surprised
    
    q "But school is important!"
    
    show alexis determined
    
    q "I'm going to an art university after this."
    
    na "You sure you're going to need it?" 
    
    q "Big companies require a university education!"
    
    na "Eh, degrees are overated."
    
    na "Did you know Steve Jobs dropped out of college?"
    
    show alexis surprised
    
    q "Oh, really?!" 
    
    na "Yeah, also Mark Zuckerburg, and Lady Gaga."
    
    q "Who's Mark Zuckerburg?"
    
    na "You seriously don't know?"
    
    show alexis worried
    
    q "It sounds familiar, sorry..."
    
    na "He was the first man on the moon, how could you not know him?"
    
    q "First man on the moon - "
    
    show alexis surprised
    
    q "No wait, are you sure...?"
    
    na "I was kidding."
    
    na "Mark Zuckerburg was the guy who invented Facebook."
    
    show alexis smiling
    
    q "Oh, that guy!"
    
    q "My father was talking about him."
    
    q "He said that I shouldn't follow his example."
    
    na "Of what, dropping out?"
    
    show alexis thinking
    
    q "Yes. He said I wasn't smart as smart as him."
    
    na "Anyone who carries around a sketchbook like that a freaking genius."
        
    q "What do you mean?"
    
    na "Well..."
    
    na "You sit down in the middle of everyone, and you can concentrate enough to sketch a full drawing..."
    
    na "I could never do it."
    
    show alexis smiling
    
    q "Anyone can learn to draw, if they practiced." 
    
    na "It's not a matter of practice."
    
    na "You pick anyone off the street and they can memorise a textbook, no problem."
    
    na "But it takes the chosen ones to have true talent."
    
    show alexis determined
    
    q "That's not true."
   
    q "I don't think I'm especially talented."
    
    q "So I have to keep working hard."
    
    na "No, you're definitely special."
    
    na "You know how I know?"
    
    show alexis smiling
    
    q "How?"
    
    na "Your eyes." 
    
    na "They're the eyes of a chosen one."
    
    show alexis surprised
    
    q "Chosen one?"
    
    show alexis smiling
    
    na "{color=#10a0e3}(She giggles at that one.){/color}"
    
    na "{color=#10a0e3}(She's beginning to let more of her show.){/color}"
    
    q "My father says it's just pigments."
    
    na "Pigments that are a one in a million."
    
    q "We're all special in our own way."
    
    na "Yeah, now that you mention it, I'm a pretty big deal myself."
    
    q "Oh?"
    
    na "{color=#10a0e3}(I slip my hand out of my pocket and showed it to her.){/color}"
    
    na "{color=#10a0e3}(Normally, I would be embarassed to show it to anyone, but this girl could accept anything.){/color}"
    
    na "{color=#10a0e3}(On the back of my right hand, is a dark birthmark in the shape of a star.){/color}"
    
    na "People ask me if this was a tattoo, or was drawn on."
    
    na "I was born with this."
    
    show alexis surprised
    
    q "Is that a comet?"
    
    q "It's beautiful."
    
    na "You can touch it if you want."
    
    show alexis smiling
    
    na "{color=#10a0e3}(She giggles again.){/color}"
    
    q "You seem really proud of it."
    
    na "Of I am!"
    
    na "No one else in the entire world has a mark like this one."
    
    na "{color=#10a0e3}(My brain moves on autopilot.){/color}"
    
    na "{color=#10a0e3}(Just an hour earlier I never would have dreamed of saying this.){/color}"
    
    na "{color=#10a0e3}(But right now, I'm never so sure of anything else in my life.){/color}"
    
    na "{color=#10a0e3}(I square my shoulders and look her dead in the eye.){/color}"
    
    na "I didn't get your name."
    
    a "It's Alexis."
    
    a "And yours?"
    
    na "I'm Zack."
    
    n "I could imagine the scene as clear as day."
    
    n "The two of us, perched on either side of a desk, our heads bent over our work."
    
    n "No different than what my life usually was - no, that was definitely different."
    
    n "Because, anytime, I could always could look up and watch those violet eyes stare into worlds unknown.."
    
    na "Alexis, let's meet up to study tomorrow."
    
    show alexis surprised
    
    a "..."
    
    a "You need help on your exams?"
    
    na "Not really."
    
    na"I just think two geniuses can work wonders when they crack their heads together."
    
    show alexis smiling
    
    na "{color=#10a0e3}(My heart doesn't even skip a beat.){/color}"

    na "{color=#10a0e3}(Because I already know the words that would come out of her mouth.){/color}"
    
    a "Sure! Why don't we - {nw}"
    
    nvl clear
    
    # train screeches
    
    #screen goes dark

label trainCrash:
    stop music
    
    stop looper
    
    scene black
    
    play sound crash fadeout 2
    
    $ renpy.pause(7.0, hard=True)
    
    play sound wind loop fadein 1
    
    scene trainMiddleHorror with fade
    
    n "She said nothing."
    
    show trainMiddleHorror with redFlash
    
    n "With the corpses around her, she looked at me and said nothing."
    
    show trainMiddleHorror with redFlash
    
    n "And then I found myself falling to the floor."
    
    show trainMiddleHorror with redFlash
    
    n "My face rested against a dying man's."
    
    n "With his last breath, he cursed me."
    
    n "This wasn't my fault."
    
    n "How could I have done anything - {nw} "
    
    stop sound
    
    nvl clear
    
    #flash
    
    show black with quickFlash
    
    na "Gaaarrggh!"
    
    n "What -"
    
    n "Where am I - "
    
    a "..."
    
    nvl clear
    
    show trainside with quickFlash
    
    n "I'm on the ground."
    
    n "We've...stopped?"
    
    a "..."
    
    na "{color=#10a0e3}(Is she okay?){/color}"
    
    na "{color=#10a0e3}(Ouch...){/color}"
    
    na "{color=#10a0e3}(I think my tailbone's going to need a massage after this..){/color}"
    
    nvl clear
    
    a "..."
    
    hide alexis
    
    n "Calm down."
    
    n "At first I thought it was a train crash, the way were were thrown..."
    
    n "But it can't be."
    
    n "I know people were complaining at the breakdowns recently, so this is just another one."
    
    n "Couldn't they have stopped above ground at least?"
    
    n "I can't see anything outside."
    
    nvl clear
        
    n "No, wait..."
    
    n "Actually, this is the perfect opportunity."
    
    n "I heard girls got scared easily when it came to situations like this."
    
    n "If the only other person close to them at the moment was a guy, then..."
    
    n "They called this the suspension bridge effect."
    
    n "Alright. The gloves are coming off."
    
    nvl clear
    
    na "Alexis, are you okay?"
    
    show alexis thinking with dissolve
    
    na "Are you hurt anywhere?"
    
    a "..."
    
    na "Don't worry. I'm sure we'll start moving again soon."
    
    a "..."
    
    na "{color=#10a0e3}(She seems more shellshocked than I expected.){/color}"
    
    na "{color=#10a0e3}(Does she have a fear of these sort of situations?){/color}"
    
    na "Well..."
    
    na "Shall we take a seat, first?"
    
    show alexis determined
    
    a "..."
    
    a "No."
    
    a "We can't wait."
    
    na "What?"

    a "We have to get off this train."
    
    na "{color=#10a0e3}(Was it my imagination, or did her voice come out huskier?){/color}"
    
    na "{color=#10a0e3}(As if she was channeling the spirit of herself ten years older.){/color}"
    
    na "Look, Alexis, calm down."
    
    na "Where is there for us to go? We're in the middle of the tunnel."
    
    na "Let's wait for help to arrive."
    
    show alexis thinking
    
    a "There should be an emergency exit at the end of the train."
    
    a "Let's head there."
    
    hide alexis with dissolve
    
    play sound footsteps
    
    na "{color=#10a0e3}(Without warning, she brushed past me and started moving down the carriage.){/color}"
    
    na "{color=#10a0e3}(Man, she must be terrified of her wits.){/color}"
    
    n "..."
    
    n "What am I still thinking, this isn't good!"
    
    n "If she's still scared, that means I'm not doing my job!"
    
    n "Man up, man up!"
    
    nvl clear
    
    na "{color=#10a0e3}(I quickly dart up to walk in front of her)."
    
    na "{color=#10a0e3}(It's gonna be a long walk to the end.){/color}"
    
    play sound footsteps

    
    scene trainDoor with wipeleft
    
    $renpy.pause(2, True)
    
    play sound  footsteps
    
    scene trainSide with wipeleft
    
    $renpy.pause(1, True)

    
    n "We had gotten on the train in the exact middle carriage, which meant that both ends of the train were equally as far from us."
    
    n "I noticed Alexis was heading towards the back of the train, not towards the front."
    
    n "Which was weird, because the driver of the train was located at the front. If anything, asking him for a help would be more sensible, instead of panicking and straight away opening the emergency exit at the back."
    
    play sound static
    
    i "{cps=*0.5} Dear...passengers. {/cps}"
    
    play sound static
    
    i "{cps=*0.5} The train...is experiencing...a momentary delay.  {/cps}" 
    play sound static
    
    i "{cps=*0.5} Please...remain in your...seats... {/cps}"
    play sound static
    
    i "{cps=*0.5} The train...will resume...shortly  {/cps}"
    
    nvl clear
    
    na "You hear that?"

    na "We'll be back running in no time."
    
    show alexis thinking
    
    a "..."
    
    show alexis determined
    
    a "Don't trust him."
    
    na "What? Don't trust who?"
    
    a "The conductor."
    
    a "We'll be safe if we get off this train."
    
    na "I don't get what you mean."
    
    show alexis thinking
    
    n "She just continues to march forward."
    
    nvl clear
    
    play sound footsteps
    
    scene trainDoor with wipeleft
    
    $renpy.pause(2, True)
    
    play sound footsteps
    
    scene trainSide with wipeleft
    
    $renpy.pause(1, True)
    
    n "Now we're in the last carriage."
    
    scene emergency with dissolve
    
    n "Only the emergency exit lies before us."
    
    n "Does she really expect us to go out there, in the dark?"
        
    show alexis determined
    
    na "{color=#10a0e3}(She steps forward to pull it open.){/color}"
    
    nvl clear
    
    #shudder
    
    play sound thud
    
    scene emergency with hpunch
    
    na "{color=#10a0e3}(The door opens a single centimeter before jerking to a stop.){/color}"
    
    show alexis worried
    
    a "..."
    
    a "I should have known."
    
    na "It's stuck?"
    
    na "Let me try!"
    
    play sound thud
    
    queue sound thud
    
    scene emergency with hpunch
    
    na "{color=#10a0e3}(I overexaggerate my attempts at first, huffing and puffing like a true man would.){/color}"
    
    na "{color=#10a0e3}(But even when I genuinely give it my best, the door wouldn't budge.){/color}"
    
    na "{color=#10a0e3}(Isn't the emergency exit supposed to be easy to open?){/color}"
    
    na "{color=#10a0e3}(Good thing there wasn't really an emergency, else we would be pounding on the doors now yelling to be let out.){/color}"

    na "{color=#10a0e3}(...){/color}"

    scene trainSide with wiperight
    
    a "The tracks are the same..." 
    
    a "If this is point C, then...."
    
    na "{color=#10a0e3}(Muttering to herself, she turns around and begins examining the train.){/color}"
    
    na "{color=#10a0e3}(This daydream of hers isn't  so cute anymore.){/color}"

    na "{color=#10a0e3}(If anything, it's getting a little creepy.){/color}"

    a "The first panel...no, the second..."
    
    na "What are you doing?"
    
    a "...."
    
    show alexis thinking
    
    a "I'm looking for a tool to open the exit."
    
    a "There's a screw wedged in there that's blocking the opening mechanism."
    
    a "We can use the spare pole located under one of those seats."
    
    na "{color=#10a0e3}(...How does she know that?){/color}"
    
    na "{color=#10a0e3}(All with one glance?){/color}"
    
    show alexis determined
    
    a "Are you satisfied?"
    
    a "Please move."
    
    show alexis thinking
    
    na "{color=#10a0e3}(She looks away and brushes past me.){/color}"
    
    na "{color=#10a0e3}(Forcefully, like you would strike one of the handles dangling on the ceiling."
    
    scene trainSide with hpunch
    
    na "Alexis!"
    
    n "My voice comes out desperate."
        
    n "I was beginning to realise that the only one afraid here, was me."
        
    n "I'm not scared of the train. Any moment, it would start up again and bring us to our destination."
    
    n "The only thing that terrifies me, is her glassy eyes."
    
    n "But even then..."

    n "She doesn't even turn my head at my cry."
    
    nvl clear
    
    play music dread loop fadein 1.0 fadeout 1.0
    
    hide alexis with dissolve
    
    n "To her, I might as well not exist."
    
    n "Was it because I didn't help her up in the beginning?"
    
    n "Because I had the audacity to ask her out?"

    n "Because I had on purpose given her that disgusting candy?"
    
    nvl clear
    
    n "In school, if you were furious at someone, absolutely mad..."
    
    n "You would ignore them."
    
    n "For that was the cruelest thing."
    
    n "And she's dead set on inflicting as much pain as possible."
    
    n "What did I do to her...?"

    nvl clear
    
    n "..."
    
    n "Calm down."
    
    n "Just have to control it and calm down."
    
    n "..."
    
    n "Oh, that's right!"
    
    nvl clear
    
    scene trainDoor with wipeleft
    
    n "In every carriage, there's an emergency communication button."
    
    n "You simply press the red button, and you can contact the driver directly through an intercom."
    
    n "Alexis must have been so lost in her own world she must have forgotten about it."
    
    n "I could just contact the driver and let him explain the whole situation."
    
    nvl clear
    
    n "Yes..."
    
    n "Will that finally paint me as worthy in her eyes?"
    
    nvl clear
    play sound static
    
    
    i "{color=#10a0e3}(*Bzzzt*){/color}"
    
    na "Hello? Is this the driver?"
    
    play sound static

    
    i "..."
    
    na "Hello? Can you hear me?"
    
    play sound static
    
    i "..."
    
    n "Was the intercom not working?"
    
    n "No, that wasn't possible. I had heard the beep indicating that my voice was live."
    
    n "My voice was being transmitted in the driver's cabin now, but no one was listening."
    
    n "Wasn't he there just a few minutes ago, giving that announcement?"
    
    n "Had he left the cabin for some reason?"
    
    nvl clear
    
    n "I peered into the carriages ahead, trying to see if the driver's room was visible from here."
        
    n "But the handles and doors and seats meshed together into one unrecognisable jungle gym, such that anything past the third carriage could have been easily hidden."
    
    n "As I craned my head trying to get a better view, my heart froze ice cold."
    
    nvl clear
    

    
    scene trainMiddle with dissolve
    
    n "It was the first time I had properly looked behind us."

    n "And it was only now did I see that the insides of the train were completely bare."
    
    n "No driver, no passengers, no people, nothing."
    
    n "You'd expect at least one or two passengers to be in the other carriages, right?!"
    
    n "It wasn't as if this was 10pm in the middle of the night."
    
    nvl clear
    
    n "Did we really board the train with no one else but ourselves?"      
    
    n "That was extremely unlikely. Maybe there had been passengers, but they had disappeared somewhere else."
    
    n "...but all of them, all at once?"
    
    n "And where would they have gone?"
    
    n "If they had rushed towards the emergency exit as well, like Alexis was trying to do, did that mean that she was right?"
    
    n "That we needed to get off at soon as possible?"
    
    nvl clear 
    
    n "I've read it in the news before."
    
    n "There's some terroist group lately...they've been threatening to bomb public places over the internet."
    
    n "No driver...train malfunction...what else could this be?"
    
    nvl clear
    
    n "No..."
    
    n "That's too unreal."
    
    n "That would never happen."
    
    n "If it really was a terrorist attack, where aren't there more gunshots?"
    
    n "Why leave us alone for so long?"
    
    nvl clear
    
    #Howard appears
    
    show howard close1 with dissolve
    
    na "...?"
    
    na "{color=#10a0e3}(There's someone there!){/color}"
    
    na "{color=#10a0e3}(Standing dead center in the middle of the train.){/color}"
    
    na "Hello?" 
    
    na "{color=#10a0e3}(Does he even hear me?){/color}"
    
    na "{color=#10a0e3}(He's probably too far away.){/color}"
    
    na "{color=#10a0e3}(Thank goodness there was another passenger after all.){/color}"
    
    scene trainSide with wipeleft
    
    na "Alexis, there's someone!"
    
    show alexis surprised with dissolve
    
    a "..."

    show alexis angry
    
    a "Close the door."
    
    a "Now."
    
    na "..What?"
    
    scene trainMiddle with wiperight
    
    stop music 
    
    show howard close2
    
    na "{color=#10a0e3}(Is it my imagination...){/color}"
    
    na "{color=#10a0e3}(Or is he a lot closer now?){/color}"
    
    na "{color=#10a0e3}(Almost as if...){/color}"
    
    na "{color=#10a0e3}(He's running.){/color}"
   
    na "{color=#10a0e3}(Towards us.){/color}"
    
    play sound thud 
    
    play music horror loop fadein 1.0 fadeout 1.0
    
    na "{color=#10a0e3}(The clang behind me jumpstarts my heart){/color}"
    
    scene emergency with slideleft
    
    show alexis determined
    
    na "{color=#10a0e3}(Alexis is crouched by the handle, and is sticking some sort of metal pole in the gap between the door.)"
    
    na "{color=#10a0e3}(One of the panels to the seats lies torn open beside her. Had she gotten the pole from there?){/color}"
    
    na "{color=#10a0e3}(Her whole body is arched like a frenzied cat.){/color}"
    
    na "{color=#10a0e3}(As if she's trying to claw her way out from something.){/color}"
    
    scene emergency with hpunch
    
    show alexis angry
    
    a "Close the fucking door!"
    
    scene trainMiddle with slideright
    
    show howard close3
        
    na "{color=#10a0e3}(Hey, hey...){/color}"
    
    na "{color=#10a0e3}(Who is that?){/color}"
    
    na "{color=#10a0e3}(He doesn't look like a passenger.){/color}"
    
    na "{color=#10a0e3}(Or a driver.){/color}"
    
    na "{color=#10a0e3}(I have to call someone.){/color}"
    
    na "{color=#10a0e3}(They'll know what to do.){/color}"
    
    show trainDoor with dissolve
    
    play sound static
        
    i "*bzzt"
    
    na "Excuse me."
   
    na "There's a strange man on board the train."
    
    #Howard moves
    
    scene trainMiddleHoward with dissolve
    
    show howard close4 with dissolve

    
    play sound static
        
    i "*bzzt"
    play sound static
    
    i "{cps=*0.5}...ac.......{/cps}"
        
    i "{cps=*0.5}bla.....ki....{/cps}"
    play sound static
    
    scene trainMiddleHoward
    
    show howard close4 with redFlash

    
    na "{color=#10a0e3}(Was the intercom damaged?){/color}"
    
    play sound static
    
    i "{cps=*0.5}Hail.......ack......{/cps}"
    
    na "{color=#10a0e3}(The door won't do any good, won't it?){/color}"
    
    na "{color=#10a0e3}(The way it was moving.){/color}"
    
    na "{color=#10a0e3}(It wasn't going to stop until it got my hands on me.){/color}"
    
    na "{color=#10a0e3}(And it has){/color}"

    na "{color=#10a0e3}(jaws.){/color}"
    play sound static
    
    i "{cps=*0.5}Hail...bla...King...{/cps}"
    
    show howardclose5 with redFlash
    
    play sound static
    
    i "{cps=*0.5}Hail...the Black King...{/cps}"
    
    #flashes of the devestation
    play sound static
    
    scene trainMiddleHorror with redFlash
    
    $ renpy.pause(0.5, True)
    
    scene trainMiddleHoward 
    
    show howard close5 with redFlash
    
    na "{color=#10a0e3}(Alexis was right){/color}"
    
    na "{color=#10a0e3}(Staying on this train, meant death.){/color}"
    scene trainDoor
    
    play sound thud
    
    na "{color=#10a0e3}(I've shut the door...){/color}"
    
    na "{color=#10a0e3}(But there's no lock.){/color}"
    
    scene trainDoorHoward with dissolve
    
    na "{color=#10a0e3}(It's looking at me.){/color}"
    
    na "{color=#10a0e3}(It whispers something..){/color}"
    
    na "{color=#10a0e3}(I summon all the strength I have to hold the door, but its grip is prying it open.){/color}"
    
    show trainDoorHoward with hpunch
    
    na "{color=#10a0e3}(It's going to rip open the door.){/color}"
    
    na "{color=#10a0e3}(I can hear its whispers.){/color}"
    
    na "{color=#10a0e3}(Two words, over, and over.){/color}"

    na "{color=#10a0e3}{cps=*0.5}(Black){/cps}{/color}{nw}"
    
    na "{color=#10a0e3}{cps=*0.5}(King){/cps}{/color}{nw}"
    
    scene trainDoorHoward with hpunch
    
    stop music
    
    play sound thud
    
    show alexis angry
    
    a "Run."
    
    n "I do what I'm told."
    
    show emergency with slideleft
    
    n "I pick up the rod that she had left behind."
    
    n "I pry open the door with the full brunt of my strength."
    
    play sound thud
    
    show emergency with hpunch
    
    $renpy.pause(0.5, True)
    
    show tunnel with dissolve
    
    play sound footstepsFast
    
    nvl clear
    
    n "And just like that..."
    
    n "I'm out in the open."
    
    n "Towards me is darkness."
    
    n "Behind me is madness."
    
    n "The last thing I want to do is turn around and look."
    
    nvl clear
    
    menu: 
    
        "Save Alexis.":
        
            n "I can't."
            
            n "I'm sorry."
        
        "Run away.":
            n "Not a single pause crosses my mind."
            
    nvl clear
    
    play sound footstepsGravelFast loop
        
    n "And I fly across the gravel."
    
    n "Letting the tracks be my only guide."
    
    nvl clear
    
    n "END OF DEMO"
    
    return
        
        
    
