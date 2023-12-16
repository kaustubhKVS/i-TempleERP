import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

import "./App.css";
import Navbar from "./components/Navbar";
import Home from "./components/Home";
import CreateNFT from "./components/CreateNFT";
import NftView from "./components/NftListView";
import NotFound from "./components/NotFound";
import useFetchNFT from "./components/useFetchNFT";
import NftDetails from "./components/NftDetails";

function App() {
  // const [nftList, setNftList] = useState([{}]);

  // Read all NFT
  // useEffect(() => {
  //   axios.get("http://127.0.0.1:8000/api/get_all_nft_data/").then((res) => {
  //     setNftList(res.data);
  //   });
  // });

  const {
    data: nftList,
    isPending,
    error,
  } = useFetchNFT("http://127.0.0.1:8000/api/get_all_nft_data/");

  console.log(nftList);

  return (
    <Router>
      <div className="App">
        <Navbar></Navbar>
        <div className="content">
          <Routes>
            <Route exact path="/" element={<Home />} />
            <Route exact path="/create" element={<CreateNFT />} />
            <Route
              exact
              path="/explore"
              element={<NftView nftList={nftList} />}
            />
            <Route path="/nft_details/?NFT:nft_id" element={<NftDetails />} />
            <Route path="*" element={<NotFound />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
