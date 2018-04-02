import media
import fresh_tomatoes

avatar = media.Movie(   #a new movie
    "avatar",
    "a marine on an aline planet",
    "https://upload.wikimedia.org/wikipedia/sco/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
    )
interstellar = media.Movie(  #a new movie
    "interstellar ",
    "With our time on Earth coming to an end, ",
    "http://images6.fanpop.com/image/photos/37500000/Interstella" +
    "r-Poster-interstellar-37588261-1310-2047.jpg",
    "https://www.youtube.com/watch?v=zSWdZVtXT7E"
    )

shape_of_water = media.Movie(   #a new movie
    "shape of water",
    " unique relationship with an that is being held in captivity." +
    "unique relaus creature that is being held in captivity.",
    "http://t1.gstatic.com/images?q=tbn:ANd9Gc" +
    "QmGqEyb3hsJDLbBH_mjF8jT-30QUY6KgQhVvsJCr86QFnO4NFu",
    "https://www.youtube.com/watch?v=XFYWazblaUA"
    )
The_Greatest_Showman = media.Movie(   #a new movie
    "The Greatest Showman ",
    "Celebrates the birth of show business," +
    " and tells of a visionary who rose from nothing to " +
    "create a spectacle that became a worldwide sensation.",
    "http://t3.gstatic.com/images?q=tbn:ANd" +
    "9GcSIBSGJLB8aasi7cB1FCPjg0L6XAw9GYZ4uQY1MsQGX2e8H_mCq",
    "https://www.youtube.com/watch?v=AXCTMGYUg9A"
    )

red_sparrow = media.Movie( #a new movie
    "red sparrow ",
    "Ballerina Dominika Egorova is recruited to 'Sparrow School,' " +
    "a Russian intelligence service where she is forced to use her" +
    "body as a weapon. Her first mission, targeting a C.I.A. agent, " +
    "threatens to unravel the security of both nations.",
    "http://t0.gstatic.com/images?q=tbn:ANd9GcQ_Sw8iyj" +
    "e2a8mnrsYRNLGzG-G50U093i76B5wHEIt7uON-O57P",
    "https://www.youtube.com/watch?v=PmUL6wMpMWw"
    )
Bilal_A_New_Breed_of_Hero = media.Movie(           #a new movie
   "Bilal: A New Breed of Hero",
   "A thousand years ago, one boy with a dream of becoming a great" +
   " warrior is abducted with his sister and taken to awa""from home." ,
   "http://t0.gstatic.com/images?q=tbn:ANd9Gc" +
   "Tdxw63--qufzVji5uw5_-Fe0gQjLOW_VwNBxaGSojcVyAKgioS",
   "https://www.youtube.com/watch?v=memYLNa-7wQ"
   )


toy_story = media.Movie(  #a new movie
    "toy story",
    "astory of a boy ",
    "https://vignette.wikia.nocookie.net/disney/images" +
    "/8/80/Toy_Story_-_Poster.jpg/revision/latest?cb=20150108180742",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc"
    )
movies = {      #all movies
    toy_story,
    avatar,
    interstellar,
    shape_of_water,
    The_Greatest_Showman,
    red_sparrow,
    Bilal_A_New_Breed_of_Hero
    }

fresh_tomatoes.open_movies_page(movies)
