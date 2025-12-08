# Exploitation Report

The current threat landscape shows intense exploitation activity centered around several critical vulnerabilities with maximum severity ratings. The React2Shell vulnerability is experiencing widespread exploitation by China-linked threat actors within hours of public disclosure, affecting over 77,000 Internet-exposed IP addresses and leading to confirmed breaches of at least 30 organizations. Simultaneously, a WordPress plugin vulnerability is being actively exploited in the wild, while Oracle zero-day exploitation has resulted in significant healthcare data breaches. The addition of React2Shell to CISA's Known Exploited Vulnerabilities catalog underscores the severity and active threat these vulnerabilities pose to organizations worldwide.

## Active Exploitation Details

### React2Shell Vulnerability
- **Description**: A critical remote code execution flaw affecting React Server Components (RSC) and Next.js applications with a maximum CVSS severity rating
- **Impact**: Allows attackers to execute arbitrary code remotely, leading to complete system compromise and data theft
- **Status**: Actively exploited in the wild by multiple China-linked threat actors within hours of disclosure, with over 77,000 vulnerable IP addresses exposed
- **CVE ID**: CVE-2025-55182

### Sneeit Framework WordPress Plugin Vulnerability
- **Description**: A critical remote code execution vulnerability in the Sneeit Framework plugin for WordPress
- **Impact**: Enables attackers to execute arbitrary code on vulnerable WordPress installations
- **Status**: Actively exploited in the wild according to Wordfence data

### Oracle E-business Suite Zero-Day
- **Description**: An undisclosed zero-day vulnerability in Oracle E-business Suite software
- **Impact**: Enables unauthorized database access and data exfiltration
- **Status**: Exploited by Clop ransomware actors to steal sensitive healthcare data from NHS systems

### Apache Tika XXE Vulnerability
- **Description**: A critical XML external entity (XXE) injection vulnerability in Apache Tika
- **Impact**: Allows attackers to read arbitrary files, perform server-side request forgery, and potentially achieve remote code execution
- **Status**: Recently disclosed with maximum CVSS 10.0 severity rating, requires urgent patching
- **CVE ID**: CVE-2025-66516

### ICTBroadcast Vulnerability
- **Description**: A security flaw in ICTBroadcast software being leveraged for botnet operations
- **Impact**: Enables attackers to build and expand botnet infrastructure
- **Status**: Actively exploited by Frost Botnet operators

## Affected Systems and Products

- **React Server Components**: Applications using React and Next.js frameworks with RSC implementation
- **WordPress Installations**: Sites using the vulnerable Sneeit Framework plugin
- **Oracle E-business Suite**: Enterprise resource planning systems, particularly in healthcare sector
- **Apache Tika**: Document analysis and content extraction systems across various organizations
- **ICTBroadcast**: Voice over IP and broadcast communication systems
- **Palo Alto GlobalProtect**: VPN portals experiencing targeted login attempts and scanning activity
- **SonicWall SonicOS**: API endpoints under active scanning and reconnaissance

## Attack Vectors and Techniques

- **Remote Code Execution via RSC**: Exploitation of server-side rendering vulnerabilities in React applications
- **WordPress Plugin Exploitation**: Targeting vulnerable WordPress plugins for initial access
- **Zero-Day Database Exploitation**: Leveraging undisclosed Oracle vulnerabilities for data access
- **XXE Injection**: Exploiting XML processing vulnerabilities in document parsing systems
- **Botnet Infrastructure**: Using ICTBroadcast flaws to establish persistent command and control
- **VPN Brute Force**: Mass login attempts against GlobalProtect portals
- **UDP-Based Backdoors**: Implementation of UDP protocol for covert command and control communications
- **Agentic Browser Attacks**: Zero-click attacks through crafted emails targeting AI-powered browsers

## Threat Actor Activities

- **China-Linked Groups**: Multiple threat actors rapidly weaponizing React2Shell vulnerability within hours of disclosure, demonstrating sophisticated capability and coordination
- **MuddyWater (Iranian APT)**: Deploying UDPGangster backdoor in targeted campaigns against Turkey, Israel, and Azerbaijan using UDP-based command and control
- **Clop Ransomware**: Exploiting Oracle zero-day vulnerabilities to breach healthcare systems and steal sensitive patient data
- **Frost Botnet Operators**: Leveraging ICTBroadcast vulnerabilities to expand botnet infrastructure and capabilities
- **PRC State-Sponsored Actors**: Using BRICKSTORM backdoor for establishing long-term persistent access in U.S. government and critical infrastructure systems
- **Intellexa/Predator Spyware**: Utilizing zero-day exploits and ads-based delivery vectors to target civil society members and activists in Pakistan