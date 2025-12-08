# Exploitation Report

Critical exploitation activity is currently dominated by the React2Shell vulnerability affecting React Server Components, which has been rapidly weaponized by multiple China-linked threat actors within hours of public disclosure. This maximum-severity remote code execution flaw has already compromised over 30 organizations with more than 77,000 vulnerable IP addresses exposed globally. Concurrently, threat actors continue exploiting an Oracle zero-day vulnerability that led to a significant NHS data breach, while Iranian groups deploy new UDP-based backdoors in targeted regional campaigns. The exploitation landscape shows sophisticated actors quickly adapting to newly disclosed vulnerabilities and maintaining persistent access through advanced malware frameworks.

## Active Exploitation Details

### React2Shell Remote Code Execution Vulnerability
- **Description**: A critical remote code execution flaw affecting React Server Components (RSC) that allows attackers to execute arbitrary code on vulnerable systems
- **Impact**: Complete system compromise, data theft, and unauthorized access to affected applications
- **Status**: Actively exploited by multiple China-linked threat actors within hours of disclosure, added to CISA KEV catalog
- **CVE ID**: CVE-2025-55182

### Oracle E-business Suite Zero-Day Vulnerability
- **Description**: An unpatched vulnerability in Oracle E-business Suite software that allows unauthorized database access
- **Impact**: Data breach and theft of sensitive files from organizational databases
- **Status**: Actively exploited by Clop ransomware group, resulting in confirmed NHS data breach

### Array Networks AG Series Command Injection Vulnerability
- **Description**: A command injection vulnerability in Array Networks AG Series secure access gateways
- **Impact**: Remote code execution and unauthorized access to network infrastructure
- **Status**: Actively exploited since August 2025, confirmed by JPCERT/CC

### Apache Tika XXE Vulnerability
- **Description**: A critical XML external entity (XXE) injection vulnerability in Apache Tika document processing library
- **Impact**: Data exfiltration, server-side request forgery, and potential remote code execution
- **Status**: Critical severity requiring urgent patching
- **CVE ID**: CVE-2025-66516

## Affected Systems and Products

- **React and Next.js Applications**: Applications using React Server Components are vulnerable to remote code execution attacks
- **Oracle E-business Suite**: Database systems running vulnerable versions targeted by ransomware groups
- **Array Networks AG Series Gateways**: Secure access gateways vulnerable to command injection attacks
- **Apache Tika**: Document processing systems using vulnerable Tika versions exposed to XXE attacks
- **AI-Powered IDEs**: Over 30 vulnerabilities discovered in AI coding tools enabling data theft and RCE
- **Palo Alto GlobalProtect**: VPN portals targeted by brute force login campaigns
- **Cloudflare Infrastructure**: Services disrupted due to emergency React2Shell vulnerability mitigations

## Attack Vectors and Techniques

- **UDP-Based Command and Control**: MuddyWater group deploying UDPGangster backdoor using UDP protocol for C2 communications
- **Rapid Zero-Day Weaponization**: China-linked groups exploiting React2Shell within hours of public disclosure
- **Ransomware Database Exploitation**: Clop group leveraging Oracle zero-day for data theft operations
- **VPN Brute Force Attacks**: Systematic login attempts against GlobalProtect portals with scanning of SonicWall endpoints
- **Agentic Browser Attacks**: Zero-click attacks using crafted emails to manipulate AI browser agents
- **Prompt Injection in AI Tools**: Exploitation of AI IDE vulnerabilities through malicious prompt injection
- **Persistent Backdoor Deployment**: BRICKSTORM backdoor used for long-term access to U.S. government systems

## Threat Actor Activities

- **China-Linked Groups**: Multiple threat actors rapidly weaponizing React2Shell vulnerability for widespread exploitation campaigns
- **MuddyWater (Iranian APT)**: Conducting targeted campaigns against Turkey, Israel, and Azerbaijan using new UDPGangster backdoor
- **Clop Ransomware Group**: Exploiting Oracle zero-day to breach NHS Trust systems and steal sensitive healthcare data
- **PRC State-Sponsored Actors**: Deploying BRICKSTORM backdoor for persistent access to critical U.S. infrastructure systems
- **Intellexa Commercial Spyware**: Using zero-day exploits and ad-based delivery vectors for Predator spyware targeting civil society