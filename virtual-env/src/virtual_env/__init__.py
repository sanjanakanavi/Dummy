# from fastapi import FastAPI
# import uvicorn
# from typing import List, Any, Optional
# from pydantic import BaseModel, Field

# class RootModel(BaseModel):
#     firstName:str = Field(min_length=2)
#     lastName: str | None = None

# app = FastAPI()

# details: list[dict] = []

# @app.post("/")
# async def create_user(rootModel: RootModel, age: int):
#     if age == None:
#         return "enter"
#     elif age <18:
#         return f"not Eligible"
#     elif age >18:
#         details.append(rootModel)
#         newFile = open("file1.txt", "w")
#         newFile.write(str(details))
#         newFile.close()
#         return f"Eligible"

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8001)

from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel, Field, ConfigDict
import uvicorn
import json
import random

class ProductModel(BaseModel):
    id: int | None = None
    name: str = Field(min_length=5)
    price: int = Field(ge=250)
    quantity: int = Field(ge=1)
    description: str | None = None

class UserModel(BaseModel):
    userId: int | None = None
    userName: str = Field(min_length= 5)
    userEmail: str =  Field(
        pattern=r"^[^@\s]+@gmail\.com$"
    )
    userPassword: str = Field(min_length=5, max_length=5)

app = FastAPI()

productDetails: list[dict] = []
userDetails: list[dict] = []
getProductInfo: list[dict] = []

@app.post("/product")
async def createProduct(productModel: ProductModel):
    productModel.id = random.randint(10,99)
    productDetails.append(productModel.model_dump())
    with open("productFile.txt", "w") as productFile:
        productFile.write("New product created:\n")
        json.dump(productDetails, productFile, indent=4)
        productFile.close()
        return f"product got created with Id: {productModel.id}"

@app.post("/user")
async def createUser(userModel : UserModel):
    userModel.userId = random.randint(100,1000)
    userDetails.append(userModel.model_dump())
    with open("userFile.txt", "w") as userFile:
        userFile.write("New user created:\n")
        json.dump(userDetails, userFile, indent=4)
        userFile.close()
        return f"user got created with Id: {userModel.userId}"

@app.get("/product")
async def getProductDetails():
    with open("productFile.txt", "r", encoding="utf-8") as productInfo:
        productInfo.readline()  # skips: New product created:
        getProductInfo = json.load(productInfo)

    return getProductInfo

#add to cart
@app.post("/cart")
async def addToCart(userId: int, productId: int = Body(..., embed=True)):
    productAdded = {
        "userId" : userId,
        "productId" : productId
    }
    with open("addToCartFile.txt", "a") as addToCartFile:
            addToCartFile.write("\nNew product added to cart:\n")
            json.dump(productAdded, addToCartFile, indent=4)
            addToCartFile.close()
    return productAdded

# @app.get("/cartItems")
# async def addToCart(userId: int):
#     with open("productFile.txt", "r") as getProduct:
#             getProductDetails = json.load(getProduct)
#             getProduct.close()
#     return getProductDetails

import json
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/cartItems")
async def get_cart_items(userId: int):
    # Read cart items and find the product IDs for this user
    with open("addToCartFile.txt", "r") as file:
        cart_content = file.read()

    cart_content = cart_content.replace("New product added to cart:", "")
    decoder = json.JSONDecoder()
    product_ids = []

    while cart_content.strip():
        cart_content = cart_content.lstrip()

        cart_item, position = decoder.raw_decode(cart_content)

        if cart_item["userId"] == userId:
            product_ids.append(cart_item["productId"])

        cart_content = cart_content[position:]

    if not product_ids:
        raise HTTPException(
            status_code=404,
            detail=f"No cart items found for userId {userId}"
        )

    # Read all product blocks from productFile.txt
    with open("productFile.txt", "r") as file:
        product_content = file.read()

    product_content = product_content.replace("New product created:", "")
    products = []

    while product_content.strip():
        product_content = product_content.lstrip()

        product_list, position = decoder.raw_decode(product_content)
        products.extend(product_list)

        product_content = product_content[position:]

    # Match cart product IDs with product details
    products_by_id = {product["id"]: product for product in products}

    cart_products = [
        products_by_id[product_id]
        for product_id in product_ids
        if product_id in products_by_id
    ]

    return {
        "userId": userId,
        "products": cart_products
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)