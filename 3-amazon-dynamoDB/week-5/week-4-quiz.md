## Amazon DynamoDB: Building NoSQL Database-Driven Applications
### Week 4 Quiz

#### Question 1: Using Optimistic Locking, the user is responsible for managing the version of an item using an attribute.

- [x] True
- [ ] False

#### Question 2: When querying a DynamoDB Local Secondary Index that doesn't have a required attribute specified in the query, what is the most optimal way to get the data if that attribute is rarely needed?

- [ ] Modify the Projected attributes field to All.
- [ ] Modify the Projected attributes field to Include and specify that specific attribute.
- [ ] After retrieving the data from the index, query the main table for the missing attribute.
- [x] DynamoDB will return the attribute from the main table if it can't find it in the index.

#### Question 3: Where should large attribute values should be stored in relation to DynamoDB?

- [ ] Amazon DynamoDB Streams
- [ ] Amazon Elasticsearch Service
- [x] Amazon Simple Storage Service
- [ ] In DynamoDB as there is no limit to the storage

#### Question 4: Which of the following statement is TRUE concerning Amazon DynamoDB Accelerator (DAX)?

- [ ] DAX should be used to speed up an application doing a lot of writes to DynamoDB.
- [x] DAX should be used for an application reading from the same partition key very often.
- [ ] DAX requires an entire rewrite of the application so that reads go to DAX and writes go to DynamoDB.
- [ ] DAX should be used for single digit millisecond latency reads.
