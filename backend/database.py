import motor.motor_asyncio
from model import ResNFT

from nexres_sdk.resdb_driver import Resdb
from nexres_sdk.resdb_driver.crypto import generate_keypair

import copy

from nft_tracking import (
    append_nft_list,
    fetch_all_nft_id_list
)

from db_config import (
    db_root_url
)


db = Resdb(db_root_url)

# MongoDB driver for FastAPI

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')

database = client.NFT_Store

collection = database.nft


alice = generate_keypair()
bob = generate_keypair()
ryan = generate_keypair()


async def create_nft(nft_data: ResNFT):

    global alice
    global bob

    num_of_tokens = nft_data.supply

    prepared_token_tx = db.transactions.prepare(
        operation="CREATE",
        signers=alice.public_key,
        recipients=[([bob.public_key],
                     num_of_tokens
                     )],
        asset=nft_data.to_asset(),
    )

    # fulfill the tnx
    fulfilled_token_tx = db.transactions.fulfill(
        prepared_token_tx,
        private_keys=alice.private_key
    )

    tx_reciept = db.transactions.send_commit(fulfilled_token_tx)
    tx_reciept_id = tx_reciept[4:]

    nft_data = nft_data.set_tx_id(tx_reciept_id)

    await append_nft_list(tx_reciept_id)

    document = nft_data.dict()

    result = await collection.insert_one(document)

    return nft_data


async def fetch_all_nft_data():

    nft_id_list = await fetch_all_nft_id_list()

    all_nft_data = []

    for nft_id in nft_id_list:
        nft_data = await fetch_one_nft_data(nft_id)
        all_nft_data.append(nft_data)

    return all_nft_data


async def fetch_one_nft_data(nft_id: str):

    nft_info = db.transactions.retrieve(nft_id)
    nft_data = nft_info["asset"]["data"]
    nft_data["tx_id"] = nft_id

    return nft_data


async def fetch_one_nft(nft_id: str):
    nft_info = db.transactions.retrieve(nft_id)
    return nft_info


async def fetch_alice_bob_keys():
    global alice
    global bob

    account_info = {
        "alice": [alice.public_key, alice.private_key],
        "bob": [bob.public_key, bob.private_key],
        "ryan": [ryan.public_key, ryan.private_key],
    }
    return account_info

# async def fetch_one_todo(title):
#     document = await collection.find_one({"title": title})
#     return document


# async def create_todo(todo):
#     document = todo
#     result = await collection.insert_one(document)
#     return document


# async def update_todo(title, desc):
#     await collection.update_one(
#         {"title": title},
#         {"$set": {
#             "description": desc
#         }})
#     document = await collection.find_one({"title": title})
#     return document


# async def remove_todo(title):
#     await collection.delete_one({"title": title})
#     return True

async def transfer_nft(nft_asset_id: str, owner_pub_key: str, owner_pvt_key: str, reciever_pub_key: str):

    global admin

    token_supply: int = 1

    transfer_tx_info = await fetch_one_nft(nft_asset_id)

    token_supply: int = 1

    transfer_asset = {"id": transfer_tx_info["id"]}

    output_index = 0

    output = transfer_tx_info["outputs"][output_index]

    transfer_input = {
        "fulfillment": output["condition"]["details"],
        "fulfills": {"output_index": output_index, "transaction_id": transfer_asset["id"]},
        "owners_before": output["public_keys"],
    }

    # Dynamic

    prepared_transfer_tx = db.transactions.prepare(
        operation="TRANSFER",
        asset=transfer_asset,
        inputs=transfer_input,
        metadata={"data": "2"},
        recipients=[(
            [reciever_pub_key],
            token_supply
        )],
    )

    # Dynamic
    fulfilled_transfer_tx = db.transactions.fulfill(
        prepared_transfer_tx,
        private_keys=owner_pvt_key
    )

    # Dynamic
    transfer_tx = db.transactions.send_commit(fulfilled_transfer_tx)
    transfer_tx_id = transfer_tx[4:]

    nft_list_token_tx_id = transfer_tx_id

    return nft_list_token_tx_id
