def total_salary(path):
    try:
        with open(path, encoding="utf-8") as f:
            salaries = [
                int(line.split(",")[1])
                for line in f
                if line.strip()
            ]

        if not salaries:
            return (0, 0)

        total = sum(salaries)
        average = total // len(salaries)
        return (total, average)

    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдено.")
        return (0, 0)
    except (ValueError, IndexError) as e:
        print(f"Помилка: файл пошкоджений або має неправильний формат. ({e})")
        return (0, 0)
