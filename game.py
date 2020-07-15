import time
import npc
from playbook import Playbook
from world import World
from player import Player

player = Player()
lady = npc.OldLady()
kid = npc.LittleKid()
girl = npc.PrettyGirl()
angry = npc.AngryMan()


def menu():
    goto = input('''You can:
(R)ead the playbook.
(C)heck your emotional state.
(I)nspect your inventory.
(X)Achievements.
(F)inish the game.
Visit:
(O)ld Lady, (P)retty Girl, (L)ittle Kid, (A)ngry Man
Hmm: ''').upper()
    if goto == 'R':
        Playbook.book()
        menu()
    elif goto == 'C':
        player.show_situation()
        menu()
    elif goto == 'I':
        player.show_inventory()
        menu()
    elif goto == 'X':
        for key, value in World.achievements.items():
            print(f'{key}: {value}')
        input()
        menu()
    elif goto == 'O':
        visit_old_lady()
    elif goto == 'P':
        visit_pretty_girl()
    elif goto == 'L':
        visit_little_kid()
    elif goto == 'A':
        visit_angry_man()
    elif goto == 'F':
        if player.inventory:
            input('You still have some gifts to give to people.')
        elif not player.inventory:
            player.result()
            input('''Going back to the beginning of the road...
No one will remember you, gifts will be ungiven, back at your inventory.
You will keep your achievements.
Meet and greet them again to hear their other songs.''')
            World.replays += 1
            if World.replays == 10:
                input('***Achievement unlocked!***')
                input("instagram/alcakhardal")
                World.achievements['Groundhog day'] = 'Play the game 10 times'
            replay()
            play()
        menu()
    elif goto == 'EASTERCENG':
        Playbook.ceng()
        menu()
    else:
        print("That is not something to 'do'. That is just gibberish.")
        menu()


def play():
    input('Before I was born there was a silence.')
    input('Before that silence there was a fire.')
    input('Before that fire, a sound.')
    print('Befo\nSomething wrong happened, please wait...')
    time.sleep(2)
    print('You have nothing to fear.')
    input(f"Current fear = '{player.fear_level * 'X' + (10 - player.fear_level) * '-'}'")
    print('...except for love.')
    input(f"Current love = '{player.love_level * 'X' + (10 - player.love_level) * '-'}'")
    menu()


def replay():
    global player
    global lady
    global kid
    global girl
    global angry
    player = Player()
    lady = npc.OldLady()
    kid = npc.LittleKid()
    girl = npc.PrettyGirl()
    angry = npc.AngryMan()


