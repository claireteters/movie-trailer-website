import fresh_tomatoes
import media

"""Creates seven Movie objects, initialising these objects with title, storyline,
    poster image link, video trailer link, release year, and movie rating."""
def main():
    toy_story = media.Movie("Toy Story", 
                    "A story a boy and his toys that come to life.", 
                    "https://vignette.wikia.nocookie.net/jack-millers-webpage-of-disney/images/7/75/Toy_Story_DVD_cover.jpg/revision/latest?cb=20150609223407", 
                    "https://www.youtube.com/watch?v=rNk1Wi8SvNc",
                    "1995",
                    "G")


    avatar = media.Movie("Avatar",
                    "A marine on an alien planet.",
                    "https://cps-static.rovicorp.com/2/Open/20th%20Century%20Fox/Avatar/_9by13/_derived_jpg_q90_410x410_m0/Avatar-PosterArt.jpg?partner=allrovi.com",
                    "https://www.youtube.com/watch?v=6ziBFh3V1aM",
                    "2009",
                    "PG-13")
    

    brother_bear = media.Movie("Brother Bear",
                    "A man turns into a bear, and can only be changed back if he embraces his new identity.",
                    "https://vignette.wikia.nocookie.net/transcripts/images/f/fd/Disney%27s_Brother_Bear_-_iTunes_DVD_Poster.jpeg/revision/latest?cb=20170206001444",
                    "https://www.youtube.com/watch?v=hVVY6i7vJXU",
                    "2003",
                    "G")   
    

    lion_king = media.Movie("The Lion King",
                    "When a lion cub decides to start a new life alone, he is in for more than he expected.",
                    "https://cdn-images-1.medium.com/max/1000/1*ibiKVRfLzrsFAdye8Mj4WQ.jpeg",
                    "https://www.youtube.com/watch?v=zx3LT_G3cIA",
                    "1994",
                    "G")
       
                    
    shark_tail = media.Movie("Shark Tale",
                    "A small fish and a shark work together to become famous, and live the lavish life.",
                    "http://cdn7.nflximg.net/images/1837/3021837.jpg",
                    "https://www.youtube.com/watch?v=mp2SbaK8dDg",
                    "2004",
                    "PG")
     

    zootopia = media.Movie("Zootopia",
                    "A little rabbit leaves her home for the big city to accomplsh the impossibe.",
                    "https://fanart.tv/fanart/movies/269149/movieposter/zootopia-573f3f2c6d6ee.jpg",
                    "https://www.youtube.com/watch?v=yCOPJi0Urq4",
                    "2016",
                    "PG")


    '''storing the movie objects in a list'''
    movies = [toy_story, avatar, brother_bear, lion_king, shark_tail, zootopia]
    '''Open the movie website in the user's browser with all of the movies above'''
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
