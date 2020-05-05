﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define n = nvl_narrator
define na = Character("Zack")
define a = Character("Alexis")
define q = Character("???")
define p = Character("Police")

define i = Character("Intercom")

define crash = "sound/crash.wav"
define footstepsGraveLoop = "sound/footstepsGraveLoop.mp3"
define footsteps = "sound/footsteps.wav"
define thud = "sound/thud.wav"
define doorCloseTrain = "sound/doorCloseTrain.wav"
define pageTurn = "sound/pageTurn.wav"
define static = "sound/static.wav"

define ambientTrain = "sound/ambientTrain.wav"
define wind = "sound/wind.wav"
define stopTrain = "sound/stopTrain.wav"
define ambientStation = "sound/ambientStation.wav"

image alexis surprised = "Alexis/alexis_surprised.png"
image alexis angry = "Alexis/alexis_angry.png"
image alexis determined = "Alexis/alexis_determined.png"
image alexis sad = "Alexis/alexis_sad.png"
image alexis smiling = "Alexis/alexis_smiling.png"
image alexis thinking = "Alexis/alexis_thinking.png"
image alexis worried = "Alexis/alexis_worried.png"

image stationSide = "Bg/stationSide.jpg"
image trainSide = "Bg/trainSide.jpg"
image trainSideDreamy = "Bg/trainSideDreamy.jpg"
image trainSideHorror = "Bg/trainSideHorror.jpg"
image trainMiddle = "Bg/trainMiddle.jpg"
image tunnel = "Bg/tunnel.jpg"

