# Docker Basic Commands

## 1. Check Docker Version
Description: Displays the installed Docker version.

```bash
docker --version
```

## 2. View Docker Information
Description: Displays detailed information about Docker Engine.

```bash
docker info
```

## 3. Download an Image
Description: Downloads an image from Docker Hub.

```bash
docker pull nginx
```

## 4. Search an Image
Description: Searches for images on Docker Hub.

```bash
docker search nginx
```

## 5. List Images
Description: Lists all Docker images available locally.

```bash
docker images
```

## 6. Build an Image
Description: Builds a Docker image from a Dockerfile.

```bash
docker build -t myapp:v1 .
```

## 7. Tag an Image
Description: Creates another tag for an existing image.

```bash
docker tag myapp:v1 myapp:latest
```

## 8. Push an Image
Description: Pushes an image to Docker Hub.

```bash
docker push username/myapp:v1
```

## 9. Remove an Image
Description: Removes a Docker image.

```bash
docker rmi nginx
```

## 10. Run a Container
Description: Creates and starts a container.

```bash
docker run nginx
```

## 11. Run a Container in Detached Mode
Description: Runs a container in the background.

```bash
docker run -d nginx
```

## 12. Run a Container with a Name
Description: Starts a container with a custom name.

```bash
docker run -d --name mynginx nginx
```

## 13. Run a Container with Port Mapping
Description: Maps a host port to a container port.

```bash
docker run -d -p 8080:80 nginx
```

## 14. Run a Container with Environment Variables
Description: Passes environment variables to the container.

```bash
docker run -e MYSQL_ROOT_PASSWORD=root mysql
```

## 15. List Running Containers
Description: Displays running containers.

```bash
docker ps
```

## 16. List All Containers
Description: Displays all containers.

```bash
docker ps -a
```

## 17. Start a Container
Description: Starts a stopped container.

```bash
docker start mynginx
```

## 18. Stop a Container
Description: Stops a running container.

```bash
docker stop mynginx
```

## 19. Restart a Container
Description: Restarts a container.

```bash
docker restart mynginx
```

## 20. Kill a Container
Description: Immediately terminates a running container.

```bash
docker kill mynginx
```

## 21. Remove a Container
Description: Removes a stopped container.

```bash
docker rm mynginx
```

## 22. Force Remove a Container
Description: Stops and removes a running container.

```bash
docker rm -f mynginx
```

## 23. Remove All Containers
Description: Removes all running and stopped containers.

```bash
docker rm -f $(docker ps -aq)
```

## 24. Stop All Running Containers
Description: Stops all running containers.

```bash
docker stop $(docker ps -q)
```

## 25. Kill All Running Containers
Description: Immediately terminates all running containers.

```bash
docker kill $(docker ps -q)
```

## 26. Remove All Exited Containers
Description: Removes all exited containers.

```bash
docker container prune -f
```

## 27. View Container Logs
Description: Displays container logs.

```bash
docker logs mynginx
```

## 28. Follow Container Logs
Description: Displays logs in real time.

```bash
docker logs -f mynginx
```

## 29. Execute Commands Inside a Container
Description: Opens an interactive shell inside a running container.

```bash
docker exec -it mynginx bash
```

If bash is unavailable:

```bash
docker exec -it mynginx sh
```

## 30. Inspect a Container or Image
Description: Displays detailed information in JSON format.

```bash
docker inspect mynginx
```

## 31. Monitor Resource Usage
Description: Displays CPU, memory, network, and disk usage of running containers.

```bash
docker stats
```

## 32. Display Running Processes
Description: Shows running processes inside a container.

```bash
docker top mynginx
```

## 33. Copy Files Between Host and Container
Description: Copies files between the host and a container.

Host to Container:

```bash
docker cp file.txt mynginx:/tmp/
```

Container to Host:

```bash
docker cp mynginx:/tmp/file.txt .
```

## 34. List Docker Networks
Description: Lists all Docker networks.

```bash
docker network ls
```

## 35. Create a Docker Network
Description: Creates a new Docker network.

```bash
docker network create mynetwork
```

## 36. Remove a Docker Network
Description: Removes a Docker network.

```bash
docker network rm mynetwork
```

## 37. List Docker Volumes
Description: Lists all Docker volumes.

```bash
docker volume ls
```

## 38. Create a Docker Volume
Description: Creates a Docker volume.

```bash
docker volume create myvolume
```

## 39. Remove a Docker Volume
Description: Removes a Docker volume.

```bash
docker volume rm myvolume
```

## 40. Display Docker Disk Usage
Description: Displays disk space used by Docker.

```bash
docker system df
```

## 41. Remove Unused Docker Resources
Description: Removes stopped containers, unused networks, dangling images, and build cache.

```bash
docker system prune
```

## 42. Remove All Unused Resources Including Images
Description: Removes all unused Docker resources, including unused images.

```bash
docker system prune -a
```

## 43. Save an Image
Description: Saves a Docker image to a tar archive.

```bash
docker save -o nginx.tar nginx
```

## 44. Load an Image
Description: Loads a Docker image from a tar archive.

```bash
docker load -i nginx.tar
```

## 45. Login to Docker Hub
Description: Authenticates with Docker Hub.

```bash
docker login
```

## 46. Logout from Docker Hub
Description: Logs out from Docker Hub.

```bash
docker logout
```

## 47. Display Docker Events
Description: Displays real-time Docker events.

```bash
docker events
```