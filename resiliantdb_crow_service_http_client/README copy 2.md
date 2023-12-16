# ResilientDB_nft_marketplace

NFT Marketplace on ResDB

This project is built using FARM Stack:

- Backend: FastAPI

- Frontend: ReactJS

- Databases: MongoDB, NexresDB

### Install FastAPI

We will be using FastAPI as the backend framework.

Key tools and their use:

1. uvicorn: FastAPI server
2. motor: FastAPI and MondoDB connection

`conda create -n nftmarketplace python=3.10`

`conda activate nftmarketplace`

`pip install fastapi uvicorn motor`

### Install Nexres SDK Dependancies

`conda activate nftmarketplace`

`pip install cryptoconditions pysha3 python-rapidjson requests jupyter`

### Setup MongoDB

Create an account on MongoDB Atlas and download the following:

- MongoDB Compass
- MongoDB Shell
- MongoDB Community Server

Connect the server and atlas using the URI provided in the connection tab

### Setup React

`cd frontend`

`npm cache clean -f`

`sudo npm install -g n`

`sudo n latest`

Install the frontend dependencies:

`npm install`

Start the frontend:

`npm start`

### Run FastAPI files:

`cd backend`

`uvicorn main:app --reload`

### Run NexresDB with Endpoints:

`cd nexres`

#### Start the KVServer:

`chmod +x ./example/start_kv_server.sh`

`./example/start_kv_server.sh`

NexresDB has started. Now in a separate terminal, we will start the endpoint service.

In the second terminal:

#### Build and Compile the CROW Service

`bazel build sdk_client/crow_service_main`

#### Run binaries and start the CROW Service

`bazel-bin/sdk_client/crow_service_main example/kv_client_config.config`
