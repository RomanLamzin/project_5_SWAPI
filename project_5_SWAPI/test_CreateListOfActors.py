from project_5_SWAPI.createListOfActors import CreateListOfActors

""" Тест по выгрузке всех имён актёров в которых снимался Darth Vader"""

# ПАРАМЕТРЫ

base_url = 'https://swapi.dev/api'
get_resource = '/people/4/'  # страница Darth Vader
get_url = base_url + get_resource

# Тест

test_5 = CreateListOfActors()

# сохраняем в переменную все url по фильмам где снимался Darth Vader
urls_by_all_films = test_5.get_all_films_by_people_number_url(get_url)

# сохраняем в переменную все url  people по данным полученым из переменной urls_by_all_films
urls_by_all_people = test_5.get_all_actors_url_by_film_numbers(urls_by_all_films)

# сохраняем в переменную все имена актёров по данным полученым из переменной urls_by_all_people
all_actors_name = test_5.get_all_names_of_actors_by_urls_list(urls_by_all_people)

# создаём и записываем все имена в файл data.txt
test_5.createAndWriteListOfData(all_actors_name)

print('Тест по выгрузке имён прошёл успешно !!!')


# python -m pytest -s -v