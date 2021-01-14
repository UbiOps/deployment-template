"""
This file simulates the platform back-end that initialises the deployment and makes a request. It should not be included
in a deployment package.
"""

import os
import sys


# Deployment_directory points to base folder of the deployment, which should therefore be called 'deployment_package'.
deployment_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'deployment_package')

# Update $PATH with the deployment base directory and libraries before importing the deployment package.
sys.path = [deployment_directory, os.path.join(deployment_directory, 'libraries')] + sys.path


# Import the deployment package
import deployment_package.deployment


def main():
    print("Starting deployment request example")

    # Initialise the deployment. The platform calls this method in exactly the same way.
    # Here, we leave the context argument as an empty dictionary since it is normally filled in by the platform
    # when loading the deployment.
    deployment = deployment_package.deployment.Deployment(
        base_directory=deployment_directory, context=dict()
    )

    # Mock input data. When a request is made, this dictionary is initialized.
    # In case of deployments with structured data, it will contain the keys defined by the user upon deployment
    # creation via the platform. In case of a deployment that receives a plain input, it will be a string.

    # Adjust this example to test deployment input and request processing
    input_data = {
        'input': 10.9
    }

    # Make the prediction. The platform calls this method in exactly the same way
    request_result = deployment.request(input_data)

    print("Deployment request result: %s" % request_result)


if __name__ == '__main__':
    main()
