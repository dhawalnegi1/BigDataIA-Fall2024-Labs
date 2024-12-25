<!--StartFragment-->


### **Part 1: Introduction to Docker and Containerization**

#### **What is Docker?**

Docker is a platform designed to help developers build, share, and run applications in containers. Containers are lightweight, isolated environments that package up your code, runtime, system tools, libraries, and configurations into a single bundle. This makes it easier to ensure that an application runs the same way in different environments.

Installing Docker Desktop\
[Get Docker Desktop | Docker Docs](https://docs.docker.com/get-started/introduction/get-docker-desktop/)


#### **Core Docker Concepts:**

- **Docker Image:** A read-only template with the application’s environment, dependencies, and configurations. It's used to create Docker containers.

- **Docker Container:** A running instance of a Docker image. It behaves like a lightweight virtual machine.

- **Dockerfile:** A script that contains a series of instructions to build a Docker image.


#### **Differences Between Pre-configured and Base Images:**

- **Pre-configured Images (e.g.,** `nginx`**,** `redis`**)**: These images are ready to use out of the box, running specific software as soon as the container starts.

- **Base Images (e.g.,** `python`**,** `streamlit`**)**: These provide the environment (like Python or Streamlit) but require you to specify the code or app to run.

***


### **Part 2: Creating the Dockerfile with Poetry**

Docker\Dockerfile



### **Explanation of the Dockerfile Commands**

1. `FROM python:3.9-slim`:

   - This specifies the base image. We are using a lightweight Python 3.9 image (`slim`), which reduces the image size.

2. `WORKDIR /app`:

   - This sets the working directory inside the Docker container to `/app`. All subsequent commands will run inside this directory.

3. `COPY project.toml poetry.lock /app/`

   - By copying the `pyproject.toml` and `poetry.lock` files before copying the application code, we take advantage of Docker's layer caching. This way, dependencies don’t need to be reinstalled unless the dependency files change.

4. `RUN pip install poetry \
       && poetry config virtualenvs.create false \
       && poetry install --no-dev`

- `What it does: Configures Poetry to not create a virtual environment when installing dependencies.`

- `Purpose: By default, Poetry creates a virtual environment to isolate dependencies. However, inside a Docker container, creating a virtual environment is usually unnecessary because the container itself acts as an isolated environment. Setting virtualenvs.create false disables virtual environment creation.`

- `Outcome: Dependencies will be installed directly in the container's global environment, rather than inside a virtual environment.`

- `This command installs all production dependencies (those under [tool.poetry.dependencies] in pyproject.toml) without installing development tools, which minimizes the container's size and security surface.`

5. `COPY . .`:

   - This copies all files and directories from the current working directory on your machine into the `/app` directory inside the Docker container. This includes your `streamlit_app.py` and any other project files.

6. `EXPOSE 8501`:

   - This informs Docker that the container will be listening on port **8501** (the default port for Streamlit). This doesn’t actually map the port; the `docker run` command will handle that.

7. `CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]`:

   - This is the command that runs when the container starts. It runs the Streamlit application and binds it to port **8501**, allowing access from outside the container (`0.0.0.0` binds it to all network interfaces).


### **Part 3: Building the Docker Image**

Now that you have the Dockerfile with Poetry, build the Docker image.


2. Build the Docker Image:In the same directory as the `Dockerfile`, run the following command to build your image:\
    \
   `docker build -t streamlit-app-poetry .`

**Explanation:**

- This command builds the Docker image, using Poetry to install the dependencies specified in `pyproject.toml`.


### **Part 4: Running the Docker Container**

Once the Docker image is built, you can run your container.


Run the Docker Container:Run the following command to start the container and expose the Streamlit app:\
 \
&#x20;\
`docker run -d -p 8501:8501 streamlit-app-poetry`

1. **Explanation:**

   - **-d**: Runs the container in detached mode (in the background).

   - **-p 8501:8501**: Maps port 8501 in the container to port 8501 on your local machine.

   - The app is now running, and you can access it in your browser at `http://localhost:8501`.


### **Part 5: Access the Streamlit Application**

**Once the container is running, open your browser and visit:**

`http://localhost:8501`

***

## `Steps to Push Your Docker Image to Docker Hub`

### `1. Create a Docker Hub Account (If You Haven't Already)`

- `Visit: Docker Hub`

- `Sign Up: Click on "Sign Up" and create a new account.`

- `Note: Remember your username; you'll need it for tagging your image.`


### `2. Log In to Docker Hub from the Command Line`

`Open your terminal in the WSL environment and log in:`
`docker login`

- `Enter your Docker Hub username and password when prompted.`

- `Successful Login: You'll see a message like Login Succeeded.`


### `1. Tag Your Docker Image`

`First, you need to tag your local Docker image so that it points to the repository you've created on Docker Hub.`

`docker tag streamlit-poetry-app YOUR_DOCKERHUB_USERNAME/YOUR_REPOSITORY_NAME:latest`

- `Replace YOUR_DOCKERHUB_USERNAME with your Docker Hub username.`

- `Replace YOUR_REPOSITORY_NAME with the name of the repository you created on Docker Hub.`


### `4. Push the Docker Image to Docker Hub`

`Now, push the tagged image to your Docker Hub repository:`

`docker push YOUR_DOCKERHUB_USERNAME/streamlit-poetry-app:latest`

- `Docker will upload your image layers to Docker Hub.`


### `5. Verify the Image on Docker Hub`

- `Log In: Go to Docker Hub and log into your account.`

- `Navigate to Repositories: You should see streamlit-poetry-app listed under your repositories.`

- `Check Details: Click on the repository to see the pushed image and its tags.`


### `6. Pulling and Running the Image from Docker Hub`

#### `Pull the Image`

`On any machine with Docker installed, you can pull the image:`

`docker pull YOUR_DOCKERHUB_USERNAME/repo_name:latest`


#### `Run the Image`

`Run the Docker container:`

`docker run -p 8501:8501 YOUR_DOCKERHUB_USERNAME/repo_name:latest`

- `Access the App: Open a web browser and go to `[`http://localhost:8501`](http://localhost:8501)


<!--EndFragment-->
