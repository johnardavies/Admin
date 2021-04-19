## Docker commands 

<ins>###Building running and stopping a container</ins>

**Build container image**\
`$ docker build --tag container_name Folder_the_dockerfile_is_in`

**Run the container**  (A -d flag runs the container in the background). The p flag maps the container port to a local port on the computer\
`$ docker run container_id (or container_name) -p localport:containerport`

**Log into a running container** the -i flag is to indicate we want to log into the container -t creates a text terminal\
`$ docker exec -it container_id (or container_name) /bin/bash`

**Log back into a container that has been exited with the previous contents still there** (the -a flag is to attach to the container)\
`$ docker start -ia container_id (or container_name)`

**Docker stop a running container**\
`$ docker stop container_id (or container_name)`

###<ins>Docker clean up</ins> 

**Remove containers that are not running**\
`$ docker rm $(docker ps -a -q)`

**Remove untagged images** the image id is the 3rd field so $3 and then pipes to bash to run the docker remove images (docker rmi) command\
`$ docker images | grep "<none>" | awk '{ print "docker rmi " $3 }' | bash  `

###<u>Docker saving and getting data off and on the container</u>

**Saving the container**\
`$ docker commit container_id  docker_user_name/name_of_saved_image:version_no`\
`$ docker save container_name > container_name.tar. # Save to a tar file`

**Exporting data from the container**\
`$ docker cp container_id:/file/path/within/container /host/path/target`

**Sending data to the container in this case from the pwd  that is being sent to the folder with filepath :/src/direct in the container**\
`$ docker run -p local_port:container_port -v  "$(pwd)":/src/direct  docker_user_name/container_name`

###<ins>Docker-compose getting the latest version of a container</ins>

**Pulls the latest version and then restarts The -d flag means the process runs in the background**\
`$ docker-compose pull && docker-compose up -d`
