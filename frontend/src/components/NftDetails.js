import { useParams } from "react-router-dom";
import useFetchNFT from "./useFetchNFT";
import { useHistory } from "react-router-dom";
import NftItem from "./NftItem";
import axios from "axios";
import { useState, useEffect } from "react";

const NftDetails = () => {
  const { nft_id } = useParams();

  const db_url = "http://127.0.0.1:8000/api/get_one_nft_data/?nft_id=" + nft_id;

  // const [nft_data, setNftdata] = useState({});

  var nft_data = null;

  console.log("Trying to fetch  :", db_url);
  // Read all NFT

  axios
    .get("http://127.0.0.1:8000/api/get_one_nft_data/?nft_id=" + nft_id)
    .then((response) => {
      console.log(response.data);
      // setNftdata(response.data);
      nft_data = response.data;
      console.log("NFT Details", nft_data);
    });

  console.log("NFT Details Passed to item", nft_data);

  return <NftItem props={nft_data}></NftItem>;
};

export default NftDetails;

// // console.log(db_url);

// // axios
// //   .get("http://127.0.0.1:8000/api/get_one_nft_data/?nft_id=" + nft_id)
// //   .then((response) => {
// //     console.log(response, "details wala");
// //     console.log("useFetchSuccess");
// //     // setData(response.data);
// //     // setPending(false);
// //   });

// import { useParams } from "react-router-dom";
// import { useState, useEffect } from "react";
// import NftItem from "./NftItem";
// import axios from "axios";

// const NftDetails = () => {
//   const { nft_id } = useParams();

//   const db_url = "http://127.0.0.1:8000/api/get_one_nft_data/?nft_id=" + nft_id;

//   const [nft_data, setNftdata] = useState({});

//   useEffect(() => {
//     const fetchData = async () => {
//       console.log("useEffect initiated");
//       try {
//         const response = await axios.get(db_url);
//         console.log(response);
//         console.log("useEffect success");
//         const newNFT = response.data;
//         console.log("useEffect", newNFT);
//         setNftdata(newNFT);
//       } catch (error) {
//         console.error(error);
//       }
//     };

//     fetchData();

//     return () => {
//       console.log("cleanup function");
//     };
//   }, ["http://127.0.0.1:8000/api/get_one_nft_data/?nft_id=" + nft_id]);

//   console.log("NFT Details Passed to item", nft_data);

//   return <NftItem props={nft_data}></NftItem>;
// };

// export default NftDetails;

// useEffect(
//   () => {
//     const abortCont = new AbortController();

//     async function fetchData() {
//       console.log("useFetchInitiated");
//       await axios
//         .get("http://127.0.0.1:8000/api/get_one_nft_data/?nft_id=" + nft_id)
//         .then((response) => {
//           console.log(response);
//           console.log("useFetchSuccess");
//           const newNFT = response.data;
//           console.log("useeffect", newNFT);
//           setNftdata(newNFT);
//           // setData(response.data);
//           // setPending(false);
//         });

//       return () => abortCont.abort();
//     }
//     fetchData();
//   },
//   [nft_id] //dependancy array
// );

//     useEffect((response) => {
//       const newNFT = response.data;
//       console.log("useeffect", newNFT);
//       setNftdata(newNFT);
//     });

//  async function fetchData() {
//     console.log("useFetchInitiated");
//     await axios
//       .get("http://127.0.0.1:8000/api/get_one_nft_data/?nft_id=" + nft_id)
//       .then((response) => {
//         console.log(response);
//         console.log("useFetchSuccess");
//         const newNFT = response.data;
//         console.log("useeffect", newNFT);
//         setNftdata(newNFT);
//         // setData(response.data);
//         // setPending(false);
//       });
