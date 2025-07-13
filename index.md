# Exploitation Report

The last week has seen a sharp uptick in real-world exploitation of high-impact remote-code-execution and data-leak flaws across widely-used enterprise platforms. Attackers are weaponizing critical server-side vulnerabilities in Wing FTP Server, Citrix NetScaler ADC/Gateway, and Fortinet FortiWeb, while also leveraging supply-chain compromises (Gravity Forms) and AI prompt-injection techniques (Google Gemini) to gain initial access and move laterally. Government agencies and security vendors confirm that several of these weaknesses are already being abused in the wild, driving urgent patching directives and defensive guidance.

## Active Exploitation Details

### Wing FTP Server Remote Code Execution
- **Description**: A maximum-severity flaw in Wing FTP Server allows unauthenticated users to send specially crafted commands that trigger arbitrary code execution with SYSTEM-level privileges.  
- **Impact**: Full takeover of the underlying operating system, data theft, lateral movement, and ransomware deployment.  
- **Status**: Confirmed in-the-wild exploitation began within 24 hours of public disclosure; security updates released by Wing FTP are available.  
- **CVE ID**: CVE-2025-47812  

### Citrix NetScaler “CitrixBleed 2” Information Disclosure / Session Hijack
- **Description**: A memory leakage flaw in NetScaler ADC and Gateway lets attackers extract session tokens and credentials, bypassing authentication and gaining administrative access.  
- **Impact**: Complete control of VPN gateways, ability to pivot into internal networks, harvest sensitive data, and deploy post-exploitation tooling.  
- **Status**: Actively exploited according to CISA; federal agencies ordered to patch within 24 hours. Fixes released by Citrix.  
- **CVE ID**: CVE-2025-5777  

### Fortinet FortiWeb Pre-Auth SQL Injection to RCE
- **Description**: A critical SQL injection vulnerability in the FortiWeb WAF permits unauthenticated attackers to execute arbitrary database commands that lead to remote code execution on the appliance.  
- **Impact**: Compromise of the WAF itself, interception or modification of protected web traffic, and foothold for network-wide attacks.  
- **Status**: Proof-of-concept exploits publicly released; mass scanning reported. Fortinet has issued patches.  
- **CVE ID**: CVE-2025-25257  

### Gravity Forms Supply-Chain Backdoor
- **Description**: The official distribution site for the popular WordPress Gravity Forms plugin was compromised, and manual installer packages were replaced with versions containing a PHP backdoor.  
- **Impact**: Backdoored plugins grant attackers persistent remote access to affected WordPress sites, enabling data theft, SEO spam, and further malware deployment.  
- **Status**: Malicious packages observed in the wild; developer is re-issuing clean builds and advising integrity checks.  

### Google Gemini Email-Summary Prompt Injection
- **Description**: Attackers manipulate Gemini for Workspace to generate convincing email summaries embedding malicious links or social-engineering instructions, effectively turning the AI assistant into a phishing facilitator.  
- **Impact**: Elevated phishing success rates, credential theft, and malware delivery without traditional attachments or obvious lures.  
- **Status**: Technique observed in active phishing campaigns; Google is refining guardrails and advising admins to restrict Gemini usage for sensitive email flows.  

## Affected Systems and Products

- **Wing FTP Server**: All platforms (Windows, Linux, macOS) prior to the vendor’s July 2025 hotfix  
- **Citrix NetScaler ADC & Gateway**: Supported versions in the 13.1, 13.0, and 12.1 branches that have not applied the latest security update  
- **Fortinet FortiWeb**: Versions 7.4.x, 7.2.x, 7.0.x, and 6.4.x before the July 2025 patch release  
- **Gravity Forms (WordPress plugin)**: Manual installer ZIP files downloaded from the vendor site between 5 July 2025 and 9 July 2025  
- **Google Workspace – Gemini Smart Reply/Summary**: All Workspace tiers with Gemini enabled for Gmail  

## Attack Vectors and Techniques

- **Unauthenticated Command Injection (FTP)**  
  - **Vector**: Crafted FTP commands exploit input-handling flaws in Wing FTP Server, spawning system shells.  

- **Memory Leak / Token Harvesting (CitrixBleed 2)**  
  - **Vector**: Repeated HTTP/HTTPS requests exfiltrate session memory, exposing authentication tokens for NetScaler management interfaces.  

- **Pre-Auth SQL Injection (FortiWeb)**  
  - **Vector**: Malicious HTTP parameters trigger SQL queries that pivot to shell execution on FortiWeb appliances.  

- **Supply-Chain Backdooring (Gravity Forms)**  
  - **Vector**: Users download tampered plugin installers containing obfuscated PHP payloads that beacon to attacker C2 servers.  

- **Prompt Injection Phishing (Google Gemini)**  
  - **Vector**: Attackers forward or spoof emails with hidden instructions; Gemini summarizes the message and surfaces attacker-supplied malicious links as “recommended actions.”  

## Threat Actor Activities

- **Unknown Criminal Clusters (Wing FTP & FortiWeb)**  
  - **Campaign**: Automated mass scanning of Internet-exposed servers, followed by deployment of coin-miners and remote-administration tools.  

- **Unattributed Actors (“CitrixBleed 2”)**  
  - **Campaign**: Targeted exploitation of government and enterprise VPN gateways for credential harvesting and espionage; activity tracked and confirmed by CISA.  

- **Supply-Chain Intruders (Gravity Forms)**  
  - **Campaign**: Compromised the plugin developer’s infrastructure, replaced legitimate downloads with backdoored builds, and leveraged WordPress auto-update gaps to maintain access.  

- **Phishing Operators leveraging AI (Google Gemini)**  
  - **Campaign**: Ongoing credential-phishing operations against corporate Gmail tenants; exploiting AI summaries for enhanced social engineering.  

- **Pay2Key Ransomware Group (Contextual Activity)**  
  - **Campaign**: Relaunched RaaS offering with an 80% affiliate profit share, encouraging exploitation of the aforementioned gateway and web-server vulnerabilities to gain initial access in U.S. and Israeli organizations.  

Security teams should prioritize patching the enumerated server-side flaws, verify plugin integrity across WordPress estates, and enforce strict controls on AI-powered email features to limit emerging phishing vectors. Continuous monitoring for anomalous outbound connections and session hijack attempts remains critical.