"""
File: my_drawing.py
Name: Zi-Ti
----------------------
My drawing by Python
"""

from campy.graphics.gobjects import GOval, GLine, GLabel, GPolygon
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


FACE = 300
NOSE = 40
EYE = 20
EAR = 25
GLASSES = 80
BLUSH = 30
MOVE_M = 10
DOT = 30
HEAD = 50

# Global Variable
window = GWindow(width=800, height=500, title='Me and the Japanese Mascot')
turn = 0
turn_label = GLabel('turn: '+str(turn))


def main():
    """
    Title: Me and the Japanese Mascot

    I've been to Hokkaido a few days ago. Walking on the street with
    the Japanese Mascot, full of happiness. It made a lot of sound like "Aah..aah.aah...",
    lots of tourists imitating the sound, including me.
    Hope the crow will bless me to learn Python well. HaHa.
    """

    # Little Me
    face = GOval(FACE, FACE+10, x=(window.width-FACE)/2, y=FACE+75)
    face.filled = 'True'
    face.fill_color = 'blanchedalmond'
    face.color = 'blanchedalmond'

    nose = GOval(NOSE, NOSE+18, x=(window.width-NOSE)/2, y=FACE+63)
    nose.filled = 'True'
    nose.fill_color = 'blanchedalmond'
    nose.color = 'blanchedalmond'

    l_eye = GOval(EYE, EYE, x=(window.width/2-FACE/4-10), y=FACE+85)
    l_eye.filled = 'True'
    r_eye = GOval(EYE, EYE, x=(window.width/2+FACE/4-10), y=FACE+85)
    r_eye.filled = 'True'
    l_ear = GOval(EAR, EAR*1.5, x=window.width/4+40, y=window.height-25)
    l_ear.filled = 'True'
    l_ear.fill_color = 'blanchedalmond'
    l_ear.color = 'blanchedalmond'
    r_ear = GOval(EAR, EAR*1.5, x=window.width*3/4-65, y=window.height-25)
    r_ear.filled = 'True'
    r_ear.fill_color = 'blanchedalmond'
    r_ear.color = 'blanchedalmond'
    r_glasses = GOval(GLASSES, 5, x=r_eye.x+EYE/2-GLASSES/2, y=window.height/2+120)
    r_glasses.color = 'maroon'
    l_glasses = GOval(GLASSES, 5, x=l_eye.x+EYE/2-GLASSES/2, y=window.height/2+120)
    l_glasses.color = 'maroon'
    l_glassesleg = GLine(l_eye.x+EYE/2-GLASSES/2, window.height/2+126, window.width/4+57, window.height-28)
    l_glassesleg.color = 'maroon'
    r_glassesleg = GLine(r_eye.x+EYE/2+GLASSES/2, window.height/2+126, window.width*3/4-58, window.height-28)
    r_glassesleg.color = 'maroon'
    blush1 = GOval(BLUSH, BLUSH/1.8)
    blush1.filled = 'True'
    blush1.fill_color = 'indianred'
    blush1.color = 'indianred'
    blush2 = GOval(BLUSH, BLUSH/1.8)
    blush2.filled = 'True'
    blush2.fill_color = 'indianred'
    blush2.color = 'indianred'
    mouth = GOval(20, 50, x=(window.width-20)/2, y=window.height-85)
    mouth.filled = 'True'
    mouth.fill_color = 'indianred'
    mouth.color = 'indianred'

    onmouseclicked(crow)

    window.add(l_eye)
    window.add(r_eye)
    window.add(face)
    window.add(nose)
    window.add(l_ear)
    window.add(r_ear)
    window.add(r_glasses)
    window.add(l_glasses)
    window.add(l_glassesleg)
    window.add(r_glassesleg)
    window.add(blush1, x=300+MOVE_M*0.5, y=FACE+120+MOVE_M*1)
    window.add(blush2, x=300+MOVE_M*16.5, y=FACE+120+MOVE_M*1)
    window.add(mouth)


def crow(mouse):
    global turn, window
    if turn == 0:
        dot1 = GOval(DOT, DOT, x=100, y=100)
        dot1.filled = 'True'
        window.add(dot1)
    elif turn == 1:
        dot2 = GOval(DOT, DOT, x=220, y=100)
        dot2.filled = 'True'
        window.add(dot2)
    elif turn == 2:
        dot3 = GOval(DOT, DOT, x=340, y=100)
        dot3.filled = 'True'
        window.add(dot3)
    elif turn == 3:
        head = GOval(HEAD*1.3, HEAD*1.2, x=630, y=80)
        head.filled = 'True'
        body = GOval(HEAD*2.3, HEAD/1.2, x=530, y=100)
        body.filled = 'True'

        beak = GPolygon()
        beak.add_vertex((650, 80+10))
        beak.add_vertex((750, 80+10))
        beak.add_vertex((720, 90+10))
        beak.add_vertex((750, 100+10))
        beak.add_vertex((650, 100+10))
        eye_bird = GOval(12, 12, x=665, y=90)
        eye_bird.filled = 'True'
        eye_bird.fill_color = 'white'

        tail = GPolygon()
        tail.add_vertex((570, 110))
        tail.add_vertex((470, 102))
        tail.add_vertex((500, 118))
        tail.add_vertex((470, 123))
        tail.add_vertex((500, 128))
        tail.add_vertex((470, 140))
        tail.add_vertex((570, 125))
        tail.filled = 'True'

        wing1 = GPolygon()
        wing1.add_vertex((604, 100))
        wing1.add_vertex((608, 40))
        wing1.add_vertex((590, 70))
        wing1.add_vertex((573, 40))
        wing1.add_vertex((580, 100))
        wing1.filled = True

        wing2 = GPolygon()
        wing2.add_vertex((604, 120+10))
        wing2.add_vertex((608, 180+10))
        wing2.add_vertex((590, 150+10))
        wing2.add_vertex((573, 180+10))
        wing2.add_vertex((580, 120+10))
        wing2.filled = True

        window.add(head)
        window.add(body)
        window.add(beak)
        window.add(eye_bird)
        window.add(tail)
        window.add(wing1)
        window.add(wing2)
    turn += 1


if __name__ == '__main__':
    main()
