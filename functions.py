def makeurl(movie_name):
    splitted_movie_name = movie_name.split()
    formatted_name = '+'.join(splitted_movie_name)
    movie_url = "https://pahe.in/?s="+formatted_name
    return movie_url
def takeinput():
    movie_name = input("enter the movie name")

    return movie_name
def menu(movie_names):
    i=1
    for movie_name in movie_names:
        print(str(i)+'.'+movie_name)
        i += 1
    choice = input('choose a no before movie u want to download:')
    return choice

