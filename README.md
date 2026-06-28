# GitLab-CI-CD-Pipeline-with-Docker-AWS-ECR-OIDC-Authentication-EC2-Deployment

This project demonstrates a complete CI/CD deployment pipeline using GitLab, Docker and AWS.

The solution automatically:

- Builds a Docker image from source code
- Authenticates securely to AWS using OpenID Connect (OIDC)
- Pushes versioned images to Amazon Elastic Container Registry (ECR)
- Pulls images from ECR
- Deploys containers onto an EC2 host
- Validates application health after deployment

The project was built to gain hands-on experience with modern DevOps practices including containerisation, CI/CD pipelines, identity federation, AWS IAM, GitLab Runners, and deployment troubleshooting.

Key technologies:

- GitLab CI/CD
- GitLab Runner
- Docker
- Amazon EC2
- Amazon ECR
- AWS IAM
- OpenID Connect (OIDC)
- Python Flask

## Skills Demonstrated

✅ Docker Image Creation

✅ Container Deployment

✅ GitLab CI/CD Pipelines

✅ GitLab Runner Administration

✅ Docker Executor Configuration

✅ Amazon ECR

✅ AWS IAM

✅ OpenID Connect (OIDC)

✅ Linux Administration

✅ Pipeline Troubleshooting

✅ Production Deployment Patterns

✅ Infrastructure Debugging

✅ Security Best Practices

---

### Deployment Flow

```text
Developer
    │
    ▼
 GitLab Repository
    │
    ▼
 GitLab Pipeline
    │
    ▼
 GitLab Runner (EC2)
    │
    ├──────────────► AWS OIDC
    │                     │
    │                     ▼
    │               AWS STS
    │                     │
    ▼                     ▼
Docker Build      Temporary Credentials
    │                     │
    └──────────────► Amazon ECR
                           │
                           ▼
                    Docker Pull
                           │
                           ▼
                      EC2 Host
                           │
                           ▼
                    Flask Application
```

---

# Repository Structure

```text
.
├── app/
│   ├── app.py
│   └── requirements.txt
│
├── Dockerfile
├── .gitlab-ci.yml
└── README.md
```

---

# CI/CD Pipeline Stages

## Stage 1 - Build

The pipeline builds a Docker image from the application source code.

### Activities

* Clone repository
* Build Docker image
* Tag image using Git commit SHA

### Example

```bash
docker build -t image-name .
```

### Screenshot

<img width="1383" height="715" alt="Screenshot 2026-06-25 at 10 00 40" src="https://github.com/user-attachments/assets/40ef311d-a6ee-4c8a-8aaa-fa117d4aadf5" />


---

## Stage 2 - Push

The pipeline authenticates to AWS using OIDC and pushes the image to Amazon ECR.

### Activities

* Request GitLab OIDC token
* Assume AWS IAM Role
* Receive temporary credentials from AWS STS
* Authenticate to Amazon ECR
* Push Docker image

### Screenshot

<img width="1398" height="733" alt="Screenshot 2026-06-25 at 10 00 50" src="https://github.com/user-attachments/assets/5167f052-2e25-4ff0-8c9d-d2e6769923c8" />

---

## Stage 3 - Deploy

The deployment stage pulls the image from ECR and deploys it onto the EC2 host.

### Activities

* Remove existing container
* Pull latest image from ECR
* Create new container
* Start container
* Verify health endpoint

### Screenshot

<img width="1422" height="732" alt="Screenshot 2026-06-25 at 10 01 20" src="https://github.com/user-attachments/assets/73cc7ca4-229b-495c-8f05-5493bd0fd688" />


The CI/CD pipeline consists of three stages:

1. Build – Create Docker image
2. Push – Authenticate via OIDC and push image to ECR
3. Deploy – Pull image from ECR and deploy onto EC2

The pipeline completed successfully in approximately 50 seconds.

---

# Security Implementation

