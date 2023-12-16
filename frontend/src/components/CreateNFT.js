import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const CreateNFT = () => {
  const backend_post_url = "http://127.0.0.1:8000/api/create_nft/";

  const [nft_name, setNft_name] = useState("");
  const [media_file_url, setMedia_file_url] = useState("");
  const [cc_name, setCC_name] = useState("");
  const [supply, setSupply] = useState(0);
  const [desc, setDesc] = useState("");
  const [cost, setCost] = useState(0.0);
  const [currency, setCurrency] = useState("");
  const [cc_external_link, setCC_external_link] = useState("");
  const [view, setView] = useState(0);
  const [tx_id, setTx_id] = useState("");

  const [isTxPending, setTxPending] = useState(true);

  const [isPending, setIsPending] = useState(false);

  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();

    setIsPending(true);

    const new_nft_data = {
      nft_name: nft_name,
      ipfs_file_url: media_file_url,
      creator_name: cc_name,
      supply: supply,
      description: desc,
      cost: cost,
      currency: currency,
      creator_external_link: cc_external_link,
      view: view,
      tx_id: tx_id,
    };

    axios.post(backend_post_url, new_nft_data).then((response) => {
      console.log(response);
      console.log("New NFT Added");

      setTx_id(response.data.tx_id);

      setTxPending(false);

      setIsPending(false);

      //   navigate("/");
    });
  };

  return (
    <div className="create_nft">
      <form onSubmit={handleSubmit}>
        <h2>Create new NFT</h2>
        <label>Name of NFT</label>
        <input
          type="text"
          required
          value={nft_name}
          onChange={(e) => setNft_name(e.target.value)}
        />

        <label>NFT Media File Link</label>
        <input
          type="text"
          required
          value={media_file_url}
          onChange={(e) => setMedia_file_url(e.target.value)}
        />

        <label>Content Creator Name</label>
        <input
          type="text"
          required
          value={cc_name}
          onChange={(e) => setCC_name(e.target.value)}
        />

        <label>Supply</label>
        <input
          type="number"
          required
          value={supply}
          onChange={(e) => setSupply(e.target.value)}
        />

        <label>Description of NFT</label>
        <input
          type="text"
          required
          value={desc}
          onChange={(e) => setDesc(e.target.value)}
        />

        <label>Cost of NFT</label>
        <input
          type="number"
          required
          value={cost}
          onChange={(e) => setCost(e.target.value)}
        />

        <label>Trading Currency</label>
        <select
          required
          value={currency}
          onChange={(e) => setCurrency(e.target.value)}
        >
          <option value="ROK">ROK</option>
          <option value="BTC">BTC</option>
          <option value="ETH">ETH</option>
          <option value="RDX">RDX</option>
          <option value="SOL">SOL</option>
        </select>

        <label>Creator Portfolio Link</label>
        <input
          type="text"
          value={cc_external_link}
          onChange={(e) => setCC_external_link(e.target.value)}
        />

        {!isPending && <button> Create NFT</button>}
        {isPending && <button> Creating NFT ... </button>}

        <div className="Blog Preview">
          <h2>NFT Data Preview:</h2>
          <p>NFT Name: {nft_name}</p>
          <p>Media Link: {media_file_url}</p>
          <p>Content Creator: {cc_name}</p>
          <p>Supply: {supply}</p>
          <p>Description: {desc}</p>
          <p>Cost: {cost}</p>
          <p>Currency: {currency}</p>
          <p>Content Creator Portfolio: {cc_external_link}</p>
        </div>

        {!isTxPending && (
          <div className="transaction_reciept">
            <h2>Transaction Successful</h2>
            <p>Transaction ID : {tx_id}</p>
          </div>
        )}
      </form>
    </div>
  );
};

export default CreateNFT;