def visit_pretty_girl():
    if girl.alive:
        if girl.visit == 0:
            a1 = World.choice('''Have you seen me here before?
I can swear you've seen me here before, don't lie.
(Y)es/(N)o: ''', ['Y', 'N'])
            if a1 == 'Y':
                input("I knew it.")
            elif a1 == 'N':
                input("I could've sworn.")
            input('''Hey,
Let's turn off the lights,
Turn on the spark,
I've always wanted to dance in the dark!''')
            a2 = World.choice('''(Y)es, I'd be honoured.
(N)o, I can't dance in the dark.
Hmm: ''', ['N', 'Y'])
            if a2 == 'N':
                player.love_level -= 1
                input('''Death to all is
Gonna come,
And it'll make dancing
Much more fun!''')
            elif a2 == 'Y':
                player.love_level += 1
                girl.dance = True
                input('''You are electric,
You are light,
You are the music itself,
And you are flight!''')
        elif girl.visit > 0:
            input(f'''Nice to see you well again,
For I don't know how many times,
Was it only now and then,
Oh wait, actually, it is {girl.visit}.''')
        girl.visit += 1
        a3 = World.choice('''(G)ive her a gift.
(L)eave.
Hmm: ''', ['L', 'G'])
        if a3 == 'L':
            input("Bye, handsome devil.")
            if girl.visit == 5:
                input('***Achievement unlocked!***')
                World.achievements['Beautiful visits'] = 'Visit the girl 5 times'
            menu()
        elif a3 == 'G':
            a4 = World.choice(f'''Which gift though?
{', '.join(player.inventory)}
Hmm: ''', ['M', 'C', 'H', 'K'])
            if a4 == 'M':
                World.give(player, 'Matches', girl)
                player.fear_level -= 3
                player.love_level -= 3
                input("She takes the matches, light the dark room up with bright fire. She frowns.")
                input('''Light is not your friend,
It catches flaws with rigor,
Yes it makes your fears end,
But in darkness love grows bigger.''')
                if girl.dance:
                    input('''But all in all I have done it,
Thanks,
I have danced in the dark at least...''')
            elif a4 == 'C':
                World.give(player, 'Candy', girl)
                player.love_level -= 3
                input("She takes the candy, unhappy.")
                input('''Can't be myself if I want to stay in this room,
A scale and a pair of eyes might be handy,
A flower maybe, a little perfume,
Albeit I can't eat this candy...''')
            elif a4 == 'H':
                World.give(player, 'Hourglass', girl)
                player.fear_level += 5
                input("Her eyes glisten with surprise. She seems happy.")
                input('''Finally!
I can use it to never stop dancing,
Stuck in time,
Not worth a dime!''')
                input('Not worth a dime.')
                input('Stuck in time.')
                input('Not worth a dime.')
                if girl.dance:
                    input('''Had a 'not bad' life though,
Once I have danced in the dark with you.
Once someone even gave me a gift,
If you catch my drift...''')
                    input('Bye, handsome devil.')
                girl.alive = False
            elif a4 == 'K':
                World.give(player, 'Knife', girl)
                input("She takes the knife, analyses it, tries to stab herself.")
                input('''Finally, something to cut deeper,
Fast, painless, cheaper.''')
                a5 = World.choice('''(L)et her harm herself.
(H)old the knife to prevent.
Hmm: ''', ['L', 'H'])
                if a5 == 'L':
                    player.fear_level += 3
                elif a5 == 'H':
                    player.fear_level += 5
                input('''Why did you give me the knife?
I thought you would know me by now,
I'm not even your wife,
Nor a chicken, a pig, nor cow.''')
                if not girl.dance:
                    input('''I even never in my whole life,
Dance in darkness with a handsome guy.''')
            menu()
    elif not girl.alive:
        input("You see a beautiful body, stuck in time, dancing forever.")
        menu()


def visit_old_lady():
    if lady.alive:
        if lady.visit == 0:
            input("You see a smiling old lady with a kind face near a great green tree.")
            input('''Hello sweetie, my handsome child,
Hope you're not hungry, lonely or upset,
Hope you laugh much and are going wild,
With no threat, hate or regret?''')
            input('''You gotta shake the tree before you know what it grows, boy.
Shake the tree boy.''')
            b1 = World.choice('''(S)hake the tree.
(D)'ont shake the tree, you don't know what it grows.
Hmm: ''', ['S', 'D'])
            if b1 == 'S':
                lady.shook = True
                player.fear_level -= 1
                input("Old lady smiles. Coughs. Sings.")
            if b1 == 'D':
                player.fear_level += 1
                input("Old lady frowns. Coughs. Sings.")
            input('''No more love eye to eye,
No more stars in the sky,
Stop stop stop stop stop
Don't tell a dead man how to .....''')
            b2 = input('''You finish the song with a rhyme.
Hmm: ''').upper()
            lady.poem = b2
            if b2 == 'CRY':
                input("You're right boy, no one ever saw a dead man weeping. My precious boy...")
            elif b2 == 'DIE':
                input("Oh that's my favourite! Yes, dead is already dead you know...")
            elif b2 == 'DROP':
                input("Yes, dead already knows how to fall. You are old, my boy.")
            elif b2 == 'IGGY POP':
                input("What does this musician have to do with it? Are you fucking with me you moron? Iggy fuckin "
                      "pop? My fucking god dude...")
                input('***Achievement unlocked!***')
                World.achievements['Iggy Pop'] = "Break the old lady's character with your nonsense"
            elif b2 == 'HOP':
                input("Yes, dead are not rabbits.")
            elif b2 == 'HOPE':
                input(
                    "Yes, that's the only time you no longer expect anything from the world. Only dead cannot be hopeful.")
            else:
                input("Hmm, that's an odd one.")
        elif lady.visit > 0:
            input("Welcome back, boy, hope you're not hungry.")
        lady.visit += 1
        b3 = World.choice('''(G)ive her a gift.
(L)eave.
Hmm: ''', ['L', 'G'])
        if b3 == 'L':
            input("Bye, my sweetie.")
            menu()
        elif b3 == 'G':
            b4 = World.choice(f'''Which gift though?
{', '.join(player.inventory)}
Hmm: ''', ['M', 'C', 'K', 'H'])
            if b4 == 'M':
                World.give(player, 'Matches', lady)
                player.love_level += 3
                input("The old lady takes the matches, lights up a candle.")
                lady.give_candle()
                if lady.candle >= 10:
                    input('***Achievement unlocked!***')
                    World.achievements['Rite with the old lady'] = 'Light 10 candles with the old lady'
                input('Thanks, boy. That means a lot.')
                menu()
            elif b4 == 'K':
                World.give(player, 'Knife', lady)
                player.fear_level -= 4
                input('Old lady takes the knife. Looks at it. Hides it under her clothes.')
                input('''What a great gift!
What a thoughtful one indeed!
I will hide it to make sure,
No harm can be done, guaranteed.''')
                if lady.shook:
                    input('''You shook the tree as well,
What a brave boy, what a great one!
You take risks, break your shell,
Easier said than done!''')
            elif b4 == 'C':
                World.give(player, 'Candy', lady)
                player.love_level += 1
                input('Old lady smiles, takes the candy')
                input('''I have eaten thousands of these,
My grandson it shall please.''')
            elif b4 == 'H':
                World.give(player, 'Hourglass', lady)
                player.love_level -= 3
                player.fear_level += 5
                input("Old lady takes the hourglass, turns it around.")
                input('''I fought the time for years and years,
And how many times I lost, I lost track,
It was all blood sweat and tears,
That's why I'd never go back.''')
                input("What a weird poem indeed...")
                input(f'''No more love eye to eye,
No more stars in the sky,
Stop stop stop stop stop
Don't tell a dead man how to {lady.poem.lower()}.''')
                input('''She holds the hourglass, turns into a little girl.''')
                lady.alive = False
            menu()
    elif not lady.alive:
        input("You see a sad little girl, wanting to grow up.")
        menu()


