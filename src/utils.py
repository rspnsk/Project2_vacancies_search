def filter_vacancies(vacancies: list, keywords: str) -> list[str]:
    """Функция фильтрации вакансий. Фильтрует список вакансий на основе ключевых слов.
       Возвращает список вакансий, в описании которых содержится ключевое слово.
       Если список ключевых слов пуст, возвращается исходный список вакансий."""
    if not keywords:
        return vacancies
    result = []
    for vacancy in vacancies:
        combined = f"{vacancy.description} {vacancy.name}".lower()
        if any(word.lower() in combined for word in keywords):
            result.append(vacancy)
    return result


def sort_vacancies(vacancies):
    """Функция сортировки вакансий"""
    return sorted(vacancies, reverse=True)


def get_top_vacancies(vacancies: list[dict], top_n: int):
    """Функция сортировки по топ введенных вакансий"""
    return vacancies[:top_n]


def print_vacancies(vacancies: list[dict]):
    """Функция вывода вакансий топа с нумерацией"""
    if not vacancies:
        print("Нет подходящих вакансий.")
        return
    print("\nТОП ВАКАНСИЙ:\n")
    for i, vacancy in enumerate(vacancies, start=1):
        print(f"{i}. {vacancy}")
