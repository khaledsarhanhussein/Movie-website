import media
import fresh_tomatoes
toy_story=media.Movie("toy story",
 	"astory of a boy " ,
 	"https://vignette.wikia.nocookie.net/disney/images/8/80/Toy_Story_-_Poster.jpg/revision/latest?cb=20150108180742",
 	"https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar=media.Movie("avatar","a marine on an aline planet",
	"https://upload.wikimedia.org/wikipedia/sco/b/b0/Avatar-Teaser-Poster.jpg",
	"https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print avatar.storyline
#avatar.show_trailer()
interstellar =media.Movie("interstellar ",
"With our time on Earth coming to an end, a team of explorers undertakes the most important mission in human history: traveling beyond this galaxy to discover whether mankind has a future among the stars.",
"http://images6.fanpop.com/image/photos/37500000/Interstellar-Poster-interstellar-37588261-1310-2047.jpg"
,"https://www.youtube.com/watch?v=zSWdZVtXT7E")
#print interstellar.storyline
#interstellar.show_trailer()
shape_of_water=media.Movie("shape of water",
	"At a top secret research facility in the 1960s, a lonely janitor forms a unique relationship with an amphibious creature that is being held in captivity."
	,"http://t1.gstatic.com/images?q=tbn:ANd9GcQmGqEyb3hsJDLbBH_mjF8jT-30QUY6KgQhVvsJCr86QFnO4NFu",
	"https://www.youtube.com/watch?v=XFYWazblaUA")
The_Greatest_Showman =media.Movie("The Greatest Showman ",
"Celebrates the birth of show business, and tells of a visionary who rose from nothing to create a spectacle that became a worldwide sensation.",
	"http://t3.gstatic.com/images?q=tbn:ANd9GcSIBSGJLB8aasi7cB1FCPjg0L6XAw9GYZ4uQY1MsQGX2e8H_mCq",
	"https://www.youtube.com/watch?v=AXCTMGYUg9A")
red_sparrow=media.Movie("red sparrow "
	,"Ballerina Dominika Egorova is recruited to 'Sparrow School,' a Russian intelligence service where she is forced to use her body as a weapon. Her first mission, targeting a C.I.A. agent, threatens to unravel the security of both nations."
	,"http://t0.gstatic.com/images?q=tbn:ANd9GcQ_Sw8iyje2a8mnrsYRNLGzG-G50U093i76B5wHEIt7uON-O57P"
	,"https://www.youtube.com/watch?v=PmUL6wMpMWw")
Bilal_A_New_Breed_of_Hero=media.Movie("Bilal: A New Breed of Hero",
	"A thousand years ago, one boy with a dream of becoming a great warrior is abducted with his sister and taken to a land far away from home. Thrown into a world where greed and injustice rule all, Bilal finds the courage to raise his voice and make a change. Inspired by true events, this is a story of a real hero who earned his remembrance in time and history",
	"http://t0.gstatic.com/images?q=tbn:ANd9GcTdxw63--qufzVji5uw5_-Fe0gQjLOW_VwNBxaGSojcVyAKgioS",
	"https://www.youtube.com/watch?v=memYLNa-7wQ")
movies={toy_story,avatar,interstellar,shape_of_water,The_Greatest_Showman,red_sparrow ,Bilal_A_New_Breed_of_Hero}
fresh_tomatoes.open_movies_page(movies)

