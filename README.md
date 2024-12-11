## Fibonacci API

[![Build and Test Pipeline](https://github.com/jaysotu5/fibonacci-api/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/jaysotu5/fibonacci-api/actions/workflows/ci-cd.yml)

This is a simple API built using Flask that computes the Fibonacci sequence for a given number. The API uses Gunicorn as the production-ready server and includes test cases to ensure functionality.

This README provides an explanation of the project structure, how to run it, and how to test it.

### Features
- Calculate Fibonacci sequence for a given number `n`.
- REST API endpoints to request the Fibonacci sequence.
- Built with Flask and Gunicorn for production readiness.
- Docker support for easy deployment.
- Unit tests for the API.

### API Endpoints

#### `GET /fibonacci/<n>`
Returns the Fibonacci number for the given integer `n`.

**Response:**
```json
{
  "fibonacci(5)": 5
}
```

### Project Structure

```bash
fibonacci-api/
├── src/
│   ├── __init__.py
│   ├── app.py
│   └── fibonacci_blueprint.py
├── tests/
│   ├── __init__.py
│   ├── test.py
├── Dockerfile
├── gunicorn_config.py
├── requirements.txt
├── run.py
└── README.md
```

Explanation of the Project Structure

* [`src/`](./src/): Contains the Flask application code.
  * [`__init__.py`](./src/__init__.py): Organizing your Flask project into packages
   * [`app.py`](./src/app.py): Contains the route definitions for the API, including the /fibonacci endpoint.
   * [`fibonacci_blueprint.py`](./src/fibonacci_blueprint.py): Defines and registers the api_blueprint to calculate the fibonacci number
* [`test/`](./test/): Contains unit tests for the application.
   * [`test.py`](./test/test.py): Includes tests for the API's (e.g., /fibonacci endpoint).
* [`Dockerfile`](./Dockerfile): Defines the steps to containerize the application using Docker.
* [`gunicorn_config.py`](./gunicorn_config.py): Contains the configuration for the Gunicorn WSGI server.
* [`requirements.txt`](./requirements.txt): Lists the Python dependencies for the project.
* [`run.py`](./run.py): Initializes and runs the Flask app with Gunicorn.
* [`README.md`](./README.md): This file, which provides an overview and instructions.

### Prerequisites
Before running the app, ensure that you have the following installed:

* Python 3.x
* pip (Python package installer)
* Docker (optional, for containerized setup)
------------------------------------------------------------------
### Steps to Run Locally
1. Clone the Repository

```bash
git clone https://github.com/yourusername/fibonacci-api.git
cd fibonacci-api
```

2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
```
3. Install Dependencies - [Requirements.txt](./requirements.txt)

```bash
pip install -r requirements.txt
```

> The Gunicorn configuration file ([gunicorn_config.py](./gunicorn_config.py)) sets some options for running the application

4. Run the Flask Application with Gunicorn

```bash
gunicorn -c gunicorn_config.py run:app
```
**This will run the API on http://127.0.0.1:5000**

5. Test the Fibonacci API

You can test the API by navigating to http://127.0.0.1:5000/fibonacci/5 in your browser or using a tool like curl:

```bash
curl http://127.0.0.1:5000/fibonacci/5
```
**Response**
```json
{
  "fibonacci(5)": 5
}
```

6. Run Unit Test
```bash
pytest ./test/test.py
```
-----------------------------------------------
### Docker Setup
If you prefer to run the application in a containerized environment, use Docker. The following steps will help you build and run the application with Docker.

1. Build the Docker Image - [Dockerfile](./Dockerfile)

```bash
docker build -t api:latest .
```

2. Run the Docker Container

```bash
docker run -d --name rest-api -p 5000:5000 api:latest
```
**This will run the API on http://127.0.0.1:5000**

--------------------------------------------------

### Operational Considerations
This section includes on how this service could be deployed and run in a production environment.

#### Deploying and Running in a Production Environment

1. Containerization
In a production environment, containerization with Docker ensures that your Flask application runs consistently across different environments. Docker allows you to encapsulate the app, its dependencies, and its configurations within a container.

* `Docker Image`: The Dockerfile provided ensures the app and all its dependencies are packaged into an image that can be run anywhere, whether in development, staging, or production environments.
* `Deployment on Cloud Provider`: Once you build your Docker image, you can push it to a container registry like Amazon ECR and deploy it to AWS. You can use services like AWS EKS or ECS Service to manage deployment.

2. Continuous Integration/Continuous Deployment (CI/CD)
To automate testing and deployment of your app, you can set up CI/CD pipelines using platforms like GitHub Actions, GitLab CI/CD, or Jenkins.
* **Example CI/CD Pipeline**:
  * `Code push`: Developers push changes to a Git repository (GitHub/GitLab/Bitbucket).
  * `CI Build`: A CI tool (like GitHub Actions or Jenkins) runs unit tests using pytest on each push or pull request.
  * `Docker Build & Push`: After the tests pass, a Docker image is built and pushed to a container registry AWS ECR.
  * `CD Pipeline`: The containerized application is deployed to production using Kubernetes or directly to AWS ECS.

```yaml
name: CI/CD Pipeline

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'
      - name: Install dependencies
        run: |
          python -m venv venv
          source venv/bin/activate
          pip install -r requirements.txt
      - name: Run tests
        run: |
          source venv/bin/activate
          pytest ./test/test.py
      - name: Build Docker image
        run: |
          docker build -t fibonacci-api .
      - name: Push Docker image
        run: |
          docker tag fibonacci-api yourdockerhubusername/fibonacci-api:latest
          docker push yourdockerhubusername/fibonacci-api:latest

```

3. Monitoring and Logging
To ensure the application runs smoothly in production, you can integrate monitoring and logging services.

`Logging`: 
* Log Aggregation: Use tools like Fluentbit to aggregate and visualize logs.
* Log Levels: Configure appropriate log levels (INFO, ERROR, DEBUG) in your app, and ensure logs are detailed enough to diagnose issues.
* Cloud Logging Services: If using a cloud provider, you can take advantage of their logging services, like AWS CloudWatch Logs to collect and store logs.

`Monitoring`:
* Prometheus/Grafana: Use Prometheus to collect metrics (e.g., response times, request counts) and visualize them with Grafana.
* AWS CloudWatch: Use cloud-native monitoring tools to track application metrics and set up alerts for anomalies.

4. Scaling the Service

As your application grows and needs to handle more traffic, you can scale it in several ways. Below, we discuss Horizontal Pod Autoscaler (HPA) and Load Balancer, which are critical components of scaling in Kubernetes and cloud environments.

`Horizontal Pod Autoscaler (HPA)`
* The Horizontal Pod Autoscaler (HPA) is a Kubernetes resource that automatically scales the number of pods in a deployment or replica set based on observed CPU utilization or other custom metrics. This enables the application to handle varying traffic loads efficiently.
* How it works: HPA monitors the resource usage (e.g., CPU or memory) of the pods in a deployment and automatically adjusts the number of pods up or down based on predefined thresholds.
Example: If the CPU utilization of your app exceeds a certain threshold (e.g., 80%), HPA will automatically scale the number of pods to handle the increased load. Similarly, when the traffic drops, it will scale down to reduce resource consumption.

**Example**
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: flask-api-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: flask-api
  minReplicas: 2   # Minimum number of pods
  maxReplicas: 10  # Maximum number of pods
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 80  # Scale up if CPU utilization exceeds 80%
```
` Loadbalancer` 
In a production environment, a Load Balancer is often used to distribute incoming traffic across multiple instances (pods) of your application. It helps to ensure that traffic is evenly distributed, preventing any single pod from becoming overwhelmed and improving the availability and fault tolerance of the application.

* Role of Load Balancer
  * `Traffic Distribution`: The Load Balancer ensures that incoming requests are distributed evenly across all available pods, preventing a single pod from becoming a bottleneck.
  * `High Availability`: If one pod or instance fails, the Load Balancer can route traffic to healthy pods, ensuring continuous availability of the service.
  * `Horizontal Scaling`: As the number of pods increases (via HPA), the Load Balancer can automatically start routing traffic to the new pods.




