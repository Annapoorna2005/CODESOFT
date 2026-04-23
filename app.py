products = [
    {"id": 1, "name": "Teddy Bear", "category": "gift", "tags": ["soft", "toy", "love"]},
    {"id": 2, "name": "Chocolate Box", "category": "food", "tags": ["sweet", "gift", "love"]},
    {"id": 3, "name": "Perfume", "category": "beauty", "tags": ["fragrance", "luxury"]},
    {"id": 4, "name": "Flower Bouquet", "category": "gift", "tags": ["love", "romantic"]},
    {"id": 5, "name": "Smart Watch", "category": "electronics", "tags": ["tech", "fitness"]},
    {"id": 6, "name": "Photo Frame", "category": "gift", "tags": ["memory", "home"]},
]
from data import products

# Function to find similar products
def recommend(product_id):
    selected_product = None

    # Find selected product
    for p in products:
        if p["id"] == product_id:
            selected_product = p
            break

    if not selected_product:
        return []

    recommendations = []

    for p in products:
        if p["id"] != product_id:
            score = 0

            # Same category
            if p["category"] == selected_product["category"]:
                score += 2

            # Matching tags
            common_tags = set(p["tags"]).intersection(set(selected_product["tags"]))
            score += len(common_tags)

            if score > 0:
                recommendations.append((p, score))

    # Sort by score
    recommendations.sort(key=lambda x: x[1], reverse=True)

    return [item[0] for item in recommendations]


# CLI Demo
def main():
    print("🛒 Product Recommendation System\n")

    print("Available Products:")
    for p in products:
        print(f"{p['id']}. {p['name']}")

    user_choice = int(input("\nEnter product ID: "))

    results = recommend(user_choice)

    print("\n🔍 Recommended Products:")
    for r in results:
        print("-", r["name"])


if __name__ == "__main__":
    main()