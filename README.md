# tensorflow-rodmap

## Installing tensorflow
```
TF_TYPE="cpu" # Change to "gpu" for GPU support
 OS="linux" # Change to "darwin" for Mac OS
 TARGET_DIRECTORY="/usr/local"
 curl -L \
   "https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-${TF_TYPE}-${OS}-x86_64-1.4.0.tar.gz" |
   sudo tar -C $TARGET_DIRECTORY -xz
```
