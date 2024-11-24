#! /bin/bash

src_directory="/usr/local/src/nanoWizard"
bin_directory="/usr/local/bin"
installed="/usr/local/src/nanoWizard/installed"

if [ ! -d "$src_directory" ]; then 
    sudo mkdir /usr/local/src/nanoWizard
    if [ ! $? -eq 0 ]; then
        echo "Failed to create required directory '$directory'  "
        exit 1
    fi
fi

if [ ! -f "$installed" ]; then 

    sudo cp ./runNanoWizard.py "$src_directory"
    sudo cp ./nanoWizard.py "$src_directory"
    sudo cp ./utility.py "$src_directory"
    sudo cp ./installed "$src_directory"
fi

# check for bin 
if [ ! -f "$bin_directory"/nanoWizard ]; then 
    sudo cp ./nanoWizard "$bin_directory"
fi


if [ $? -eq 0 ]; then 
    source ~/.bashrc
    if [ $? -eq 0 ]; then 
        echo "Sucessfully installed nanoWizard in '$bin_directory' "
        exit 0
    else
         echo "Process failed. Exiting ...."
        exit 1
    fi 
else
    echo "Process failed. Exiting ...."
    exit 1
fi 

