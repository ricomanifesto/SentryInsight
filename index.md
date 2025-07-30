# Exploitation Report

Recent reporting highlights a surge in targeted exploitation of enterprise software platforms. The most critical events include mass, automated attacks against un-patched Microsoft SharePoint servers across multiple African organizations, an in-the-wild exploitation of a freshly patched SAP NetWeaver flaw (CVE-2025-31324) that enabled the delivery of new Linux “Auto-Color” malware, and a critical access-bypass issue in the popular Base44 “vibe coding” platform. These campaigns show that attackers are moving quickly—often within days of vendor advisories—to weaponize high-impact vulnerabilities for initial access, espionage, and ransomware deployment.

## Active Exploitation Details

### SAP NetWeaver Application Server Java Deserialization Vulnerability  
- **Description**: A critical flaw in SAP NetWeaver AS Java that allows adversaries to send crafted HTTP requests resulting in unsafe deserialization and remote code execution on the underlying Linux host.  
- **Impact**: Full system compromise leading to deployment of the “Auto-Color” backdoor, persistence, and lateral movement inside corporate environments.  
- **Status**: Exploited in April 2025 against a U.S. chemicals company; patches are available and should be applied immediately.  
- **CVE ID**: CVE-2025-31324  

### Microsoft SharePoint On-Premises Remote Code Execution Chain  
- **Description**: A set of long-standing SharePoint server vulnerabilities that enable pre-authentication code execution and arbitrary file upload when servers remain unpatched or misconfigured.  
- **Impact**: Attackers gain initial foothold, exfiltrate sensitive treasury documents, and stage credential theft that cascades to Active Directory compromise.  
- **Status**: Actively exploited in a mass campaign impacting government and private entities in South Africa and neighboring countries; security updates are available but adoption is low.  

### Base44 Vibe Coding Platform Access-Bypass Flaw  
- **Description**: A critical logic vulnerability in Base44’s AI-driven coding platform that lets unauthenticated users enumerate and access otherwise private applications and source code repositories.  
- **Impact**: Exposure of proprietary code, intellectual property theft, and the possibility of supply-chain poisoning by injecting malicious code into private projects.  
- **Status**: Patched by the vendor after responsible disclosure; evidence indicates opportunistic exploitation before the fix was released.  

### Gunra Ransomware Linux Variant Initial-Access Weakness  
- **Description**: The newly ported Gunra ransomware leverages publicly facing Linux services with weak authentication or unpatched flaws to execute a multithreaded encryption routine.  
- **Impact**: Rapid encryption of Linux servers and attached NFS shares, disrupting production workloads and backup repositories.  
- **Status**: Observed in the wild; no vendor patch required—mitigation centers on hardening exposed services and closing known vulnerabilities used for initial entry.  

## Affected Systems and Products

- **SAP NetWeaver AS Java (7.x)**: All unsupported or pre-patch versions  
  - **Platform**: Linux (x86_64) enterprise servers  

- **Microsoft SharePoint Server (2019, 2016, 2013)**: On-premises deployments lacking latest cumulative updates  
  - **Platform**: Windows Server environments, often integrated with Active Directory  

- **Base44 Vibe Coding Platform (Cloud SaaS)**: Instances prior to July 2025 hot-fix release  
  - **Platform**: Multi-tenant cloud; developer CI/CD pipelines  

- **Linux Servers running SSH, Web or Database Services**: Targets of the new Gunra ransomware build  
  - **Platform**: Ubuntu, RHEL, Debian, SUSE, and derivatives in data-center and cloud VMs  

## Attack Vectors and Techniques

- **HTTP Deserialization RCE (SAP)**  
  - **Vector**: Crafted HTTP/S requests to NetWeaver’s `/ctc/` endpoints trigger unsafe deserialization, spawning a reverse shell.  

- **Pre-Auth SharePoint File Upload / RCE**  
  - **Vector**: Automated scanning for vulnerable `/Layouts/Upload.aspx` and SOAP API routes followed by malicious DLL upload and execution.  

- **Access-Control Logic Bypass (Base44)**  
  - **Vector**: Manipulated session tokens in API calls circumvent tenant-scoping checks, exposing private repositories.  

- **Ransomware Dropper via Weak SSH Credentials (Gunra)**  
  - **Vector**: Brute-forced or default SSH keys grant shell access; bash script installs XOR-encoded ELF payload that launches multithreaded encryptor.  

## Threat Actor Activities

- **Unnamed SAP Campaign Operator**  
  - **Campaign**: Compromised a U.S. chemicals firm in April 2025 to deploy Auto-Color backdoor, focusing on proprietary formula theft.  

- **SharePoint Mass-Exploitation Cluster**  
  - **Actor/Group**: Likely financially motivated cyber-criminal crew leveraging automated tooling; targeting South African treasury and private sector for large-scale data exfiltration and ransomware staging.  

- **Copycat Groups Post-Scattered Spider Arrests**  
  - **Campaign**: Imitating Scattered Spider’s cloud-focused TTPs, these actors are probing SaaS platforms like Base44 for access-control weaknesses to steal source code and credentials.  

- **Gunra Ransomware Operators**  
  - **Campaign**: Expanding from Windows to Linux, leveraging cross-platform Golang payloads; observed targeting manufacturing and technology firms for double-extortion attacks.  

**Bold** mitigation guidance: prioritize patching SAP NetWeaver (CVE-2025-31324) and Microsoft SharePoint, review Base44 tenant permissions, enforce MFA on SSH, and monitor for unknown ELF binaries to counter the emergent threat landscape.