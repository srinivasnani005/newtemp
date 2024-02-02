import telegram


def my_bot():
    return telegram.Bot(token='6810685025:AAG3twwDGZ8tPC-qdT9SwP0XKulrvIBWe_A')


def my_bot_token():
    return '6810685025:AAG3twwDGZ8tPC-qdT9SwP0XKulrvIBWe_A'


def scrap_master():
    return 'https://www.1377x.to/'


def movies_api():
    url = "https://api.themoviedb.org/3/movie/now_playing" #api reference https://www.themoviedb.org
    api_key = "c09817b546bde3e23e32f891feefce38"
    language = "en-US"
    limit_page = "1"
    movies_api_url = f"{url}?{api_key}&language={language}&page={limit_page}"
    return movies_api_url
