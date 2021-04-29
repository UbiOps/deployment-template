# Deployment Template R

### Deployment package structure

The uploaded deployment package directory should have the following structure:

* `deployment.R`
  * `init` method for initialization takes two arguments:
    * `base_directory` - the absolute path to the deployment directory. The base_directory can be used by the
    to locate other files in the package.
    * `context` - a named list containing deployment version details. It contains the name of the project,
    deployment and deployment version, input/output type and fields of the deployment, programming language
    and environment variables defined for the deployment version.
    You can also access those as normal environment variables via `Sys.getenv()`.
  * `request` method to make a prediction, run a statistical analysis, or some other code. It takes three arguments:
    * `input_data` - a list-object containing all input data for the request.
    * `base_directory` - the absolute path to the deployment directory. The base_directory can be used by the
    to locate other files in the package.
    * `context` - a named list containing deployment version details. It contains the name of the project,
    deployment and deployment version, input/output type and fields of the deployment, programming language
    and environment variables defined for the deployment version.
    You can also access those as normal environment variables via `Sys.getenv()`.

* `renv.lock` [OPTIONAL]
  - A file with package requirements that can be installed with `renv::restore()`. It will automatically be installed in
    your deployment when uploading your package to UbiOps. For more information, take a look at
    <a href="https://rstudio.github.io/renv/reference/lockfiles.html" target="_blank">renv documentation</a>.

* `install_packages.R` [OPTIONAL]
  * A file with package requirements that will run when uploading your package to UbiOps.
    It typically contains lines, like, `install.packages("randomForest")`.

The deployment package can contain as many additional files and sub-directories as needed, but the `deployment.R` will
need to interact with them. For example, if a model is contained in a pickle file, then code in the `init`/`request`
functions should handle the interaction with the pickle (loading, using etc.).


### Dependencies
Deployments often rely on external libraries and packages. You can use R packages in your deployment by defining
the packages in the `renv.lock` file or by defining installation instructions in the `install_packages.R`. The platform
will retrieve and install those packages for you during the building phase.
When both `renv.lock` and `install_packages.R` are present, `renv.lock` will be handled first.
