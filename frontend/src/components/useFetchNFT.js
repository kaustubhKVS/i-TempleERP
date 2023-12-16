import { useState, useEffect } from "react";
import axios from "axios";

const useFetchNFT = (db_url) => {
  const [data, setData] = useState([{}]);
  const [isPending, setPending] = useState(true);
  const [error, setError] = useState(null);
  // const [fetch_url, setFetchurl] = useState(null);

  // setFetchurl(db_url);

  console.log("useFetchEntered");
  console.log(data, "pre Data");
  console.log("Trying to fetch  :", db_url);

  useEffect(
    () => {
      console.log("useFetchInitiated");
      const abortCont = new AbortController();

      async function fetchData() {
        await axios
          .get(db_url)
          .then((response) => {
            console.log(response);
            console.log("useFetchSuccess");
            setData(response.data);
            setPending(false);
          })
          .catch((err) => {
            if (err.name === "AbortError") {
              console.log("fetch aborted");
            } else {
              setPending(false);
              setError(err.message);
            }
          });

        return () => abortCont.abort();
      }
      fetchData();
    },
    [db_url] //dependancy array
  );
  console.log(data);
  return { data, isPending, error };
};

export default useFetchNFT;
