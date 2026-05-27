Instructions for using the containerized app

1- create a project folder
2- clone the project into it
2- Within the project folder create a results folder to store the .csv results with the calculated indicators.
3- set permisions on the results folfer to 777 so both the user and the container app can read and write files in it.
4- take the .env_temlpate file, fill it with the required conection databases information and save it as .env file.
5- pull the eurocardiab:latest container image from docker-hub by ..... or create yourself the container by using the comand: [docker build -t eurocardiab:latest]
6- run the container with the following command: [docker run -v '/full/route/to/results-folder':/app/results --env-file .env eurocardiab:latest] or if your OMOP database (postgres) is runing as a container: [docker run -v '/full-route-to/results-folder':/app/results --env-file .env --network 'omop_container_network' eurocardiab:latest]