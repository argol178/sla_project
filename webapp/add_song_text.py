from webapp.model import db, Songs

def get_new_song():
    songs_list = [
        {'title' :'Nothing Else Matters', 'artist' : 'Metallica', 'text' : """So close, no matter how far
Couldn't be much more from the heart
Forever trust in who we are
And nothing else matters
Never opened myself this way
Life is ours, we live it our way
All these words, I don't just say
And nothing else matters
Trust I seek and I find in you
Every day for us something new
Open mind for a different view
And nothing else matters
Never cared for what they do
Never cared for what they know
And I know
So close, no matter how far
Couldn't be much more from the heart
Forever trusting who we are
And nothing else matters"""},
        {'title' : 'Highway to Hell', 'artist' : 'AC/DC', 'text' : """Living easy, living free
Season ticket on a one-way ride
Asking nothing, leave me be
Taking everything in my stride
Don't need reason, don't need rhyme
Ain't nothing I would rather do
Going down, party time
My friends are gonna be there too
I'm on the highway to hell
On the highway to hell
Highway to hell
I'm on the highway to hell
No stop signs, speed limit
Nobody's gonna slow me down
Like a wheel, gonna spin it
Nobody's gonna mess me around
Hey Satan, paid my dues
Playing in a rocking band
Hey mama, look at me
I'm on my way to the promised land, whoo!
I'm on the highway to hell
Highway to hell
I'm on the highway to hell
Highway to hell
Don't stop me
I'm on the highway to hell
On the highway to hell
I'm on the highway to hell
On the highway
Yeah, highway to hell
I'm on the highway to hell
Highway to hell
Highway to hell
And I'm going down
All the way
Whoa!
I'm on the highway to hell"""},
        {'title' : 'Hotel California', 'artist' : 'Eagles', 'text' : """On a dark desert highway
Cool wind in my hair
One smell of colitas
Rising up through the air
Up ahead in the distance
I saw a shimmering light
My head grew heavy, and my sight grew dim
I had to stop for the night
There she stood in the doorway
I heard the mission bell
And I was thinking to myself
This could be Heaven or this could be Hell
Then she lit up a candle
And she showed me the way
There were voices down the corridor
I thought I heard them say
Welcome to the Hotel California
Such a lovely place
Such a lovely place (background)
Such a lovely face
Plenty of room at the Hotel California
Any time of year
Any time of year (background)
You can find it here
Her mind is Tiffany-twisted
Shes's got the Mercedes-Bends
She's got a lot of pretty, pretty boys
That she calls friends
How they dance in the courtyard
Sweet summer sweat
Some dance to remember
Some dance to forget
So I called up the Captain
Please bring me my wine
He said
We haven't had that spirit here since 1969
And still those voices are calling from far away
Wake you up in the middle of the night
Just to hear them say
Welcome to the Hotel California
Such a lovely Place
Such a lovely Place (background)
Such a lovely face
They're livin' it up at the Hotel California
What a nice surprise
What a nice surprise (background)
Bring your alibies
Mirrors on the ceiling
The pink champagne on ice
And she said
We are all just prisoners here
Of our own device
And in the master's chambers
They gather for the feast
They stab it with their steely knives
But they just can't kill the beast
Last thing I remember
I was running for the door
I had to find the passage back
To the place I was before
Relax said the nightman
We are programed to recieve
You can check out any time you like
But you can never leave"""},
        {'title' : 'Numb', 'artist' : 'Linkin Park', 'text' : """I'm tired of being what you want me to be
Feeling so faithless, lost under the surface
I don't know what you're expecting of me
Put under the pressure of walking in your shoes
Caught in the undertow, just caught in the undertow
Every step that I take is another mistake to you
Caught in the undertow, just caught in the undertow
I've become so numb, I can't feel you there
Become so tired, so much more aware
By becoming this all I want to do
Is be more like me and be less like you
Can't you see that you're smothering me?
Holding too tightly, afraid to lose control
'Cause everything that you thought I would be
Has fallen apart right in front of you
Caught in the undertow, just caught in the undertow
Every step that I take is another mistake to you
Caught in the undertow, just caught in the undertow
And every second I waste is more than I can take!
I've become so numb, I can't feel you there
Become so tired, so much more aware
By becoming this all I want to do
Is be more like me and be less like you
And I know I may end up failing too
But I know you were just like me with someone disappointed in you
I've become so numb, I can't feel you there
Become so tired, so much more aware
By becoming this all I want to do
Is be more like me and be less like you
I've become so numb, I can't feel you there
I'm tired of being what you want me to be
I've become so numb, I can't feel you there
I'm tired of being what you want me to be"""},
        {'title' : 'Word UP!', 'artist' : 'Korn', 'text' : """Yo pretty ladies around the world
Got a weird thing to show you
So tell all the boys and girls
Tell your brother, your sister and your mamma too
We're about to go down
And you know just what to do
Wave your hands in the air like you don't care
Glide by the people as they start to look and stare
Do your dance, do your dance, do your dance quick mama
Come on baby tell me what's the word
Word up (up up) everybody say
When you hear the call you've got to get it on the way
Word up (up up) it's the code word
No matter where you say it you know that you'll be heard
Now all you sucker DJ's who think you're fly
There's got to be a reason and we know the reason why
You try to put on those airs and act real cool
But you got to realize that you're acting like fools
If there's music we can use it
Be free to dance
We don't have the time for psychological romance
No romance, no romance, no romance for me mama
Come on baby tell me what's the word
Word up (up up) everybody say
When you hear the call you've got to get it on the way
Word up (up up) it's the code word
No matter where you say it you know that you'll be heard
Word up (up up) everybody say
When you hear the call you've got to get it on the way
Word up (up up) it's the code word
No matter where you say it you know that you'll be heard
Word up (up up) everybody say
When you hear the call you've got to get it on the way
Word up (up up) it's the code word
No matter where you say it you know that you'll be heard
"""},
        {'title' : 'I want it all', 'artist' : 'Queen', 'text' : """Adventure seeker on an empty street
Just an alley creeper, light on his feet
A young fighter screaming, with no time for doubt
With the pain and anger can't see a way out
It ain't much I'm asking, I heard him say
Gotta find me a future move out of my way
I want it all, I want it all, I want it all, and I want it now
I want it all, I want it all, I want it all, and I want it now
Listen all you people, come gather round
I gotta get me a game plan, gotta shake you to the ground
But just give me, huh, what I know is mine
People do you hear me, just gimme the sign
It ain't much I'm asking, if you want the truth
Here's to the future for the dreams of youth
I want it all (give it all I want it all)
I want it all (yeah)
I want it all and I want it now
I want it all (yes I want it all)
I want it all hey
I want it all and I want it now
I'm a man with a one track mind
So much to do in one lifetime (people do you hear me)
Not a man for compromise and where's and why's and living lies
So I'm living it all, yes I'm living it all
And I'm giving it all, and I'm giving it all
Oh oh yeah yeah ha ha ha ha ha
Yeah yeah yeah yeah
I want it all
It ain't much I'm asking, if you want the truth
Here's to the future
Hear the cry of youth (hear the cry of youth) (hear the cry of youth)
I want it all, I want it all, I want it all and I want it now
I want it all yeah yeah yeah
I want it all, I want it all and I want it now
Oh oh oh oh oh
And I want it (now)
I want it, I want it
Oh ha"""}]
    for songs in songs_list:
        title = songs['title'] 
        artist = songs['artist']
        text = songs['text']

        save_songs(title, artist, text)

def save_songs(title, artist, text):
    new_song = Songs(song_title = title, artist = artist, text = text)
    db.session.add(new_song)
    db.session.commit()

