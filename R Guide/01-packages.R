# File: 01-packages.R
# Date: 18/01/2023

### THEORY #####################################################################

# There are 2 types of packages: Base and Contributed
# Base: Installed with R but not loaded by default.
# Contributed: Need to be downloaded, installed & loaded separately.

# But from where you will download?
# 1. CRAN: Official R documentation (https://cran.r-project.org)
# 2. Crantastic!: Listing the packages and will redirect to CRAN if you click
#     (https://crantastic.org)
# 3. GitHub: can download from GitHub (https://github.com/trending/r)

# Commonly used packages:
# 1. dplyr: for manipulating data-frames
# 2. tidyr: for cleaning up information
# 3. stringr: for working with strings or text information
# 4. lubridate: for manipulating date information
# 5. httr: for working with website data
# 6. ggvis: grammar for graphics for interactive visualizations
# 7. ggplot2: most commonly used data visualization
# 8. shiny: for interactive application working with websites
# 9. rio: for input/output or importing/exporting data
# 10. rmarkdown: create interactive notebook riched docs

# And one package to load them all - pacman

# LOAD PACKAGES ############################################

# I recommend "pacman" for managing add-on packages. It will
# install packages, if needed, and then load the packages.
install.packages("pacman")

# Then load the package by using either of the following:
require(pacman)  # Gives a confirmation message.
library(pacman)  # No message.

# Or, by using "pacman::p_load" you can use the p_load
# function from pacman without actually loading pacman.
# These are packages I load every time.
pacman::p_load(pacman, dplyr, GGally, ggplot2, ggthemes, 
               ggvis, httr, lubridate, plotly, rio, rmarkdown, shiny, 
               stringr, tidyr) 

library(datasets)  # Load/unload base packages manually

# CLEAN UP #################################################

# Clear packages
p_unload(dplyr, tidyr, stringr) # Clear specific packages
p_unload(all)  # Easier: clears all add-ons
detach("package:datasets", unload = TRUE)  # For base

# Clear console
cat("\014")  # ctrl+L

# Clear mind :)