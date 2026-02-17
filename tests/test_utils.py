from src.utils import sort_vacancies, get_top_vacancies, filter_vacancies


def test_sort_empty_list():
    """Тестирование функции с пустым списком."""
    vacancies = []
    sorted_vacancies = sort_vacancies(vacancies)

    assert sorted_vacancies == []


def test_sort_single_item():
    """Тестирование функции с одним элементом."""
    vacancies = [{'name': 'Only Vacancy', 'salary': 60000}]
    sorted_vacancies = sort_vacancies(vacancies)

    assert sorted_vacancies == vacancies


def test_get_top_vacancies():
    """Тестирование функции получения топ вакансий."""
    vacancies = [
        {'name': 'Junior Developer', 'salary': 50000},
        {'name': 'Senior Developer', 'salary': 100000},
        {'name': 'Middle Developer', 'salary': 75000},
    ]

    top_vacancies = get_top_vacancies(vacancies, 2)
    assert len(top_vacancies) == 2
    assert top_vacancies[0]['name'] == 'Junior Developer'
    assert top_vacancies[1]['name'] == 'Senior Developer'


def test_get_top_more_than_available():
    """Тестирование функции при запросе больше вакансий, чем доступно."""
    vacancies = [
        {'name': 'Junior Developer', 'salary': 50000},
        {'name': 'Senior Developer', 'salary': 100000},
    ]

    top_vacancies = get_top_vacancies(vacancies, 5)
    assert len(top_vacancies) == 2
    assert top_vacancies == vacancies


def test_get_top_empty_list():
    """Тестирование функции с пустым списком вакансий."""
    vacancies = []

    top_vacancies = get_top_vacancies(vacancies, 3)
    assert len(top_vacancies) == 0


def test_get_top_zero():
    """Тестирование функции с нулевым значением top_n."""
    vacancies = [
        {'name': 'Junior Developer', 'salary': 50000},
        {'name': 'Senior Developer', 'salary': 100000},
    ]

    top_vacancies = get_top_vacancies(vacancies, 0)
    assert len(top_vacancies) == 0


def test_filter_by_single_keyword(sample_vacancies):
    result = filter_vacancies(sample_vacancies, "python")
    assert result[0].name == "Python Developer"


def test_filter_with_no_match(sample_vacancies):
    result = filter_vacancies(sample_vacancies, "ruby")
    assert len(result) == 4


def test_filter_with_empty_keywords(sample_vacancies):
    result = filter_vacancies(sample_vacancies, "")
    assert len(result) == len(sample_vacancies)


def test_filter_in_description(sample_vacancies):
    result = filter_vacancies(sample_vacancies, "react")
    assert len(result) == 4
    assert result[0].name == 'Python Developer'


def test_filter_multiple_words_in_different_fields(sample_vacancies):
    result = filter_vacancies(sample_vacancies, "sql javascript")
    assert len(result) == 4
    names = [vac.name for vac in result]
    assert "Frontend Developer" in names
    assert "Data Analyst" in names


def test_filter_with_none_keywords(sample_vacancies):
    result = filter_vacancies(sample_vacancies, None)
    assert len(result) == len(sample_vacancies)
