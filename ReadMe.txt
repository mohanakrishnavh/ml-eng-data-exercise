Requirement : Python3

Run the python file in the command prompt by the command:
python test.py

1. How does your solution handle malformed or corrupt data?
   Test 1 : My solution reads all the json files and validates the 'event_date' with the current date to ensure that information is updated correctly.
   Test 2 : I have assumed that "First Name" and "Last Name" as mandatory fields and a value has to be entered for both of these attributes.
   Test 3 : I have validated the email address using regular expression to ensure it is in the correct format.

2. Is your solution optimized for query latency or throughput?
   The solution first parses the json files and builds an index to fetch the account information with minimum latency.

3. What would you do differently if the client doesn’t send the account ID?
   I have build a unique custom argument "address" which combines the values in "street_number, street_name, city, state and zipcode" , this can be used to identify the account owner.

4. If the view gets very large (can no longer fit into memory), how can we modify it to ensure we’re still able to look up examples?
   We can modify the program to build the index and distriute the index files to multiple machines and write a spark job to lookup the information.