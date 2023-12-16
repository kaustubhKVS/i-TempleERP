from pydantic import BaseModel


class ResNFT(BaseModel):
    nft_name: str
    ipfs_file_url: str
    creator_name: str
    creator_external_link = 'NULL'
    supply: int
    description: str
    cost: float
    currency: str
    view = 1
    tx_id = 'NULL'

    def to_asset(self):
        asset = {"data": self.dict()}
        return asset

    def set_tx_id(self, tx_id: str):
        self.tx_id = tx_id
        return self

    class Config:
        orm_mode = True
