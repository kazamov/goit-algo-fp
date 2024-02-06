def greedy_algorithm(foods, budget):
    sorted_foods = sorted(foods.items(), key=lambda x: x[1]["calories"], reverse=True)
    selected_foods = {}
    total_calories = 0
    total_cost = 0

    for food, details in sorted_foods:
        if total_cost + details["cost"] <= budget:
            selected_foods[food] = details
            total_cost += details["cost"]
            total_calories += details["calories"]

    return selected_foods, total_calories


def dynamic_programming(foods, budget):
    dp = [[0] * (budget + 1) for _ in range(len(foods) + 1)]
    selected_foods = {}

    for i, (food, details) in enumerate(foods.items(), 1):
        for j in range(1, budget + 1):
            if details["cost"] <= j:
                dp[i][j] = max(
                    dp[i - 1][j], dp[i - 1][j - details["cost"]] + details["calories"]
                )
            else:
                dp[i][j] = dp[i - 1][j]

    total_calories = dp[len(foods)][budget]

    i, j = len(foods), budget
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            food = list(foods.keys())[i - 1]
            selected_foods[food] = foods[food]
            j -= foods[food]["cost"]
        i -= 1

    return selected_foods, total_calories


def print_food_selection(selected_foods, total_calories):
    print("Selected foods:")
    for food, details in selected_foods.items():
        print(f"  {food}: {details['cost']} cost, {details['calories']} calories")
    print(f"Total calories: {total_calories}")


if __name__ == "__main__":
    foods = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }

    budget = 100

    selected_greedy, total_calories_greedy = greedy_algorithm(foods, budget)
    selected_dp, total_calories_dp = dynamic_programming(foods, budget)

    print("Greedy algorithm")
    print_food_selection(selected_greedy, total_calories_greedy)

    print("\nDynamic programming algorithm")
    print_food_selection(selected_dp, total_calories_dp)
