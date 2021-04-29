# Deployment Template Python

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
        * Takes one argument: `data` - a dictionary containing all input data for the request.
        
* A `libraries` directory [OPTIONAL]
    * Dependencies can be installed in this directory. You can read more about this in the section Dependencies,
      and the README located in the 'libraries' directory.
    
* A `requirements.txt` file [OPTIONAL]
    * A file with package requirements that will be installed in your deployment when uploading your package to UbiOps.

The deployment package can contain as many additional files and sub-directories as needed, but the `deployment.py` will
need to interact with them. For example, if a model is contained in a pickle file, then code in the Deployment class
should handle the interaction with the pickle (loading, using etc.).


### Dependencies
Deployments often rely on external libraries and packages. You can use Python packages in your deployment by defining
the packages in the `requirements.txt` file as you would normally do in a local project. The platform will retrieve
and install those packages for you during the building phase using Python pip.

If you want to use custom libraries that are not available on public package repositories, you can install these
libraries into the `libraries` directory manually. This directory will be added to the system `$PATH`, allowing the
deployment to import them in the usual way.

Your deployment will run in an 64 bit (x86–64) Linux environment. Therefore, if you use any low level libraries that for
example include compiled C extensions or other less portable software, make sure that these are compatible on these
types of systems. Libraries compiled on Windows or Mac machines will often not function properly or encounter
performance issues.
