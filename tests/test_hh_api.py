from unittest.mock import patch, MagicMock

from src.hh_api import HeadHunterAPI
import requests_mock

def test_initialization(hh_api):
    """Проверка инициализации параметров"""
    assert getattr(hh_api, '_HeadHunterAPI__url') == "https://api.hh.ru/vacancies"
    assert getattr(hh_api, '_HeadHunterAPI__params') == {"text": "", "per_page": 20, "page": 0}


# Тестирование метода _connect
@patch('requests.get')
def test_connect_success(mock_get, hh_api):
    """Проверка успешного подключения к API"""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"items": []}
    mock_get.return_value = mock_response

    result = hh_api._connect()
    assert result == {"items": []}
    mock_get.assert_called_with(hh_api._HeadHunterAPI__url, params=hh_api._HeadHunterAPI__params)


@patch('requests.get')
def test_connect_failure(mock_get, hh_api):
    """Проверка обработки ошибки подключения"""
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    result = hh_api._connect()
    assert result is None

# Тестирование метода load_vacancies
def test_load_vacancies():
    with requests_mock.Mocker() as m:
        m.get("https://api.hh.ru/vacancies", json={"items": [{"name": "Python Developer",
                                                 "alternate_url": "https://example.com/vacancy1",
                                                 "salary": {"from": 100000, "to": 150000}, "snippet": {"requirement": "Опыт работы с Python"}}]})
        api = HeadHunterAPI()
        result = api.load_vacancies("Python разработчик")
        assert len(result) == 5
        assert result[0]["name"] == "Python Developer"
        assert result[0]["url"] == "https://example.com/vacancy1"
        assert result[0]["salary"] == {"from": 100000, "to": 150000}
        assert result[0]["description"] == "Опыт работы с Python"

