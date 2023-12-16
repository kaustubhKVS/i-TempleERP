import React from "react";

const NftItem = (props) => {
  console.log("NFT Data Recieved:", props);

  return (
    <div>
      <p>
        <span style={{ fontWeight: "bold" }}> NFT Name : </span>{" "}
        {props.nft.nft_name} <br />
        <span style={{ fontWeight: "bold" }}> IPFS URL : </span>{" "}
        {props.nft.ipfs_file_url} <br />
        <span style={{ fontWeight: "bold" }}> Creator Name : </span>{" "}
        {props.nft.creator_name} <br />
        <span style={{ fontWeight: "bold" }}> Supply : </span>{" "}
        {props.nft.supply} <br />
        <span style={{ fontWeight: "bold" }}> Description : </span>{" "}
        {props.nft.description} <br />
        <span style={{ fontWeight: "bold" }}> Cost : </span> {props.nft.cost}{" "}
        <br />
        <span style={{ fontWeight: "bold" }}> Currency : </span>{" "}
        {props.nft.currency} <br />
        <span style={{ fontWeight: "bold" }}> Creator Portfolio : </span>{" "}
        {props.nft.creator_external_link} <br />
        <hr></hr>
      </p>
    </div>
  );
};

export default NftItem;

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
