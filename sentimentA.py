import sys
import json
from os.path import join, dirname
from watson_developer_cloud import AlchemyLanguageV1
from time import sleep
import vlc


alchemy_language = AlchemyLanguageV1(api_key='2028a073cb9e01642fc80f06c315946833cdb0a2')

neutralScene = "Harry, who was on a top bunk above Ron, lay staring up at the\
canvas ceiling of the tent, watching the glow of an occasional leprechaun\
lantern flying overhead, and picturing again some of\
Krum's more spectacular moves. He was itching to get back on his\
own Firebolt and try out the Wronski Feint. . . . Somehow Oliver\
Wood had never managed to convey with all his wriggling diagrams\
what that move was supposed to look like. . . . Harry saw\
himself in robes that had his name on the back, and imagined the\
sensation of hearing a hundred-thousand-strong crowd roar, as\
Ludo Bagman's voice echoed throughout the stadium, I give\
you . . . Potter!"

fearScene = 'Harry never knew whether or not he had actually dropped off to\
sleep - his fantasies of flying like Krum might well have slipped\
into actual dreams - all he knew was that, quite suddenly, Mr.\
Weasley was shouting.\
"Get up! Ron - Harry - come on now, get up, this is urgent!"\
Harry sat up quickly and the top of his head hit canvas.\
"" S matter?"" he said.\
Dimly, he could tell that something was wrong. The noises in\
the campsite had changed. The singing had stopped. He could hear\
screams, and the sound of people running. He slipped down from\
the bunk and reached for his clothes, but Mr. Weasley, who had\
pulled on his jeans over his own pajamas, said, "No time, Harry -\
just grab a jacket and get outside - quickly!"\
Harry did as he was told and hurried out of the tent, Ron at his\
heels.\
By the light of the few fires that were still burning, he could see\
people running away into the woods, fleeing something that was\
moving across the field toward them, something that was emitting\
odd flashes of light and noises like gunfire. Loud jeering, roars of\
laughter, and drunken yells were drifting toward them; then came\
a burst of strong green light, which illuminated the scene"'

print(json.dumps(alchemy_language.emotion(text=neutralScene), indent=2))
print(json.dumps(alchemy_language.emotion(text=fearScene), indent=2))
#print alchemy_language.emotion(text=fearScene).get("docEmotions").get("anger")
p = vlc.MediaPlayer("01. Thundertruck.mp3")
p.play()
for i in neutralScene:
	sleep(0.01)
	sys.stdout.write(i)
	sys.stdout.flush()
p.pause()
p = vlc.MediaPlayer("05 Alors On Danse (Radio Edit).mp3")
p.play()
for i in fearScene:
	sleep(0.01)
	sys.stdout.write(i)
	sys.stdout.flush()

