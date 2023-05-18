# rpi-dht11-api-docker

Collect data from DHT11 sensors via docker container

## :rocket: Technologies

Main technologies used in the Docker image

- [Python3](https://www.python.org/downloads/source)
- [Flask](https://www.python.org/downloads/source)
- [RPi.GPIO](https://pypi.org/project/RPi.GPIO)
- [DHT11](https://pypi.org/project/dht11)
- [Docker](https://docs.docker.com/engine/install/ubuntu)
- [Docker Compose](https://docs.docker.com/compose/install/linux)

Main technologies used in Raspberry Pi 3/4
- Raspberry Pi OS (64 bit)
- Docker

Hint with commands to install

```
sudo apt update
sudo apt upgrade
sudo apt install raspberrypi-kernel raspberrypi-kernel-headers
curl -sSL https://get.docker.com | sh
sudo usermod -aG docker <device-user>
sudo reboot
```

## How to Connect DHT11 on Raspberry Pi 3/4

To use this image on the Raspberry Pi 3/4 assemble your electronic circuit as shown below

![Raspberry pi with dht11](https://github.com/eltonlazzarin/rpi-dht11-api-docker/blob/update-readme-with-electronic-schematic/docs/dht11.jpeg)

## :information_source: How to clone this repository on your Raspberry Pi

```bash
git clone https://github.com/eltonlazzarin/rpi-dht11-api-docker.git
```

## :information_source: How to build the Docker image

To build run:

```
cd rpi-dht11-api-docker && docker image build --tag elazzar/rpi-dht11-api-docker -f Dockerfile . 
```

## :information_source: How to run the Docker container

To run the container:

```
docker compose up -d 
```

## :information_source: How to view sensor data in your browser

#### Access the endpoint below to view data from temperature and humidity sensors

```
http://<your-device-ip>:5000
```

#### Access the endpoint below to see only temperature sensor data

```
http://<your-device-ip>:5000/temperature
```

#### Access the endpoint below to see only the humidity sensor data

```
http://<your-device-ip>:5000/humidity
```

The docker image can be found [here](https://hub.docker.com/r/elazzar/rpi-dht11-api-docker).

## :memo: License

This project is under the MIT license.

Made with ♥ by Elton Lazzarin :wave: [Get in touch!](https://www.linkedin.com/in/eltonlazzarin/)
