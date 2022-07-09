## Week 6 Quiz


#### 1. Which file contains your credentials that the CLI uses to make calls AWS on Cloud9 or from your laptop?

.aws/creds
.aws/keys
.aws/config
- [x] .aws/credentials

#### 2. Consider this scenario: You have created a REST API using Amazon API Gateway, and the data that is returned from your API is relatively static. You want to reduce the latency of your API, what feature can you use to enhance performance? Choose 2 answers.

API Gateway Stage Caching
- [x] Edge Optimized Endpoints 
Private VPC Endpoints
- [x] API Gateway Response Caching

#### 3. What is NOT a best practice for AWS Lambda Functions?

- [x] Run background processes to shorten execution time
Avoid recursive code
Cache static assets in the locally available storage for your function in the /tmp directory
Minimize the complexity of function dependencies


4. Consider this scenario: You are designing an API using Amazon API Gateway that will simply proxy backend resources. There is no need to validate or transform incoming HTTP requests at the Amazon API Gateway level. Which type of API should you use?

REST API
 - [x] HTTP API
Private REST API
WebSocket API


5. In order to optimize your Amazon API Gateway API, you should turn on caching for all resources and HTTP methods, including GET, POST, and DELETE.

True
- [x] False


6. Which of the following use case would benefit from using an edge-optimized endpoint type for a REST API in API Gateway?

The clients are browsers on laptops all from the same office.
- [x] The clients are mobile phones that are geographically distributed.
The communication between the client and the API needs to stay within a VPC.
The clients are EC2 instances running in the same region as the API.


7. In which of the following locations is Amazon CloudFront hosted?

Local zone
- [x] Edge location
Region
Availability zone

8. There are many more AWS Edge locations than AWS Regions.

- [x] True
False


9. What are the steps to make a Lambda layer available to use?

Create a Lambda function, publish it as a Lambda layer and add permissions using a resource policy.
Create a Lambda function with an IAM Role for permissions and publish it as a Lambda layer.
Create the Lambda layer and attach an IAM Role to the Lambda layer for permissions.
- [x] Create the Lambda layer and add permissions using a resource policy.


10. AWS Lambda bills for running functions in what increments?

- [x] 100 ms
10 ms
10 sec
1 sec
