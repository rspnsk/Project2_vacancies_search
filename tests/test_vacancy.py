import pytest

from src.vacancy import Vacancy


def test_initialization_with_salary(sample_vacancy):
    """Проверка инициализации с зарплатой"""
    assert sample_vacancy.name == "Python Developer"
    assert sample_vacancy.salary_from == 100000
    assert sample_vacancy.salary_to == 150000
    assert sample_vacancy.url == "https://hh.ru/vacancy/123 "
    assert sample_vacancy.description == "Требуется Python разработчик"


def test_initialization_without_salary(vacancy_without_salary):
    """Проверка инициализации без зарплаты"""
    assert vacancy_without_salary.salary_from == 0
    assert vacancy_without_salary.salary_to == 0


def test_partial_salary():
    """Проверка частичного указания зарплаты"""
    # Только 'from'
    vacancy = Vacancy(
        name="Test",
        salary={"from": 80000},
        url="test.com",
        description="Test"
    )
    assert vacancy.salary_from == 80000
    assert vacancy.salary_to == 0

    # Только 'to'
    vacancy = Vacancy(
        name="Test",
        salary={"to": 200000},
        url="test.com",
        description="Test"
    )
    assert vacancy.salary_from == 0
    assert vacancy.salary_to == 200000


def test_comparison():
    """Проверка оператора сравнения"""
    vacancy1 = Vacancy("Job1", {"from": 100000}, "url1", "desc1")
    vacancy2 = Vacancy("Job2", {"from": 150000}, "url2", "desc2")

    assert vacancy1 < vacancy2
    assert not (vacancy2 < vacancy1)


def test_slots_restriction(sample_vacancy):
    """Проверка ограничения __slots__"""
    with pytest.raises(AttributeError):
        sample_vacancy.new_attribute = "test"
