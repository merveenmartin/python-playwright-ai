from ai.test_generator import generate_test_cases

features = [
    "Verify email textbox is displayed"
]

if __name__ == "__main__":
    for feature in features:
        print(f"\n{'=' * 60}\nFeature: {feature}\n{'=' * 60}")
        generate_test_cases(feature)
