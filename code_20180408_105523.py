import webbrowser  # bulit in file


class Movie():  # class for movies
    def __init__(self, movietitle, moviestoryline, posterimage, traleryoutube):
            self.title = movietitle
            self.storyline = moviestoryline
            self.poster_image_url = posterimage
            self.trailer_youtube_url = traleryoutube

            def show_trailer(self):
                webbrowser.open(self.trailer_youtube_url)