def visit_little_kid():
    if kid.alive:
        if kid.visit == 0:
            input("You see a little kid, dancing and singing.")
            input('''One-Two-Three gluten free
For-Five-Six candlesticks
Seven-Eight-Nine make you miiiiine.''')
            input("Hi sir! Am I going to be a good man, or a bad man?")
            c1 = World.choice('''(G)ood man of course!
(B)ad... probably a bad man considering everything.
Hmm: ''', ['G', 'B'])
            if c1 == 'G':
                kid.good = True
                input('Oh thanks, sir!')
            elif c1 == 'B':
                input('Oh thanks, sir!')
        elif kid.visit > 0:
            input("Welcome back, sir, I was just about to miss you.")
        kid.visit += 1
        c2 = World.choice('''(G)ive a gift.
(L)eave.
Hmm: ''', ['G', 'L'])
        if c2 == 'L':
            input("Bye, sir. Do comeback.")
            menu()
        elif c2 == 'G':
            c3 = World.choice(f'''Which gift though?
{', '.join(player.inventory)}
Hmm: ''', ['M', 'C', 'K', 'H'])
            if c3 == 'C':
                World.give(player, 'Candy', kid)
                player.love_level += 5
                input("Kid looks extremely grateful.")
                input('''One-Two-Three somebody up there loves me,
For-Five-Six like a junkie loves its fix,
Seven-Eight-Nine in rain or shine.''')
            elif c3 == 'H':
                World.give(player, 'Hourglass', kid)
                player.fear_level -= 3
                input("Kid looks extremely scared.")
                input("""I wanna stay as a child,
I don't want to know what time is
Can I stay as disguised?
Can I not now what time is please?""")
                if kid.good:
                    input('''Yes you said I'll be a good man,
But you can't see the forest for the trees.''')
                elif not kid.good:
                    input('''Yes you said I'll be a bad man,
But I'll dot the i's and cross the t's.''')
            elif c3 == 'M':
                World.give(player, 'Matches', kid)
                player.fear_level += 3
                input("Kid's eyes shine, wickedly.")
                input('''Thanks sir, I will now burn things,
Thanks, now I can get a life,
Thanks sir, I will become a real man,
Only thing I need now is a knife.''')
            elif c3 == 'K':
                World.give(player, 'Knife', kid)
                player.fear_level += 3
                input("Kid's eyes get red with a wicked smile.")
                input('''Oh thanks sir, oh thanks!
Now I can end a life indeed,
For shits, giggles, fun, and pranks!
Now some matches are all I need!''')
            if kid.inventory_check:
                kid.alive = False
                player.fear_level += 3
                input("Oh wait, I do have some matches and a knife.")
                input('''One-Two-Three, none so blind as those who will not see,
For-Five-Six, like a cat on hot bricks,
Seven-Eight-Nine end of the line,
Seven-Eight-Nine end of the line,
Seven-Eight-Nine make you mine,
Seven-Eight-Nine make you mine,
Ten, time and time again.''')
                input("Ten, time and time again.")
                input('***Achievement unlocked!***')
                World.achievements['A bad boy'] = 'Gift the matches and the knife to the boy'
            menu()
    elif not kid.alive:
        input('''You see a little kid, with some matches and a knife, and a creepy smile. He doesn't look cute.''')
        menu()


