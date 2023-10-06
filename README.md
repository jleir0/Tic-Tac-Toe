# Tic-Tac-Toe

Juan Luis Leiro Ventoso (Juan)

## Proyect

Online web based Tic- Tac-Toe game SaaS service.

## Deployment

When a tag is created for a new release, the automatic deployment succeeds.

## Configuration

There are Action Secrets to configure the connection with Docker, OpenShift, and the database.

## Schema

The code and tests are in the 'src' folder, and the configuration for Docker, Git, and the database is at the same level as the 'src' folder.

## Execution

This is the URI to run the service: http://a003ec227614d48719ad48f477b0d36c-631706736.us-east-2.elb.amazonaws.com:5000/

## Technical documentation

Code was made with python and flask, and tests were developed with unittest.
CI/CD workflow run the test automatically, build the container and push it to docker and finally, connect with opensift to send the secrets and create the imagestream.
Openshift hosts the deployment for the image using a load balancer to enable access from the outside, as well as the PostgreSQL service for the database.

## ISSUES

Due to a credentials issue that I don't understand, it's not logging into the database, which prevents the creation of the API. So, if we access the link, we won't get a response. Because of this, some tests fail, and I had to change their names so that they aren't detected and the complete CI/CD workflow can be executed.

I also tried to connect to a database created on Google Cloud Platform, but it was giving timeout issues that I couldn't figure out how to fix.

## USERS

I have created a little service code for the login. The secret_key must be a github secret but I mocked one in the test and I dont code how to save the data in the db due to the connection problems and because I make some similar code in the match service.