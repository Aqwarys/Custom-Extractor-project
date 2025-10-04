import requests
import time
from tqdm import tqdm


BASE_SIZE = 'https://jsonplaceholder.typicode.com/posts'
PAGE_SIZE = 100
MAX_RETRIES = 5
WAIT_TIME_ON_429 = 180


def get_total_count():
    try:
        response = requests.head(f'{BASE_SIZE}?_limit=1', timeout=10)
        response.raise_for_status()
        return int(response.headers.get('X-Total-Count', 0))
    except Exception as e:
        print(f"Ошибка при получении общего количества: {e}")
        return 0


def fetch_data_page(page_num, page_size):
    url = f'{BASE_SIZE}?_page={page_num}&_limit={page_size}'

    for attempt in range(MAX_RETRIES):
        try:
            response =requests.get(url, timeout=30)

            if response.status_code == 429:
                print(f"⚠️ Получена ошибка 429. Ждем {WAIT_TIME_ON_429} секунд...")
                time.sleep(WAIT_TIME_ON_429)
                continue
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Ошибка запроса на странице {page_num}: {e}")
            time.sleep(2 ** attempt)

    print(f"❌ Не удалось получить данные со страницы {page_num} после {MAX_RETRIES} попыток.")
    return []


def fetch_data_all():
    total_records = get_total_count()
    if total_records == 0:
        print("Не удалось определить общее количество записей или записей нет.")
        return []

    total_pages = (total_records + PAGE_SIZE - 1) // PAGE_SIZE
    all_data = []

    print(f"Найдено {total_records} записей на {total_pages} страницах.")

    for page in tqdm(range(1, total_pages+1), desc="Извлечение данных"):
        page_data = fetch_data_page(page, PAGE_SIZE)
        all_data.extend(page_data)

        time.sleep(0.5)

    return all_data
