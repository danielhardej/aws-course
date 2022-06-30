# Building Modern Python Applications on AWS
## Week 2 Quiz

#### 1. Consider a scenario where you have created a REST API, and the client using this API is submitting a POST request to an endpoint being hosted by Amazon API Gateway. The client wants to send the payload of the request in a format that is different than the format of the payload the backend code needs. What Amazon API Gateway REST API feature can you use to transform the payload of the request from the clients format to the format the backend code needs?

- [ ] Integration Request
- [x] A Mapping
- [ ] Method Response
- [ ] A Model


#### 2. A Model is written in VTL and used for Request Validation.

- [ ] True
- [x] False


#### 3. You can create key-value pairs as configuration attributes associated with a deployment stage of a REST API. They act like environment variables and can be used in your API setup and mapping templates. You can access these variables through the use of:

- [ ] $environmentVariables
- [ ] $context
- [ ] $util
- [x] $stageVariables


#### 4. Which of the following list three ways to add access controls or authorizers for a REST API in Amazon API Gateway?

Usage plan, AWS WAF and Security Group
- [ ] IAM, Client-side SSL certificate and Key Management Service
- [x] Lambda authorizer, VPC endpoint policy, Cognito User Pool
- [ ] Resource policy, cross-origin resource sharing and Secrets Manager


#### 5. Which of the following is a way to do access control for an HTTP API in Amazon API Gateway?

- [ ] IAM
- [x] JSON Web Token
- [ ] Lambda authorizer
- [ ] Cognito Federated Identities


#### 6. Which access control mechanism can be used to throttle the amount of request being sent from a client to a REST API in API Gateway?

- [ ] Secret Key
- [x] API Key
- [ ] Access Key
- [ ] Key Management Service


#### 7. At which point of the flow in a method execution in Amazon API Gateway can you add a Cognito User Pool, Lambda or IAM authorizer?

- [ ] Integration Response
- [ ] Integration Request
- [x] Method Request
- [ ] Method Response


#### 8. Which of the following authorizer mechanism will require you to develop it using code in a REST API in API Gateway?

- [x] Lambda authorizer
- [ ] Identity and Access Management
- [ ] Cognito Identity Pool
- [ ] Cognito User Pool


#### 9. What types of APIs can Amazon API Gateway NOT be used to create?

- [ ] HTTP
- [ ] WebSocket
- [ ] REST
- [x] BPM


#### 10. What is used to manage and configure API deployments in Amazon API Gateway?

- [ ] Platform
- [x] Stage
- [ ] Ledge
- [ ] Cliff
