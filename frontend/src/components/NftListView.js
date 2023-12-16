import NftItem from "./NftItem";
import NftDetails from "./NftDetails";
import { Link } from "react-router-dom";

const NftView = ({ nftList }) => {
  return (
    <div className="nft-list">
      {nftList.map((nft) => (
        <div className="nft-preview" key={nft.tx_id}>
          {/* <Link to={`/nft_details/${nft.tx_id}`}>
            <h2> {nft.nft_name} </h2>
            <p>Produced by {nft.creator_name}</p>
            <p>
              Cost: {nft.cost} {nft.currency}{" "}
            </p>
            <p>Asset ID: {nft.tx_id} </p>
          </Link> */}
          <h2> {nft.nft_name} </h2>
          <p>Produced by {nft.creator_name}</p>
          <p>
            Cost: {nft.cost} {nft.currency}{" "}
          </p>
          <p>Asset ID: {nft.tx_id} </p>
        </div>
      ))}
    </div>
  );
};

export default NftView;

//   "nft_name": "string",
//   "ipfs_file_url": "string",
//   "creator_name": "string",
//   "supply": 0,
//   "description": "string",
//   "cost": 0,
//   "currency": "string",
//   "creator_external_link": "NULL",
//   "view": 1,
//   "tx_id": "NULL"
// }
