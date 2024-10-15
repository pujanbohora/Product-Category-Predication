import json
import pandas as pd
import numpy as np
# from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Load the JSON data from a file
f = open('sample.json')
products_data = json.load(f)  # returns JSON object as a dictionary

#CSV File
# products_data = pd.read_csv('sample.csv')

# Prepare lists to store extracted data
names, descriptions, categories = [], [], []

# Extract the product names, descriptions, and categories from the JSON
for product in products_data:
    names.append(product['name'])
    descriptions.append(product['description'])
    productCategories = []
    for cat in product['category']:
        productCategories.append(cat['name'])  # Assuming 'name' is the key for the category
    categories.append(productCategories)

# Create a DataFrame with product names, descriptions, and categories
column_names = ['name', 'description', 'category']
df = pd.DataFrame(list(zip(names, descriptions, categories)), columns=column_names)

# Separate out categories into individual columns
cat = pd.DataFrame(df['category'].to_list())
cat.head()

# Find unique categories from all category columns
unique_categories = []
for i in range(cat.shape[1]):
    unique_categories += list(cat[i].unique())

# Clean up unique categories list
unique_categories = list(dict.fromkeys([x for x in unique_categories if x is not None]))



# Define FastAPI app
app = FastAPI()

# Define the request model for POST
class ProductRequest(BaseModel):
    name: str

# Endpoint to return all unique categories
@app.get("/categories")
def get_categories():
    return {"categories": unique_categories}

# Endpoint to get categories by product name
@app.post("/product-categories")
def get_product_categories(product: ProductRequest):
    
    # Find the product in the DataFrame by its name
    # product_row = df[df['name'] == product.name]

    # Find products in the DataFrame that match any part of the product name
    product_row = df[df['name'].str.contains(product.name.split()[0], case=False, na=False)]
    
    if product_row.empty:
        raise HTTPException(status_code=404, detail="Product not found")
    
    product_categories = product_row.iloc[0]['category']

    print("product_categories: ", product_categories)

    # if not product_categories:
    #     product_categories.append("Others")

    return {"name": product.name, "categories": product_categories}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
