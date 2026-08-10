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

from fastapi import FastAPI
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
        return f"product got created with Id: {userModel.userId}"

@app.get("/product")
async def getProductDetails():
    with open("productFile.txt", "r", encoding="utf-8") as productInfo:
        productInfo.readline()  # skips: New product created:
        getProductInfo = json.load(productInfo)

    return getProductInfo

#add to cart


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)