# container

## network

* replace your eth care in there

```sh
podman network create --subnet 10.89.0.0/24 --gateway 10.89.0.1 franklin_custom_network # create a bridge
podman network ls
sudo podman network create --driver macvlan --opt parent="enp9s0" research
```

## build container

```sh
sudo sysctl -w net.ipv6.conf.all.forwarding=1 # Use when you have IPv6 network issues
export CR_PAT=$(pass show ghcr)
echo $CR_PAT | docker login ghcr.io -u devsecfranklin --password-stdin
podman build -t devsecfranklin/buckwheats .
podman image ls 
```

## run container

* ` podman run -it localhost/devsecfranklin/buckwheats:latest`
* [How to install and use Podman Desktop on Windows](https://developers.redhat.com/articles/2023/09/27/how-install-and-use-podman-desktop-windows)

## Kali

```sh
docker pull kalilinux/kali-rolling
docker images -a # You should see a list of Docker images in the output, specifically our Kali image
docker run -t -i kalilinux/kali-rolling /bin/bash # create a Docker container using the kalilinux/kali-rolling image we just downloaded
Copycopy code to clipboard
cat /etc/os-release # verify after prompt changed
```