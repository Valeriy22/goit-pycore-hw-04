def get_cats_info(path):
    try:
        with open(path, encoding="utf-8") as f:
            return [
                {"id": cat_id, "name": name, "age": age}
                for line in f
                if line.strip()
                for cat_id, name, age in [line.strip().split(",")]
            ]

    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдено.")
        return []
    except ValueError as e:
        print(f"Помилка: неправильний формат файлу. ({e})")
        return []
