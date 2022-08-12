# AWS Course: Modern Application Development with Python on AWS Specialization
## Amazon DynamoDB: Building NoSQL Database-Driven Applications (Course 3 of 4)

### End of Course Assessment

#### Question 1: Which of the following is a type of NoSQL Database? Select two.

- [ ] Graphical store
- [x] Key-value store
- [x] Document database
- [ ] Short-column database
- [ ] Relational database

#### Question 2: Which of the following can be added or changed after the creation of a DynamoDB table?

- [ ] Partition Key
- [ ] Local Secondary Index
- [x] Global Secondary Index
- [ ] Sort Key


#### Question 3: Which of the following are part of the mandatory parameters when creating a DynamoDB table via the SDK with the on-demand read/write capacity mode? Select two.

- [ ] Read Capacity Unit and Write Capacity Unit
- [x] Table name
- [ ] Attribute Definitions
- [x] Partition Key name
- [ ] Sort Key name


#### Question 4: The metric of ConsumedReadCapacityUnits is currently much lower than the Read Capacity Unit provisioned on a DynamoDB table. However, users are saying that they are receiving an error message of ProvisionedThroughputExceededException. What could be the issue?

- [ ] The amount of Write Capacity Unit consumed is higher than normal and uses Read Capacity Units instead.
- [ ] The BatchGetItem operation exceeds the maximum request of 100 items.
- [x] The queries aren't uniformly distributed across all logical partition keys in the table.
- [ ] The throughput exceeds the current throughput limit of the account.


#### Question 5: Which of the following AWS service will help determine latency issues per query in DynamoDB?

- [ ] Amazon CloudWatch Logs
- [ ] AWS CloudTrail
- [x] AWS X-Ray
- [ ] AWS Config


#### Question 6: What are the two types of read/write capacity modes for processing reads and writes on your tables? Select 2.

- [x] Provisioned
- [ ] Reserved
- [ ] Dynamic
- [x] On-demand
- [ ] Auto-Scale


#### Question 7: How many Scan queries need to be sent to DynamoDB to get all the items from the table if the table contains 10 items each with 200KB of data?

- [ ] 1
- [x] 2
- [ ] 5
- [ ] 10


#### Question 8: A DynamoDB table is made up of a Partition Key of UserID, a Sort Key with the date and time and an attribute of Score providing the list of all the scores for a game. A dashboard needs to display the 5 highest scores from the table. What is the most efficient way to keep this dashboard in real time?

- [x] Use DynamoDB Stream and AWS Lambda to update the dashboard each time a higher score is added.
- [ ] Query the table and issue a sort on the Score attribute with a limit of 5 every minute.
- [ ] Scan the table to read all the entries and sort the data in the code to find the highest score.
- [ ] Scan the table and use a FilterExpression for any score that is higher than the last 5 high scores every minute.


#### Question 9: How can the data at rest that was encrypted by DynamoDB be decrypted?

- [ ] Use the Amazon DynamoDB Encryption Client to decrypt the data on the client side.
- [ ] In the query to DynamoDB, send the key to use to decrypt it and let DynamoDB handle the decryption.
- [x] Send a query to DynamoDB as normal and let it transparently decrypt the data.
- [ ] Send a query to DynamoDB and use the AWS Key Management Service to decrypt the data on the client side.


#### Question 10: Which statement is FALSE about DynamoDB Global Tables?

- [x] The data is synchronous replicated between tables.
- [ ] DynamoDB Streams is used to replicate the data between tables.
- [ ] All DynamoDB tables that are part of the DynamoDB Global Table can be written to.
- [ ] The tables must have the same write capacity management settings.


#### Question 11: How can the permissions of a user be restricted only query specific attributes with the least amount of work?

- [ ] Use the Amazon DynamoDB Encryption Client to encrypt the data and don't allow that user to access the key to decrypt it.
- [ ] It's not possible.
- [x] Configure an Identity and Access Management Policy and apply it to the User.
- [ ] Create a Global Secondary Index (GSI) with only those specific attributes projected and only allow the GSI to be queried by the user.


#### Question 12: Which of the following statement is FALSE concerning secondary indexes in DynamoDB?

- [ ] A Global Secondary Index can have a different Partition Key than the main table.
- [x] Local and Global Secondary Indexes are synchronously updated when the main table is updated.
- [ ] A Local Secondary Index can only be created at the time of creation of a table.
- [ ] A table can have more Global Secondary Index than Local Secondary Index.


#### Question 13: What type of datasets stored in DynamoDB should be spread across more than one table?

- [x] Datasets with Time-Series Data.
- [ ] Datasets with Many-to-Many Relationships.
- [ ] Datasets with Many-to-One Relationships.
- [ ] Datasets with similar access patterns.


#### Question 14: What feature of DynamoDB is necessary to make use of Optimistic Locking?

- [x] Conditional writes
- [ ] Locking of items
- [ ] Transaction support
- [ ] Versioning of items


#### Question 15: Given a table that has a Partition Key of UserID, an attribute named AccountLocked and many other attributes. The AccountLocked attribute is set to TRUE when the UserID is has its account locked and isn't set when it's not locked. Not many accounts are typically locked at a time compared to the hundreds of thousands of users in that table. What would be the most optimal way to get a list of all UserID that have their account locked (AccountLocked set to TRUE)?

- [x] Create an index with UserID as the Primary Key and AccountLocked as the Sort Key. Send a Scan to the index to find the list of account locked.
- [ ] Send a scan to the table with the attribute_exists filter expression.
- [ ] Create an index with UserID as the Primary Key and AccountLocked as the Sort Key. Send a Query to the index to find the list of account locked.
- [ ] Send a query to the table with the attribute_exists filter expression.
