# Product Category Prediction

### Overview

This project aims to predict the categories of products based on their features such as name, type, price, and other attributes. The main goal is to develop an API that can take in product information and output a list of predicted categories, facilitating the organization and classification of a large product catalog.

### Features

- **API-Based Product Category Prediction**: A FastAPI-based system to predict product categories based on input product details.
- **Machine Learning Model**: The prediction model has been trained on a dataset of product information, with categories being classified using machine learning algorithms.
- **Handling Missing Categories**: If no matching category is found for a product, it is classified under a default "Others" category.
- **Partial Name Matching**: The system supports partial name matching, so even products with similar names can be categorized correctly.

### Tech Stack

- **Backend Framework**: FastAPI
- **Data Handling**: pandas, NumPy
- **Machine Learning**: TensorFlow (or any library you're using)
- **Deployment**: Uvicorn, Gunicorn
- **Other**: JSON handling, CSV for data storage and preprocessing

### Setup and Installation

#### Prerequisites

- Python 3.8+
- pip (Python package installer)

#### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/product-category-prediction.git
   cd product-category-prediction

2. Create and activate a virtual environment
   ```bash
    python3 -m venv myenv
    source myenv/bin/activate

3. Install the dependencies:
    pip install -r requirements.txt

4. Run the FastAPI server:
    uvicorn main:app --reload



### API Endpoints

- **`POST /product-categories`**: Predicts categories for a product based on its features.

  - **Request Body**:
    ```json
    {
      "name": "MEElectronics - M9P Earbud Headphones - Red"
    }
    ```

  - **Response**:
    ```json
    {
      "name": "MEElectronics - M9P Earbud Headphones - Red",
      "categories": ["Headphones", "Electronics"]
    }
    ```

  - **If no category is found, it defaults to**:
    ```json
    {
      "name": "Some Product",
      "categories": ["Others"]
    }
    ```

# Product-Category-Predication
# Product-Category-Predication
