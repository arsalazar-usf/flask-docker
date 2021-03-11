### Docker Assignment

This exercise will get you hands-on with Docker so that you can see what it takes to deploy a web application. On windows, you will run the commands in WSL.

In Mac/Linux, you will run these in the terminal.

##### Fork git repo
Fork this repo to your GitHub account

##### Clone web service
- From your forked repo, get the git url
- In terminal/WSL, run `git clone <your git url>`
- Change directory to the cloned repo: `cd <flask-docker>`

##### Create Dockerfile
- Create and edit Dockerfile: With wsl, you'll have to do this from the terminal. You can run `vim Dockerfile`.
- Add each of these instructions to the Dockerfile to do the following:
- Pull python:3.7-alpine as base image: `FROM python:3.7-alpine`
- Set `/app` as the working directory: `WORKDIR /app`
- Copy python requirements file into image: `COPY requirements.txt requirements.txt`
- Install python dependencies: `RUN pip install -r requirements.txt`
- Expose port 5000 to the host: `EXPOSE 5000`
- Copy contents of current directory to /app: `COPY . /app`
- Run python app.py at start of container: `CMD ["python", "app.py"]`

##### Build Docker Image
- `docker build -t cs486-flask .`
- `docker images`
- You should now see an image tagged cs486-flask:latest

##### Run Docker Container
- In your terminal, run the docker container: `docker run -p 5000:5000 cs486-flask`
- Notice that you can't input anything into your terminal while the container is running
- Verify that it is running by going to your web browser and navigating to localhost:5000
- In your terminal, press ctrl+c to kill the process running your container
- `docker run -p 5000:5000 -d cs486-flask`
- You'll see that the container is now running as a daemon, freeing up your ability to interact with the terminal.
- Run `docker ps` to see the running container
- Notice that it generates a UUID for the container ID and a unique name, both used for Docker to identify the container
- Ensure that the port 5000 is forwarding to 5000
- Go to your browser and navigate to localhost:5000
- To stop the container, locate the id or name of the container under docker ps
- Run `docker stop <container id or name>`
- Now you can see that the container still exists but is stopped: `docker ps -a`
- To remove a container, you can run docker rm <name or id of stopped container>
- If you want to stop and remove a container that's still running, you can run `docker rm -f <name or id of container>`
- Start the container back up with the development environment variable to allow Flask to update it: `docker run -d -p 5000:5000 -v $(pwd):/app -e FLASK_ENV=development cs486-flask`
- Check that localhost:5000 show the current Hello World message
- Change the message returned by `hello()` in app.py
- Go to browser and navigate to localhost:5000
- Verify that your new message is shown

##### Assignment Submission
Commit and push the following:
- Dockerfile
- Your changes to app.py
- Screenshot of your browser showing the new message to your forked repo

Submit a link to your repo to Canvas.
