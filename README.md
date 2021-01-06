# cloudwatch-event-lambda
Example of triggering a lambda in response to cloudwatch alarm state change via Eventbridge

## Deploying the stack
* Clone the repository
* Open a terminal and configure the bucket name of your target Amazon S3 distribution bucket and region where you'd like to deploy
```
export ACCOUNT_NAME=<name of the account to deploy the solution to>
export SOLUTION_NAME=cloudwatch_event_lambda
export DIST_OUTPUT_BUCKET=<S3 bucket to deploy the solution>
export VERSION=1.0.0
export AWS_REGION=us-east-2
```
_Note:_ You have to manually create an S3 bucket with the name "$DIST_OUTPUT_BUCKET"; 

* Create a file in the parameters folder named '$ACCOUNT_NAME-$AWS_REGION.json' with the following parameters;

```json
[
  {
    "ParameterKey": "AlarmName",
    "ParameterValue": "<name of alarm to trigger on state change>"
  },
  {
    "ParameterKey": "EmailTo",
    "ParameterValue": "<email address to send notification>"
  }
]
```
* Next make the deploy script executable and run it
```
cd ./deployment
chmod +x ./deploy.sh  \n
./deploy.sh
```
---


Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

Licensed under the Apache License Version 2.0 (the "License"). You may not use this file except in compliance with the License. A copy of the License is located at

    http://www.apache.org/licenses/

or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions and limitations under the License.
