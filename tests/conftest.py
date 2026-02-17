import pytest
from src.hh_api import HeadHunterAPI
from src.json_saver import JSONSaver
from src.vacancy import Vacancy


# Фикстура для создания экземпляра класса HeadHunterAPI
@pytest.fixture
def hh_api():
    return HeadHunterAPI()


# Фикстура для создания тестового файла
@pytest.fixture
def test_file(tmp_path):
    file_path = tmp_path / "test_vacancies.json"
    return str(file_path)


# Фикстура для создания экземпляра JSONSaver.
@pytest.fixture
def json_saver(test_file):
    return JSONSaver(test_file)


# Фикстура для создания тестовых данных вакансии. (возвращает словарь (dict)).
@pytest.fixture
def vacancy_data():
    return {"name": "Python Developer",
            "url": "https://example.com/vacancy1",
            "salary": {"from": 100000, "to": 150000},
            "description": "Опыт работы с Python"}


# Фикстуры для создания тестовых данных вакансии. (возвращает экземпляр класса Vacancy).
@pytest.fixture
def sample_vacancy():
    return Vacancy(
        name="Python Developer",
        salary={"from": 100000, "to": 150000},
        url="https://hh.ru/vacancy/123 ",
        description="Требуется Python разработчик")


@pytest.fixture
def vacancy_without_salary():
    return Vacancy(
        name="Java Developer",
        salary=None,
        url="https://hh.ru/vacancy/456 ",
        description="Требуется Java разработчик")


def json_sav_test():
    """Создает экземпляр JSONSaver для тестирования."""
    return JSONSaver(path="test_vacancies.json")


@pytest.fixture
def sample_vacancies():
    return [
        Vacancy("Python Developer", {"from": 80000, "to": 120000}, "https://example.com/1",
                "Looking for Python developer with Django and Flask experience"),
        Vacancy("Java Developer", {"from": 90000, "to": 130000}, "https://example.com/2",
                "We are hiring a Java developer with Spring Boot expertise"),
        Vacancy("Frontend Developer", {}, "https://example.com/3",
                "Need JavaScript and React.js skilled developer"),
        Vacancy("Data Analyst", {"from": 70000}, "https://example.com/4",
                "Experience with SQL and data visualization is required"),
    ]
