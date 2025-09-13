# Container

## Podman Desktop

* [How to install and use Podman Desktop on Windows](https://developers.redhat.com/articles/2023/09/27/how-install-and-use-podman-desktop-windows)

## Kali

```sh
docker pull kalilinux/kali-rolling
docker images -a # You should see a list of Docker images in the output, specifically our Kali image
docker run -t -i kalilinux/kali-rolling /bin/bash # create a Docker container using the kalilinux/kali-rolling image we just downloaded
Copycopy code to clipboard
cat /etc/os-release # verify after prompt changed
```
