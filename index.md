# Exploitation Report

During the last week, nation-state and financially-motivated adversaries have been aggressively exploiting multiple enterprise-grade platforms. The most critical activity centers on three new Microsoft SharePoint zero-days that are already being chained in espionage intrusions against U.S. government agencies, as well as the long-running remote-code-execution bugs in Ivanti Connect Secure VPN appliances that continue to provide Chinese operators with footholds in Japanese networks six months after patches were issued. In parallel, the threat actor “Mimo” has shifted tactics to abuse legacy vulnerabilities in Magento CMS and openly-exposed Docker daemons to deploy crypto-miners and proxyware, while the new “Coyote” banking trojan is leveraging Windows’ UI Automation framework to bypass user interaction safeguards. Collectively, the campaigns highlight attackers’ preference for edge-facing software and misconfigurations that deliver high-privilege access with minimal user interaction.

## Active Exploitation Details

### Microsoft SharePoint Zero-Day Trio
- **Description**: Three previously unknown SharePoint Server flaws are being weaponized in the wild. Attackers can chain the bugs to upload arbitrary files, achieve remote code execution, and perform privilege escalation inside on-premises SharePoint farms.
- **Impact**: Full takeover of SharePoint sites, lateral movement into connected Microsoft 365 tenants, and exfiltration of sensitive government data.
- **Status**: Two of the vulnerabilities are now patched in the latest cumulative update; one remains unpatched, with Microsoft recommending temporary mitigations.
- **CVE ID**: (explicit IDs were not provided in the source articles)

### Ivanti Connect Secure / Policy Secure RCE Vulnerabilities
- **Description**: A set of remote-code-execution flaws in Ivanti’s VPN gateway products allow unauthenticated attackers to run arbitrary commands and deploy webshells by targeting the edge appliance’s management interface.
- **Impact**: Persistent access to internal networks, credential theft, deployment of custom malware, and direct pivoting to high-value systems.
- **Status**: Patches were released last year, but exploitation remains widespread due to complex upgrade procedures that require factory resets and downtime.
- **CVE ID**:

### Magento CMS Code-Execution Vulnerabilities
- **Description**: Legacy vulnerabilities in Magento enable attackers to upload malicious PHP modules or exploit deserialization flaws, granting code execution on the underlying web server.
- **Impact**: Installation of crypto-miners, proxyware, and backdoors that monetize traffic or support further intrusions.
- **Status**: Security updates are available; exploitation persists against outdated Magento stores.
- **CVE ID**:

### Misconfigured Docker Remote API
- **Description**: Exposed Docker daemons without authentication allow remote attackers to create containers, mount host filesystems, and execute arbitrary code.
- **Impact**: Deployment of resource-intensive crypto-mining containers and relay infrastructure that conceals malicious traffic.
- **Status**: No patch required; remediation involves disabling the public API or enforcing TLS/ACL controls.
- **CVE ID**:

### Windows UI Automation Abuse (Coyote Trojan)
- **Description**: The Coyote banking trojan is the first malware family observed abusing Microsoft’s UI Automation (UIA) framework to simulate user actions, hijack browser sessions, and steal credentials.
- **Impact**: Fraudulent transfers from online‐banking portals and cryptocurrency exchanges, primarily in Brazil.
- **Status**: No vendor patch—this is a living-off-the-land technique; mitigations focus on EDR detection and application control.
- **CVE ID**:

## Affected Systems and Products

- **Microsoft SharePoint Server (on-premises)**  
  - **Platform**: Windows Server environments hosting SharePoint 2019/Subscription Edition

- **Ivanti Connect Secure & Policy Secure Gateways**  
  - **Platform**: Hardware and virtual VPN appliances across enterprise networks

- **Magento Open-Source & Adobe Commerce (2.x)**  
  - **Platform**: Linux/Windows web servers running PHP and MySQL

- **Docker Engine with Remote API exposed (any version)**  
  - **Platform**: Linux hosts (cloud and on-prem)

- **Windows 10/11 endpoints running Chromium-based browsers**  
  - **Platform**: Clients targeted by the Coyote banking trojan via phishing lures

## Attack Vectors and Techniques

- **Edge-Service RCE**: Direct exploitation of web-exposed management interfaces (Ivanti VPN, SharePoint, Magento admin).
- **Zero-Day Chaining**: Sequential use of multiple unknown SharePoint flaws to bypass upload restrictions and escalate privileges.
- **Container Takeover**: Abuse of unauthenticated Docker Remote API (`tcp://0.0.0.0:2375`) to spin up malicious containers.
- **UI Automation Hijacking**: Leveraging the Windows UIA framework to script GUI interactions and bypass browser anti-fraud measures.
- **Webshell Deployment**: Post-exploitation persistence via ASPX, JSP, or PHP webshells dropped on compromised servers.
- **Crypto-Mining & Proxyware**: Monetization through XMRig miners and residential proxy agents executed within cloud or on-prem containers.

## Threat Actor Activities

- **Chinese Nation-State Groups**  
  - **Campaign**: Coordinated exploitation of the SharePoint zero-days against U.S. government entities (including the Nuclear Regulatory Commission) and Japanese enterprises using Ivanti VPNs.

- **Threat Actor “Mimo”**  
  - **Campaign**: Transitioned from Craft CMS to Magento and Docker targets, deploying crypto-miners and proxyware across misconfigured cloud infrastructure.

- **Coyote Operators (Brazil-based cybercriminals)**  
  - **Campaign**: Dozens of financially-motivated attacks against Latin American banks and crypto exchanges using Windows UI Automation techniques.