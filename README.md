### Mobile Factory code challenge :

Files:

- database.json : list of all the items, in the inventory
- client.py : inorder to make request to the server, if postman is not available
- server.py : inorder to make a locally available server to make requests
- price_calculator.py : contains logic to calculate price
- constants.py : contains all the constants used, inorder to reduce hardcoding
- caching.py : contains logic to cache data from db for rapid use and one time loading

#### Run:

python3 server.py --- To start the server
python3 client.py --- To make the requests if postman not available

Note: Please ensure without running the server you will not be able to make POST request

### Sample Output

{'order_id': 3, 'total': 99.99, 'parts': ['LED Screen', 'Wide-Angle Camera', 'USB-C Port', 'Metallic Body']}


### Suggested Features:

- Can make use of other type of database, like SQL, Postgres.
- Can make use of some server side framework like Django or Flask, instead of writing RAW python.
- Will make other type of requests like delete, update etc.
- When i will scaling it, will use logging as well as Custom APIExceptions, right now its just RAW python.


