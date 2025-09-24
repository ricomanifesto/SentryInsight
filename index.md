# Exploitation Report

The current threat landscape reveals several critical exploitation campaigns targeting diverse infrastructure components. State-sponsored actors are actively exploiting vulnerabilities in email security gateways and enterprise software, while cybercriminals continue to leverage misconfigurations in cloud services and open-source utilities. Most concerning are the active exploitations of Pandoc utility for AWS credential theft, Libraesva Email Security Gateway by state actors, and the widespread abuse of misconfigured Docker containers for botnet operations. Federal agencies have also fallen victim to GeoServer exploits, highlighting the persistent threat to government infrastructure.

## Active Exploitation Details

### Pandoc Vulnerability Exploitation
- **Description**: A security flaw in the Linux utility Pandoc that enables attackers to infiltrate Amazon Web Services environments
- **Impact**: Attackers can target AWS Instance Metadata Service (IMDS) and steal EC2 IAM credentials, potentially leading to full cloud environment compromise
- **Status**: Currently being exploited in the wild by threat actors
- **CVE ID**: CVE-2025-51591

### Libraesva Email Security Gateway Vulnerability
- **Description**: A critical security flaw in Libraesva's Email Security Gateway (ESG) solution that allows unauthorized access
- **Impact**: State-sponsored threat actors can compromise email security infrastructure and potentially access sensitive communications
- **Status**: Actively exploited by state-sponsored hackers; emergency security update has been released
- **CVE ID**: Not specified in source materials

### GeoServer Vulnerability
- **Description**: An unpatched vulnerability in GeoServer instances that allows network compromise
- **Impact**: Complete network breach of federal agency systems, enabling lateral movement and data exfiltration
- **Status**: Successfully exploited against U.S. federal civilian executive branch agency; patch available but not applied in compromised instance
- **CVE ID**: Not specified in source materials

### SolarWinds Web Help Desk Remote Code Execution
- **Description**: Critical vulnerability in SolarWinds Web Help Desk software allowing remote code execution without authentication
- **Impact**: Attackers can execute arbitrary commands on susceptible systems, potentially leading to full system compromise
- **Status**: Third patch released; vulnerability requires immediate attention due to RCE potential
- **CVE ID**: CVE-2025-26399

### Supermicro BMC Firmware Vulnerabilities
- **Description**: Two security vulnerabilities in Supermicro Baseboard Management Controller (BMC) firmware affecting root of trust security
- **Impact**: Malicious firmware can evade security controls and maintain persistent access to server infrastructure
- **Status**: Vulnerabilities disclosed; patches likely available from vendor
- **CVE ID**: Not specified in source materials

## Affected Systems and Products

- **Pandoc**: Linux utility used for document conversion, affecting AWS environments when exploited
- **Libraesva Email Security Gateway**: Enterprise email security solutions across multiple organizations
- **GeoServer**: Open-source server for geospatial data, particularly in federal agency implementations
- **SolarWinds Web Help Desk**: IT service management software used by enterprises
- **Supermicro BMC Firmware**: Server management controllers across data center infrastructure
- **Docker Containers**: Misconfigured AWS Docker instances being exploited for botnet operations
- **npm Ecosystem**: JavaScript package repository being targeted through malicious packages
- **SonicWall SMA 100 Series**: Secure remote access appliances affected by rootkit malware

## Attack Vectors and Techniques

- **Cloud Metadata Service Exploitation**: Targeting AWS IMDS through Pandoc vulnerability to steal IAM credentials
- **SEO Poisoning**: Using search engine optimization manipulation to redirect traffic and deliver malware payloads
- **Supply Chain Attacks**: Compromising npm packages with malicious code, including innovative QR code-based payload delivery
- **Container Misconfiguration Abuse**: Exploiting improperly configured Docker daemons for botnet recruitment
- **Web Shell Deployment**: Installing persistent backdoors through compromised web servers
- **Authentication Bypass**: Exploiting vulnerabilities that allow unauthenticated remote code execution
- **Firmware Manipulation**: Bypassing root of trust security mechanisms in server management controllers

## Threat Actor Activities

- **State-Sponsored Groups**: Actively targeting email security infrastructure through Libraesva ESG vulnerabilities, focusing on intelligence gathering and persistent access
- **Chinese-Speaking Actors**: Conducting Operation Rewrite SEO poisoning campaign using BadIIS malware to compromise legitimate web servers for financial gain
- **ShadowV2 Botnet Operators**: Operating DDoS-for-hire service by exploiting misconfigured AWS Docker containers to build distributed attack infrastructure
- **Federal Agency Attackers**: Successfully breached U.S. government systems through unpatched GeoServer vulnerabilities, demonstrating targeted government focus
- **npm Package Poisoners**: Deploying sophisticated supply chain attacks using QR codes and other evasion techniques to steal browser cookies and credentials
- **Iranian-Linked Groups**: Nimbus Manticore expanding operations to target European infrastructure with improved malware variants