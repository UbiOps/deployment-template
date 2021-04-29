# Deployment Template

This repository contains deployment structure templates for deployments in [UbiOps](https://ubiops.com).

### Supported programming languages and versions

| Language / version | Template directory |
| ------------------ | ------------------ |
| Python 3.5 - 3.8   | `python`           |
| R 4.0              | `r`                |

### Documentation and examples

An extensive documentation about UbiOps can be found at [UbiOps docs](https://docs.ubiops.com "UbiOps docs").

The template deployment package in this repository implements a dummy structured deployment that simply returns a
random number. It expects one input field `input` of type `double precision`, and returns one output field `output` of
type `double precision`.

A more extensive working example of a deployment package zip file can be found at
[Example deployment package](https://storage.cloud.google.com/ubiops/example-deployment-packages/mnist_deployment_package.zip "GCS Bucket: ubiops/mnist_deployment_package.zip") (200 MB), which contains an image recognition model that recognises
a number from an image. Three example images are available to make requests with:
[Image 1](https://storage.cloud.google.com/ubiops/example-deployment-packages/1.jpg "Example input image 1"),
[Image 2](https://storage.cloud.google.com/ubiops/example-deployment-packages/2.jpg "Example input image 2"),
[Image 3](https://storage.cloud.google.com/ubiops/example-deployment-packages/3.jpg "Example input image 3").

Instructions on how to deploy this example deployment can be found at
[UbiOps Quickstart](https://docs.ubiops.com/docs/quickstart "UbiOps Quickstart").

### Directory contents

UbiOps currently supports Python (versions 3.5 / 3.6 / 3.7 / 3.8) and R (version 4.0).

The language directory (`python` or `r`) contains a `deployment_package` directory, and an example script for
calling the deployment (`run_deployment.py` or `run_deployment.R`). A deployable file in UbiOps should be a zipped
version of the `deployment_package` directory that is found in this repository.

The `run_deployment.py` or `run_deployment.R` file in this repository contains example code that runs the deployment
and returns the result, similar to how it is done when running the deployment inside the UbiOps platform. This file is
there for testing and illustration purposes and is not part of the `deployment_package`. It should not be uploaded to
the platform.

### Deployment package structure

The structure of the deployment package can be found in the README in the language directory (`python` or `r`).

### Input/Output types

UbiOps supports two types of input and output:

- **Structured**. Structured data consists of a dictionary (a named list in R) with one or more fields (key value pairs)
  with an associated data type (integer, string, double, boolean, array of integers, array of doubles, array of strings
  or file (`blob`)).
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
