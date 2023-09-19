

#As a user
#So that I can keep track of my music listening
# I want to add tracks I've listened to and see a list of them.

class music_tracker():
    def __init__(self):
        self.tracks = []

    def add_tracks(self, track):
        if track not in self.tracks:
            self.tracks.append(track)
    def display_tracks(self):
        return self.tracks            

    