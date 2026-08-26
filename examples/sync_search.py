from themoviedb import TMDb


def main():
    tmdb = TMDb(key="YOUR_API_KEY")
    results = tmdb.search().multi("jack")
    for result in results:
        if result.is_movie():
            movie = tmdb.movie(result.id).details()
            print(movie, movie.overview, "\n")
        elif result.is_person():
            person = tmdb.person(result.id).details()
            print(person, person.biography, "\n")
        elif result.is_tv():
            tv = tmdb.tv(result.id).details()
            print(tv, tv.overview, "\n")


main()
