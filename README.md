# weather-station

In order to run django server it is preffered to use either docker image or virtual environment.

Docker image:
1. Execute the following docker command to create local image based on a DockerFile: docker build -t weather-station .
2. Execute the docker command to run previously created docker image: docker run -it --rm -p 8000:8000 weather-station
3. Open your brower and paste the following line: http://127.0.0.1:8000/ 

Virtual environment using pipenv module:
1. Execute pipenv command to create a virtual environment: python -m pipenv install
2. Switch to virtual environment using: python -m pipenv shell 
3. Run the server using the following command: python manage.py runserver
4. Open your brower and paste the following line: http://127.0.0.1:8000/ 