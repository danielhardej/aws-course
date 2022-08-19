# Improve Your Python Code Using Amazon CodeGuru
## Week 2 Quiz

#### Question 1: True or False: Unhandled resource leaks can lead to memory exhaustion and cause systems to run slowly or crash.

- [x] True
- [ ] False

##### Note: Resources can use memory when they are not acquired and released correctly. This situation can lead to memory issues within a system, which can then lead to slowdowns—or, in a worst-case scenario—a system crash.

#### Question 2: What are some of the recommendation categories that Amazon CodeGuru Reviewer can make recommendations on? (Select THREE.)

- [x] AWS best practices
- [x] Common coding best practices
- [ ] Compilation errors
- [x] Resource leaks

##### Note: CodeGuru Reviewer does not flag syntactical mistakes because these types of errors are relatively easy to find. Instead, CodeGuru Reviewer identifies more complex problems and suggests improvements that are related to the following categories: AWS best practices, concurrency, resource leak prevention, sensitive information leak prevention, common coding best practices, refactoring, input validation, security analysis, and code quality

#### Question 3: True or False: After a pull request is opened, you must manually add Amazon CodeGuru Reviewer as a reviewer so that it can leave comments on the pull request.

- [ ] True
- [x] False

##### Note: The answer to this question is False. After CodeGuru Reviewer is associated with a repository, it will automatically be added as a reviewer on any pull request that is opened. CodeGuru Reviewer will then analyze the code in the pull request, and leave comments on it.
