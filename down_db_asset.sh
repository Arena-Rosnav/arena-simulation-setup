#!/bin/bash

# Check if gdown is installed
if ! command -v gdown &> /dev/null
then
    echo "gdown could not be found, installing now..."
    pip install gdown
fi

# Download the file using gdown
echo "Downloading file from Google Drive..."
gdown https://drive.google.com/drive/u/1/folders/154WwCZ7o7PytpcrFcsndX25gezJ4otx5 -O ./arena_models --folder
unzip './arena_models/*.zip' -d './arena_models'
rm ./arena_models/*.zip

echo "Download completed!"

# Extracting Asset bundles
echo "Replacing Asset bundles in ../arena-unity/Assets/StreamingAssets/StandaloneLinux64"
rm --recursive --force ../arena-unity/Assets/StreamingAssets/StandaloneLinux64/
tar -xzf ./arena_models/StandaloneLinux64.tar.gz -C ../arena-unity/Assets/StreamingAssets/
rm ./arena_models/StandaloneLinux64.tar.gz

echo "Done!"
