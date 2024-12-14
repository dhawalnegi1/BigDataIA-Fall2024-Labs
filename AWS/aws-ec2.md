390844750194
VPC->
    Logically isolated network to launch your resources
    Provides control over networking env, IP addresses, subnets, route tables and network gateways

EC2->
    web service that provide secure, resizable compute capacity in cloud
    renting computer virtually to run your application

Launching EC2-> 
    https://console.aws.amazon.com/ -> Navigate to EC2 -> Launch Instance
    Name and Tag
    Amazon Linux 2023 AMI
    key-pair (download pem file)
    Network settings->
        select vpc, subnet(public)
        auto-assign public ip
        create security group->
            ssh - tcp - 22 - anywhere(ideally should be local ip)
            http - tcp - 80 - anywhere(app has to be publically accsible)
            add more if you plan to host multiple apps
        storage - default
        advanced setting - deafault
        launch instance
    
Configuring VPC instance->
    Go to EC2 -> Subnet
    Check route table for that subnet (ROute table should have entry to Internet Gateway)
    directs internet traffic (0.0.0.0/0) to an Internet Gateway (igw-xxxxxxxx).
    if required->
        destination - 0.0.0.0/0
        Target - Internet Gateway
    
Connecting via SSH
    copy pem file to wsl 
    chmod 400 /path/to/your-key-pair.pem -> change pem file permission
    ssh -i /path/to/your-key-pair.pem ec2-user@<public-ip-address>
    ssh -i demo-lab-kp.pem ec2-user@3.226.249.147          

Installing docker in ec2
    sudo yum install -y
    sudo yum install docker -y
    sudo service docker start
    sudo usermod -a -G docker ec2-user
    exit
    ssh -i demo-lab-kp.pem ec2-user@3.226.249.147
    docker info
    dcker pull disfiiguredsoul/fastapi-app
    docker run -d --name fastapi-container -p 80:80 disfiiguredsoul/fastapi-app
    docker ps

Recap
    



