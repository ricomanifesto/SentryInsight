# Exploitation Report

A surge of high-impact vulnerabilities is drawing the attention of both cyber-criminal gangs and advanced persistent threats (APTs). The most critical activity centers on a previously unknown Microsoft Exchange zero-day leveraged by a North-American APT to spy on targets in China, combined with a long-standing Oracle-based flaw that leaves eSIM-equipped phones open to covert takeover. Open-source ecosystems are also under fire: a critical remote-code-execution bug in the widely downloaded `mcp-remote` package is already weaponized by proof-of-concept exploits, while unsafe Bluetooth firmware (PerfektBlue) exposes millions of connected vehicles. Together, these issues illustrate a widening attack surface across mobile, cloud, AI, and IoT environments.

## Active Exploitation Details

### Microsoft Exchange Zero-Day
- **Description**: An undisclosed vulnerability in on-premises Microsoft Exchange that permits remote code execution and email exfiltration without authentication.  
- **Impact**: Full compromise of Exchange servers, lateral movement within corporate networks, theft of sensitive mailboxes.  
- **Status**: Actively exploited by a North-American APT; no public patch released at time of reporting.  
- **CVE ID**: *Not referenced in source material*

### Oracle-Derived eSIM Vulnerability
- **Description**: A six-year-old flaw in Oracle technology embedded in billions of eSIMs allows attackers with either physical proximity or SIM-over-the-air access to clone profiles, intercept traffic, and assume device identity.  
- **Impact**: Espionage, account takeover, stealth device tracking, and interception of SMS-based MFA.  
- **Status**: Exploitation proven by researchers; underlying defect remains unpatched in many carrier implementations.  
- **CVE ID**: *Not referenced in source material*

### `mcp-remote` Remote-Code-Execution Bug
- **Description**: Command-injection flaw in the open-source `mcp-remote` utility that fails to adequately sanitise input before passing it to OS commands.  
- **Impact**: Unauthenticated attackers can execute arbitrary commands with the privileges of the running service.  
- **Status**: Proof-of-concept exploit publicly available; maintainers have issued a fixed release.  
- **CVE ID**: *Not referenced in source material*

### PerfektBlue Bluetooth Stack Flaws
- **Description**: Four vulnerabilities in OpenSynergy’s BlueSDK (“PerfektBlue”) used by several automotive vendors; issues include heap overflows and improper input validation in Bluetooth Low Energy (BLE) routines.  
- **Impact**: Remote code execution on in-vehicle infotainment units, potential pivot to CAN bus and safety-critical systems.  
- **Status**: Vendors are rolling out firmware updates; researchers demonstrated practical exploits at short range.  
- **CVE ID**: *Not referenced in source material*

### NVIDIA Container Toolkit Escape
- **Description**: A privilege-escalation flaw whereby a crafted container can access the host’s GPU driver, breaking isolation and accessing cross-tenant AI workloads.  
- **Impact**: Data theft from AI training sets, host takeover from malicious containers.  
- **Status**: Exploit technique released to vendors; patches and hardening guidance published by NVIDIA.  
- **CVE ID**: *Not referenced in source material*

### ServiceNow ACL Exposure (CVE-2025-3648)
- **Description**: Misconfigured Access-Control Lists allow unauthenticated retrieval of sensitive table data through specific API endpoints.  
- **Impact**: Data exfiltration of tickets, attachments, and PII stored in ServiceNow instances.  
- **Status**: Patched in the July 2025 ServiceNow release; cloud-hosted customers auto-patched, on-premise users must update.  
- **CVE ID**: CVE-2025-3648

## Affected Systems and Products

- **Microsoft Exchange Server**: All supported on-prem versions; cloud/Exchange Online not affected  
- **eSIM-equipped Phones**: Android and iOS devices using vulnerable Oracle-based eUICC firmware across multiple carriers  
- **`mcp-remote` Package**: Versions prior to the fixed release 3.4.1 on NPM/PyPI (≈437 k downloads)  
- **Vehicles using OpenSynergy BlueSDK**: Mercedes-Benz, Volkswagen, Škoda (model years 2022-2025)  
- **Kubernetes clusters with NVIDIA Container Toolkit**: GPU-accelerated nodes on Linux (all major distros)  
- **ServiceNow Instances**: All platform versions prior to July 2025 hotfix

## Attack Vectors and Techniques

- **Server-Side Request Forgery (SSRF)**  
  - **Vector**: Crafted HTTP requests exploit the Exchange zero-day to proxy arbitrary calls through the server.

- **SIM Over-The-Air (SOTA) Manipulation**  
  - **Vector**: Malicious profile updates pushed via carrier channels exploit the Oracle eSIM flaw.

- **Package Supply-Chain Injection**  
  - **Vector**: Attackers publish exploits or typosquatted `mcp-remote` modules, triggering RCE during installation or runtime.

- **Bluetooth Low-Energy RCE**  
  - **Vector**: Malformed BLE packets delivered from nearby devices exploit buffer-overflow bugs in BlueSDK.

- **Container Escape via GPU Driver Abuse**  
  - **Vector**: A user-controlled container loads a crafted driver interface, gaining root access on the host.

- **Unauthenticated API Enumeration**  
  - **Vector**: Direct API calls to misconfigured ACL endpoints leak ServiceNow records.

## Threat Actor Activities

- **North-American APT (Unnamed)**  
  - **Campaign**: Leveraging the Exchange zero-day to infiltrate Chinese governmental and industrial mail servers, conducting long-term espionage.

- **Scattered Spider (Suspected)**  
  - **Activities**: Ransomware and data-extortion operations against UK retailers (M&S, Co-op, Harrods) and US firms; recent arrests may disrupt but not dismantle group.

- **Unknown Vehicle-Focused Researchers**  
  - **Campaign**: Demonstrated PerfektBlue exploits to automotive OEMs; no public criminal campaign yet observed.

- **Open-Source Supply-Chain Actors**  
  - **Activities**: Weaponizing `mcp-remote` flaw through malicious package uploads, targeting developers and CI/CD pipelines.

- **Cloud Tenant Intruders**  
  - **Campaign**: Testing NVIDIA container escape techniques in AI-centric SaaS environments to access proprietary models and datasets.

