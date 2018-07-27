import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", 
                        "A story a boy and his toys that come to life.", 
                        "http://www.filmtakeout.com/wp-content/uploads/2014/07/TOYSTORY.jpg", 
                        "https://www.youtube.com/watch?v=rNk1Wi8SvNc")

# print(toy_story.storyline)
# toy_story.show_trailer()

avatar = media.Movie("Avatar",
                    "A marine on an alien planet.",
                    "https://cps-static.rovicorp.com/2/Open/20th%20Century%20Fox/Avatar/_9by13/_derived_jpg_q90_410x410_m0/Avatar-PosterArt.jpg?partner=allrovi.com",
                    "https://www.youtube.com/watch?v=6ziBFh3V1aM")
# print(avatar.storyline)
# avatar.show_trailer()

brother_bear = media.Movie("Brother Bear",
                            "A man turns into a bear, and can only be changed back if he embraces his new identity.",
                            "https://vignette.wikia.nocookie.net/transcripts/images/f/fd/Disney%27s_Brother_Bear_-_iTunes_DVD_Poster.jpeg/revision/latest?cb=20170206001444",
                            "https://www.youtube.com/watch?v=hVVY6i7vJXU")   
# print(brother_bear.storyline)
# brother_bear.show_trailer()

movies = [toy_story, avatar, brother_bear]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
