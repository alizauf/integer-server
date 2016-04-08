Aliza's Integer Server
======================

This server returns integers from the following sequences.

- [The fibonacci sequence](https://oeis.org/A000045)
- [Happy numbers](https://oeis.org/A007770)
- [Abundant numbers](https://oeis.org/A005101)

Users can request two types of data:

- the first *n* terms of a specific number sequence.
- the *n*th term of a specific number sequence


Run the server
--------------
1. Create a new directory and cd into it
2. `git clone https://github.com/alizauf/integer-server.git` 
3. `$ python integer-server/app.py`
4. If all goes well, you should see your server running with this message:

`Running on http://127.0.0.1:5000/`
If you use a different port, change below.

Access the API endpoint
-----------------------
The URL path has 3 required parameters:

`http://localhost:5000/api/v1.0/functions/FUNCTION/NUMBER/OPTION`

**FUNCTION**

Valid input: 
- `fibonacci`
- `happy`
- `abundant`

**NUMBER** (the nth term)

Valid Input:
- `Any integer > 0`

3. **OPTION**

Valid Input:

- `1` Will return a list of the first *n* terms of selected number sequence
- `2` Will return the the *n*th term of selected number sequence

Try it out
----------
Once your server is running, try it out. 
The following command will return the first 10 numbers in the *fibonacci* sequence, as well as JSON metadata about your request.

`curl -i http://localhost:5000/api/v1.0/functions/fibonacci/10/1`

returns:

```
{
  "list": [
    0,
    1,
    1,
    2,
    3,
    5,
    8,
    13,
    21,
    34
  ],
  "n": 10,
  "sequence": "fibonacci"
}
```
The follow request will return the 20th happy number.

`curl -i http://localhost:5000/api/v1.0/functions/happy/20/2`

returns:

```
{
  "n": 20,
  "sequence": "happy",
  "term": 100
}
```






