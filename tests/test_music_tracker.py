from lib.music_tracker import *

def test_music_tracker():
    my_music = music_tracker()
    assert my_music.tracks == []
    my_music.add_tracks("yellow sub")
    my_music.add_tracks("yellow sub")
    assert my_music.tracks == ['yellow sub']

def test_show_tracks():
    my_music = music_tracker()
    my_music.add_tracks('penny lane')
    my_music.add_tracks('yellow sub')
    assert my_music.display_tracks() == ['penny lane', 'yellow sub']     