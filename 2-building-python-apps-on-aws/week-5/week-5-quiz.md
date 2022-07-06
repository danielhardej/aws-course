# Building Modern Python Applications on AWS
## Week 5 Quiz

#### 1. In order to turn on distributed tracing with AWS Lambda and capture a segment for the lambda function execution, you must include the AWS SDK for X-Ray in your deployment package.

- [ ] True
- [x] False


#### 2. When using the AWS SDK for X-Ray, to measure granular performance of a singular API call or specific line(s) of code, you can create a new:

- [ ] Trace
- [x] Subsegment
- [ ] Annotation
- [ ] Sampling Document


#### 3. When using the AWS X-Ray SDK in code that will be run on top of AWS Lambda, you must also create and manage the X-Ray Daemon on your own by including it as a dependency in your deployment package.

- [ ] True
- [x] False


#### 4. What do you need to provide to Step Functions so it can be allowed to send logs to CloudWatch Logs?

- [ ] IAM Policy
- [ ] IAM User
- [x] IAM Role
- [ ] IAM Group


#### 5. Which of the following matches the definition of an Amazon CloudWatch Log Group?

- [ ] A group of events coming from the application instance or resource being monitored.
- [x] A group of log streams that share the same retention, monitoring, and access control settings.
- [ ] A group of settings determining how long log events are kept in CloudWatch Logs.
- [ ] A group of records of some activity recorded by the application or resource being monitored.


#### 6. What is the proper flow for sending logs to Amazon CloudWatch Logs?

- [x] Create a Log Group, then create a Log Stream and send Log Events from the application to the Log Stream.
- [ ] Create a Log Group, then create a Log Stream and send Log Events from the application to the Log Group.
- [ ] Create a Log Stream, add the Log Stream to the Log Group and send Log Events from the application to the Log Stream.
- [ ] Create a Log Stream, add the Log Stream to the Log Group and send Log Events from the application to the Log Group.


#### 7. What protocol can be used to send events to Amazon CloudWatch Logs?

- [ ] UDP
- [ ] RELP
- [x] HTTPS
- [ ] syslog


#### 8. What is the easiest way to send logs to Amazon CloudWatch Logs from code in a Lambda function?

- [ ] Make an HTTPS call to Amazon CloudWatch logs
- [ ] Use the syslog library to send logs directly to CloudWatch logs
- [ ] Use the Amazon CloudWatch SDK to send logs
- [x] Write to stdout or stderr and logs will be sent automatically


#### 9.What do you need to define on a Lambda function to send logs to CloudWatch Logs?

- [ ] The Log Stream to send logs to and an IAM Role
- [ ] An IAM Role
- [x] The Log Group to send logs to and an IAM Role
- [ ] The Log Group and Log Stream to send logs to


#### 10. In AWS X-Ray, what represents the compute resources running the application logic?

- [ ] Rays
- [ ] Parts
- [x] Segments
- [ ] Instances
