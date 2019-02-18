

#*******************************
#USER INFORMATION - currently only edited in source code

#scale sets:
chroma_tones = ["A","B","C","D","E","F","G","Ab/G#","Bb/A#","Db/C#","Eb/D#","F#/Gb"]
beginner = ["G", "D", "A"]

#mode sets:
major_only = ["major", "major arpeggio", "chromatic scale"]
bi_mode = ["major", "minor", "major arpeggio", "minor arpeggio"]
more_minors = ["major", "major arpeggio", "minor arpeggio", "melodic minor", "harmonic minor", "natural minor"]

#bowing patterns:
main_bowing = ["separate bows", "slurred, two notes to a bow"]
more_bowing = ["separate bows", "slurred, two to a bow", "slurred, four to a bow", "slurred, three to a bow"]

#user dictionaries:
lilit = {
    "my_scale_set": chroma_tones,
    "my_mode": more_minors,
    "my_bow_pattern": main_bowing
    }
beginners = {
    "my_scale_set": beginner,
    "my_mode": major_only,
    "my_bow_pattern": main_bowing
    }
test = {
    "my_scale_set": [1,2,3],
    "my_mode": [4,5],
    "my_bow_pattern": [6]
    }

#database of all users:
user_list = {
    "lilit":lilit,
    "beginner": beginners,
    "test": test
    }

#*******************************
#FUNCTIONS


#returns random scale:
from random import randint
def random_scale(scale_set, mode, bow_pattern):
    s = len(scale_set)
    m = len(mode)
    b = len(bow_pattern)
    s_i = randint(1,s) -1
    m_i = randint(1,m) -1
    b_i = randint(1,b) -1
    practice = '{} {}, {}'.format(scale_set[s_i],mode[m_i],bow_pattern[b_i])
    return practice

#returns random scale from user's set:
def users_random_scale(username):
    a_scale = random_scale(username["my_scale_set"], username["my_mode"],username["my_bow_pattern"])
    return a_scale

#returns the number of different scale variations possible out of the user's set:
def no_of_combos(username):
    max_combos = 1
    for key in username:
       max_combos *= len(username[key])
    return max_combos

#prints user's random scale to console:
    """checks if the random scale has already been printed,
    and if so generates another to avoid duplication:
        initiates go_again repeat function
            and indicates when all possible combos have been generated"""
def generate_scale(username,scale_checklist):
    limit = no_of_combos(username)
    if len(scale_checklist) == limit:
        return ("""
You have now tried every scale variation that you know so far.
You can now learn a new scale, practice a piece of music, or...
perhaps you'd like to try these scales again, in a different random order?
""")
        scale_checklist = []
        go_again(username, scale_checklist)
    else:
        scale = users_random_scale(username)
        if scale in scale_checklist:
            generate_scale(username, scale_checklist)
        else:
            print ()
            print (scale)
            print ()
            scale_checklist.append(scale)
#            go_again(username, scale_checklist)

#*******************************
def run_scale_gen():
    name = lilit
    scale_list = []
    generate_scale(name, scale_list)
#*******************************


"""*******************************
#BUGS NOT YET FIXED#

(1) if i enter the name incorrectly, it successfully initiates re-prompt,
but then when the name is entered correctly, it produces a "NoneType" error.

*NOTE TO SELF*
#if username is not None:
#suggestion from stackoverflow.com for NoneType error.
but now im getting another one elsewhere...what's the issue?

(2) function: no_of_combos(u), variable: max_combos =*len(u[key])
# danger - what if there is an empty list stored in the dict? then *0!

(3) see function: user_selection

*********************************"""
