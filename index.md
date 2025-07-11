# Exploitation Report

Over the last week, defenders have had to react to a fast-moving set of in-the-wild attacks that center on enterprise infrastructure and core communications platforms.  Two campaigns stand out: (1) opportunistic exploitation of Citrix NetScaler CVE-2025-5777 to gain initial access to corporate networks, and (2) a stealth offensive operation in which a North-American-based APT weaponized an unpatched Microsoft Exchange Server zero-day against organizations in China.  In parallel, researchers disclosed a long-standing Oracle-derived flaw in eSIM technology that can be used for covert surveillance and full device compromise, underscoring the breadth of targets now exposed—from data-center appliances to mobile handsets.

## Active Exploitation Details

### Citrix NetScaler ADC / Gateway Authentication Bypass  
- **Description**: A critical flaw in Citrix NetScaler ADC and Gateway allows remote, unauthenticated attackers to bypass authentication controls and execute arbitrary commands or hijack user sessions.  
- **Impact**: Full compromise of appliances, lateral movement into internal networks, and potential data exfiltration.  
- **Status**: Actively exploited in the wild; CISA added the issue to the Known Exploited Vulnerabilities (KEV) catalog. Vendor patches are available and should be applied immediately.  
- **CVE ID**: CVE-2025-5777  

### Microsoft Exchange Server Unpatched Zero-Day  
- **Description**: An undisclosed vulnerability in on-premises Microsoft Exchange Server permits remote code execution and post-exploitation persistence without valid credentials.  
- **Impact**: Attackers can deploy web shells, exfiltrate mailbox data, and maintain long-term footholds inside targeted organizations.  
- **Status**: Zero-day actively exploited by a North-American APT group against Chinese entities; no vendor patch released at time of reporting.  

### Oracle-Derived eSIM Vulnerability  
- **Description**: A six-year-old flaw originating from Oracle code used in eSIM management lets adversaries manipulate the remote SIM provisioning process or perform physical attacks on the eUICC.  
- **Impact**: Stealth location tracking, interception of voice/SMS, and full device takeover across millions of smartphones worldwide.  
- **Status**: Proof-of-concept exploitation demonstrated by researchers and considered practical for both network-based and physical attacks. Mitigations are limited because the vulnerability is embedded in hardware and ecosystem tooling.  

## Affected Systems and Products

- **Citrix NetScaler ADC & Gateway**: All supported versions prior to the vendor’s July 2025 security updates  
  - **Platform**: On-premises and cloud-hosted Citrix application delivery controllers and VPN gateways  

- **Microsoft Exchange Server**: Supported on-premises versions (2019, 2016) not yet updated with forthcoming security fix  
  - **Platform**: Windows Server environments running Microsoft Exchange in self-managed data centers or IaaS clouds  

- **Smartphones with eSIM / eUICC components using Oracle-based code**  
  - **Platform**: Android and iOS devices from multiple OEMs that rely on GSMA Remote SIM Provisioning infrastructure  

## Attack Vectors and Techniques

- **HTTP(S) Request Smuggling / Authentication Bypass (Citrix)**  
  - **Vector**: Crafted web requests sent to vulnerable NetScaler endpoints bypass built-in AAA mechanisms and reach administrative interfaces.  

- **Web-Shell Deployment via Outlook Web Services (Exchange Zero-Day)**  
  - **Vector**: Malicious requests inject a web shell into the Exchange Front-End, allowing command execution under SYSTEM context.  

- **Remote SIM Provisioning Manipulation (eSIM Bug)**  
  - **Vector**: Adversary tampers with the SMDP+ server communication or uses physical interfaces to rewrite the eUICC profile, subverting carrier trust models.  

## Threat Actor Activities

- **Unknown Opportunistic Actors**  
  - **Campaign**: Mass scanning and exploitation of CVE-2025-5777 to obtain footholds in enterprise networks, often preceding ransomware deployment.  

- **North-American APT (unnamed)**  
  - **Campaign**: Targeted intrusion against Chinese organizations leveraging an Exchange zero-day; objectives include espionage and strategic data theft.  

- **Security Researchers / Proof-of-Concept Authors**  
  - **Campaign**: Public demonstration of the eSIM vulnerability to pressure vendors and carriers to redesign provisioning workflows and issue firmware updates.