# This file (containing the deployment code) is required to be called 'deployment.R' and should contain an 'init'
# and 'request' method.

#' @title Init
#' @description Initialisation method for the deployment.
#'     It can for example be used for loading modules that have to be kept in memory or setting up connections.
#' @param base_directory (str) absolute path to the directory where the deployment.R file is located
#' @param context (named list) details of the deployment that might be useful in your code
init <- function(base_directory, context) {
    print("Initialising My Deployment")
}

#' @title Request
#' @description Method for deployment requests, called separately for each individual request.
#' @param input_data (str or named list) request input data
#'     - In case of structured input: a named list, with as keys the input fields as defined upon deployment creation
#'     - In case of plain input: a string
#' @param base_directory (str) absolute path to the directory where the deployment.R file is located
#' @param context (named list) details of the deployment that might be useful in your code
#' @return output data (str or named list) request result
#'     - In case of structured output: a named list, with as keys the output fields as defined upon deployment creation
#'     - In case of plain output: a string
request <- function(input_data, base_directory, context) {
    print("Processing request for My Deployment")


    # ADD YOUR CODE HERE...


    # Another script can be called using: source(file.path(base_directory, "<script name>.R"))
    # Environment variables can be obtained via: Sys.getenv("ENV_VAR", unset = "")


    # In this example, the input field "input" in multiplied by a random number and returned in output field "output"
    list( output = input_data[["input"]] * runif(1) )
}
