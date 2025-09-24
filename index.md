# Exploitation Report

Critical exploitation activity is currently targeting multiple high-value systems across cloud infrastructure, enterprise security solutions, and government networks. State-sponsored threat actors are actively exploiting vulnerabilities in Libraesva Email Security Gateway solutions and GeoServer instances to breach federal agencies. Meanwhile, cybercriminals are leveraging CVE-2025-51591 in Pandoc to target AWS cloud environments and steal EC2 IAM credentials. The ShadowV2 botnet is exploiting misconfigured Docker containers for DDoS-for-hire services, while Scattered Spider continues large-scale ransomware operations generating over $115 million in proceeds. Additional threats include SEO poisoning campaigns using BadIIS malware, supply chain attacks through npm packages, and newly discovered vulnerabilities in Supermicro BMC firmware that could bypass root of trust security mechanisms.

## Active Exploitation Details

### Pandoc Command Line Utility Vulnerability
- **Description**: A vulnerability in the Pandoc Linux utility that allows attackers to target AWS Instance Metadata Service (IMDS)
- **Impact**: Enables theft of EC2 IAM credentials and potential cloud infrastructure compromise
- **Status**: Actively exploited in the wild as discovered by Wiz security researchers
- **CVE ID**: CVE-2025-51591

### Libraesva Email Security Gateway Vulnerability
- **Description**: A security flaw in Libraesva's Email Security Gateway (ESG) solution being exploited by state-sponsored actors
- **Impact**: Allows unauthorized access to email security infrastructure
- **Status**: Emergency patch released by Libraesva following active exploitation reports
- **CVE ID**: Not specified in the articles

### GeoServer Vulnerability
- **Description**: An unpatched vulnerability in GeoServer instances used to breach federal agency networks
- **Impact**: Enables network compromise and lateral movement within government systems
- **Status**: CISA confirmed exploitation against unnamed U.S. federal civilian executive branch agency
- **CVE ID**: Not specified in the articles

### SolarWinds Web Help Desk RCE Vulnerability
- **Description**: Critical remote code execution vulnerability in SolarWinds Web Help Desk software
- **Impact**: Allows attackers to execute arbitrary commands on susceptible systems without authentication
- **Status**: Third patch released, indicating ongoing exploitation attempts
- **CVE ID**: CVE-2025-26399

### Supermicro BMC Firmware Vulnerabilities
- **Description**: Two security vulnerabilities in Supermicro Baseboard Management Controller firmware
- **Impact**: Enables attackers to bypass critical security mechanisms and evade root of trust protections
- **Status**: Recently disclosed by cybersecurity researchers, exploitation potential confirmed
- **CVE ID**: Not specified in the articles

## Affected Systems and Products

- **AWS EC2 Instances**: Systems running Pandoc utility vulnerable to credential theft
- **Libraesva Email Security Gateway**: All ESG solution deployments prior to emergency patch
- **GeoServer**: Unpatched instances in federal government networks
- **SolarWinds Web Help Desk**: All versions prior to latest hotfix release
- **Supermicro BMC Firmware**: Baseboard Management Controller systems with vulnerable firmware
- **Docker Containers**: Misconfigured AWS Docker deployments targeted by ShadowV2 botnet
- **NPM Ecosystem**: JavaScript packages and dependencies vulnerable to supply chain attacks
- **IIS Web Servers**: Compromised servers used in BadIIS malware SEO poisoning campaigns
- **SonicWall SMA 100 Series**: Devices infected with rootkit malware requiring firmware updates

## Attack Vectors and Techniques

- **Cloud Metadata Service Exploitation**: Targeting AWS IMDS through Pandoc vulnerability to steal IAM credentials
- **SEO Poisoning**: Using compromised legitimate web servers to deliver malicious content and redirect traffic
- **Supply Chain Attacks**: Injecting malicious code into npm packages, including QR code-based payload delivery
- **Container Misconfiguration Exploitation**: Leveraging exposed Docker daemons for botnet recruitment
- **Email Security Gateway Compromise**: State-sponsored actors targeting enterprise email security infrastructure
- **Social Engineering**: Scattered Spider group using sophisticated social engineering for initial access
- **Ransomware Operations**: Large-scale ransomware deployments generating millions in illicit proceeds
- **Web Shell Deployment**: Planting persistent backdoors through BadIIS malware on compromised servers

## Threat Actor Activities

- **State-Sponsored Groups**: Actively exploiting Libraesva ESG and GeoServer vulnerabilities to target government and enterprise networks
- **Scattered Spider**: 19-year-old U.K. national Thalha Jubair and associates responsible for $115 million in ransomware proceeds through sophisticated social engineering campaigns
- **Chinese-Speaking Threat Actors**: Conducting Operation Rewrite SEO poisoning campaign using BadIIS malware to compromise legitimate web servers for financial gain
- **ShadowV2 Botnet Operators**: Running DDoS-for-hire service by exploiting misconfigured AWS Docker containers for distributed denial-of-service attacks
- **Supply Chain Attackers**: Targeting npm ecosystem with malicious packages, including innovative QR code-based payload delivery mechanisms
- **Cryptocurrency Fraud Networks**: European law enforcement dismantled ring responsible for €100 million in investment fraud across 23 countries