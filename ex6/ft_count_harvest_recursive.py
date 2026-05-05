def recursion(current_day: int, total_days: int) -> None:
    if current_day > total_days:
        print("Harvest time!")
        return
    print(f"Day {current_day}")
    recursion(current_day + 1, total_days)


def ft_count_harvest_recursive() -> None:
    current_day = 1
    total_days = int(input("Days until harvest: "))
    recursion(current_day, total_days)
