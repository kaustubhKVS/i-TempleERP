# Backend of NFT-Marketplace on [ResilientDB](https://resilientdb.com/)

Backend of NFT Marketplace on ResilientDB is developed using [FastAPI](https://fastapi.tiangolo.com/). FastAPI is a modern and high-performance based web framework for building APIs using Python.

## Available Scripts

### ResDB URI Setup

Set the URL of the hosted ResDB Instance in `db_config.py`

### FastAPI Development Server Setup

To run the development server with hot-reload:

#### `conda activate nftmarketplace`

#### `uvicorn test:app --reload`

#### `sudo systemctl start mongod`

Runs the app in the development mode.\
Use the auto documentation feature of FastAPI on [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for Interactive API documentation and exploration of web user interfaces.

## Advantages of FastAPI:

- New Powerful Better
- Hot reload
- Auto documentation API endpoints
- Autocompletion and code suggetion: ease fo development for new members
- less data validation : info sent to API is automatically checked for datatypes. We define expected value.
- automatic JSONify the python types
- ASGI Server : Do not need to use async io in python and very fast in deploymrnt because of concurrency. Eliminates Express.
- The page will reload when you make changes.\