def visit_angry_man():
    if angry.alive:
        if angry.saved:
            input('You see a boy, eating candy.')
            menu()
        if angry.visit == 0:
            input("You see an angry man, huffing and puffing around.")
            input('''Little men telling us what to do,
Little men telling us what to wear,
Little men deciding where we grew
And what we view and what we bear.''')
            input("Tell me, is there anything worth living for?")
            d1 = World.choice('''(Y)es, there is more in life than sorrow.
(N)o, for men there is no cause, no reason.
Hmm: ''', ['Y', 'N'])
            if d1 == 'Y':
                player.fear_level -= 2
                angry.reason = True
            elif d1 == 'N':
                player.fear_level += 2
            input('''Cruel men deciding which one to love,
Cruel men deciding which war to fight,
Cruel men deciding which one's above,
Which poem we write, who's wrong or right.''')
        elif angry.visit > 0:
            input("It is nice to see you, again.")
        angry.visit += 1
        d2 = World.choice('''(G)ive a gift.
(L)eave.
Hmm: ''', ['L', 'G'])
        if d2 == 'L':
            input("Farewell.")
            menu()
        elif d2 == 'G':
            d3 = World.choice(f'''Which gift though?
{', '.join(player.inventory)}
Hmm: ''', ['M', 'C', 'K', 'H'])
            if d3 == 'M':
                World.give(player, 'Matches', angry)
                input('Angry man takes the matches, pull out a cigarette, lights it.')
                input('''I know these are killing me,
But I chose to to it, didn't I?
Doesn't it show that I am free?
Cruel men know that it's a lie...''')
                input('Take one, my friend.')
                d4 = World.choice('''(T)ake one, even if we're not free, we can enjoy things.
(D)'ont take one.
Hmm: ''', ['T', 'D'])
                if d4 == 'T':
                    player.fear_level -= 5
                elif d4 == 'D':
                    player.fear_level -= 2
            elif d3 == 'K':
                World.give(player, 'Knife', angry)
                player.fear_level += 4
                player.love_level -= 8
                input("Angry man takes the knife, looks at you in disbelief, then stabs himself.")
                input('''Was I alive, was I dead?
Is there anything else after?''')
                if angry.reason:
                    input('''"Life's worth living" you said,
At least I won't hear cruel men's laughter.''')
                elif not angry.reason:
                    input('''"Life's not worth living" you said,
At least I won't hear cruel men's laughter.''')
                angry.alive = False
            elif d3 == 'C':
                World.give(player, 'Candy', angry)
                input('Angry man cries.')
                input('''Wish I could go back in time,
Be a baby, eat this candy...''')
                player.love_level += 1
            elif d3 == 'H':
                World.give(player, 'Hourglass', angry)
                input('Angry man smiles.')
                input('''I'll go back in time with this,
Where all I need is something sweet...''')
            if angry.saved_check:
                angry.saved = True
                player.fear_level -= 7
                player.love_level += 7
                input('Oh wait, I do have an hourglass and some candy.')
                input('''"Man is condemned to be free; because once thrown into the world, he is responsible for everything he does.
It is up to you to give life a meaning."
I choose to not rhyme my words with one another.''')
                input('Angry man holds the hourglass, turns into a little boy, eating a candy.')
                input('***Achievement unlocked!***')
                World.achievements['Salvation of a man'] = 'Gift the matches and the knife to the boy'
            menu()
    elif not angry.alive:
        input('You see the angry man, stabbed himself to death.')
        menu()


play()
