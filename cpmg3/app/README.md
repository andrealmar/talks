# Microservices with Python and Flask

Clone the repo:
```
git clone https://github.com/andrealmar/tcc-microservices.git
```
Enter the directory:
```
cd tcc-microservices
```
If you are running for the 1st time you need to build the container:
```
docker-compose up --build
```
After that, the container will be up and running and you can start making microservice calls via browser or using curl:

```
ADD: http://localhost:5000/add?a=1&b=5 | Ex. 1 + 5 = 6
```
```
SUBTRACT: http://localhost:5000/subtract?a=1&b=5 | Ex. 1 - 5 = -4
```
```
MULTIPLY: http://localhost:5000/multiply?a=2&b=5 | Ex. 2 * 5 = 10
```
```
DIVIDE: http://localhost:5000/divide?a=10&b=2 | Ex. 10 / 2 = 5
```
