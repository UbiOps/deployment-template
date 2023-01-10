# This file (containing the deployment code) is required to be called 'deployment.R' and should contain an 'init'
# and 'request' method. Optionally, the file contains a 'requests' method which accepts a list of requests. If the
# deployment receives a list of requests and has a 'requests' function then it will be called. Otherwise, the 'request'
# function will be called separately for each individual request.

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
#' @param context (named list) details of the deployment and deployment request that might be useful in your code
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

# (OPTIONAL) Uncomment these lines in case you want to use 'requests' functionality
# #' @title Requests
# #' @description Method for deployment requests, called with a list of requests
# #' @param input_data list[str or named list] requests input data
# #'     - In case of structured input: a list of named lists, with as keys the input fields as defined upon deployment
# #'       creation
# #'     - In case of plain input: a list of strings
# #' @param base_directory (str) absolute path to the directory where the deployment.R file is located
# #' @param context (named list) details of the deployment and deployment request that might be useful in your code
# #' @return output data list[str or named list] requests result
# #'     - In case of structured output: a list of named lists, with as keys the output fields as defined upon deployment
# #'       creation
# #'     - In case of plain output: a list of strings
# requests <- function(input_data, base_directory, context) {
#     print("Processing requests for My Deployment")
#
#     # ADD YOUR CODE HERE...
#
#
#     # Another script can be called using: source(file.path(base_directory, "<script name>.R"))
#     # Environment variables can be obtained via: Sys.getenv("ENV_VAR", unset = "")
#
#
#     # In this example, we loop over all request input items and construct the output data for the output field "output"
#     # by multiplying each value for the input field "input" with a random number. This results in an output list of the
#     # same length as the input data. This is not required; it is possible to return a different output length.
#     # It is also possible to return a single output item and thereby reducing the size from many to one.
#     output_data <- list()
#     for(i in 1:length(input_data)) {
#         output_data[[i]] <- list( output = input_data[[i]][["input"]] * runif(1) )
#     }
#
#     # Return the output data
#     output_data
# }
