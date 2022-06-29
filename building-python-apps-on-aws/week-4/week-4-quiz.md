## Building Modern Python Applications on AWS
## Week 4 Quiz

#### Q1. You have an....?

- [ ] Invoking a Lambda Function
- [ ] Run an Amazon Elastic Container Service task
- [ ] Send a message in Amazon Simple Queue Service
- [x] Execute a program running on an external server

#### Q2. When defining a Step Function state machine, what language can be used?

- [ ] Java
- [x] JSON
- [ ] NodeJS
- [ ] Python

#### Q3. What state type can be used to execute a set of steps for each element of an input array in parallel?

- [ ] Array
- [ ] Choice
- [ ] Parallel
- [x] Map

#### Q4. A state machine in AWS Step Function is used for doing continuous deployment as part of a pipeline. One of the steps is to use Lambda to send an email asking for a manager to approve or not the deployment in production. Which of the following service integration pattern should be used?

- [x] Wait for Callback
- [ ] Activity Task
- [ ] Run a Job
- [ ] Request Response

#### Q5. A state machine in AWS Step Function makes use of the AWS Batch service to run a batch job on many EC2 instances. The state machine doesn’t need to see the output of the batch job, but only that it started. Which of the following service integration pattern should be used?

- [x] Wait for Callback
- [ ] Activity Task
- [ ] Run a Job
- [ ] Request Response

#### Q6. Existing EC2 instances are used to do batch processing on data hosted in an S3 bucket. A state machine in AWS Step Functions must be used to send the location where that data is to that group of instances. Which of the following would be appropriate steps in the right order for this scenario to work?

- [ ] Create an activity, add the activity to the state machine, and Step Function will now call the code in the EC2 instance to do the work.
- [ ] Change the code in the EC2 instances to pull from the state machine for work to do using the Wait for Callback integration pattern of a Task type state.
- [ ] Use the Run a Job integration pattern of a Task type state that will call the EC2 instances to do the work.
- [x] Create an activity, add the activity to the state machine, and change the code in the EC2 instances to pull from the activity for work to do.

#### Q7. Which setting of a Step Function activity task type definition is used to make sure that the worker is still working on activity task it was asked to do?

- [ ] TimeoutSeconds
- [ ] RetrySeconds
- [x] HeartbeatSeconds
- [ ] CallbackSeconds

#### Q8. Which of the following service integration pattern is supported by an AWS Step Function Express workflow?

- [ ] Wait for Callback
- [ ] Activity Task
- [ ] Run a Job
- [x] Request Response

#### Q9. For orchestrating a few Lambda functions that run for a very short duration at volumes as high as 5,000 concurrent execution, which type of workflow should be used?

- [ ] Dedicated workflow
- [ ] Concurrent workflow
- [ ] Standard workflow
- [x] Express workflow

#### 10. Which of the following has the right associations between the service and its function?

- [x] SNS is a pub/sub and EventBridge is a service bus
- [ ] SQS is a queue service and SNS is a service bus
- [ ] Step Function orchestrates and SQS is a service bus
- [ ] EventBridge is a service bus and Step Function is a pub/sub
