import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const TransferNFT = () => {
  const backend_post_url = "http://127.0.0.1:8000/api/transfer_one_nft/";

  const [nft_id, setNft_id] = useState("");
  const [owner_pub_key, setOwner_pub_key] = useState("");
  const [owner_pvt_key, setOwner_pvt_key] = useState("");
  const [reciever_pub_key, setReciever_pub_key] = useState("");
  const [num_tokens, setNum_tokens] = useState("");

  const [tx_id, setTx_id] = useState("");

  const [isTxPending, setTxPending] = useState(true);

  const [isPending, setIsPending] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();

    setIsPending(true);

    const data = {
      nft_asset_id: nft_id,
      owner_pub_key: owner_pub_key,
      owner_pvt_key: owner_pvt_key,
      reciever_pub_key: reciever_pub_key,
    };

    axios
      .post(backend_post_url, null, {
        params: {
          nft_asset_id: nft_id,
          owner_pub_key: owner_pub_key,
          owner_pvt_key: owner_pvt_key,
          reciever_pub_key: reciever_pub_key,
        },
      })
      .then((response) => {
        console.log("NFT Transfer Succesful");
        console.log(response);

        setTx_id(response.data);

        setTxPending(false);

        setIsPending(false);

        //   navigate("/");
      });
  };

  return (
    <div className="create_nft">
      <form onSubmit={handleSubmit}>
        <h2>Transfer NFT</h2>
        <label>NFT Asset ID</label>
        <input
          type="text"
          required
          value={nft_id}
          onChange={(e) => setNft_id(e.target.value)}
        />

        <label>Owner Public Key</label>
        <input
          type="text"
          required
          value={owner_pub_key}
          onChange={(e) => setOwner_pub_key(e.target.value)}
        />

        <label>Owner Private Key</label>
        <input
          type="text"
          required
          value={owner_pvt_key}
          onChange={(e) => setOwner_pvt_key(e.target.value)}
        />

        <label>Number of Tokens</label>
        <input
          type="number"
          required
          value={num_tokens}
          onChange={(e) => setNum_tokens(e.target.value)}
        />

        <label>Reciever Public Key</label>
        <input
          type="text"
          required
          value={reciever_pub_key}
          onChange={(e) => setReciever_pub_key(e.target.value)}
        />

        {!isPending && <button> Add Blog</button>}
        {isPending && <button> Adding Blog ... </button>}

        <div className="Blog Preview">
          <h2>NFT Transfer Preview:</h2>
          <p>NFT ID: {nft_id}</p>
          <p>Owner Public Key: {owner_pub_key}</p>
          <p>Owner Private Key: {owner_pvt_key}</p>
          <p>Number of Tokens: {num_tokens}</p>
          <p>Reciever Public Key: {reciever_pub_key}</p>
        </div>

        {!isTxPending && (
          <div className="transaction_reciept">
            <h2>Transfer Transaction Successful</h2>
            <p>Transfer Transaction ID : {tx_id}</p>
          </div>
        )}
      </form>
    </div>
  );
};

export default TransferNFT;
