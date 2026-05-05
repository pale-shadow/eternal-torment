# Visualization

- [Terraform graph](https://developer.hashicorp.com/terraform/cli/commands/graph)

```sh
terraform graph -type=plan | dot -Tsvg -o graph.svg
terraform graph -type=plan | dot -Tpng -o graph.png
```

- neato
- [Terraform Visualizer](https://hieven.github.io/terraform-visual/)
- [go-dag](https://github.com/clarkmcc/go-dag)
- [Rover](https://github.com/im2nguyen/rover)

`docker run --rm -it -p 9000:9000 -v (pwd):/src im2nguyen/rover -standalone true`

## Gephi Debian

```sh
sudo apt install nvidia-openjdk-8-jre
LIBGL_ALWAYS_SOFTWARE=1 /home/franklin/Downloads/gephi-0.9.2/bin/gephi --jdkhome /usr/lib/jvm/java-8-openjdk-amd64
```

## Gephi Pop OS

```sh
sudo apt install openjdk-8-jdk
LIBGL_ALWAYS_SOFTWARE=1 /home/franklin/Downloads/gephi-0.9.2/bin/gephi --jdkhome /usr/lib/jvm/java-8-openjdk-amd64
```

## Gephi OpenBSD

- Add these packages

```sh
doas pkg_add maven jdk netbeans
```

- Clone the [Gephi repo on github](https://github.com/gephi/gephi)
- Open this clone directory in `netbeans`
