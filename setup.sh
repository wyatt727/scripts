#!/usr/bin/sh
# using xargs to exclude .zshrc file (ls doesn't show hidden files) 
sudo ls |xargs cp /usr/local/bin/. 2>/dev/null 
sudo chmod +x /usr/local/bin/*
sudo cp -r .cmedb /root/.cmedb
sudo cp -r .cmedb /root/cmedb
# Install oh-my-zsh with curl
sudo rm -rf /root/.oh-my-zsh 2>/dev/null
sudo sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
sudo cp .zshrc /root/.zshrc
sudo su
whoami
pwd
