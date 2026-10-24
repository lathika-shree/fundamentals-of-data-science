import pandas as pd

structured_data = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
})
print("Structured Data:")
print(structured_data)

unstructured_data = "This is unstructured text. Images, audio, and videos are other examples."
print("\nUnstructured Data:")
print(unstructured_data)

semi_structured_data = {
    "ID": 1,
    "Name": "Alice",
    "Attributes": {"Height": 165, "Weight": 68}
}
print("\nSemi-structured Data (dictionary/JSON-like):")
print(semi_structured_data)
