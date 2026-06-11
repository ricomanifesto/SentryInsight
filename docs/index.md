# Exploitation Report

Critical zero-day vulnerabilities are currently under active exploitation across multiple Microsoft products and enterprise platforms. Microsoft has patched several zero-day vulnerabilities including Exchange Server cross-site scripting flaws and Windows privilege escalation vulnerabilities known as YellowKey, GreenPlasma, and MiniPlasma that allow attackers to gain SYSTEM privileges on fully patched systems. Additionally, a maximum-severity vulnerability in Ivanti Sentry is being actively exploited for remote code execution, while threat actors are targeting Oracle PeopleSoft servers and exploiting a path traversal flaw in the AI development platform Langflow.

## Active Exploitation Details

### **Microsoft Exchange Server Zero-Day**
- **Description**: Cross-site scripting (XSS) vulnerability in Exchange Server that allows execution of arbitrary JavaScript code
- **Impact**: Attackers can execute malicious JavaScript code targeting Outlook Web Access users
- **Status**: Actively exploited in the wild, patch available from Microsoft

### **YellowKey Windows Zero-Day**
- **Description**: Windows privilege escalation vulnerability allowing attackers to gain SYSTEM privileges
- **Impact**: Complete system compromise on fully patched Windows systems
- **Status**: Actively exploited, patched by Microsoft in latest security update

### **GreenPlasma Windows Zero-Day**
- **Description**: Windows privilege escalation vulnerability enabling SYSTEM-level access
- **Impact**: Full administrative control over compromised Windows systems
- **Status**: Under active exploitation, fixed in recent Microsoft patch

### **MiniPlasma Windows Zero-Day**
- **Description**: Vulnerability granting unauthorized access to BitLocker-protected drives
- **Impact**: Bypass of BitLocker encryption protection, potential data exposure
- **Status**: Exploited in attacks, patched by Microsoft

### **Ivanti Sentry Maximum Severity Vulnerability**
- **Description**: Critical flaw in Ivanti Sentry secure mobile gateways
- **Impact**: Remote code execution with root privileges on Internet-exposed devices
- **Status**: Currently being exploited by attackers, patch recently released

### **Langflow Path Traversal Vulnerability**
- **Description**: Path traversal flaw in AI development platform Langflow
- **Impact**: Arbitrary file writing on exposed servers, potential for remote code execution
- **Status**: Actively exploited in attacks, currently unpatched
- **CVE ID**: CVE-2026-5027

## Affected Systems and Products

- **Microsoft Exchange Server**: Outlook Web Access components vulnerable to XSS attacks
- **Windows Operating Systems**: Multiple versions affected by privilege escalation zero-days
- **BitLocker Protected Systems**: Drives vulnerable to unauthorized access via MiniPlasma
- **Ivanti Sentry**: Internet-exposed secure mobile gateways
- **Langflow Platform**: AI development platform installations exposed to internet
- **Oracle PeopleSoft Servers**: Enterprise resource planning systems targeted by ShinyHunters
- **Cisco, Chrome, and Arista Systems**: Multiple products added to CISA's Known Exploited Vulnerabilities catalog

## Attack Vectors and Techniques

- **Cross-Site Scripting (XSS)**: JavaScript injection targeting Outlook Web Access users
- **Privilege Escalation**: Multiple zero-day vulnerabilities enabling SYSTEM-level access on Windows
- **Path Traversal**: File system manipulation attacks against Langflow installations
- **Remote Code Execution**: Root-level code execution on Ivanti Sentry gateways
- **Data Theft Campaigns**: Targeted attacks against Oracle PeopleSoft servers for data exfiltration
- **Supply Chain Attacks**: Credential-stealing through compromised open-source ecosystems

## Threat Actor Activities

- **ShinyHunters Extortion Gang**: Actively targeting Oracle PeopleSoft servers, claiming data theft from over 100 organizations
- **OceanLotus (Vietnam-aligned)**: Conducting two distinct campaigns against domestic entities and stock investors using SPECTRALVIPER backdoor in FireAnt attacks
- **Chinese State-Sponsored Groups**: Operating expanded JDY botnet with over 1,500 SOHO devices for cyber reconnaissance targeting U.S. military networks
- **Nightmare-Eclipse Researcher**: Released RoguePlanet proof-of-concept exploit for Windows Defender vulnerability allowing system takeover
- **The Gentlemen Ransomware Group**: Emerged as second most active ransomware gang by victim count with aggressive recruitment strategy
- **North Korean Threat Groups**: Expanding operations in Asia-Pacific region with increased GDP growth partly attributed to cybercrime activities