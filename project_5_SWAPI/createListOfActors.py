import requests

"""  Класс по работе с https://swapi.dev/
  умеет возвращать списки url фильмов, списки url актёров, списки имён актёров, запись списка в файл"""


class CreateListOfActors:

    # МЕТОДЫ

    def get_all_films_by_people_number_url(self, url):
        """Метод который возвращает список фильмов в которых снимался актёр"""
        info_films = requests.get(url)
        info_films_list = info_films.json().get('films')
        get_sts = info_films.status_code
        print(f'Статус код  = {get_sts}')
        print(info_films_list)
        return info_films_list

    def get_all_actors_url_by_film_numbers(self, url_film_list):
        """Метод который возвращает список актёров по номеру фильма"""

        actors_list_nuber_url = set()  # делаем set для наполнения его уникальным списком characters по каждому фильму

        for url_film in url_film_list:
            get_list_actors = requests.get(url_film)

            actors_list_url = set(get_list_actors.json().get('characters'))
            get_sts = get_list_actors.status_code  # проверка статус кода
            print(f'Статус код  = {get_sts}')
            actors_list_nuber_url.update(actors_list_url)
        print("Формирование списка актёров по номерам фильмов закончено УСПЕШНО !!!")
        print(actors_list_nuber_url)
        return actors_list_nuber_url

    def get_all_names_of_actors_by_urls_list(self, url_people_list):
        """Метод который возвращает список имён актёров по его номеру (people/#)"""
        actors_name_list = []  # делаем list для наполнения его уникальным списком имён актёров по каждой ссылке people/#

        for url_people in url_people_list:
            get_list_actors_name = requests.get(url_people)

            actors_list_name = get_list_actors_name.json().get('name')
            get_sts = get_list_actors_name.status_code  # проверка статус кода
            print(f'Статус код  = {get_sts}  по актёру {url_people} ')
            actors_name_list.append(actors_list_name)

        print("Формирование списка имён актёров по people/# закончено УСПЕШНО !!!")
        print(actors_name_list)
        return actors_name_list

    def createAndWriteListOfData(self, list_of_data):
        """ Метод по созданию файла и записи в него списка данных"""

        with open('data.txt', 'w', encoding="utf-8") as file:
            for some_data in list_of_data:
                file.write(some_data + '\n')

        print("Запись в файл прошла успешно !!!")
