tree -> 
    recursive directory listing program 
    produces a depth-indented listing of files. 
    useful tool for visualizing and documenting the directory structure of an application

installation->
    sudo apt-get install tree (Ubuntu)
    brew install tree (MacOS)

Basic Usages
    tree - directory tree of the current directory
    tree /path/to/directory - directory tree of a specific path
    tree -a - Hidden files
    tree > directory_structure.txt -  output to a text file
    tree --help - For more details on more option

AWS account setup->
    https://aws.amazon.com/console/
    Create an AWS Account
    email address, password, and AWS account name.
    contact information, "Personal" or "Company"
    payment information
    Basic Support Plan
    Wait for the account activation email

Setting Up a Budget
    Importance: 
        Setting up a budget helps prevent unexpected charges.
        Allows you to set custom budgets that alert you when your costs exceed or are forecasted to exceed your budgeted amount.
    select and Create a Budget
    Set up an alert for when actual or forecasted costs reach 80% and 100% of your budget.
    Provide your email address for notifications.
    Review and Complete

Set Up IAM Users and Roles
    Importance: For security best practices, avoid using root accounts for daily tasks.
    Log in to the AWS 
    Navigate to IAM
    Create new user
    Click on "Users" > "Add user".
    AWS Management Console access
    Set a custom password 
    Attach existing policies directly
    Attach AdministratorAccess
    Review and create the user
    Setup Access Key ID and Secret Access Key

Login to IAM user 

Setting Up Networking and VPC
    VPC: virtual network dedicated to your AWS account, logically isolated from other virtual networks in the AWS Cloud.
    Components:
        Subnets: Segments within your VPC to group resources.
        Route Tables: Rules that determine where network traffic is directed.
        Internet Gateways: Allows communication between your VPC and the internet.
        Security Groups: Virtual firewalls for your instances.

Creating an S3 Bucket
    Explanation: Amazon S3 is an object storage service used to store and retrieve any amount of data.
    Navigate to "S3 Dashboard".
    Click "Create bucket".
    Configure bucket settings:
        Provide a unique bucket name
        Choose a region
        Configure options
        Block all public access
    Review and create the bucket.

Accessing the S3 Bucket and Pushing Files Using Python
    Boto3: AWS SDK for Python to interact with AWS services programmatically.
    Install AWS CLI
        sudo apt-get install awscli -y (Ubuntu)
        brew install awscli (MacOS)
        aws --verion
        aws configure
    Install Boto3 using Poetry
        poetry add boto3
    Demo upload, list and download s3 files via boto3




