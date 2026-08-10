
'''
from typing import List, Optional, Any
from dataclasses import dataclass

@dataclass
class Dimensions:
    width: float
    height: float
    depth: float

@dataclass
class Reviews:
    rating: int
    comment: str
    date: str
    reviewerName: str
    reviewerEmail: Optional[str] = None

@dataclass
class Meta:
    createdAt: str
    updatedAt: str
    barcode: str
    qrCode: str

@dataclass
class Products:
    id: int
    title: str
    description: str
    category: str
    price: float
    discountPercentage: float
    rating: float
    stock: int
    tags: List[str]
    brand: Optional[str] = None
    sku: str = ""
    weight: int = 0
    dimensions: Dimensions = None
    warrantyInformation: str = ""
    shippingInformation: str = ""
    availabilityStatus: str = ""
    reviews: List[Reviews] = None
    returnPolicy: str = ""
    minimumOrderQuantity: int = 0
    meta: Meta = None
    images: List[str] = None
    thumbnail: str = ""

@dataclass
class ProductsList:
    products: List[Products]
    total: int
    skip: int
    limit: int

def products_info():
    url = "https://dummyjson.com/products"
    response = requests.get(url).json()
    products = []
    for product in response["products"]:
        obj = Products(**product)
        products.append(obj)

    status =  requests.get(url).status_code
    print(status)

    products_list = ProductsList(
        products=products,
        total=response.get("total", 0),
        skip=response.get("skip", 0),
        limit=response.get("limit", len(products))
    )

    brands = []
    revEmails = []
    for i in products_list.products:
        brand = i.brand
        brands.append(brand)
        for j in i.reviews:
            comments = j["comment"]
            revEmails.append(comments)
#    print(brands, revEmails)

    total_products = products_list.limit
    return total_products

def main():
    total_products = products_info()
#  print(f"Total products {total_products}")

if __name__ == "__main__":
    main()
'''
#----------------------------------------------------------------------------------------
import requests

class ApiService:
    def __init__(self, payload, headers, url):
        self.payload = payload
        self.headers = headers
        self.url = url
    def get_api(self):
        try:
            response = requests.post(url=self.url, json=self.payload, headers=self.headers)
            if response.status_code == 200:
                data = response.json()
                if data:
                    return data
        except requests.exceptions.HTTPError:
            print("HTTP error")
        except requests.exceptions.RequestException as e:
            print("Something went wrong")

def login(payload, headers, url):
    api1 = ApiService(payload, headers, url)
    print(api1.get_api())

# def fetch(url1, headers1, credentials):
#     try:
#         response1 = requests.get(url=url1, json=credentials, headers=headers1)
#         status1 = response1.status_code
#         data1= response1.json()
#         print(f"status code 2 : {status1}, data2 : {data1}")
#     except requests.exceptions.RequestException as e:
#         print("Something wrong in api 2")

if __name__ == "__main__":
    url = "https://dummyjson.com/auth/login"
    username =  str(input("Enter username"))
    password = str(input("Enter password"))

    payload = {
        "username" : username,
        "password" : password,
        "expiresInMinutes" : 30
    }

    headers = {
        "Content-Type" : "application/json"
    }

    login(payload, headers, url)

'''
    url1 = "https://dummyjson.com/auth/me"

    headers1 = {
        "Authorization" : f"Bearer {access_token}"
    }

    credentials = {
        "credentials" : str(input("Enter your creds : "))
    }

    fetch(url1, headers1, credentials)
'''