define flash = Fade(1, 1, 1, color="#fff")
define redFlash = Fade(0.25, 0.25, 0.25, color="#8a0303")
image black = "#000"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    show alexis surprised
    
    na "This is a test."
        
    scene black 
    
    play sound wind loop fadein 1
    
    n "When trains are born, they have one function." 
    
    n "{vspace=50}They move from point A to point B."
    
    nvl clear
    
    n "{vspace=15}When millions of dollars construct one ten-carriage unit, there is one purpose."

    n "{vspace=15}They travel from point A to point B."
    
    n "{vspace=15}When placed on the rails and their wheels locked in, there is only one home for them."
    
    n "{vspace=15}The road that lies from point A to point B."
    
    nvl clear
    
    n "If a train were to rebel, it would be impossible."
    
    n "{vspace=15}There are laws in place."
    
    n "{vspace=15}The train can only move forward."
    
    n "{vspace=15}It cannot move left or right."
    
    n "{vspace=15}It cannot go past the end of the track."

    n "{vspace=15}It cannot remain in place or go too fast."
    
    nvl clear
    
    n "This is the existence of a train."
    
    n "{vspace=50}Point A. Point B."
    
    nvl clear
    
    #slow fade out
    
    n "A train cannot think, so it cannot feel the horror of this arrangement."
    
    n "{vspace=20}But if it did, I'm sure it would be screaming."
    
    n "{vspace=20}I'm sure it would fly off the tracks and crash through the tunnel."
    
    n "{vspace=20}Perhaps it would burst into the surface and face the blue sky."
    
    nvl clear
    
    n "Could it?"
    
    n "{vspace=20}There are laws in place, after all."
    
    nvl clear
    
    #slow fade out
    
    n "{vspace=50}But laws are made to be broken."
    
    nvl clear
    
    #scene of the devestation
    
    n "This is the carcass of a rebel."
    
    n "A once proud warrior stripped bare."
    
    n "Already, it's organs are failing."
    
    n "The occupants have long since descended into madness."
    
    n "My tongue comes out dry and my head like brass."
    
    nvl clear
    
    n "Behind me, a man succumbs."
    
    n "His limbs distort and he convulses to the ground."

    n "In front of me, the rest are trying to get the door open."
    
    n "Their hands pull until their fingers turn red, but the train fails them."
    
    n "A foot crushes my collarbone as someone throws himself against the windows."
    
    nvl clear
    
    n "Shocked by the pain, I remember how to move my leg again."
    
    n "My instinct alone plants me back on my feet."
    
    n "From here, I have a full view of the carnage before me."
    
    n "The dying and the desperate broiling against each other."
    
    n "The fire stroking out from beneath the ceiling."
    
    n "I have a full view of the carriage which dared fly too close to the sun."
    
    n "I have a full view of Hell."
    
    nvl clear 
    
    n "I can see her."
    
    n "Just the shape, hovering above the sea of corpses."
    
    n "She might have already left this world, but still."
    
    n "My legs turn, and they shuffle, and instead of fleeing I approach the carnage."
    
    n "The darkness begins to lift and I start to make out her dress."
    
    nvl clear
    
    n "Again, the two of us had arrived."
    
    n "{vspace=20}On the same road on the same track on the same route."
    
    n "{vspace=20}The beginning of the journey, and the end."
    
    n "{vspace=20}Point A..."
    
    nvl clear
    
    n "{vspace=50}...to Point B"
    
    stop sound
    
    nvl clear
    
    scene stationSide with flash
    #change scene 
    
    play sound ambientStation
    
    #Now we are in a brightly lit station
    
    n "Okay, maybe I gotta introduce myself first."
    
    n "My name is Zack, and I've just seventeen years old, halfway through high school." 
    
    n "Everyday I leave my house at eight o clock, catch the morning train and arrive only slightly late."
    
    n "My main subjects are Maths, Chemistry, and Physics."
    
    n "I listen to lectures for eight hours before I'm finally let off."
    
    nvl clear
    
    n "Sounds boring, doesn't it?"
    
    n "I'm sure if someone were to read a script of my life, he would fall asleep of boredom before the very end."
    
    n "But don't worry! The story's about to get interesting."
    
    n "I'm not going to be an ordinary high school student for the rest of my life! "
    
    n "Unlike my classmates, I'm always looking for interesting things to do. I'm not scared of treading off the beaten path."

    n "The other day, I stole a pencil from my teacher's desk when he wasn't looking."

    n "Okay, maybe that sounds a little lame. But I'm trying."
    
    nvl clear
    
    n "But today, any viewers tuning in are in for a treat."
    
    n "No joke, right now, my heart's pumping like crazy and I can't stop squeezing my fingers."
    
    n "Because, just two meters away from me, sitting on the next bench over, is her."
    
    n "Staring at something in the distance, past the barriers and through the apartment buildings that surround the station."
    
    n "Most people, when waiting for the train, would just keep their head down and stare into their phone, no?"
    
    n "But she's always like this, when she's resting. Just examining something that the rest of us can't fathom to see."
    
    nvl clear
    
    n "Okay, I probably sound like a stalker, but hear me out."
    
    n "It's not like I tracked her every move - but in a fancy school like mine, where everyone followed each other and no one stepped out of line..."
    
    n "It was impossible for her not to stand out."
    
    n "Most people moved around in groups, blending in with their banter and smiles, swinging their arms and telling jokes, always knee deep in the swing of things."
    
    n "But her? She wasn't concerned with anything like that."
    
    n "Her childish dress style, for one, stuck out like a sore thumb."
    
    n "Often, you could see her sitting alone at the cafeteria, sipping from a modest fruit juice packet, simply observing the world around her."
    
    n "Other times, she would carry this huge notebook around with her, and would spend a whole half hour in the same spot with her head bent down, scribbling something down for only her to see."
    
    nvl clear
    
    n "What was in that sketchbook?"
    
    n "That was one of the many questions I found swimming in my head when I caught sight of her."
    
    n "But most importantly, I wanted to know how she did it."
    
    n "How she managed to detach herself from the flow, and still remain calm about herself."
    
    n "The flow was a strange thing. When I started high school, I was swept up before I even realized it."
    
    n "Laughing at lame jokes, patting shoulders of people I didn't like."
    
    n "I even forced myself to learn soccer, just because all the other strong looking boys played."
    
    nvl clear
    
    n "But her? She had it all figured out, you could tell."
    
    n "I wanted to know her secret."
    
    n "In fact, I wanted to know everything about her."
    
    n "Now that I think about it, this is pretty much a confession of my feelings."
    
    n "Yeah, there's not denying it."
    
    n "I've fallen in love with her."
    
    nvl clear
    
    n "But, how do you even talk to girls?"
    
    n "That's something they never teach you in school."
    
    n "I know her, but I'm not sure if she knows me."
    
    n "If a random stranger suddenly comes up and tries to talk to you, wouldn't be weird as hell?"
    
    n "If it were me, and I was a girl...yeah, pretty sure I would be running for the nearest exit."
    
    nvl clear
    
    n "Okay. So what I need is some sort of excuse."
    
    n "..."
    
    n "Maybe I could drop my pen near me and pretend that it's hers..."
    
    n "..."
    
    n "Then how do I continue the conversation from there?!"
    
    n "I don't even know her name!"
    
    #*train comes*
    
    play sound stopTrain fadein 1.0
    
    n "Damn the train's coming!"
    
    n "I don't know which station she gets off."
    
    n "It could be a long journey, or she could be gone by next stop."
    
    n "No, never mind that, she's already moving inside."
    
    n "I have to follow her..."
    
    nvl clear
    
    stop sound
    
    show trainside
    
    play sound ambientTrain loop fadein 1.0
    
    n "...The train's empty."
    
    n "It's in the middle of the afternoon, after all, and all the adults are away."
    
    n "That means, of course, that I have to stand far away from her so I don't look weird."
    
    n "I was close to her when we entered the train, together, though."
    
    n "...she smelled nice."
    
    nvl clear
    
    n "This is driving me crazy."
    
    n "The next station's only three minutes, and she might get off!."
    
    n "This is the only chance I have."
    
    n "Her existence was like a dandelion in the wind - no, that's not entirely accurate."
    
    n "She's more like a lily in a pond."
    
    n "Always visible in the distance, but out of reach."
    
    n "It's only in this train when she's within my grasp."
    
    n "There's no time to think. No point in playing what might happen. I had to do it now or lose it forever."
    
    nvl clear
    
    n "So... I stood up, and approached her."
    
    #approach alexis
    
    show alexis thinking with fade
    
    $ renpy.pause(1.5, hard=True)
    
    nvl clear
    
    n "Her eyes..."
    
    n "I never thought that color could exist."
    
    nvl clear
    
    show alexis surprised
    
    na "..."
    
    a "..."
    
    na "..."
    
    n "She's inching away..."
    
    n "I have to open my mouth or I'll just be another creep!"
    
    nvl clear
    
    na "Which stop are you getting off at!"
    
    show alexis worried
    
    a "..."
    
    a "N-newton station."
    
    n "That's an obvious lie, Newton's in the complete opposite direction..."
    
    nvl clear
    
    na "Sorry, I don't mean to shout so loud, my voice is just like that, and the train's really echoey underground, so that adds to the volume, you know what I mean?"
    
    a "..."
    
    a "Yes."
    
    na "Um, anyway, um, right now I haven't eaten or drunk lately and I feel like I'm going to faint..."
    
    n "I'm not sure what's come over me, but I'm going to Hell for all the words that's spilling out of my mouth."
    
    n "There's nothing wrong with my body save my out of control beating heart."
        
    na "Do you have some Panadol? I'm not sure if - "
    
    show alexis surprised
    
    a "Oh yes! I have some right here. Is three tablets enough?"
    
    na "Yes, thank you so much!" 
    
    na "Mind if we sit down? It's getting a little blurry..."
    
    a "Oh!"
    
    a "Come on, here."
    
    #they sit down
    
    n "So it's not exactly the most ethical way to start a conversation, but it's working!"
    
    n "The best part is when I bow my head and suddenly act like I'm in great pain."
    
    n "She automatically moves in close to see what's wrong, and her soft hair tickles my arm."
    
    n "If I keep this charade up any longer, I may not be able to live with myself for a few weeks."
    
    n "I notice her sketchbook, the one in which she scribbles in all day, and it's poking out of her slingbag."
    
    nvl clear
    
    na "Hey, what's that inside your bag?"
    
    show alexis worried
    
    a "This? It's just a book."
    
    na "Mind if I have a look inside?"
    
    na "Sorry, it's just, I need something to focus on, or I'll really lose conscienceness."
    
    a "Really?! Should I call an ambulance?"
    
    na "No, no, just reading something is okay. It's called a grounding technique, my doctor taught me that."
    
    na "Even if you have just doodles written down, just looking at them will help."
    
    n "She actually believed that?!"
    
    n "Like taking candy from a baby, except the baby is turning out more and more to be the girl of my dreams..."
    
    n "That straightforward naviety of hers is so cute, it's maddening."
    
    nvl clear
    
    #flips through sketchbook
    
    a "Erm...is it okay if you only see the first few pages?"
    
    n "Is she embarassed?"
    
    n "These drawings of hers are really, really good though."
    
    n "I don't know how many flavours of 'punk' there are apart from steampunk or cyberpunk, but she's all the science fiction styles down."
    
    n "Buildings, cities, skyscrapers, a few rough sketches of characters, all dressed up in their own unique style."
    
    n "There's no way single person in the entire school would even think of drawing something like this."
    
    nvl clear
    
    na "This is amazing."
    
    na "Where did you learn all this?"
    
    show alexis smiling
    
    a "I'm happy you like it."
    
    a "My dad was a painter, so I just learned from him."
    
    na "This is seriously Picasso tier."
    
    na "You could earn millions from this!"
    
    show alexis surprised
    
    a "Nononono, no one would buy these!"
    
    n "I was exaggerating, of course, but I'd heard overcompliments are the best way to a girl's heart."
        
    na "And what are these?"
    
    hide alexis with fade
    
    n "A few pages on, the fantastical drawings ceased, and more mundane everyday sketches emerged."
    
    n "Most of them were random places around the city."
       
    nvl clear 
    #time passes
    
    #background 1
    na "(*flip)"

    #background 2 
    
    na "(*flip)"
    
    
    show alexis worried with fade
    
    a "Sorry, do you dislike them?"
    
    a "I make it a schedule to draw from real life reference every few weeks."
    
    a "My father always said that I needed to branch out into other styles, so I can find something I'm can really specialize in."
    
    na "If you want my take on it, anybody can draw anything from real life."
    
    na "But it takes true talent to draw from imagination."
    
    na "Your first few drawings are the best ones, you should focus on those."
    
    show alexis smiling
    
    n "She looked at me as if she would a lighthouse in the middle of a stormy sea, and I inwardly cheered."
    
    n "And to think I made that piece of advice up on the spot!"
    
    nvl clear 
    
    #time passes
    
    hide alexis
    
    n "The train cruised on."
    
    nvl clear
    
    #background
    
    n "The windows flashed black, as we hurtled along the endless tunnel."
    
    #background
    nvl clear
    
    n "The engine hummed around us, the melody reaching deep into my heart and rattling my bones."
    
    nvl clear
    
    show alexis smiling
    
    a "...A concept artist would be really hard. Everyone wants to be one. Some people work for ten years before they finally get that position."
    
    na "A concept artist? You mean, like for a movie?"
    
    a "Movies are great, but they're too competitive. I'm thinking maybe for a video game studio."
    
    na "Ubisoft! Or Blizzard!"
    
    show alexis worried
    
    a "Those companies are competitive too! I won't get in."
    
    show alexis thinking
    
    a "Maybe in a small studio..."
    
    na "Let me tell you something."
    
    na "You should drop out of school and send your drawings to Ubisoft right now."
    
    show alexis surprised
    
    a "I told you, I won't get it!"
    
    show alexis determined
    
    a "I'm going to an art university after this."
    
    na "You sure you're going to need it?" 
    
    a "Big companies require a university education!"
    
    na "Eh, degrees are overated."
    
    na "Did you know Steve Jobs dropped out of college?"
    
    show alexis surprised
    
    a "Oh, really?!" 
    
    na "Yeah, also Mark Zuckerburg, and Lady Gaga."
    
    a "Who's Mark Zuckerburg?"
    
    na "You seriously don't know?"
    
    show alexis worried
    
    a "It sounds familiar, sorry..."
    
    na "He was the first man on the moon, how could you not know him?"
    
    a "First man on the moon - "
    
    show alexis surprised
    
    a "No wait, are you sure...?"
    
    na "I was kidding."
    
    na "Mark Zuckerburg was the guy who invented Facebook."
    
    show alexis smiling
    
    a "Oh, that guy!"
    
    a "My father was talking about him."
    
    a "He said that I shouldn't follow his example."
    
    na "Of what, dropping out?"
    
    show alexis thinking
    
    a "Yes. He said I wasn't smart enough."
    
    na "Anyone who carries around a sketchbook like that a freaking genius."
        
    a "What do you mean?"
    
    na "Well..."
    
    na "You sit down in the middle of everyone, and you can concentrate enough to sketch a full drawing..."
    
    na "I could never do it."
    
    show alexis smiling
    
    a "Anyone can learn to draw, if they practiced." 
    
    na "It's not a matter of practice."
    
    na "It's about...I mean, we're at school, aren't we? Doing our maths and science and studying to become the nation's next greatest doctors."
    
    na "So...it's not a matter of whether I start drawing or not, in the end it won't matter, right?"
    
    a "I get what you mean."
    
    show alexis determined
    
    a "But art is like that."
    
    a "You have to make sacrifices."
    
    a "I don't think I'm especially talented."
    
    a "So I have to keep working hard."
    
    na "No, you're definitely special."
    
    na "You know how I know?"
    
    show alexis smiling
    
    a "How?"
    
    na "Your eyes." 
    
    na "They're the eyes of a chosen one."
    
    show alexis surprised
    
    a "Chosen one?"
    
    show alexis smiling
    
    na "(She giggled at that one.)"
    
    na "(She was beginning to let more of her show.)"
    
    a "My father says it's just pigments."
    
    na "Pigments that are a one in a million."
    
    a "We're all special in our own way."
    
    na "Yeah, now that you mention it, I'm a pretty big deal myself."
    
    a "Oh?"
    
    na "(I slipped my hand out of my pocket and showed it to her.)"
    
    na "(Normally, I would be embarassed to show it to anyone, but this girl could accept anything.)"
    
    na "(On the back of my right hand, was a dark birthmark in the shape of a star.)"
    
    na "People ask me if this was a tattoo, or was drawn on."
    
    na "I was born with this."
    
    show alexis surprised
    
    a "Is that a comet?"
    
    a "It's beautiful."
    
    na "You can touch it if you want."
    
    show alexis smiling
    
    na "(She giggled again.)"
    
    a "You seem really proud of it."
    
    na "There has to be a reason why God marked me this way, you know?"
    
    na "Just the same way he marked you."
    
    na "So don't count yourself out. You're definitely special."
    
    a "And so are you!"
    
    na "(My brain moved on autopilot.)"
    
    na "(Just an hour earlier I never would have dreamed of saying this.)"
    
    na "(But right now, I was never so sure of anything else in my life.)"
    
    na "(I squared my shoulders and looked her dead in the eye.)"
    
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
    
    na"I just think two special people can work wonders when they crack their heads together."
    
    show alexis smiling
    
    na "(My heart didn't even skip a beat at that.)"

    na "(Because I already knew the words that would come out of her mouth.)"
    
    a "Sure! Why don't we - {nw}"
    
    nvl clear
    
    # train screeches
    
    #screen goes dark

