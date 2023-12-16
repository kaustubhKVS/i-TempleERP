import motor.motor_asyncio
from model import ResNFT

from nexres_sdk.resdb_driver import Resdb
from nexres_sdk.resdb_driver.crypto import generate_keypair

import copy

from db_config import (
    db_root_url
)

db = Resdb(db_root_url)


# MongoDB driver for FastAPI

admin = generate_keypair()

alice = generate_keypair()
bob = generate_keypair()

nft_list_initialise_status = False

nft_list_token_tx_id: str = "HASHID_EMPTY"


async def append_nft_list(nft_asset_id: str):

    global admin
    global nft_list_initialise_status
    global nft_list_token_tx_id

    token_supply: int = 1

    if nft_list_initialise_status == False:
        await intialise_nft_list()

    transfer_tx_info = db.transactions.retrieve(nft_list_token_tx_id)

    transfer_asset = {"id": transfer_tx_info["asset"]["id"]}

    output_index = 0

    output = transfer_tx_info["outputs"][output_index]

    transfer_input = {
        "fulfillment": output["condition"]["details"],
        "fulfills": {"output_index": output_index, "transaction_id": transfer_asset["id"]},
        "owners_before": output["public_keys"],
    }

    old_metadata = transfer_tx_info["metadata"]["data"]

    new_metadata = copy.deepcopy(old_metadata)

    new_list_element = nft_asset_id

    new_metadata.append(new_list_element)

    # Dynamic

    prepared_transfer_tx = db.transactions.prepare(
        operation="TRANSFER",
        asset=transfer_asset,
        inputs=transfer_input,
        metadata={"data": new_metadata},
        recipients=[(
            [admin.public_key],
            token_supply
        )],
    )

    # Dynamic
    fulfilled_transfer_tx = db.transactions.fulfill(
        prepared_transfer_tx,
        private_keys=admin.private_key
    )

    # Dynamic
    transfer_tx = db.transactions.send_commit(fulfilled_transfer_tx)
    transfer_tx_id = transfer_tx[4:]

    nft_list_token_tx_id = transfer_tx_id

    return nft_list_token_tx_id


async def intialise_nft_list():

    global admin
    global nft_list_initialise_status
    global nft_list_token_tx_id

    token_supply: int = 1

    nft_list_init_token = {
        "data": {
            "token_for": {"NFT_list": "Used to store"},
            "description": "NFT List Token",
        },
    }

    nft_init_metadata = {
        "data": "INIT EMPTY HASH"
    }

    prepared_token_tx = db.transactions.prepare(
        operation="CREATE",
        signers=admin.public_key,
        recipients=[([admin.public_key], 1)],
        asset=nft_list_init_token,
        metadata={"data": "LIST INITIALISED"}
    )

    # fulfill the tnx
    fulfilled_token_tx = db.transactions.fulfill(
        prepared_token_tx,
        private_keys=admin.private_key
    )

    tx_reciept = db.transactions.send_commit(fulfilled_token_tx)
    tx_reciept_id = tx_reciept[4:]

    # Making a generic transfer token for further use

    create_tx_info = db.transactions.retrieve(tx_reciept_id)

    # Dynamic
    transfer_asset = {"id": create_tx_info["id"]}

    output_index = 0

    output = create_tx_info["outputs"][output_index]

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
        metadata={"data": []},
        recipients=[(
            [admin.public_key],
            token_supply
        )],
    )

    # Dynamic
    fulfilled_transfer_tx = db.transactions.fulfill(
        prepared_transfer_tx,
        private_keys=admin.private_key
    )

    # Dynamic
    transfer_tx = db.transactions.send_commit(fulfilled_transfer_tx)
    transfer_tx_id = transfer_tx[4:]

    nft_list_token_tx_id = transfer_tx_id

    nft_list_initialise_status = True


async def fetch_all_nft_id_list():

    global admin
    global nft_list_initialise_status
    global nft_list_token_tx_id

    if nft_list_initialise_status == False:
        await intialise_nft_list()

    tracker_tx_info = db.transactions.retrieve(nft_list_token_tx_id)

    old_metadata = tracker_tx_info["metadata"]["data"]

    return old_metadata
