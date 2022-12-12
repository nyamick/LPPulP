from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable
def lpMain():
    #определяем модель
    model = LpProblem(name="LP1", sense=LpMaximize)

    # Описываем переменные
    x = {i: LpVariable(name=f"x{i}", lowBound=0, cat = "Integer") for i in range(1, 3)}

    # Добавляем ограничения

    model += (22 * x[1] + 28 * x[2] <= 325, "ограничение 1")
    model += (10 * x[1] + 14 * x[2] <= 155, "ограничение 2")
    model += (1 * x[1] + 2 * x[2] <= 20, "ограничение 3")
    model += (2 * x[1] + 0.8 * x[2] <= 20, "ограничение 4")
    model += (1 * x[1] + 1.1 * x[2] <= 15, "ограничение 5")


    # Описываем цель
    model += 45000 * x[1] + 76000 * x[2]
    # Решаем задачу оптимизации
    status = model.solve()
    # Выводим результаты решения
    print(f"status: {model.status}, {LpStatus[model.status]}")
    print(f"objective: {model.objective.value()}")


    for var in x.values():
        print(f"{var.name}: {var.value()}")

    for name, constraint in model.constraints.items():
        print(f"{name}: {constraint.value()}")
    print(
        "\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
def lpOne():
    #определяем модель
    model = LpProblem(name="LP1", sense=LpMaximize)

    # Описываем переменные
    x = {i: LpVariable(name=f"x{i}", lowBound=0) for i in range(1, 3)}

    # Добавляем ограничения

    model += (22 * x[1] + 28 * x[2] <= 325, "ограничение 1")
    model += (10 * x[1] + 14 * x[2] <= 155, "ограничение 2")
    model += (1 * x[1] + 2 * x[2] <= 20, "ограничение 3")
    model += (2 * x[1] + 0.8 * x[2] <= 20, "ограничение 4")
    model += (1 * x[1] + 1.1 * x[2] <= 15, "ограничение 5")
    model += (x[2] <= 7, "ограничение 6")


    # Описываем цель
    model += 45000 * x[1] + 76000 * x[2]
    # Решаем задачу оптимизации
    status = model.solve()
    # Выводим результаты решения
    print(f"status: {model.status}, {LpStatus[model.status]}")
    print(f"objective: {model.objective.value()}")


    for var in x.values():
        print(f"{var.name}: {var.value()}")

    for name, constraint in model.constraints.items():
        print(f"{name}: {constraint.value()}")
    print(
        "\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
def lpTwo():
    ##LP2
    #определяем модель
    model2 = LpProblem(name="LP2", sense=LpMaximize)

    # Описываем переменные
    x = {i: LpVariable(name=f"x{i}", lowBound=0) for i in range(1, 3)}

    # Добавляем ограничения

    model2 += (22 * x[1] + 28 * x[2] <= 325, "ограничение 1")
    model2 += (10 * x[1] + 14 * x[2] <= 155, "ограничение 2")
    model2 += (1 * x[1] + 2 * x[2] <= 20, "ограничение 3")
    model2 += (2 * x[1] + 0.8 * x[2] <= 20, "ограничение 4")
    model2 += (1 * x[1] + 1.1 * x[2] <= 15, "ограничение 5")
    model2 += (x[2] >= 8, "ограничение 6")

    # Описываем цель
    model2 += 45000 * x[1] + 76000 * x[2]
    # Решаем задачу оптимизации
    status2 = model2.solve()
    # Выводим результаты решения
    print(f"status: {model2.status}, {LpStatus[model2.status]}")
    print(f"objective: {model2.objective.value()}")


    for var in x.values():
        print(f"{var.name}: {var.value()}")

    for name, constraint in model2.constraints.items():
        print(f"{name}: {constraint.value()}")
    print(
        "\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
#вызов функций
lpMain()
#pOne()
#lpTwo()