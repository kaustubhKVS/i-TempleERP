import motor.motor_asyncio
from model import ResNFT

from nexres_sdk.resdb_driver import Resdb
from nexres_sdk.resdb_driver.crypto import generate_keypair

import copy

from db_config import (
    db_root_url
)

from database import (
    create_nft,
    fetch_all_nft_data,
    fetch_one_nft_data
)

db = Resdb(db_root_url)


# MongoDB driver for FastAPI

admin = generate_keypair()

alice = generate_keypair()
bob = generate_keypair()


async def transfer_nft(nft_asset_id: str, owner_pub_key: str, owner_pvt_key: str, reciever_pub_key: str):

    global admin

    token_supply: int = 1

    async def get_nft(nft_id: str):
        nft_info = db.transactions.retrieve(nft_id)
        return nft_info()

    transfer_tx_info = await get_nft(nft_asset_id)

    transfer_asset = {"id": transfer_tx_info["asset"]["id"]}

    output_index = 0

    output = transfer_tx_info["outputs"][output_index]

    transfer_input = {
        "fulfillment": output["condition"]["details"],
        "fulfills": {"output_index": output_index, "transaction_id": transfer_asset["id"]},
        "owners_before": output["public_keys"],
    }

    old_metadata = transfer_tx_info["metadata"]["data"]

    # Dynamic

    prepared_transfer_tx = db.transactions.prepare(
        operation="TRANSFER",
        asset=transfer_asset,
        inputs=transfer_input,
        metadata={"data": old_metadata},
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
