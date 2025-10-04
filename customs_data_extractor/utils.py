import pandas as pd
import os


def save_to_csv(data, filename="customs_data.csv"):
    if not data:
        print("Список данных пуст. Сохранение пропущено.")
        return

    try:
        df = pd.DataFrame(data)

        df.to_csv(filename,sep='\t' ,index=False, encoding='utf-8')

        print(f"✅ Данные успешно сохранены в файл: {os.path.abspath(filename)}")
    except Exception as e:
        print(f"❌ Ошибка при сохранении в CSV: {e}")