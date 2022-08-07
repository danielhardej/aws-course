## Amazon DynamoDB: Building NoSQL Database-Driven Applications
### Week 3 Quiz

#### How can the data of a DynamoDB Table be encrypted at rest with the least amount of work?

- [ ] Use AWS Key Management Service to encrypt the data before storing it in DynamoDB.
- [ ] Use a library to encrypt the data before storing it in DynamoDB.
- [x] Do nothing, it's encrypted by default.
- [ ] Use the Amazon DynamoDB Encryption Client to encrypt the data before storing it in DynamoDB.

#### How can a user be authenticated with the DynamoDB service via the SDK?

- [ ] Using a Username and a Password.
- [ ] Using a Certificate.
- [ ] Using a API Keys.
- [x] Using an Access Key and a Secret Access Key.

#### How can DynamoDB be accessed from within a VPC without going through an Internet Gateway?

- [ ] Use a NAT Gateway instead.
- [ ] Use a Virtual Private Gateway.
- [x] Use a VPC Gateway Endpoint.
- [ ] Use the Private IP of DynamoDB.

#### How does DynamoDB know when to expire the items from a table using the Time To Live feature?

- [ ] When using the PutItem API call, a TTL parameter is specified in seconds at which to expire this particular item.
- [x] An attribute in the item contains the time at which to expire the item.
- [ ] When enabling the TTL feature, an amount of time in seconds is specified as the amount of time each item can stay in the table.
- [ ] DynamoDB looks for an attribute named ExpirationTime as part of the item to know when to expire the item.
