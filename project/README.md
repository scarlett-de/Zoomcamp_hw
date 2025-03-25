# 






# Steps of running the project

# Set up GCP by usting Terraform

## set up service account and bucket
[DE Zoomcamp 1.3.1 - Terraform Primer](https://www.youtube.com/watch?v=s2bOYDCKl_M&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=12)


<img src="https://github.com/user-attachments/assets/a61ff11a-6312-4d6d-9afa-1e45ad3c0f64" alt="image" width="500">

**Terraform** is an infrastructure code tool that lets you define noth could and on-prem resources in human-readable configuration files that you can version, reuse and share.  

**Provider**: Code that allows terraform to communicate resources on AWS/Azure/GCP etc. 

https://registry.terraform.io/browse/providers  

**Key Terraform commands**:

**which terraform**: check version.
**terraform fmt**: format tf file.
**terraform init**: initializes & configures the backend installs plugins/providers, & checks out an existing configuration from a version control.
**terraform plan**: matches/previews local changes against a remote state, and proposes an Execution Plan.
**terraform apply**:asks for approval to the proposed plan, and applies changes to cloud.
**terraform destroy**: removes your stack from the Cloud.
**terraform validate** (optional): returns a success message if the configuration is valid and no errors are apparent.




## DE Zoomcamp 1.3.2 - Terraform Basics
[DE Zoomcamp 1.3.2 - Terraform Basics](https://www.youtube.com/watch?v=Y2ux7gq3Z0o&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=13)


**Create servcice accounts**
<img src="https://github.com/user-attachments/assets/4b27bf55-5104-48ef-8a59-7455e02e3831" alt="image" width="500">
<img src="https://github.com/user-attachments/assets/a61ff11a-6312-4d6d-9afa-1e45ad3c0f64" alt="image" width="500">

Cloud storage -> Sotrage Admin
BigQuery -> BigQuery Admin
Compute Engine -> Compute Admin

**Manage Keys
<img src="https://github.com/user-attachments/assets/438e8cae-fed9-4652-ab5b-b1574a57d52c" alt="image" width="500">
<img src="https://github.com/user-attachments/assets/021d74c9-a255-46e8-9ad2-9cd9fcc3fb01" alt="image" width="500">

a json file with your keys will be downloaded, save it to a folder