label trainCrash:
    
    scene black
    
    play sound crash fadeout 1
    
    $ renpy.pause(7.0, hard=True)
    
    play sound wind loop fadein 1
    
    n "Panic."
    
    show black with redFlash
    
    n "Terror."
    
    show black with redFlash
    
    n "Despair."
    
    show black with redFlash
    
    n "The ugly and the desperate clawing for their lives."
        
    n "I could see it all."
    
    n "Standing up with my flayed skin dangling down, I could believe."
    
    n "That in this world, there was a Hell on Earth - "
    
    stop sound
    
    nvl clear
    
    #flash
    
    na "Gaaarrggh!"
    
    n "What -"
    
    n "Where am I - "
    
    a "..."
    
    nvl clear
    
    show trainside
    
    n "The train..."
    
    n "it's not moving anymore."
    
    n "I'm on the ground."
    
    n "That means the train must stopped so hard I was sent flying."
    
    a ",,,"
    
    n "Alexis...it looks like she was roughed up a bit too."
    
    nvl clear
    
    a "..."
    
    n "These stupid trains."
    
    n "I know people were complaining at the breakdowns recently, but it was just ridiculous."
    
    n "What if I, or Alexis, had gotten seriously hurt?"
    
    n "Without thinking my fist slammed into the pole next to me."
    
    nvl clear
        
    n "No, wait..."
    
    n "If I calmed down enough to think about it, this was the perfect opportunity."
    
    n "I heard girls got scared easily when it came to situations like this."
    
    n "If the only other person close to them at the moment was a guy, then..."
    
    n "They called this the suspension bridge effect."
    
    n "Alright. The gloves are coming off."
    
    n "Playing Mr Hero shouldn't be too hard, especially if it's with a girl like her."
    
    nvl clear
    
    na "Alexis, are you okay?"
    
    show alexis thinking with fade
    
    na "Are you hurt anywhere?"
    
    a "..."
    
    na "Don't worry. I'm sure they'll get us out soon."
    
    a "..."
    
    na "(She seems more shellshocked than I expected.)"
    
    na "(Does she have a fear of these sort of situations?)"
    
    na "Well, there's point in standing around."
    
    na "Let's just have a seat and wait for them to arrive."
    
    show alexis determined
    
    a "..."
    
    a "No."
    
    a "We can't wait."
    
    na "What?"

    a "We have to get out of this tunnel."
    
    na "(Was it my imagination, or was her voice coming out huskier?)"
    
    na "(As if she had aged ten years in a single instant, such was the seriousness of her tone.)"
    
    na "Look, Alexis, calm down."
    
    na "Where is there for us to go? We're in the middle of the tunnel."
    
    na "Let's wait for help to arrive."
    
    show alexis thinking
    
    a "There should be an emergency exit at the end of the train."
    
    a "Let's head there."
    
    hide alexis with fade
    
    na "(Without warning, she brushed past me and started moving down the carriage.)"
    
    na "(Man, she must be terrified of her wits.)"
    
    n "..."
    
    n "What am I still thinking, this isn't good!"
    
    n "If she's still scared, that means I'm not doing my job!"
    
    n "Man up, man up!"
    
    nvl clear
    
    na "(I quickly darted up to walk in front of her)."
    
    na "It's gonna be a long walk to the end."
    
    n "We had gotten on the train in the exact middle carriage, which meant that both ends of the train were equally as far from us."
    
    n "I noticed Alexis was heading towards the back of the train, not towards the front."
    
    n "Which was weird, because the driver of the train was located at the front. If anything, asking him for a help would be more sensible, instead of panicking and straight away opening the emergency exit at the back."
    
    n " I was debating how to tell her this, but then conveniently the intercom above us started to speak."
    
    nvl clear
    
    i "{cps=*0.7} Dear...passengers. {/cps}"
    
    i "{cps=*0.7} The train...is experiencing...a momentary delay.  {/cps}" 
    
    i "{cps=*0.7} Please...remain in your...seats... {/cps}"
    
    i "{cps=*0.7} The train...will resume...shortly  {/cps}"
    
    na "See, There's nothing to worry about."
    
    show alexis thinking
    
    a "..."
    
    show alexis determined
    
    a "Don't trust him."
    
    na "What? Trust who?"
    
    a "The conductor."
    
    a "We'll be safe if we get off this train."
    
    na "I don't get what you mean."
    
    show alexis thinking
    
    n "She ignored that question and continued to march forward."
    
    hide alexis with fade
    
    n "What was wrong with her?"
    
    n "The other passengers in the train were probably sitting in their seats, obediently waiting for the crisis to resolve."
    
    n "But instead, we walked down the carriage like panicked idiots."
    
    n "We soon reached the door that divided this carriage from the next carriage."
    
    show alexis determined
    
    n "She stepped forward to pull it open."
    
    #shudder
    
    na "(The door opened a single centimeter before jerking to a stop.)"
    
    show alexis worried
    
    a "..."
    
    a "I should have known."
    
    na "It's stuck?"
    
    na "Let me try!"
    
    na "(I overexaggerated my attempts at first, huffing and puffing like a true man worked.)"
    
    na "(But even when I genuinely gave it my best, the door wouldn't budge.)"
    
    na "(Do train doors normally jam this badly?)"
    
    na "(It's the first time I've heard of this.)"
    
    show alexis thinking
    
    a "There should be a way to open it." 
    
    na "(Again, as if barely acknowledging my presence, she turn around and began examining the train.)"
    
    hide alexis with fade
    
    n "The air of the train was getting to me."
    
    n "All that action must have worked it up, because my mouth was dryer than the Sahara desert."
    
    n "So I stood there sweating my guts out, and watched Alexis rummage through the seats as if searching for a hidden pot of gold."
    
    n "Nothing about this situation made any sense."
    
    na "What are you doing?!"
    
    na "(My voice came out rougher than I intended.)"
    
    na "(And she didn't even bother to look around.)"
    
    show alexis thinking
    
    a "I'm looking for the fishing pole."
    
    na "What?"
    
    a "..."
    
    n "And apparently that didn't even deserve a reply."
    
    n "I had thought she was just scared, but I realised what she was really communicating was that she thought I was absolutely useless."
    
    n "What was the hurry, anyway?"
    
    n "She's just going off on her own..."
    
    n "For the first time, her purple expression sparked a new emotion in me."
    
    n "Confusion."
    
    hide alexis with fade
    
    nvl clear
    
    n "..."
    
    n "Calm down."
    
    n "Just have to control it and calm down."
    
    n "..."
    
    n "Oh, that's right!"
    
    nvl clear
    
    n "In every carriage, there's an emergency communication button."
    
    n "You simply press the red button, and you can contact the driver directly through an intercom."
    
    n "Alexis must have been so lost in her own world she must have forgotten about it."
    
    n "I could just contact the driver and let him explain the whole situation."
    
    nvl clear
    
    na "(I pressed the button firmly, and spoke clearly into the microphone.)"
    
    na "Hello? Is this the driver?"
    
    i "..."
    
    na "Hello? Can you hear me?"
    
    i "..."
    
    n "Was the intercom not working?"
    
    n "No, that wasn't possible. I had heard the beep indicating that my voice was live."
    
    n "My voice was being transmitted in the driver's cabin now, but no one was listening."
    
    n "Wasn't he there just a few minutes ago, giving that announcement?"
    
    n "Had he left the cabin for some reason?"
    
    nvl clear
    
    n "I peered into the carriages ahead, trying to see if the driver's room was visible from here."
    
    n "But the handles and doors and seats meshed together into one unrecognisable jungle gym, such that anything past the third carriage could have been easily hidden."
    
    n "As I craned my head trying to get a better view, the veins of my heart froze ice cold."
    
    nvl clear
    
    n "There was nothing in sight save for the insides of the train."
    
    n "No driver, no passengers, no people, nothing."
    
    n "You'd expect at least one or two passengers to be in the other carriages, right?!"
    
    n "It wasn't as if this was 10pm in the middle of the night?"
    
    nvl clear
    
    n "Did we really board the train with no one else but ourselves?"
    
    n "That was unextremely unlikely. Maybe there had been passengers, but they had disappeared somewhere else."
    
    n "That thought made something rise up in my throat, and I forced the sudden terror back down."
    
    n "I didn't want to think about where they had gone."
    
    n "If they had rushed towards the emergency exit as well, like Alexis was trying to do, did that mean that she was right?"
    
    n "That we needed to get off at soon as possible?"
    
    nvl clear 
    
    n "I've read in the news before."
    
    n "There's some terroist group lately...they've been threatening to bomb public places over the internet."
    
    n "No driver...train malfunction...what else could this be?"
    
    n "And why the fuck did they have to pick me of all people?"
    
    n "There's four million people in this city and I have to be the only unlucky one!"

    n "I'm a diligent student, I submit my homework most of the time, my parents are good people and I've always been nice to the people I meet..."
    
    n "Why only me?!"
    
    nvl clear
    
    n "The heat."
    
    n "It wraps around my face like a veil."
    
    n "I can't breathe."
    
    n "They shut the air conditioning off."
    
    n "The only oxygen flowing here is decades old."
    
    n "In the tunnel, untouched, alone, cut off from the sky above."
    
    nvl clear
    
    n "Unbelievable."
    
    n "Insane."
    
    n "And she just doesn't care."
    
    n "I'm dying in the middle of the underground and she doesn't give a shit!"
    
    nvl clear
    
    n "Before I know it, I'm standing over her."
    
    n "She's bending over the seats, her back to me, searching for something underneath."
    
    n "My hand found her shoulder, and squeezed it."
    
    nvl clear 
    
    n "She turned, and I imagined what she saw."
    
    n "A wild eyed, sweaty lunatic, panting so hard his spit was raining down."
    
    n "I expected her to recoil."
    
    n "At least, then, she would finally act human about the situation."
    
    n "But instead..."
    
    n "She regarded me, with that same cold, impassive gaze."
    
    nvl clear 
    
    show alexis determined with fade
    
    a "Don't get so excited."
    
    a "Were you always like this?"
    
    a "So jumpy?"
    
    na "You're not helping."
    
    na "Tell me exactly what's going on."
    
    a "I've been looking for a tool to help us open the door."

    na "(She held up a long metal rod.)"
    
    na "(I looked past her and saw an opened metal panel.)"

    na "(This must have been a storage compartment of this carriage. Inside was a few first aid kits and a few office appliances.)"
    
    na "(But how did she know it was going to be there?)"
    
    a "There's a few coins wedged in the bottom of the door."
    
    a "If I slide the rod in, I can - "
    
    # flash
    
    a "!"
    
    na "(What?)"
    
    na "(She was looking at something behind me.)"
    
    hide alexis with fade
    
    na "(Without warning she suddenly ran to the door - )"
    
    na "(No, she sprinted.)"
    
    na "(I looked in the direction she had been staring at, which was the train carriages towards the driver's cabin.)"
    
    n "The chaos of metal poles still remained undisturbed."
    
    n "The handles lay still and the seats empty."
    
    nvl clear
    
    n "..."
    
    nvl clear
    
    n "No, wait."
    
    show trainmiddle
    
    n "Something was moving through the carriages."
    
    n "No, it was someone."
    
    n "It was a tiny line of black from where I was sitting, but it was definitely a figure around human height. Maybe even slightly taller."
     
    n "That must be...the driver, right?"
    
    n "Who else could it be?"
    
    nvl clear
    
    na "(*ping)"
    
    na "(I turned to see Alexis bent over, panting, leaning the metal rod on the ground.)"
    
    na "Alexis, help's here - "
    
    show alexis angry 
    
    a "Don't!"
    
    a "Don't look at him. It'll encourage him."
    
    na "Who is he?"
    
    na "(*ping)"
    
    na "(She stood up, having finally managed to kick the rod into an l-shape.)"
    
    na "(Without hesitation, she stuck it in the gap of the door and began to heave.)"
    
    na "(...Was it my imagination, or did her movements seem a little more frantic now?)"
    
    na "(Almost as if...)"
    
    na "(She was afraid.)"
    
    hide alexis with fade
        
    n "It was closer now."
    
    n "In fact, the thin black line was growing bigger with alarming speed."
    
    n "It wasn't just moving towards us, I realised."
    
    nvl clear 
    
    n "It was running." 
    
    nvl clear
    
    na "(I didn't know what to do.)"
    
    na "(Alexis was hammering away at the door, her grunts mingling with the screech of steel.)"
    
    na "(In one final bid to regain some sanity, I went to the intercom once more.)"
    
    na "(I kept my eyes on the approaching figure, even as I depressed the button.)"
    
    na "Hello?"
        
    i "*bzzt"
    
    na "(It was only three carriages away now.)"
    
    na "Excuse me."
    
    na "(A door burst open - now it was two.)"
   
    na "There's a dangerous man on board the train."
    
    na "Can you call the police?"
    
    na "(The man could have just been a panicked passenger wanting to seek help, it was true.)"
    
    na "(But take a closer look and you would notice how its feet shuffled forward perfectly along the guided floor lines.)"
    
    na "(How its head bumped smoothly against the hanging handles without slowing down.)"
    
    na "(This man was running in a line that was perfectly straight.)"
    
    na "(As if he knew exactly where to to go.)"
    
    # flashes?
    
    na "(Something about terrified me.)"
    
    # flashes
    
    na "And the worst part was..."
    
    na "The man had fangs."
    
    na "I didn't know what was happening, but what jutted from his jaw were a wolf's fangs."
    
    i "*bzzt"
    
    na "(The intercom was breaking up.)"
    
    na "(Had the crash damaged some of its systems after all?)"
    
    i "...ac......."
    
    i "bla.....ki...."
    
    i "Hail.......ack......"
    
    na "(Another door thrown aside.)"
    
    na "(Only one single carriage seperated us from him.)"
    
    i "Hail...bla...King..."
    
    i "Hail...the Black King..."
    
    # more red flashes 

    na "Agghh...."
    
    na "Fuck..."
    
    na "Fuck this shit..."
    
    n "Alexis was still struggling with the door."
    
    n "Her skinny frame with her skeleton arms, trying to swing back the rod like a five year old kid."
    
    n "As if she fully expected she would be strong enough to pry open to our freedom."
        
    nvl clear
    
    na "Give it to me, Alexis."
    
    n "She didn't hear me - "

    n "No - she pretended not to hear me."
    
    n "I was sure."
    
    n "We were seconds away from what I was certain was the walking death, and she would rather ignore my entire existence that escape."
    
    nvl clear
    
    na "Give the rod to me."
    
    n "She swung it back instead, and it flew inches from my face."
    
    n "You can't be fucking serious."
    
    n "He's coming. He's already opening the last door."
    
    n "He's going to catch us."
    
    n "Stupid, stupid, fucking dumb, idiotic, brainless."
    
    n "It's because of this fucking girl."
    
    nvl clear
    
    n "I need to do some thing."
    
    n "It's hot, I'm sweating, it's dripping off my cheeks and he's coming."
    
    n "She's in my way."
    
    n "I need to - "
    
    nvl clear
    
    n "I need - "
    
    nvl clear
    
    menu: 
    
        "Slap her.":
            $ evil = "true"
        
        "Barricade the door.":
        
            n "I don't know why on earth the thought of physically harming her came to my mind."
            
            n "The heat of the train, the fear of our approaching doom, it's all gotten to me."
            
            n "There's no point to throw a tantrum. I should look for something to barricade the door." 
            
            nvl clear
            
            n "My mind thinks all this, and my body moves on its own."
            
    n "It was almost mechanical."

    n "A command was issued and my body carried it out."
    
    n "My hand swung back and slams into her face."
    
    nvl clear
    
    show alexis thinking
    
    n "The best part?"
    
    n "She didn't say a word."
    
    a "..."
    
    show alexis determined
    
    a "The same track..."
    
    na "(She mumbled something.)"
    
    a "It always travels on the same line."
    
    #switch view to approaching figure
    
    hide alexis
    
    na "(The final barrier protecting us slid open.)"
    
    na "(The smell of decay filled the carriage.)"
    
    na "(And the man with the head of the wolf finally came to claim us.)"
    
    show alexis thinking
    
    na "(Alexis had completely disappeared into another world.)"
    
    na "(Her iron rod lay at her side, and she stares our doom straight in the face.)"
    
    na "(Almost as if accepting it.)"
    
    hide alexis
    
    n "And me?"
    
    nvl clear
    
    n "I was filled with a rage as feral as the animal across me."
    
    n "Nothing made sense."
    
    n "The whole world was dragging me for a ride."
    
    n "The only thing my overloaded brain could want now..."
    
    n"...was blood."

    nvl clear

    na "(I grabbed the rod out of Alexis's hands.)"
    
    q "You..."
    
    q "You are the Black King..."
    
    n "And that was when I smacked that fuckhead right in his perfect teeth."
    
    nvl clear
    
    q "Gggglll!"
        
    na "(I stuck the rod in the crack of the door, and gave it one final pull.)"
    
    na "(The coin trapped in there shot out and bounced off the seats, landing near the foot of the groaning man on the floor.)"
    
    show alexis surprised
    
    na "(I threw the rod onto the floor, close enough to Alexis to make her jump.)"
    
    na "Let's fuck off."
    
    n "Like a bird with its wings newly freed..."
    
    n "I flew into the next carriage, panting like a mad dog."
    
    n "It's was a while before I realised Alexis isn't following me."
    
    nvl clear
    
    n "She stood framed in the doorway, her arms hanging by her sides."
    
    n "Before she had been passive, now, she just looked lost."
    
    n "The man behind her was still trying to get to his feet, but could rise up any moment."
    
    n "And yet, she stayed there, just staring at me."
    
    nvl clear
    
    na "What the fuck are you doing?"
    
    show alexis surprised
    
    $ renpy.pause(1, hard=True)
    
    show alexis worried
    
    $ renpy.pause(1, hard=True)
    
    show alexis sad
    
    $ renpy.pause(1, hard=True)
    
    na "(For a moment I forgot everything - the darkness, the heat, the howls of our pursuer.)"
    
    na "(All that was there was the look on her face.)"
    
    na "(Watery eyes that must have been at least a hundred years old.)"
    
    na "Come on!"
    
    na "Are you fucking deaf?!"
    
    na "(She leapt forward to join me, tears fleeing behind her."
    
    nvl clear
    
    n "Together we raced down the carriage."
    
    n "The emergency exit at the back was easy enough to open, and we spilled out into the dark tunnel."
    
    n "Ahead, the path was shrouded in darkness, a straight line leading into infinity."
    
    n "Still, we ran."
    
    n "Away from the safety of the train, straight towards the belly of the beast."
    
    nvl clear
    
    n "Our breaths came out ragged and our legs intertwined."
    
    n "At one point, our hands had touched and now we grasped one another like a lifeline." 
    
    n "We didn't look back, we didn't stop, we just ran."
    
    n "All that mattered was that we were moving."
    
