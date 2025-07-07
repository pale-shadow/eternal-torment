# container

## network

* replace your eth care in there

```sh
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

