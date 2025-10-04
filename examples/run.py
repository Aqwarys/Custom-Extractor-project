from customs_data_extractor.api_client import fetch_data_all
from customs_data_extractor.utils import save_to_csv


def run_module_interface():
    print("🚀 Начинаем выгрузку данных...")
    data = fetch_data_all()
    save_to_csv(data)
    print("✨ Выгрузка завершена.")

if __name__ == '__main__':
    run_module_interface()