<!--StartFragment-->

Google Cloud Storage

Cloud Storage is a service for storing your [_objects_](https://cloud.google.com/storage/docs/objects) in Google Cloud. An object is an immutable piece of data consisting of a file of any format. You store objects in containers called [_buckets_](https://cloud.google.com/storage/docs/buckets).\
\
Buckets are associated with a [_project_](https://cloud.google.com/storage/docs/projects) and you can group your projects under an [_organization_](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations). 

Each project, bucket, managed folder, and object in Google Cloud is a _resource_ in Google Cloud, as are things such as [Compute Engine instances](https://cloud.google.com/compute/docs/instances).

Steps to Create Google Cloud Bucket

1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.\
   [Go to Buckets](https://console.cloud.google.com/storage/browser)

2. Click add\_box **Create**.

3. On the **Create a bucket** page, enter your bucket information. After each of the following steps, click **Continue** to proceed to the next step:

   1. In the **Get Started** section, do the following:

      - Enter a globally unique name that meets the bucket name requirements.

Bucket Naming Convention

Your bucket names must meet the following requirements:

4. Bucket names can only contain lowercase letters, numeric characters, dashes (`-`), underscores (`_`), and dots (`.`). Spaces are not allowed. Names containing dots require verification.

5. Bucket names must start and end with a number or letter.

6. Bucket names must contain 3-63 characters. Names containing dots can contain up to 222 characters, but each dot-separated component can be no longer than 63 characters.

7. Bucket names cannot be represented as an IP address in dotted-decimal notation (for example, 192.168.5.4).

8. Bucket names cannot begin with the "goog" prefix.

9. Bucket names cannot contain "google" or close misspellings, such as "g00gle".

- To enable [hierarchical namespace](https://cloud.google.com/storage/docs/hns-overview) ([preview](https://cloud.google.com/products#product-launch-stages)), click the expand\_moreexpander arrow to expand the **Optimize for file oriented and data-intensive workloads** section, and then select **Enable Hierarchical namespace on this bucket**.\
  **Note:** You cannot enable hierarchical namespace in an existing bucket.

- To add a [bucket label](https://cloud.google.com/storage/docs/tags-and-labels#bucket-labels), click the expand\_more expander arrow to expand the **Labels** section, click add\_box **Add label**, and specify a `key` and a `value` for your label.

2. In the **Choose where to store your data** section, do the following:

   - Select a [Location type](https://cloud.google.com/storage/docs/locations).

   - Use the location type's drop-down menu to select a [**Location**](https://cloud.google.com/storage/docs/locations#available-locations) where object data within your bucket will be permanently stored.

     - If you select the [dual-region](https://cloud.google.com/storage/docs/locations#location-dr) location type, you can also choose to enable [turbo replication](https://cloud.google.com/storage/docs/availability-durability#turbo-replication) by using the relevant checkbox.

3. In the **Choose a storage class for your data** section, either select a [default storage class](https://cloud.google.com/storage/docs/storage-classes) for the bucket, or select [Autoclass](https://cloud.google.com/storage/docs/autoclass) for automatic storage class management of your bucket's data.

Storage Class for Data


### **Standard storage**

Standard storage is best for data that is frequently accessed ("hot" data), as well as data that is stored for only brief periods of time.


### **Nearline storage**

Nearline storage is a low-cost, highly durable storage service for storing infrequently accessed data. Nearline storage is ideal for data you plan to read or modify on average once per month or less. Nearline storage is also appropriate for data backup, long-tail multimedia content, and data archiving.


### **Coldline storage**

Coldline storage is a very-low-cost, highly durable storage service for storing infrequently accessed data. Coldline storage is ideal for data you plan to read or modify at most once a quarter. 


### **Archive storage**

Archive storage is the lowest-cost, highly durable storage service for data archiving, online backup, and disaster recovery

4. In the **Choose how to control access to objects** section, select whether or not your bucket enforces [public access prevention](https://cloud.google.com/storage/docs/public-access-prevention), and select an [access control model](https://cloud.google.com/storage/docs/access-control) for your bucket's objects.\
   **Note:** If public access prevention is already enforced by your project's [organization policy](https://cloud.google.com/storage/docs/org-policy-constraints#public-access-prevention), the **Prevent public access** checkbox is locked.

5. In the **Choose how to protect object data** section, do the following:

   - Select any of the options under **Data protection** that you want to set for your bucket.

   - To choose how your object data will be encrypted, click the expand\_more expander arrow labeled **Data encryption**, and select a [**Data encryption** method](https://cloud.google.com/storage/docs/encryption).

10) Click **Create**.

[Steps to Install gcloud CLI](https://cloud.google.com/sdk/docs/install)

**Before you install the gcloud CLI, make sure that your operating system meets the following requirements:**

    sudo apt-get update

**It has** [`apt-transport-https`](https://packages.debian.org/bullseye/apt-transport-https) **and** `curl` **installed:**

    sudo apt-get install apt-transport-https ca-certificates gnupg curl

**Installation**

**Import the Google Cloud public key.\
For newer distributions (Debian 9+ or Ubuntu 18.04+) run the following command:**

    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg

**Add the gcloud CLI distribution URI as a package source.**

**For newer distributions (Debian 9+ or Ubuntu 18.04+), run the following command:**

    echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

**Update and install the gcloud CLI**

    sudo apt-get update && sudo apt-get install google-cloud-cli

To get started started with gcloud CLI


# **1. Authentication & Initialization**

#### **Initialize the Google Cloud SDK**

Set up your account and project:

    gcloud init OR gcloud init --console-only

to prevent the command from automatically opening a web browser.


#### **Login to Google Cloud**

Authenticate your Google Cloud account:

    gcloud auth login


#### **View Authentication Credentials**

To see the accounts you’re authenticated with:

    gcloud auth list


### **2. Project Management**

#### **List Available Projects**

    gcloud projects list


#### **Set Default Project**

To set a default project for future operations:

    gcloud config set project [PROJECT_ID]


#### **Create a New Project**

    gcloud projects create [PROJECT_ID]


### **3. Google Cloud Storage (GCS)**

#### **Create a Google Cloud Storage Bucket** `gcloud storage buckets create gs://[BUCKET_NAME] --location [LOCATION]`

#### <https://cloud.google.com/sdk/gcloud/reference/storage/buckets/create#FLAGS>

Example:

    gcloud storage buckets create gs://my-new-bucket --location us-central1


#### **List Buckets in a Project**

    gcloud storage buckets list


#### **Upload a File to a Bucket**

    gsutil cp [LOCAL_FILE_PATH] gs://[BUCKET_NAME]


#### **Download a File from a Bucke**`t`

    gsutil cp gs://[BUCKET_NAME]/[FILE_NAME] [LOCAL_DESTINATION]



References\
\
Creating Google Buckets using gcloud CLI

<https://cloud.google.com/storage/docs/creating-buckets#command-line>

<https://cloud.google.com/storage/docs/discover-object-storage-gcloud>

How to Setup Python env to use GCP programatically

<https://cloud.google.com/python/docs/setup#linux>

Python Programmatic Approach GCP Buckets

<https://cloud.google.com/appengine/docs/legacy/standard/python/googlecloudstorageclient/read-write-to-cloud-storage>



<!--EndFragment-->
