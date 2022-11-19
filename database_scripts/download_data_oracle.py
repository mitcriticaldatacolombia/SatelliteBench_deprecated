import io
import oci
import sys
import json
import os
import shutil
import skimage
from tifffile import imread, imwrite
import numpy as np

def get_objects(config, data_folder, verbose=False):
    # Resource Principal for connecting to Object Storage/Logs
    signer = oci.auth.signers.get_resource_principals_signer()
    client = oci.object_storage.ObjectStorageClient(config={}, signer=signer, timeout=(100, 100))

    # Get the list of objects
    objects = client.list_objects(namespace_name=config['os_namespace'],
                            bucket_name=config['os_bucket'])
    
    files = []
    for obj in objects.data.objects:
        if obj.name.startswith(data_folder):
            files.append(obj)
            
    if verbose:
        print('The files in folder are: ')
        print(files)
    
    print(f"The files in path {config['os_bucket']}/{data_folder} are: {len(files)}")
            
    return objects, client
def get_files(config, data_folder, data_out=None):
    
    objects, client = get_objects(config, data_folder, verbose=True)
    
    for obj in objects.data.objects:
        if not(obj.name.startswith(data_folder)):
            continue
            
        # Download file from Object Storage
        file = client.get_object(namespace_name=config['os_namespace'],
                                bucket_name=config['os_bucket'],
                                object_name=obj.name)

        # Image from OCI to bytes
        #image_bytes = io.BytesIO(image.data.content)

        """ 
        If "data_out"; take all files to data_out folder:
        Note: Use this option on archives that only contain files, not subdirectories
        """
        if data_out:
            # Create directory to store the data if not exist
            if not os.path.exists(data_out):
                os.makedirs(data_out)
            
            dir_name = obj.name.split('/')[0]
            filename = obj.name.split('/')[1]
            # Add the files in the 
            with open(os.path.join(data_out,filename), "wb", buffering=0) as f:
                f.write(file.data.content)

        #If not "data_out" save all the files exactly as they are in the bucket:
        else:
            try:
                with open(obj.name, "wb", buffering=0) as f:
                    f.write(file.data.content)
            # If is a directory; then just creates the directory
            except IsADirectoryError:
                os.makedirs(obj.name)
   
if __name__ == "__main__":
    # Object Storage Parameters (for building a connection)
    config = {
        'os_namespace' : '******',
        'os_bucket' : 'Sentinel_2_Images',
        'os_cmpt' : '******',
        'os_tenancy' : '******'    
    } 
    data_folder = 'Dataset_5_best_cities'

    get_files(config, data_folder)