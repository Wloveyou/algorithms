import random

def get_size():
    size = int(input("Введите размер массива: "))
    if size <= 0:
        print("Введён неверный размер")
        return 0
    return size

def array_print(my_array):
    if my_array is None:
        print("Массива не существует")
    else:
        print("\nМассив:\n", my_array)

def fill_random_array(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]

def qsort_recursive(array, size, counter):
    if size <= 1:
        return
    mid = array[size // 2]
    i, j = 0, size - 1

    while True:
        while array[i] < mid:
            i += 1
        while array[j] > mid:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
        if i > j:
            break

    counter[0] += 1
    qsort_recursive(array[:i], i, counter)
    qsort_recursive(array[i:], size - i, counter)

def insertion_sort(array, counter):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
            counter[0] += 1
        array[j + 1] = key

def main():
    size = get_size()
    if size == 0:
        return

    min_value = -100
    max_value = 100
    my_array = fill_random_array(size, min_value, max_value)

    counter1, counter2, counter3, counter4, counter5 = 0, 0, 0, 0, 0

    for a in range(10):
        counter1 = 0
        counter2 = [0]

        # Сортировка пузырьком
        for index in range(size - 1):
            for j in range(size - index - 1):
                counter1 += 1
                if my_array[j] > my_array[j + 1]:
                    my_array[j], my_array[j + 1] = my_array[j + 1], my_array[j]
        counter3 += counter1

        # Быстрая сортировка
        array = fill_random_array(size, min_value, max_value)
        qsort_recursive(array, size, counter2)
        counter4 += counter2[0]

        # Сортировка вставками
        array_for_insertion = fill_random_array(size, min_value, max_value)
        counter_insertion = [0]
        insertion_sort(array_for_insertion, counter_insertion)
        counter5 += counter_insertion[0]

        print(f"Результаты подсчётов {a + 1} эксперимента: "
              f"Пузырьком: {counter1}, "
              f"Быстрой сортировкой: {counter2[0]}, "
              f"Сортировкой вставками: {counter_insertion[0]}")

    print("Средние результаты: ")
    print(f"Пузырьком: {counter3 / 10.0}")
    print(f"Быстрой сортировкой: {counter4 / 10.0}")
    print(f"Сортировкой вставками: {counter5 / 10.0}")

if __name__ == "__main__":
    main()