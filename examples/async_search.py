import asyncio

from themoviedb import aioTMDb


async def main():
    tmdb = aioTMDb(key="YOUR_API_KEY")
    results = await tmdb.search().multi("jack")
    for result in results:
        if result.is_movie():
            movie = await tmdb.movie(result.id).details()
            print(movie, movie.overview, "\n")
        elif result.is_person():
            person = await tmdb.person(result.id).details()
            print(person, person.biography, "\n")
        elif result.is_tv():
            tv = await tmdb.tv(result.id).details()
            print(tv, tv.overview, "\n")


asyncio.run(main())
