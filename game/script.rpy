﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define n = nvl_narrator
define na = Character("Zack")
define a = Character("Alexis")

define i = Character("Intercom")


image alexis surprised = "Alexis/alexis_surprised.png"

image stationSide = "Bg/stationSidevers2.jpg"



define flash = Fade(1, 1, 1, color="#fff")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    show alexis surprised
    
    na "This is a test."
    

    
    scene stationSide with flash
    show alexis suprised
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
    
    n "It's dark."
    
    n "It's hot."
    
    n "It's cramped."
    
    n "The occupants have long since descended into madness."
    
    n "My tongue comes out dry and my head like brass."
    
    nvl clear
    
    n "Behind me, a man succumbs."
    
    n "His limbs distort and he convulses to the ground."
    
    n "Foam gushes out of his mouth and he kicks his legs like a dying spider."

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
    
    n "The darkness begins to lift and I start to make out her dress.  "
    
    nvl clear
    
    n "Again, the two of us had arrived."
    
    n "{vspace=20}On the same road on the same track on the same route."
    
    n "{vspace=20}The beginning of the journey, and the end."
    
    n "{vspace=20}Point A..."
    
    nvl clear
    
    n "{vspace=50}...to Point B"
    
    nvl clear
    
    
    #change scene 
    
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
    
    n "But right now, any viewers tuning in are in for a treat."
    
    n "No joke, my hearts pumping like crazy and I can't stop squeezing my fingers."
    
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
    
    n "Damn the train's coming!"
    
    n "I don't know which station she gets off."
    
    n "It could be a long journey, or she could be gone by next stop."
    
    n "No, never mind that, she's already moving inside."
    
    n "I have to follow her..."
    
    nvl clear
    
    n "...The train's empty."
    
    n "It's in the middle of the afternoon, after all, and all the adults are away."
    
    n "That means, of course, that I have to stand far away from her so I don't look weird."
    
    n "I was close to her when we entered the train, together, though."
    
    n "...she smelled nice."
    
    nvl clear
    
    n "This is driving me crazy."
    
    n "As the distance to the next station nears, my anxiety keeps shooting up."
    
    n "This is the only chance I have."
    
    n "Her existence is like a dandelion in the wind - no, that's not entirely accurate."
    
    n "She's more like a lily in a pond."
    
    n "Always visible in the distance, but out of reach."
    
    n "It's only in this train when she's within my grasp."
    
    n "There's no time to think. No point in playing what might happen. I have to do it now or lose it forever."
    
    nvl clear
    
    n "So... I stand up, and approach her."
    
    #approach alexis
    
    # her sprite fades in
    
    nvl clear
    
    n "Her eyes..."
    
    n "I never thought that color could exist."
    
    n "...."
    
    nvl clear
    
    na "..."
    
    a "..."
    
    na "..."
    
    n "She's inching away..."
    
    n "I have to open my mouth or I'll just be another creep!"
    
    nvl clear
    
    na "Which stop are you getting off at!"
    
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
    
    a "I'm happy you like it."
    
    a "My dad was a painter, so I just learned from him."
    
    na "This is seriously Picasso tier."
    
    na "You could earn millions from this!"
    
    a "Nononono, no one would buy these!"
    
    n "I was exaggerating, of course, but I'd heard overcompliments are the best way to a girl's heart."
        
    na "And what are these?"
    
    n "A few pages on, the fantastical drawings ceased, and more mundane everyday sketches emerged."
    
    n "Most of them were random places around the city."
       
    nvl clear 
    #time passes
    
    a "Sorry, do you dislike them?"
    
    a "I make it a schedule to draw from real life reference every few weeks."
    
    a "My father always said that I needed to branch out into other styles, so I can find something I'm can really specialize in."
    
    na "If you want my take on it, anybody can draw anything from real life."
    
    na "But it takes true talent to draw from imagination."
    
    na "Your first few drawings are the best ones, you should focus on those."
    
    n "She looked at me as if she would a lighthouse in the middle of a stormy sea, and I inwardly cheered."
    
    n "And to think I made that piece of advice up on the spot!"
    
    nvl clear 
    
    #time passes
    a "...A concept artist would be really hard. Everyone wants to be one. Some people work for ten years before they finally get that position."
    
    na "A concept artist? You mean, like for a movie?"
    
    a "Movies are great, but they're too competitive. I'm thinking maybe for a video game studio."
    
    na "Ubisoft! Or Blizzard!"
    
    a "Those companies are competitive too! I won't get in."
    
    a "Maybe in a small studio..."
    
    na "Let me tell you something."
    
    na "You should drop out of school and send your drawings to Ubisoft right now."
    
    a "I told you, I won't get it!"
    
    a "I'm going to an art university after this."
    
    na "You sure you're going to need it?"
    
    a "Big companies require a university education!"
    
    na "Eh, degrees are overated."
    
    na "Did you know Steve Jobs dropped out of college?"
    
    a "Oh, really?!" 
    
    na "Yeah, also Mark Zuckerburg, and Lady Gaga."
    
    a "Who's Mark Zuckerburg?"
    
    na "You seriously don't know?"
    
    a "It sounds familiar, sorry..."
    
    na "He was the first man on the moon, how could you not know him?"
    
    a "First man on the moon - "
    
    a "No wait, are you sure...?"
    
    na "I was kidding."
    
    na "Mark Zuckerburg was the guy who invented Facebook."
    
    a "Oh, that guy!"
    
    a "My father was talking about him."
    
    a "He said that I shouldn't follow his example."
    
    na "Of what, dropping out?"
    
    a "Yes. He said I wasn't smart enough."
    
    na "Anyone who carries around a sketchbook like that a freaking genius."
    
    a "What do you mean?"
    
    na "Well..."
    
    na "You sit down in the middle of everyone, and you can concentrate enough to sketch a full drawing..."
    
    na "I could never do it."
    
    a "Anyone can learn to draw, if they practiced." 
    
    na "It's not a matter of practice."
    
    na "It's about...I mean, we're at school, aren't we? Doing our maths and science and studying to become the nation's next greatest doctors."
    
    na "So...it's not a matter of whether I start drawing or not, in the end it won't matter, right?"
    
    a "I get what you mean."
    
    a "But art is like that."
    
    a "You have to make sacrifices."
    
    a "I don't think I'm especially talented."
    
    a "So I have to keep working hard."
    
    na "No, you're definitely special."
    
    na "You know how I know?"
    
    a "How?"
    
    na "Your eyes." 
    
    na "They're the eyes of a chosen one."
    
    a "Chosen one?"
    
    na "(She giggled at that one.)"
    
    na "(She was beginning to let more of her show.)"
    
    a "My father says it's just pigments."
    
    na "Pigments that are a one in a million."
    
    a "We're all special in our own way."
    
    na "Yeah, now that you mention it, I'm a pretty big deal myself."
    
    a "Oh?"
    
    na "(I slipped my hand out of my pocket and showed it to her.)"
    
    na "(Normally, I would be embarassed to show it to anyone, but this girl could accept anything."
    
    na "(On the back of my right hand, was a dark birthmark in the shape of a star.)"
    
    na "People ask me if this was a tattoo, or was drawn on."
    
    na "I was born with this."
    
    a "It's beautiful."
    
    na "You can touch it if you want."
    
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
    
    na "Alexis, let's make a video game together."
    
    a "..."
    
    a "Wow."
    
    a "Do you mean, an actual video game?"
    
    na "You've got the art, and I can learn some programming."
    
    na "I'm serious, Alexis."
    
    na "I never wanted to end up like the rest of them in the first place."
    
    na "And you don't want to either."
    
    na "Together, I'm sure we can - "
    
    # train screeches
    
    #screen goes dark
    
    play sound "sound/crash.wav" fadeout
    
    $ renpy.pause(7, hard=True)
    
    n "Panic."
    
    #flash?
    
    n "Terror."
    
    #flash
    
    n "Despair."
    
    #flash?
    
    n "The ugly and the desperate clawing for their lives."
        
    n "I could see it all."
    
    n "Standing up with my flayed skin dangling down, I could believe."
    
    n "That in this world, there was a Hell on Earth - "
    
    nvl clear
    
    #flash
    
    na "Gaaarrggh!"
    
    n "What -"
    
    n "Where am I - "
    
    a "..."
    
    nvl clear
    
    n "The train..."
    
    n "it's not moving anymore."
    
    n "I'm on the ground."
    
    n "That means the train must stopped so hard I was sent flying."
    
    a ",,,"
    
    n "Alexis...it looks like she was roughed up a bit too."
    
    nvl clear
    
    a "..."
    
    n "These bloody trains."
    
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
    
    na "Are you hurt anywhere?"
    
    a "..."
    
    na "Don't worry. I'm sure they'll get us out soon."
    
    a "..."
    
    na "(She seems more shellshocked than I expected.)"
    
    na "(Does she have a fear of these sort of situations?)"
    
    na "Well, there's point in standing around."
    
    na "Let's just have a seat and wait for them to arrive."
    
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
    
    a "There should be an emergency exit at the end of the train."
    
    a "Let's head there."
    
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
    
    i "{cps = *0.7} Dear...passengers. {/cps}"
    
    i "{cps = *0.7} The train...is experiencing...a momentary delay." 
    
    i "{cps = *0.7} Please...remain in your...seats..."
    
    i "{cps = *0.7} The train...will resume...shortly"
    
    na "See, There's nothing to worry about."
    
    a "..."
    
    a "Don't trust him."
    
    na "What? Trust who?"
    
    a "The conductor."
    
    a "We'll be safe if we get off this train."
    
    na "I don't get what you mean."
    
    na "(We had reached the end of the first carriage, and there was a door to the next one blocking our way."
    
    na "(Ignoring my last question, she stepped forward to pull it open.)"
    
    #shudder
    
    na "(The door opened a quarter of the way before jerking to a stop.)"
    
    a "..."
    
    a "I should have known."
    
    na "It's stuck?"
    
    na "Let me try!"
    
    na "(I overexaggerated my attempts at first, huffing and puffing like a true man worked.)"
    
    na "(But even when I genuinely gave it my best, the door wouldn't budge.)"
    
    na "(Do train doors normally jam this badly?)"
    
    na "(It's the first time I've heard of this.)"
    
    a "There should be a way to open it." 
    
    na "(Again, as if barely acknowledging my presence, she turn around and began examining the train.)"
    
    n "The air of the train was getting to me."
    
    n "At some point the air conditioning must have shut off, because the inside of the carriage was dryer than the Sahara desert."
    
    n "So I stood there sweating my guts out, and watched Alexis rummage through the seats as if searching for a hidden pot of gold."
    
    n "Nothing about this situation made any sense."
    
    na "What are you doing?!"
    
    na "(My voice came out rougher than I intended.)"
    
    a "I'm looking for a ."
    
    na "What?"

        `
    
    
    
    
    
    
    
    
   
    

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
