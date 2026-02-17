import json

import pytest

from src.json_saver import JSONSaver


def test_get_vacancies_nonexistent_file(tmp_path):
    """Проверка чтения несуществующего файла"""
    saver = JSONSaver(path=tmp_path / "nonexistent.json")
    with pytest.raises(FileNotFoundError):
        saver.get_vacancies()


# Тестирование метода save_vacancies
def test_save_vacancies(json_saver, test_file, vacancy_data):
    # Создаем тестовый файл с пустым списком вакансий
    with open(test_file, "w", encoding="utf-8") as f:
        json.dump([], f)

    # Вызываем метод save_vacancies
    json_saver.save_vacancies(vacancy_data)

    # Проверяем результат
    with open(test_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert len(data) == 1
    assert data[0]["name"] == "Python Developer"
    assert data[0]["url"] == "https://example.com/vacancy1"
    assert data[0]["salary"] == {"from": 100000, "to": 150000}
    assert data[0]["description"] == "Опыт работы с Python"


# Тестирование метода delete_vacancies
def test_delete_vacancies(json_saver, test_file, vacancy_data):
    # Создаем тестовый файл с одной вакансией
    with open(test_file, "w", encoding="utf-8") as f:
        json.dump([vacancy_data], f)

    # Проверяем, что файл содержит одну вакансию
    with open(test_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert len(data) == 1

    # Вызываем метод delete_vacancies
    json_saver.delete_vacancies()

    # Проверяем, что файл очищен
    with open(test_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert len(data) == 0


