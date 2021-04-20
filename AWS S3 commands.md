## Commands to access s3 buckets using aws cli 

**Make a bucket**

`$ aws s3 mb s3://bucket-name`

**List files in a bucket**

`$ aws s3 ls bucket-name`

**Copy file on home computer to s3 bucket**

`$ aws s3 cp 'filepath to file A1 on home computer to s3' s3://bucket_name`

**If the copy item is not a file, but a folder add --recursive to copy all the files in a folder**

`$ aws s3 cp --recursive 'Folder filepath'  s3://bucket-name//destination-folder`

**Copies all the files in a bucket to the present working directory**

`$ aws s3 cp s3://bucket-name ./ --recursive`

**Delete the file A1 in the bucket**

`$ aws s3 rm s3://bucket-name/A1`

**sync Uploads all the files in a folder that are new or modified to an s3 bucket**

`$ aws s3 sync . s3://bucket-name`

**Moves files (in this case jpegs) to a folder 'summer_holiday' inside a bucket called photos**

`$ aws s3 mv s3://photos/   s3://photos/summer_holiday --recursive --exclude "*" --include "*.jpg"`
 

