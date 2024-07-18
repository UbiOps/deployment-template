"""
The file containing the deployment code is required to be called 'deployment.py' and should contain the 'Deployment'
class and 'request' method. Optionally, the file contains a 'requests' method which accepts a list of requests. If the
deployment receives a list of requests and has a 'requests' function then it will be called. Otherwise, the 'request'
function will be called separately for each individual request.
"""

# Always use absolute imports when importing modules from the deployment package directory. For example
# `import my_module` instead of `import .my_module`
import random


class Deployment:

    def __init__(self, base_directory, context):
        """
        Initialisation method for the deployment. It can for example be used for loading modules that have to be kept in
        memory or setting up connections. Load your external deployment files (such as pickles or .h5 files) here.

        :param str base_directory: absolute path to the directory where the deployment.py file is located
        :param dict context: a dictionary containing details of the deployment that might be useful in your code.
            It contains the following keys:
                - deployment (str): name of the deployment
                - version (str): name of the version
                - input_type (str): deployment input type, either 'structured' or 'plain'
                - output_type (str): deployment output type, either 'structured' or 'plain'
                - language (str): programming language the deployment is running
                - environment_variables (str): the custom environment variables configured for the deployment.
                    You can also access those as normal environment variables via os.environ
        """

        print("Initialising My Deployment")

    def request(self, data, context):
        """
        Method for deployment requests, called separately for each individual request.

        :param dict/str data: request input data. In case of deployments with structured data, a Python dictionary
            with as keys the input fields as defined upon deployment creation via the platform. In case of a deployment
            with plain input, it is a string.
        :param dict context: a dictionary containing details of the request that might be useful in your code.
            It contains the following keys:
                - id (str): the id of the request
                - pipeline_id (str): the pipeline_id if the request is part of a pipeline request
                - pipeline_version_id (str): the pipeline_version_id if the request is part of a pipeline request
                - pipeline_object_id (str): the pipeline_object_id if the pipeline is part of the pipeline request
                - pipeline_request_id (str): the pipeline_request_id if the request is part of a pipeline request
                - request_mode (str): if the type of request is express or batch
        :return dict/str: request output. In case of deployments with structured output data, a Python dictionary
            with as keys the output fields as defined upon deployment creation via the platform. In case of a deployment
            with plain output, it is a string. In this example, a dictionary with the key: output.
        """

        print(f"Processing request {context['id']} for My Deployment")

        # You can run any code to handle the request here.

        # For a structured deployment, we return a Python dict with output. In this example, we are assuming this
        # deployment receives one input field called 'input' and outputs one field called 'output'
        return {
            "output": data['input'] * random.random()
        }

    # (OPTIONAL) Uncomment these lines in case you want to use 'requests' functionality
    # def requests(self, data, context):
    #     """
    #     Method for deployment requests, called once with a list of requests.
    #
    #     :param list[dict/str] data: request input data. In case of deployments with structured data, a list of Python
    #         dictionaries with as keys the input fields as defined upon deployment creation via the platform. In case
    #         of a deployment with plain input, it is a list of strings.
    #     :param dict context: a dictionary containing details of the request that might be useful in your code.
    #         It contains the following keys:
    #             - id (str): the id of the request
    #             - pipeline_id (str): the pipeline_id if the request is part of a pipeline request
    #             - pipeline_version_id (str): the pipeline_version_id if the request is part of a pipeline request
    #             - pipeline_object_id (str): the pipeline_object_id if the pipeline is part of the pipeline request
    #             - pipeline_request_id (str): the pipeline_request_id if the request is part of a pipeline request
    #             - request_mode (str): if the type of request is express or batch
    #     :return list[dict/str] or dict/str: request output. In case of deployments with structured output data, a
    #         Python dictionary (or list of dictionaries) with as keys the output fields as defined upon deployment
    #         creation via the platform. In case of a deployment with plain output, it is a string (or list of strings).
    #         In this example, a list of dictionaries with the key: output.
    #     """
    #
    #     print(f"Processing requests {context['id']} for My Deployment")
    #
    #     # You can run any code to handle the requests here.
    #
    #     # For a structured deployment, we return a list of Python dicts as output. In this example, we are assuming
    #     # this deployment receives a list of dicts with one input field called 'input' and outputs a list of dicts
    #     # with one field called 'output'. It is also possible to return a single dict as output and thereby reducing
    #     # the number of requests from many to one.
    #
    #     output = []
    #     for item in data:
    #         output.append({
    #             "output": item['input'] * random.random()
    #         })
    #     return output
