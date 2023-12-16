from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Path, HTTPException

from nexres_sdk.resdb_driver import Resdb
from nexres_sdk.resdb_driver.crypto import generate_keypair


from model import ResNFT

from database import (
    create_nft,
    fetch_all_nft_data,
    fetch_one_nft_data,
    fetch_one_nft,
    transfer_nft,
    fetch_alice_bob_keys
)

from nft_tracking import (
    fetch_all_nft_id_list,
)

# App FastAPI object
app = FastAPI()

origins = ['http://localhost:3000',]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"Data": "Testing"}


@app.get("/about")
def about():
    return "NFT-Marketplace Under Construction"


@app.post("/api/create_nft/", response_model=ResNFT)
async def post_nft_data(nft_data: ResNFT):
    response = await create_nft(nft_data)
    if response:
        return response
    raise HTTPException(400, "Something went wrong/ Bad Request")


@app.get("/api/get_nft_id_list/")
async def get_all_nft_id():

    response = await fetch_all_nft_id_list()
    if response:
        return response
    raise HTTPException(400, "Something went wrong/ Bad Request")


@app.get("/api/get_all_nft_data/")
async def get_all_nft_data():

    response = await fetch_all_nft_data()
    if response:
        return response
    raise HTTPException(400, "Something went wrong/ Bad Request")


@app.get("/api/get_one_nft_data/")
async def get_one_nft_data(nft_id: str):

    response = await fetch_one_nft_data(nft_id)
    if response:
        return response
    raise HTTPException(400, "Something went wrong/ Bad Request")


@app.get("/api/get_one_nft/")
async def get_one_nft(nft_id: str):

    response = await fetch_one_nft(nft_id)
    if response:
        return response
    raise HTTPException(400, "Something went wrong/ Bad Request")


@app.post("/api/transfer_one_nft/")
async def transfer_nfts(nft_asset_id: str, owner_pub_key: str, owner_pvt_key: str, reciever_pub_key: str):

    response = await transfer_nft(nft_asset_id, owner_pub_key, owner_pvt_key, reciever_pub_key)
    if response:
        return response
    raise HTTPException(400, "Something went wrong/ Bad Request")


@app.get("/api/get_account_info/")
async def get_account_info():

    response = await fetch_alice_bob_keys()
    if response:
        return response
    raise HTTPException(400, "Something went wrong/ Bad Request")

# @app.get("/api/init_list/")
# async def get_init_nft_list():

#     response = await intialise_nft_list()
#     return response


# @app.get("/api/append_list/")
# async def get_nft_append_list(nft_tx_id: str):

#     response = await append_nft_list(nft_tx_id)
#     return response
