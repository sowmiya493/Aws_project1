# Product-AWS

# youtube video
[![Serverless web application using AWS](https:/0Roel5sMxPUd-qR_/img.youtube.com/vi//0.jpg)](https://www.youtube.com/watch?v=0Roel5sMxPUd-qR_)



# Serverless web application

This is a  Serverless web application built using AWS Lambda, DynamoDB, and an HTML interface.

## Features

- **Add Product:** Allows users to add a new product with a product code and price.
- **Update Product:** Enables users to update the price of existing products.
- **List Products:** Displays a list of all products in the system.

## Setup

1. **AWS Setup:** Ensure you have an AWS account set up with appropriate permissions to use Lambda and DynamoDB.
2. **Lambda Function:** Deploy the provided `lambda_function.py` code as a Lambda function.
3. **DynamoDB Table:** Create a DynamoDB table named `Product` with `productCode` as the primary key.
4. **API Gateway:** Set up an API Gateway to trigger the Lambda function.
5. **HTML Interface:** Host the `index.html` file on a web server or use GitHub Pages.

## Usage

1. Access the HTML interface in your web browser.
2. Use the form to add new products by entering a product code and price, then clicking "Add Product."
3. The product list will be automatically updated to display the newly added product.
4. To update a product's price, modify the price field and click "Update Product" for the corresponding product.
5. The product list will reflect the changes made.

## Contributors

- [@sowmiya493](https://github.com/sowmiya493) - Sowmiya S
