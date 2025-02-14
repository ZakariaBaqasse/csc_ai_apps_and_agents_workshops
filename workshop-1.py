import ollama
import os
import re

MODEL = "llama3.2"

input_file = "./data/grocery-list.txt"
output_file = "./data/categorized-grocery-list.txt"

if not os.path.exists(input_file):
    print(f"Input file: {input_file} does not exist")
    exit(1)

with open(input_file,"r") as file:
    print(f"Reading items list")
    items = file.read().strip()
    prompt = f"""
    You are an assistant that categorize grocery list items.
    Here is a list of grocery items:
    {items}
    Please:

    1. Categorize these items into appropriate categories such as Produce, Dairy, Meat, Bakery, Beverages, etc.
    2. Sort the items alphabetically within each category.
    3. Present the categorized list in a clear and organized manner, using bullet points or numbering.
    RULE:
    Every item in the list should only appear in one and only one category that is the most fit for it.
""" 
    
try:
    print(f"generating organized list")
    response = ollama.generate(model=MODEL,prompt=prompt)
    generated_text = response.get("response","")
    with open(output_file,"w") as file:
        file.write(generated_text.strip())
        print(f"categorized grocery items saved to: {output_file}")
except Exception as e:
    print(f"An error has occurred: {str(e)}")