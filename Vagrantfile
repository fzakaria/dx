# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.provision :ansible, :playbook => 'playbook.yml'

  # This configuration is for our local box, when we use virtualbox as the provider
  config.vm.provider :virtualbox do |vb, override|
    override.vm.box = "precise64"
    override.vm.box_url = "http://files.vagrantup.com/precise64.box"
  end

  # This configuration is for our EC2 instance
  config.vm.provider :aws do |aws, override|
    aws.access_key_id = ENV['AWS_ACCESS_KEY_ID']
    aws.secret_access_key = ENV['AWS_SECRET_ACCESS_KEY']
    # amazon linux AMI
    aws.ami = "ami-8786c6b7"
    aws.keypair_name = "vagrant"
    aws.security_groups = ["sg-886771ea"]
    aws.region = "us-west-2"
    aws.subnet_id = ENV['AWS_SUBNET_ID']
    aws.instance_type = "t2.medium"
    aws.associate_public_ip = true
    override.vm.box = "dummy"
    override.vm.box_url = "https://github.com/mitchellh/vagrant-aws/raw/master/dummy.box"
    override.ssh.username = "ec2-user"
    override.ssh.private_key_path = ENV['AWS_SSH_KEY_PATH']
    aws.tags = {
      'Name' => 'Vagrant-Dx'
    }
    #For RHEL5 machines, running sudoers commands require a tty. This is a workaround!
    config.ssh.pty = true
  end
end
