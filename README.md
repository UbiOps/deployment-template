# Deployment Template

This repository contains a deployment structure template for deployments in [UbiOps](https://ubiops.com).


### Documentation and examples

Extensive documentation about UbiOps can be found at [UbiOps docs](https://docs.ubiops.com "UbiOps docs").

The template deployment package in this repository implements a dummy structured deployment that simply returns a
random number. It expects one input field `input` of type `double precision`, and returns one output field `output` of
type `double precision`.

A more extensive working example of a deployment package zip file can be found at
[Example deployment package](https://storage.cloud.google.com/ubiops/example-deployment-packages/mnist_deployment_package.zip "GCS Bucket: ubiops/mnist_deployment_package.zip") (14 MB), which contains an image recognition model that recognises
a number from an image. Three example images are available to make requests with:
[Image 1](https://storage.cloud.google.com/ubiops/example-deployment-packages/1.jpg "Example input image 1"),
[Image 2](https://storage.cloud.google.com/ubiops/example-deployment-packages/2.jpg "Example input image 2"),
[Image 3](https://storage.cloud.google.com/ubiops/example-deployment-packages/3.jpg "Example input image 3").

Instructions on how to deploy this example deployment can be found in the
[UbiOps Starter Tutorial](https://ubiops.com/docs/starter-tutorial/ "UbiOps Starter Tutorial").


### Repository contents

This repository contains a `deployment_package` directory, and an example script for calling the deployment when you
are developing locally (`run_deployment.py`).

A deployment as uploaded to UbiOps should be a zipped version of the `deployment_package` directory that is found in 
this repository.

The `run_deployment.py` file contains example code that runs the deployment and returns the result, similar to how it is
done when running the deployment inside the UbiOps platform. This file is there for testing and illustration purposes 
and is not part of the `deployment_package`. It should not be uploaded to the platform.


### Deployment package structure

The uploaded deployment package directory should have the following structure:

* `deployment.py` with a class `Deployment`
    * `__init__` method for initialization
        * Takes two arguments:
            * `base_directory` - the absolute path to the deployment directory. The base_directory can be used by the
            Deployment class to locate other files in the package.
            * `context` - a dictionary containing deployment version details. It contains the name of the project,
              deployment and deployment version, input/output type and fields of the deployment, programming language
              and environment variables defined for the deployment version.
              You can also access those as normal environment variables via `os.environ`.
    * `request` method to make a prediction, run a statistical analysis, or some other code
        * Takes two arguments:
          * `data` - a dictionary containing all input data for the request.
          * `context` - a dictionary containing request metadata.
        
* A `libraries` directory [OPTIONAL]
    * Dependencies can be installed in this directory. You can read more about this in the section Dependencies,
      and the README located in the `libraries` directory.
    
* A `requirements.txt` file [OPTIONAL]
    * A file with package requirements that will be installed in your deployment when uploading your package to UbiOps.

The deployment package can contain as many additional files and sub-directories as needed, but the `deployment.py` will
need to interact with them. For example, if a model is contained in a pickle file, then code in the Deployment class
should handle the interaction with the pickle (loading, using etc.).

UbiOps currently supports Python (versions 3.8 and above) natively. Using other languages is possible by - where 
necessary - installing the required software using a `ubiops.yaml` file and calling it from the `deployment.py`.


### Dependencies

Deployments often rely on external libraries and packages. You can use Python packages in your deployment by defining
the packages in the `requirements.txt` file as you would normally do in a local project. The platform will retrieve
and install those packages for you during the building phase using Python pip.

If you want to use custom libraries that are not available on public package repositories, you can install these
libraries into the `libraries` directory manually. This directory will be added to the system `$PATH`, allowing the
deployment to import them in the usual way.

Your deployment will run in an 64 bit (x86–64) Linux environment. Therefore, if you use any low level libraries that for
example include compiled C extensions or other less portable software, make sure that these are compatible with these
types of systems.


### Input/Output types

UbiOps supports two types of input and output:

- **Structured**. Structured data consists of a dictionary (a named list in R) with one or more fields (key value pairs)
  with an associated data type (integer, string, double, boolean, array of integers, array of doubles, array of strings
  or file).
- **Plain**. Any string without structure.

Combinations between input and output types are supported, e.g. a deployment with structured input and plain output, or
vice-versa.


### External sources

The example deployment package and example input data make use of public sources. The model used is a pre-trained
Convolutional Neural Network as made available with the open-source package [Keras](https://keras.io) (Chollet,
François. "Keras." (2015)). It has been trained on the
[MNIST database](http://yann.lecun.com/exdb/mnist/, "MNIST database") (Creative Commons license). No additional changes
to the model have been made. The example input images are images of the
[MNIST database](http://www.pymvpa.org/datadb/mnist.html "MNIST database resource") (LeCun et al. (1999): The MNIST
Dataset Of Handwritten Digits (Images)). We've linked to these files solely for the purpose of demonstrating the
functionality of the UbiOps platform.
