# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "bento/centos-7.3"
  config.vm.synced_folder ".", "/vagrant", type: "virtualbox"
  config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
  config.vm.network "forwarded_port", guest: 3000, host: 8888, host_ip: "127.0.0.1"

  config.ssh.insert_key = false

  # config.vm.provision "shell", path: "./provision/scripts/install_ansible.sh"

  config.vm.provision "shell", path: "provision/mount_node_modules.sh", run: "always"

  # Run Ansible from the Vagrant VM
  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "./provision/playbook.yml"
    ansible.verbose = true
  end
end
