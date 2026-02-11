# Kali Linux latest with useful tools by tsumarios
FROM kalilinux/kali-rolling

WORKDIR /workspace

RUN apt-get -y update && DEBIAN_FRONTEND=noninteractive apt-get -y dist-upgrade && apt-get -y autoremove && apt-get clean
RUN apt-get -y install curl wget vim git net-tools whois netcat-traditional pciutils usbutils
RUN apt -y install python3-pip # golang nodejs npm
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install kali-tools-top10 exploitdb man-db dirb nikto wpscan uniscan lsof apktool dex2jar ltrace strace binwalk

RUN apt -y install tor proxychains
#COPY config/proxychains.conf /etc/proxychains.conf

#RUN apt -y install zsh
#RUN sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
#COPY config/.zshrc .

COPY files/io.podman.dhcp.service /usr/lib/systemd/system/io.podman.dhcp.service
COPY files/io.podman.dhcp.socket /usr/lib/systemd/system/io.podman.dhcp.socket
RUN systemctl --global enable /usr/lib/systemd/system/io.podman.dhcp.socket

ENTRYPOINT ["/bin/bash"]