## OpenID Connect (OIDC)

This project uses OIDC authentication instead of long-lived AWS Access Keys.

### Benefits

* No AWS secrets stored in GitLab
* Temporary credentials only
* Reduced credential exposure risk
* Modern cloud security approach
* Production-aligned authentication model

### Authentication Flow

```text
GitLab Pipeline
       │
       ▼
OIDC Token
       │
       ▼
AWS STS
       │
       ▼
Temporary AWS Credentials
       │
       ▼
Amazon ECR
```

### Screenshot

<img width="747" height="342" alt="Screenshot 2026-06-25 at 10 04 38" src="https://github.com/user-attachments/assets/73d988dc-3d69-4afa-b2ce-7e4dd0e5b91f" />

### ECR Repository

The pipeline successfully pushed versioned Docker images into Amazon Elastic Container Registry (ECR).

<img width="1198" height="520" alt="Screenshot 2026-06-25 at 11 01 40" src="https://github.com/user-attachments/assets/1c72850c-ece4-47fc-8039-ef8bbc543292" />

---

# Engineering Challenges Solved

One of the most valuable parts of this project was troubleshooting real deployment issues.

| Problem                          | Root Cause                             | Resolution                   |
| -------------------------------- | -------------------------------------- | ---------------------------- |
| Docker permission denied         | User not in Docker group               | Added user to Docker group   |
| Runner offline                   | Registered in user mode                | Re-registered in system mode |
| Jobs stuck in pending            | Runner assigned to wrong project       | Recreated runner correctly   |
| Docker not found                 | Missing Docker CLI in Alpine container | Installed required packages  |
| Unable to locate credentials     | AWS authentication not configured      | Implemented OIDC             |
| Image unavailable between stages | Images not shared across jobs          | Introduced Amazon ECR        |

---

# Validation & Testing

## Docker Images

```bash
docker images
```

### Screenshot

<img width="656" height="47" alt="Screenshot 2026-06-25 at 10 06 58" src="https://github.com/user-attachments/assets/d5f6dedc-adae-47cc-8b67-db93fe29d731" />

---

## Running Containers

```bash
docker ps
```

### Screenshot

<img width="945" height="66" alt="Screenshot 2026-06-25 at 10 21 06" src="https://github.com/user-attachments/assets/192db276-d40c-4493-b89f-88de45463da3" />


---

## Application Health Check

```bash
curl http://localhost/health
```

Expected Output:

```text
OK
```

### Screenshot

<img width="445" height="42" alt="Screenshot 2026-06-25 at 10 08 24" src="https://github.com/user-attachments/assets/073a9334-8dae-426b-9d64-accd5243c44a" />

---

## Browser Validation

The application was successfully accessible through the EC2 public IP address. I cleared that acutal 

### Screenshot

<img width="1142" height="902" alt="Screenshot 2026-06-25 at 10 25 06" src="https://github.com/user-attachments/assets/591c23b1-a12e-42e6-8063-1dff5574f244" />

---

# Key DevOps Concepts Learned

This project helped me develop practical understanding of:

* Docker CLI vs Docker Daemon
* Docker Images vs Containers
* Docker Build Context
* GitLab Runner Architecture
* Docker Executors
* Shell Executor vs Docker Executor
* Amazon ECR Workflows
* AWS IAM Trust Policies
* OpenID Connect (OIDC)
* AWS STS Temporary Credentials
* CI/CD Pipeline Design
* Deployment Automation
* Infrastructure Troubleshooting

---

# Future Enhancements

Potential future improvements include:

* Terraform provisioning of AWS infrastructure
* Terraform provisioning of OIDC provider and IAM roles
* ECS Fargate deployment
* Blue/Green deployments
* Automated rollback strategy
* Vulnerability scanning
* CloudWatch monitoring and alerting
* Application Load Balancer integration
* Auto Scaling
* Multi-environment deployments (Dev/Test/Prod)
