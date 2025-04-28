# Cloud-Based ETL Pipeline Project

## Project Description
This project focuses on building a scalable, cloud-based ETL (Extract, Transform, Load) pipeline. The pipeline extracts data from an S3 bucket, transforms it using AWS Glue (with PySpark scripts), and loads it into a Snowflake database. The infrastructure components are managed and deployed using Terraform, ensuring reproducibility and infrastructure as code (IaC) best practices.

The goal is to simulate a real-world cloud ETL workflow that a Data Engineer would design, deploy, and automate in a professional environment.

---

## Tools and Technologies Used
- **AWS S3**: Data storage
- **AWS Glue**: Data transformation (Crawler and ETL Jobs using PySpark)
- **Snowflake**: Cloud data warehouse for loading the final data
- **Terraform**: Infrastructure as Code (IaC) to manage AWS resources
- **Python**: Used to initially upload the data to S3
- **Git & GitHub**: Version control and project sharing

---

## Project Workflow
1. **Upload raw data** to AWS S3 using a Python script.
2. **Create AWS Glue Crawler** to catalog and infer the schema from the S3 data.
3. **Create AWS Glue ETL Job** using PySpark to clean and transform the data.
4. **Load the transformed data** into Snowflake database.
5. **Use Terraform** to automate the creation of AWS resources (S3 bucket, IAM roles, Glue components).
6. **Version control** all infrastructure and code using Git and GitHub.

---

## Why This Project Matters
This project shows the ability to:
- Work with real cloud services (AWS, Snowflake).
- Automate cloud resources deployment (Terraform).
- Build and orchestrate ETL pipelines (AWS Glue).
- Manage and document projects using GitHub.

---
