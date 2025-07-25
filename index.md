# Exploitation Report

Over the last week, threat hunters observed a surge in server-side exploitation that is enabling both ransomware deployment and large-scale cryptomining.  Storm-2603 is chaining two Microsoft SharePoint flaws to gain initial foothold before detonating ransomware, while new Soco404 and Koske campaigns weaponize cloud-service misconfigurations and container weaknesses to drop cross-platform miners.  Koske’s Linux variant further raises the bar by hiding payloads in seemingly innocuous panda JPEGs that unpack directly into memory, evading EDR.  Collectively, these campaigns highlight the continued abuse of unpatched collaboration software and poorly secured cloud workloads, underscoring the need for rapid patching, hardening, and continuous monitoring.

## Active Exploitation Details

### SharePoint ‘ToolShell’ Vulnerability Chain
- **Description**: A two-step attack abusing a privilege-escalation flaw followed by a remote-code-execution flaw in Microsoft SharePoint, allowing attackers to bypass authentication and run arbitrary code as nt authority\system.  
- **Impact**: Full takeover of SharePoint servers, lateral movement to domain controllers, and deployment of ransomware payloads.  
- **Status**: Actively exploited by Storm-2603 in the wild; Microsoft patches available.  
- **CVE ID**: CVE-2023-29357, CVE-2023-24955  

### Container & Cloud Misconfiguration Exploits (Soco404 campaign)
- **Description**: Automated exploitation of exposed Docker REST APIs, weak Kubernetes API servers, and publicly accessible Redis instances to deploy Golang-based binaries that mine cryptocurrency.  
- **Impact**: High CPU consumption, resource exhaustion, potential service outages, and cloud cost spikes.  
- **Status**: Ongoing attacks observed; no vendor patches because flaws stem from insecure default configurations.  

### Koske Steganographic Loader
- **Description**: Linux malware that embeds an ELF loader inside innocuous panda JPEG images. When the file is processed, the loader extracts to memory and executes a Monero miner along with a rootkit module.  
- **Impact**: File-less execution evades disk-based detection; attackers gain persistent root access and monetize compromised servers through mining.  
- **Status**: Active campaign; defenders must rely on network/behavioral detections rather than patches.  

### Redis Unauthorized Access for Miner Deployment (Cross-Platform)
- **Description**: Attackers connect to Redis instances left open on the Internet, leverage the CONFIG command to write an SSH key to /root/.ssh/authorized_keys, and then install Soco404 or Koske miners.  
- **Impact**: Remote shell access, system hijacking, data exfiltration risk, and prolonged illicit mining.  
- **Status**: Widespread scanning and exploitation; mitigation through Redis hardening and access-control lists.  

## Affected Systems and Products

- **Microsoft SharePoint**: Versions prior to the June 2023 cumulative update  
  - **Platform**: On-premises SharePoint Server (all supported editions)  

- **Docker Engine hosts**: Instances exposing TCP port 2375/2376 without TLS or authentication  
  - **Platform**: Linux and Windows container hosts in cloud and on-prem environments  

- **Kubernetes Clusters**: API servers reachable from the Internet or internal networks without RBAC restrictions  
  - **Platform**: Managed (EKS/GKE/AKS) and self-managed clusters  

- **Redis Databases**: Stand-alone or clustered nodes running with default configuration and no authentication  
  - **Platform**: Linux/Unix servers in public cloud or on-prem  

- **General Linux Servers**: Any distribution susceptible to the Koske steganographic loader  
  - **Platform**: x86-64 and ARM architectures  

## Attack Vectors and Techniques

- **Authentication Bypass & RCE Chaining**  
  - **Vector**: Crafted HTTP requests against SharePoint endpoints to trigger CVE-2023-29357, followed by module upload via CVE-2023-24955.

- **Exposed API Abuse**  
  - **Vector**: Direct REST calls to unauthenticated Docker/Kubernetes APIs to spawn privileged containers that download miners.

- **Steganographic Payload Delivery**  
  - **Vector**: PNG/JPEG files containing hidden ELF payloads transmitted over HTTP(S); decoded and executed in-memory.

- **Unauthorized Redis CONFIG Write**  
  - **Vector**: Use of CONFIG and SLAVEOF/replica commands to overwrite file paths and establish SSH persistence.

- **Living-off-the-Land Privilege Escalation**  
  - **Vector**: Abuse of native system utilities (cron, systemd) inside containers/hosts to maintain persistence for miners and ransomware loaders.

## Threat Actor Activities

- **Storm-2603 (China-based)**  
  - **Campaign**: Leveraging SharePoint ‘ToolShell’ chain to gain domain-wide access, exfiltrate data, and deliver ransomware payloads.

- **Soco404 Operators**  
  - **Campaign**: Automated cloud targeting focusing on misconfigured Docker and Kubernetes to deploy Golang and Rust miners across Windows, Linux, and ARM devices.

- **Koske Operators**  
  - **Campaign**: Steganography-enabled cryptomining against Linux servers; employs AI-generated code snippets and memory-only loaders to hinder forensic analysis.

- **Associated Ransomware Crews**  
  - **Campaign**: Post-exploitation monetization of SharePoint compromises through double-extortion ransomware, correlating with spikes in BlackSuit and related operations (now partially disrupted by Operation Checkmate).

