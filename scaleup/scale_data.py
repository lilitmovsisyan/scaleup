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
