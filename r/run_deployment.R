# This file simulates the platform back-end that initialises the deployment and makes a request. It should not be included
# in a deployment package.

# Deployment_directory points to base folder of the deployment, which should therefore be called 'deployment_package'.
deployment_directory <- file.path("ENTER_YOUR_LOCAL_ABSOLUTE_PATH_HERE", "deployment_package")

# Import the deployment package
source(file.path(deployment_directory, "deployment.R"))

init( base_directory = deployment_directory, context = list() )

input_data <- list(input=10.9)
request_result <- request( input_data = input_data, base_directory = deployment_directory, context = list() )

print(paste("Deployment request result:", request_result))
