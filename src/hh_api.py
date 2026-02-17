from abc import ABC, abstractmethod
import requests


class AbstractAPI(ABC):
    """Абстрактный класс для соединения и запроса с API вакансий"""
    @abstractmethod
    def _connect(self):
        pass

    @abstractmethod
    def load_vacancies(self, text):
        pass


class HeadHunterAPI(AbstractAPI):
    """ Класс для соединения с АПИ """
    def __init__(self):
        """Инициализирует класс, устанавливая базовый URL для API hh.ru.
           Задает параметры запроса по умолчанию: text (поисковый запрос),
           per_page (количество вакансий на странице, 20),
           page (номер страницы, начинается с 0)."""
        self.__url = "https://api.hh.ru/vacancies"
        self.__params = {"text": "", "per_page": 20, "page": 0}

    def _connect(self):
        """ Выполняет GET-запрос к API hh.ru. Если запрос успешен (код ответа 200),
            возвращает данные в формате JSON.
            В случае ошибки соединения выводит сообщение "Ошибка соединения"."""
        response = requests.get(self.__url, params=self.__params)
        if response.status_code == 200:
            return response.json()
        else:
            print("Ошибка соединения")

    def load_vacancies(self, text: str) -> list:
        """Метод запроса вакансий. Принимает строку text для поиска вакансий.
           Обновляет параметр text в self.__params для текущего поиска.
           Вызывает self._connect() для получения данных вакансий с текущей страницы.
           Из полученных вакансий извлекает только необходимую информацию."""
        self.__params["text"] = text
        all_vacancies = []
        while self.__params["page"] < 5:
            vacancies = self._connect()["items"]
            # Фильтрация вакансий внутри метода load_vacancies
            filtered_vacancies = []
            for vacancy in vacancies:
                filtered_vacancies.append({
                    "name": vacancy["name"],
                    "url": vacancy["alternate_url"],
                    "salary": vacancy["salary"],
                    "description": vacancy["snippet"]["requirement"]
                })
            all_vacancies.extend(filtered_vacancies)
            self.__params["page"] += 1
        return all_vacancies


if __name__ == "__main__":
    # Создаем экземпляр класса HeadHunterAPI
    hh_api = HeadHunterAPI()

    # Получаем вакансии по ключевому слову
    keyword = "Python"
    hh_vacancies = hh_api.load_vacancies(keyword)

    # Печатаем результаты
    for vacancy in hh_vacancies:
        print(vacancy)
