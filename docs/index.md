# Exploitation Report

Critical exploitation activity is dominated by supply chain attacks targeting software repositories and browser-based malware operations. The most significant threats include the ShadyPanda browser extension campaign affecting 4.3 million users, the Shai-Hulud 2.0 worm spreading across npm and Maven ecosystems, and North Korean threat actors distributing 197 malicious npm packages. Additionally, CISA has added CVE-2021-26829, an actively exploited XSS vulnerability in OpenPLC ScadaBR, to their Known Exploited Vulnerabilities catalog, indicating ongoing exploitation of industrial control systems.

## Active Exploitation Details

### OpenPLC ScadaBR Cross-Site Scripting Vulnerability
- **Description**: XSS vulnerability in OpenPLC ScadaBR industrial control system software
- **Impact**: Allows attackers to execute malicious scripts in the context of affected applications, potentially leading to data theft or system compromise
- **Status**: Actively being exploited in the wild, added to CISA KEV catalog
- **CVE ID**: CVE-2021-26829

### ShadyPanda Browser Extension Malware
- **Description**: Long-running malware operation using seemingly legitimate Chrome and Edge browser extensions that evolve into malware after installation
- **Impact**: Data theft, credential harvesting, and unauthorized access to user browsing activities
- **Status**: Active campaign with 4.3 million installations already achieved

### Shai-Hulud 2.0 Supply Chain Attack
- **Description**: Self-replicating worm targeting npm and Maven package repositories, evolved from previous npm-only attacks
- **Impact**: Credential and secret theft from AWS, Google Cloud Platform, and Azure environments; supply chain compromise
- **Status**: Actively spreading across multiple package ecosystems with over 830 compromised npm packages

### North Korean OtterCookie Malware Campaign
- **Description**: Contagious Interview campaign distributing updated OtterCookie malware through malicious npm packages
- **Impact**: System compromise and data exfiltration targeting developers and software supply chains
- **Status**: Ongoing with 197 new malicious packages deployed since last month

## Affected Systems and Products

- **Chrome and Edge Browsers**: Browser extensions in ShadyPanda campaign affecting millions of users
- **OpenPLC ScadaBR**: Industrial control system software vulnerable to XSS attacks
- **npm Registry**: Over 830 packages compromised by Shai-Hulud 2.0 worm
- **Maven Repository**: Newly targeted by Shai-Hulud 2.0 expansion beyond npm
- **Cloud Platforms**: AWS, Google Cloud Platform, and Azure credentials targeted by supply chain attacks
- **Android Devices**: Albiriox MaaS malware targeting 400+ applications for on-device fraud
- **Microsoft Teams**: Guest access feature creating security blind spots in Defender for Office 365
- **GitLab Cloud**: 5.6 million public repositories with over 17,000 exposed secrets across 2,800 domains

## Attack Vectors and Techniques

- **Browser Extension Abuse**: Legitimate-appearing extensions that transform into malware post-installation
- **Supply Chain Poisoning**: Self-replicating worms spreading through package repositories
- **Social Engineering**: Fake job interviews and technical assessments to distribute malware
- **Cross-Site Scripting (XSS)**: Exploitation of web application vulnerabilities in industrial systems
- **Malware-as-a-Service (MaaS)**: Albiriox offering comprehensive fraud capabilities to cybercriminals
- **Evil Twin WiFi Networks**: Rogue access points targeting travelers in airports
- **Domain Takeover**: Exploitation of legacy Python bootstrap scripts in PyPI packages
- **Guest Access Exploitation**: Bypassing security controls through Microsoft Teams external tenant access

## Threat Actor Activities

- **ShadyPanda Group**: Operating long-running browser extension malware campaign with 4.3M+ installations
- **North Korean APT**: Continuing Contagious Interview operations with updated OtterCookie malware distribution
- **Shai-Hulud Operators**: Expanding supply chain attacks from npm to Maven repositories with credential theft capabilities
- **Tomiris APT**: Targeting government entities and foreign ministries using public service implants for stealth
- **Bloody Wolf**: Conducting Java-based NetSupport RAT attacks in Kyrgyzstan and Uzbekistan
- **Albiriox Developers**: Offering Android malware-as-a-service for on-device fraud operations
- **Scattered LAPSUS$ Hunters**: Mass extortion group stealing and publicly exposing corporate data