label traintracks:
    
    nvl clear
      
    n "Only when the train was swallowed up completely by the trailing darkness, did we slow to a jog."
    
    nvl clear
    
    na "Alexis..."
    
    na "Does it..."
    
    na "Does it hurt?"
    
    show alexis smiling
    
    a "Does what hurt?"
    
    na "Your cheek..."
    
    na "I'm sorry...that I hit you..."
    
    show alexis thinking
    
    a "..."
    
    show alexis surprised
    
    a "What do you mean?"
    
    na "Huh?"
    
    a "And..."
    
    a "Um..."
    
    show alexis worried
    
    a "Sorry, I'm just very confused now."
    
    a "This might sound weird, but..."
    
    a "Why are we running again?"
    
    na "What?"
    
    a "I must have hit my head..."
    
    a "Something happened, right?"
    
    a "The last thing I remember was the train crashing."
    
    na "Are you for real?!"
    
    na "So... you don't remember anything?"
    
    na "About the train?"
    
    na "The door?"
    
    na "And the wolf man?"
    
    a "Wolf man?"
    
    a "Sorry, but I don't know what you mean by that."

    a "But I seem to remember something..."
    
    a "About getting to the exit."
    
    na "Okay..."
    
    na "You're not going to believe this."
    
    na "But first, let me check your head."
    
    show alexis smiling
    
    a "Alright."
    
    n "For an amnesiac, she seemed to have accepted this rather easily, which didn't improve the oddity of the situation, but I didn't care."
    
    n "Alexis was back, and once more I was her guardian."
    
    n "Using the flashlight from my phone, we both crouched down in the middle of the tracks, and I inspected the back of her head for damage."
    
    nvl clear
    
    na "Sorry, I'm going to brush your hair away now."
    
    a "It's okay. Tell me if it's bad."
    
    n "Her silky brown hair was soft to the touch, and I dared to use only my fingertips to peel away the strands to inspect her skull."
    
    n "No signs of blood or even dirt on her scalp."
    
    n "I wasn't expecting any, because I hadn't seen her hit her head at all back there."
    
    n "So, what then, had caused this sudden bout of amnesia?"
    
    hide alexis
    
    nvl clear
    
    n "This quiet, sweet girl with whom I had showed my birthmark to..."
    
    n "She ended up to be someone who was hiding many secrets."
    
    n "What was up with that sudden change of personality, after the train crash?"
    
    n "Why had she known so much about the situation?"
    
    n "Heck, she even knew that there was a coin stuck in the door? How does someone even deduce that without even a few minutes of inspection?"
    
    nvl clear
    
    n "And above all..."
    
    n "Why had she treated me like I wasn't even there?"
    
    n "Staring at the back of her skull now, I wondered what would be like I could peel apart the layers, reach in and grab all the answers floating around in her mind."
    
    nvl clear
    
    n "I remembered how I had drew back my hand..."
    
    n "And almost broke her face in two."
    
    n "All for the sake of gaining those very answers."
    
    n "What the hell had I been thinking, then?"
    
    nvl clear
    
    n "It was a good thing, then, that she didn't remember."
    
    n "I wouldn't have been able to face her."
    
    n "With my hands on her head, I swore, strapped over a lock on my heart, repeated a mantra to never, ever let my emotions get the better of me again."
    
    show alexis worried
    
    a "Zack? Is it that bad?"
    
    na "Ah, no, sorry."
    
    na "Looks like it's all in the clear."
    
    na "(Just as normalcy was returning, a footstep thudded in the darkness)."
    
    na "(A faint, soft sound, far away behind us)."
    
    na "(But it was a footstep all the same)."
    
    na "(Our pursuer wasn't giving up)."
    
    na "Shit, shit, shit..."
    
    a "Should we go?"
    
    a "Towards the exit?"
    
    na "Yeah."
    
    na "Let's move fast."
    
    na "Hold on to my hand and don't let go."
    
    n "We started running again, the light from my phone pointing the way."
    
    #running sounds?
    
    a "Huff...."
    
    n "After running for a bit more, it sounded like she badly needed a break."
    
    n " I tugged her arm, and brought us to a slow, brisk walk."
   
    n "The footsteps were gone."
    
    a "Where is he?"
    
    na "Not sure..."
    
    na "We might have lost him."
    
    n "I shone my light behind us and saw nothing but empty tracks."
    
    n "Had he given up so easily?"
    
    n "Of course, we kept trudging forward nonetheless."
    
    n "Feet bumping against the tracks, we followed the path that had been set for us."
    
    n "Surely this tunnel would have an end."
    
    n "We could arrive at the next station and then call for help."
    
    nvl clear
    
    n "After a while, I realised I was calm once more."
    
    n "Walking like this, feeling her bounce beside me with every step, was calming in a way."
    
    n "Since everything around us was a blank darkness, I could imagine we were transversing under the night sky, and the brief blinking lights around were simply tiny stars."
    
    nvl clear
    
    n "Along the way, I updated her on what had happened."
    
    n "About the train crash, the man on the intercom, and the shadow who was currently on our tail."
    
    n "I omitted all mention of her strange behaviour, though."
    
    n "I didn't want to frighten her."
    
    n "Instead, of course, I gave her the juicy details on how I had saved her from our aggressor."
    
    nvl clear
    
    show alexis surprised
    
    a "So you broke his bones?"
    
    a "You sure?"
    
    na "I felt it."
    
    na "And I heard the crack as well!"
    
    na "Guy flew so far I thought he was on his way out the window."
    
    show alexis smiling
    
    a "I didn't know you were so tough."
    
    na "Well, I wouldn't know, it happened all so fast."
    
    a "How convenient that I don't remember any of it."
    
    na "You're in a good mood, for someone trapped in a terrorist attack."
    
    show alexis surprised
    
    a "You think the person who's after us is a terrorist?"
    
    na "Probably. The person on the intercom and the person who chased us - I think they're the same person, actually -"
    
    na "Anyway, they both said the same two words."
    
    na "Black King."
    
    na "....."
    
    na "I think I've heard that name before."
    
    na "Can't exactly recall, but it was something to do with a terrorist group."
    
    show alexis thinking
    
    a "The Kangaroo Court."
    
    na "Kangaroo Court...?"
    
    na "Oh yeah, I remember."
    
    na "(Amidst photos of carnage and mourning, the reporter had uttered the name of the criminals, and I had thought their moniker was so ridiculous that I had wiped it from my memory.)"
    
    na "Yeah, that's what they called them."
    
    a "And the Black King was their leader, right?"
    
    na "Yeah, that's right."
    
    na "Terrorists don't really come to mind when you say the name out loud."
    
    a "I don't think they were they had a choice."
    
    a "They were just following the name of the book."
    
    na "A book?"
    
    show alexis determined
    
    a " 'The Black King.' "
   
    a "It was published a few decades ago."
    
    a "Their masks, their speeches...it all appears in the book. It's where the Kangaroo Court got their inspiration from."
    
    na "Seriously? I've never heard about that before."
    
    na "Do you know what the book's about?"
    
    a "..."
    
    show alexis thinking
    
    a "I didn't read it directly...but some people on the internet did, and they put out a summary."
    
    a "It's quite a sad story though."
    
    na "Can you narrate it?"
    
    na "I'm all ears."
    
    show alexis worried
    
    na "(Wearing a grim expression, Alexis began to recount the tale.)
    
    #switch to story mode
    
    a "Long long ago, there lived a prosperous city."

    a "It was one of the richest countries in the globe, with buildings decked in gold and roads paved with silver."
    
    a "The main reason for this city's fortune was one single material."
    
    a "It was a material that, when used as a power source, brought immense economic benefits."
    
    a "It was because of this material that allowed the city a strong trading position, and thus established its power."
    
    nvl clear
    
    n "To the outsider, the city was the greatest in the world.
    
    n "No one outside the city knew about the secret population that lived away from the public eye."
    
    n "In order to harvest this material, a large amound of labor had to be spent to purify it from its raw form."
    
    n "Deep underground, the downtrodden and the poor worked as slaves to satisfy their masters at the top."
    
    n "Only 20 percent of the population lived in the government. The rest were not allowed to even raise their heads above the surface."
    
    nvl clear
    
    n "It became inevitable that a rebellion arose."
    
    n "Civil war arose between the lower ranks and the upper class."
    
    n "Eventually, the slaves won back their freedom, and the leader of the rebellion stood in front of the city's throne."
    
    n "But the leader realised something the other's did not."
    
    n "In the city's history, there had been a previous rebellion, and a rebellion before that, and then others before then." 
    
    n "And after every rebellion, nothing had changed."
    
    nvl clear
    
    n "The greedy and ambitious who were once slaves took over the role of the government."
    
    n "And the master slave relationship would continue."
    
    n "The leader of the current rebellion realised, that the only way to break away from the path set before him, was to eliminate human greed altogether."
    
    n "But to do so, he had to have help from those who were not human."
    
    n "At his wits end, he went on a journey to find the best mystics he could find, in order to seek an answer."
    
    nvl clear
    
    n " 'Please help save my city,' he asked the most legendary socerer in the nation. The sorceror dug out his most prized artifacts and delivered an incantation."
    
    n "After the ritual had finished, he told the leader to go back to his city and wait."
    
    n "When he had returned, the leader found that his people had changed."
    
    n "Their minds had been disturbed. No longer did any of them house any big ideas or ambitious thoughts."
    
    n "They no longer saw the value of their prized material. A group went to the furnace in the bottom of the city and destroyed it."
    
    nvl clear
    
    n "Soon, the city descended into madness."
    
    n "With its only source of income gone, everything special about the city slowly rotted away."
    
    n "With no man-made system in place, it returned to its natural order."
    
    n "Lawlessness and violence roamed the streets, and only the strongest earned the right to live."
    
    n "The people were still changing. They began to grow more hair. Their teeth grew longer. Their limbs grew stronger, Instead of talk with their words they swung with their claws."
    
    nvl clear
    
    n "And yet, after the initial violence, a surreal peace desecended over what was once the city."
    
    n "Because once everyone settled in their rightful place, there was no reason to step out of it."
    
    nvl clear
    
    n "There are many stories now, of the once proud city."

    n "Any outsiders who strayed into the city were killed on the spot."

    n "In fact, many has since ceased to call it a city."
    
    n "Nothing civilsed grew there anymore. It was a mockery of all human decency and order."
    
    n "It was the Kangaroo Court."
    
    nvl clear
    
    n "It was generally accepted that the inhabitants of the court, who were resembling humans less month by month, were lawless with government."
    
    n "Still, there were whispers of one man who sat perched on the throne, a privlege that was not given to him, but one that had been earned."
    
    n "The original leader of the rebellion, who in a jungle of his own creation had proved himself the strongest through the rightful trials."
    
    n "He did not oppress, or command. His kingdom worshipped him of their own free will."
    
    nvl clear
    
    n "He was the Black King."
   
    nvl clear
    
    show alexis worried
    
    a "And that's all I know about the basic story."
    
    a "I don't know how it ends, but this is the summary of what happened."
    
    na "Huh."
    
    na "So why does the Kangaroo Court like this book so much?"
    
    show alexis thinking
    
    a "I'm not quite sure..."
    
    a "But there is a certain subtext behind the story."
    
    a "Do you see how someone can be influenced by it?"
    
    na "(It was a hard answer, and I wasn't one to ponder over the philosopies of criminals, but I tried to think it through nonetheless.)
    
    na "(Any thoughts ahead, however, were broken by her sudden gasp.)"
    
    #show outside
    
    na "(Quite literally, there was light at the end of tunnel.)"
    
    na "(We had reached our destination, as I knew we would.)"
    
    na "(The platform came into view quickly, and we ran towards it like starving animals.)"
    
    na "(Of course, I had enough sense in me to remember to climb up the platform first, before extending a hand down to her.)"
    
    na "We made it, Alexis!"
    
    a "Yeah!"
    
    q "Don't move!"
    
    n "Two men in blue uniform had popped out of nowhere."
    
    n "I had to blink a few times before I registered the blue and white insignias on their shoulders."
    
    n "These were police officers."
    
    n "Their pistols were in their holsters, for now, but they didn't seem too friendly."
    
    na "Let me help her up first! She's been hurt."
    
    show alexis surprised
    
    p "Don't move."
    
    hide alexis
    
    n "One of the policeman, avoiding eye contact, went over to the platform and beckoned Alexis to grasp his hand. She did so with a nonplussed demeanour."
    
    n "I imagined reaching forward and slamming him with the iron rod as I had done to our other enemy earlier."
    
    n "The other police officer must have sensed my panic, and held out a hand of appeasal."
    
    p "Easy now."
    
    p "We just want to know what happened."
    
    na "(As if he assumed I knew anything more than he did.)"
    
    show alexis determined
    
    a "The train broked down, and we were attacked by a man in a wolf mask."
    
    a "The last we saw him, he was still in the tunnel."
    
    na "(The officers muttered quietly to each other, as if confirming something they already knew.)"
    
    p "Sorry, but we'd like you to come with us for a while."
    
    a "Have we done anything wrong?"
    
    p "We just want to get the story straight. Follow us."
    
    na "What happened? Was it the Kangaroo Court?"
    
    p "We have to get the story straight first."
    
    n "They showed us into a small office that looked like it used to be the station manager's, and told us to wait there."
    
    n "I couldn't help but notice that when they closed the door behind them, there was the distinct sound of a lock turning into place."
    
    n "This office was not a good place to substitute for a jail cell. There was only a single chair, a table, and a computer which looked like it hadn't been turned on in years."
    
    n "What was worse, it was hot in here, too."
    
    n "As if I was still trapped in a tiny box carriage."
    
    nvl clear
    
    show alexis worried
    
    a "Are you okay?"
    
    n "Focus, Zack."
    
    n "You still have to be strong for her."
    
    nvl clear
    
    na "Is it just me, or is it the weirdest day ever?"
    
    show alexis smiling 
    
    a "it's definitely in my top five."
    
    na "Top five? You mean being chased by a crazy guy isn't enough for you?"
    
    a "...Sort of?"
    
    a "Sit down, and I'll show you."
    
    na "Nah, the floor's okay with me."
    
    n "For the next hour, sitting on the rickety chair, she told another story to her faithful listener  down below. A true one this time, of her aunt who thought she had been going to a church but didn't realise that she had been neck deep in a cult instead."
    
    n "The story was accompanied by a helpful illustration of the cult's building, which reminded me of vacation photos I saw from England."
    
    n "More and more I was learning more new things about the world. I had no idea buildings like that still existed in this country."
    
    n "Imagine living in one of those grand structures. You'd definitely be the talk of the town."
    
    nvl clear
    
    show alexis worried
    
    a "...so when I found what ithe church really was, I didn't confront my aunt immediately. I knew I had to build a case first."
    
    na "Your aunt sounds like she was brainwashed."
    
    a "That's an understatement. She was a slave to whatever the head chief ordered. So if I had to find some evidence, I needed help. Luckily my father was still living with me, so I told him."
    
    show alexis smiling
    
    a "Then he got a lawyer friend of his and you know what happened? The three of us got so worked up that we bypassed our aunt and went straight to the courts."
    
    a "The cult was outed and then shut down within a month.
   
    a "To this day, my aunt still believes that the government gave them a bad hand."
    
    na "She never found out in the end?"
    
    show alexis worried
    
    a "We did have a big row about it after the court case."
    
    a "But in the end, I think she just couldn't cchange her mindset."
    
    a "She would always go on thinking a certain way."
    
    na "That's pretty sad."
    
    na "Luckily for us we'll still agile thinkers."
    
    show alexis smiling.
    
    a "Hopefully."
    
    a "Anyway.".
    
    a "That was my crazy story."
    
    na "Pretty crazy, alright."
    
    a "But I think you have more crazy stories, don't you?"
    
    n "She threw me off guard, and I panicked."
    
    n "How could I have anything to say to impress her, after that? I was just a normal average boy."
    
    n "Come on Zack! You've got to make something up fast!"
    
    na "Well, um,"
    
    na "There was time I, uh, smoked a full cigerette once..."
    
    na "(Her smile deepened, and I wasn't sure what that meant.)
    
    nvl clear
    
    hide alexis
    
    n "Just in time, there was a click, and the door swung open."
    
    n "One of police officers from before came lumbering in."
    
    p "Follow me, you two."
    
    p "We'll take you somewhere more comfortable."
    
    na "Can't be worse than this dump."
    
    na "(I hadn't intended to be witty, but the relief in not having to continue the previous conversation spilled over.)"
    
    na "(Incredibly, the officer cracked a slight chuckle.)"
    
    p "We're taking you down to the police station. I promise, there's enough room for both of you this time."
    
    a  "When are you going to release us?" 
    
    show alexis determined
    
    p "When we sort this whole mess out. You two kids have no idea what you wandered into."
    
    n "On our way down to his car I pestered him with questions, and of course he didn't answer any of them."
    
    n "Instead, he was more concerned with asking us questions of his own."
    
    n "Where we lived, which school we went to, what were our parents doing."
    
    n "It was funny - I had never thought about how my parents had been doing up til now."
    
    n "I was supposed to be home an hour ago, and right now they must have been worried sick."
    
    n "Strangely, Alexis didn't seem concerned about her parents either."
    
    nvl clear
    
    n "I learnt one more thing about her, though."
    
    n "Namely, the fact that she was living alone, in a house her parents had paid for." 
    
    n "Everyone around the same age I had met all lived with their parents."
    
    n "Why was she so special?"
    
    n "Once again, a yearning blossomed within me, and I resolved to dig deeper the next time we could speak." 
    
    nvl clear
    
    n "We passed another road sign."
    
    n "The neigbourhood police station must be really out of the way, for us to travel so far."
    
    n "How long would it be before we returned home?"
    
    n "Not that I minded."
    
    n "The business in the train had scared me shitless, but it had worked out well after all."
    
    n "After all, as good days went, this blew any study date way out of the water."
    
    nvl clear
    
    #police cell
    
    p "Alright, you kids sit tight."
    
    p "This will all be over soon, I promise." 
    
    #he leaves
    
    show alexis worried
    
    na "Well..."
    
    na "This is much better."
    
    na "(I hopped onto the bed.)"
    
    na "(The sheets had been tucked in neatly at the sides.)"
    
    na "(If you closed your eyes, you could actually imagine we were in a middle tier hotel."
    
    a "You don't seem concerned."
    
    na "The hard parts already over, right?"
    
    show alexis smiling
    
    a "Don't get mad, Zack, but..."
    
    a "...I don't really think you smoked a cigerette."
    
    na "W-what?!"
    
    show alexis angry

    a "It's a good thing!"
    
    a "People who smoke are the worst."
    
    na "Oh..."
    
    na "Well, I could have anyway! You don't know me!"
    
    show alexis smiling
    
    a "...."
    
    na "What?"
    
    a "Have you eaten yet?"
    
    na "Nice changing the subject."
    
    a "No, really. I don't know about you, but I'm famished."
    
    nvl clear
    
    n "I was, too."
    
    n "Luckily, drawing from their continued hotel hospitality, the police had left us with a kettle and two cups of instant noodles."
    
    n "It was Tom Yum flavour, too. My favourite."
    
    n "Could this day get any better?" 
    
    na "Why are you putting only half the seasoning?"
    
    show alexis worried
    
    a "I can't handle spicy food! This is the thai curry, right?"
    
    na "Give it to me."
    
    show alexis surprised
    
    a "You sure you can take it?"
    
    na "Of course. I can live on spicy food."
    
    hide alexis
    
    n "After the cooking procedures were done, we plonked ourselves on the bed and sat elbow to elbow against the wall."
    
    n "We were much closer than we were on the train seats. She snuggled in deeper, and her hair actually brushed my shoulder."
    
    n "But, strangely, I wasn't flustered by this at all."
    
    n "We had gone way beyond that." 
    
    nvl clear
    
    na "Why are you living alone?"
    
    show alexis smiling
    
    a "..."
    
    a "You like to ask a lot of questions, don't you?"
    
    na "Is that a bad thing?"
    
    a "Sometimes it's better off not knowing."
    
    a "Sometimes the truth will not set you free."
    
    a "(Having proudly delivered this pearl of wisdom, her head bent down to slurp up the noodles.)"
    
    na "How's the noodles?"
    
    a "I was afraid it'll be too spicy, but it's just the right amount."
    
    na "That's great."
    
    a "Normally the noodles get so spicy you can't even taste anything else."
    
    a "But this brand? It does the spicy well." 
    
    na "Don't get your hopes up yet."
    
    na "Did you mix it?"
    
    show alexis surprised
    
    a "Oh? What do you mean?"

    na "For some brands - this brand for example - the seasoning clomps together if you just leave it like that from the start."
    
    na "You have to constantly stir around the noodles to ensure the seasoning splits apart."
    
    na "May I?"
    
    na "(I dug the cheap chopsticks in between the springy yellow strands, and unearthed a whole new mountain of color.)"
    
    na "See? That's all the tom yum paste that didn't dissolve."
    
    show alexis worried
    
    a "And I've been eating all this time without knowing..."
    
    na "Don't worry about it. It's just that you've never had this brand before."
    
    n "This time, I was prepared." 
    
    n "Armed with my expert knowledge on the subject of our generation's favourite midnight snack, I educated her on the best choices to pick from the supermarket shelf."
    
    n "We soon found ourselves trading names of our favourite brands."
    
    n "Turned out, she was quite the connesieur herself."
    
    n "Still, we had to sometimes agree to disagree."
    
    n "I mean, who enjoys dry instant noodles in this day and age?"
    
    n "Letting the water drain out is way too much hassle for such a convenient product."
    
    nvl clear
    
    n "I wasn't aware how much time passed."
    
    n "We flew through the texture, the flavours, the packaging, the garnish..."
    
    n "At some point, I remember asking her about whether she was still up for meeting at the library tomorrow."
    
    n "Not a request, but a confirmation."
    
    n "She nodded, and we returned to the benefits and drawbacks of leaving the seasoning outside the sachets instead of in."
    
    nvl clear
    
    hide alexis
    
    #fade to black time passes
    
    n "A sound awoke me."
    
    n "Judging from the clock on the wall, I found three hours had passed."
    
    n "Next to me, Alexis was still dozing, breathing softly in her sleep."
    
    n "The sound came again. The door to our cell was opening."
    
    n "A scarecrow stood in the doorway."
    
    nvl clear
    
    n "That was how I saw him at first. A towering, eerie shape."
    
    n "Then he ducked his head under the doorway to get in, and I realised he was simply very tall and thin."
    
    n "He didn't look like a policeman, although his uniform seemed vaguely familiar." 
    
    n "My first image of him went away as I saw his features under the light - he could have been someone's grandpa."
    
    p "Are you two alright?"
    
    na "(Alexis jerked awake, nearly throwing me off.)" 
    
    show alexis surprised
    
    a "..."
    
    na "(Was it my imagination, or did she suddenly freeze up?)"
    
    na "(Every limb in her body tensing, like a deer in the headlights preparing to bolt at any second.)"
    
    na "(But like my first impression of the old man, that image of Alexis melted away so quickly I wondered if I had imagined it.)"
    
    show alexis angry
    
    a "Who are you?"
    
    q "..."
    
    q "I'm the train conductor."
    
    na "(Of course - that was the uniform of the train attendants.)"
    
    na "(But what was he doing all the way here?)"
    
    q "You two must have many questions."
    
    q "Please, ask away."
    
    q "Someone coming and offering to dump answers in our lap, must have stunned us, because we just stared at him."
    
    q "Still smiling, he went to the remnants of our tom yum meal, and began to gather the trash to clear it."
    
    q "When can we leave?"
    
    q "Whenever you are satisfied."
    
    q "As of this moment, you two are cleared of all suspicion."
    
    q "They had thought you two were members of the Blackhats, but a few background checks corrected their fears."
    
    na "Why... would they think that?"
    
    na "(He picked up the bin and scooped the trash inside.)"
    
    na "(I couldn't help but notice he had to bend over double to do so.)"
    
    q "Because you two came directly from the site of the attack."
    
    q "Earlier this morning, the Blackhats seized control of a train, and forcibly brought it to a halt."
    
    na "(I was surprised that chills weren't immediately running down my spine.)"
    
    na "(It was probably because what he was saying still felt like it was from a storybook."
    
    na "(The chase in that train was much more than a simple terrorist attack.)"
    
    q "Rest assured, all the culprits have already captured, and the only uncertain variables were the two of you."
    
    q "Now that even that has been resolved, you two are free to go." 
    
    na "Ah..."
    
    a "Thanks. And thank you for cleaning up."
    
    q "Don't worry about it. Off you two go."
    
    na "(But I couldn't go just yet.)"
    
    na "(The mystery was hardly resolved. So many pieces were still left unfound.)"
    
    na "(And this tall, strange man, had almost challenged us to probe deeper.)"
    
    na "(I could sense it. He knew everything.)"
    
    na "What happened to the man in the wolf mask?"
    
    na "He was the one chasing us."
    
    q "Mister Howard Roark, I believe his name was."
    
    q "The police couldn't find him in time, so I had to step in."
    
    na "(With a sweep of his hand...)"
    
    na "(An object clunked to the floor.)"
    
    na "(It rolled towards me.)"
    
    n "What...."
    
    n "Is this real?"
    
    n "Here, nestled within the confines of law and order, was the real world."
    
    n "Why was I seeing those jaws again?"
    
    nvl clear
    
    n "The wolf's head finally spun to a stop, facing me with its hollow eyes."
    
    n "It wasn't a head, at all, I realised. It was just a mask."
    
    n "A cheap, plastic mask, the kind you would find in the halloween store."
    
    n "I wasn't reassured, however."
    
    n "Those same flimsy jaws were ones who had threatened to rip me and Alexis apart." 
    
    nvl clear
    
    na "(I slowly became aware that I was being watched.)"
    
    na "(The old man, he truly was a scarecrow.)"
    
    na "(For he had suddenly turned stock still, cocking his head.)"
    
    na "(What...was he looking for?)"
    
    q "..."
    
    q "Little girl, what is your name?"
    
    a "Alexis."
    
    q "Mrs Alexis, do you recognise this mask?"
    
    a "Yes." 
    
    a "One of the terrorists had them."
    
    na "But..."
    
    na "But, why do you have it?"
    
    na "(Wasn't it supposed to be evidence?)"
    
    na "(Where did it even come from?)"
    
    na "(His hands were empty when he walked in!)"
    
    q "The answer to your question is simple."
    
    q "He was disrupting the order, and I took care of him."
    
    q "Now that we can consider that matter settled, I'd like to ask the two of you a question."
    
    a "I thought you said we could leave."
    
    q "After you answer my question."
    
    a "We'd like to go now, please."
    
    q "I'm afraid you two are being quite unfair."
    
    q "I've told you something, and so you must tell me something."
    
    q "Quid Pro Quid."
    
    n "He took a folded piece of paper from his pocket and took his sweet time spreading it out."
    
    n "I thought, briefly, of overpowering him and shouting for Alexis to run for the door."
    
    n "But my instincts screamed at me that laying even a finger on him would be a fatal mistake."
    
    n "My whole body was telling me that."
    
    n "This scarecrow...was a monster."
    
    nvl clear
    
    q "Look at this, if you would be so kind."
    
    n "It was a pencil sketch of the inside of a train carriage."
    
    n "Much like the one we had been trapped in, but of course, all trains were the same."
    
    nvl clear
    
    na "...What about it?"
    
    q "Do you notice anything strange in this picture?"
    
    na "What?"
    
    n "As far as I could tell, it was a completely ordinary drawing."
    
    n "It was pretty detailed, and I could tell a lot of effort had been put in, but other than that, what did he expect me to say?"
    
    n "No...wait."
    
    n "There was something about this picture."
    
    nvl clear
    
    n "I had seen it before."
    
    n "I wasn't sure where, but it was definitely familiar."
    
    n "And I wasn't about to let this shady old man know that."
    
    nvl clear
    
    na "What am I supposed to see?"
    
    q "..."
    
    q "And you, Mrs Alexis?"

    a "The shading is really good."
    
    a "i don't know what to say.
    
    na "(Again, his body, still holding out the drawing, stiffened."
    
    na "(Nothing on his face moved, not even his smile, but his eyes darted left and right, between us, conducting a thorough examination.)"
    
    na "(It was the best poker face I had put on in my entire life.)"
    
    q "..."
    
    q "I understand."
    
    q "I'm terribly sorry for keeping you."
    
    q "Please. Your parents must be worried."
    
    n "He stepped aside, leaving us a clear pathway to the door."
    
    n "We didn't need to think twice."
    
    n "The two of us rushed out of the room as fast as we dared."
    
    nvl clear
    
    #scene change
    
    na "How are you getting home?"
    
    a "Bus number 265. You?"
    
    na "Well, normally I'd take the train from here, but..."
    
    a "Where do you live?"
    
    a 'The bus should also be pretty reliable."
    
    n "Considering we had been attacked by a weirdo hours earlier, only to meet with another weirdo after that, I would say we were taking things lightly."
    
    n "But then again, why wouldn't I? This whole affair had been a resounding success."
    
    n "I gazed into the back of Alexis's head, as she studied the board to pick out the bus routes for me."
    
    nvl clear
    
    n "There was only one niggling doubt."
    
    n "One tiny pocket of unease, that made me recoil from the time in the tunnel."
    
    n "It wasn't about the wolf mask."
    
    n "It was the other Alexis."
    
    nvl clear
    
    n "You could chalk it up to increased stress."
    
    n "That she was so frightened she just clammed up and changed her entire personality."
    
    n "But could humans really do that?"
    
    n "The alternative to that explanation was..."
    
    n "That she was lying."
    
    nvl clear
    
    n "The whole story about having amnesia was a way to avoid being asked any more questions."
    
    n "When in fact, she knew all the answers."
    
    n "She knew the attack was going to happen."
    
    n "She knew who the creepy old man was."
    
    n "All the while playing innocent."
    
    n "Stirring her noodles as if she didn't know any better."
    
    n "Was a human..."
    
    n "Capable of that as well?"
    
    nvl clear
    
    a "So, I think if you take 176, then transfer to 156, this should do the trick."
    
    na "Alright, that works out."
    
    n "I would see her tomorrow."
    
    n "We would share a table together, and then the day after that, and then all the days from onwards."
    
    n "We would get to know each other better."
    
    n "That should be good enough."
    
    nvl clear
    
    show alexis surprised
    
    a "My bus is here!"
    
    a "Well, see you tomorrow?"
    
    na "Of course!"
    
    a "Thanks for...the lesson on instant noodles."
    
    na "And thanks for the stories."
    
    a "I'll see you - whoops!"
    
    na "(Her sketchbook had fallen out of her bag.)"
    
    na "(I bent down to take it.)"
    
    n "And my heart went cold."
    
    a "Thanks."
    
    a Bye! See you tomorrow!"
   
    n "She was rushing to get on, so she didn't see the expression on my face."
    
    n "Now I knew where I had seen that drawing of the train."
    
    n "At the very start of the day, when she was showing my her sketchbook."
    
    nvl clear
    
    n "The artist of that drawing..."
    
    n "... was her."
    
    nvl clear
    
    n "The next day, when we met, I didn't bring it up."
    
    n "Instead, we were preoccupied with being the talk of the town, and everyone badgered us on how we had survived such a terrible tragedy."
    
    n "We escaped to the roof that day, and had a laugh over a few homemade sandwiches."
    
    n "The full details of the incident emerged later."
    
    nvl clear
    
    n "The train had been empty because the Blackhats had herded all the passengers off into the other side of the tunnel."
    
    n "There, they held the passengers hostage while they issued a list of demands to the government."
    
    n "A police tactical team was sent in."
    
    n "Twelve people died. Four terrorists, two police officers, and six civilians."
    
    n "The reporter said it was the first time so much blood had been spilled in out otherwise crime free country."
    
    nvl clear
    
    n "There was one Blackhat member accounted for."
    
    n "One who was last seen wearing the mask of a wolf."
    
    n "No one knew his whereabouts."
    
    nvl clear
    
    n "A few weeks later, I got a phone call."
    
    n "It was the police officer from the station."
    
    n "Apparently..."
    
    n "That day, no one had seen a train conductor enter the building."
    
    #TO BE CONTINUED

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
