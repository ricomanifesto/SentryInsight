# Exploitation Report

Critical exploitation activity is currently targeting multiple high-value systems across enterprise infrastructure. Most concerning are active attacks against Ivanti Sentry gateways through a maximum-severity vulnerability, ongoing exploitation of a path traversal flaw in the AI development platform Langflow, and a Microsoft Exchange Server zero-day being leveraged for cross-site scripting attacks. Additionally, threat actors are targeting Oracle PeopleSoft servers in widespread data theft campaigns, while state-sponsored groups continue expanding botnet operations for reconnaissance against U.S. military networks.

## Active Exploitation Details

### Ivanti Sentry Maximum Severity Vulnerability
- **Description**: A recently patched maximum-severity flaw in Ivanti Sentry secure mobile gateways
- **Impact**: Enables attackers to execute code with root privileges on Internet-exposed systems
- **Status**: Currently being exploited in active attacks, patch available

### Langflow Path Traversal Vulnerability
- **Description**: High-severity path traversal vulnerability in the AI development platform Langflow
- **Impact**: Allows attackers to write arbitrary files on exposed servers, leading to potential remote code execution
- **Status**: Under active exploitation, currently unpatched
- **CVE ID**: CVE-2026-5027

### Microsoft Exchange Server Zero-Day
- **Description**: Cross-site scripting (XSS) vulnerability in Exchange Server
- **Impact**: Allows threat actors to execute arbitrary JavaScript code targeting Outlook Web Access
- **Status**: Previously exploited as zero-day, now patched by Microsoft

### Cisco, Chrome, and Arista Vulnerabilities
- **Description**: Multiple vulnerabilities across Cisco systems, Google Chrome browser, and Arista network equipment
- **Impact**: Various impacts including potential code execution and privilege escalation
- **Status**: Added to CISA's Known Exploited Vulnerabilities catalog due to active exploitation

## Affected Systems and Products

- **Ivanti Sentry**: Secure mobile gateways with Internet exposure
- **Langflow Platform**: AI development platform servers running vulnerable versions
- **Microsoft Exchange Server**: Outlook Web Access components vulnerable to XSS attacks
- **Oracle PeopleSoft**: Enterprise resource planning servers targeted in data theft campaigns
- **Cisco Systems**: Various Cisco products added to KEV catalog
- **Google Chrome**: Browser vulnerabilities under active exploitation
- **Arista Networks**: Network equipment with exploited vulnerabilities

## Attack Vectors and Techniques

- **Remote Code Execution**: Exploiting maximum-severity Ivanti Sentry vulnerability for root access
- **Path Traversal Attacks**: Leveraging Langflow vulnerability to write malicious files on servers
- **Cross-Site Scripting**: Using Exchange Server zero-day for JavaScript injection in web applications
- **Data Theft Operations**: Targeting PeopleSoft servers for large-scale data extraction
- **Supply Chain Attacks**: Miasma worm framework targeting open-source ecosystems
- **Botnet Operations**: JDY botnet expansion for reconnaissance activities

## Threat Actor Activities

- **ShinyHunters**: Conducting widespread data theft attacks against Oracle PeopleSoft servers, claiming to have compromised over 100 organizations
- **OceanLotus (APT32)**: Vietnam-aligned threat actor running FireAnt campaigns targeting domestic entities and stock investors using SPECTRALVIPER backdoor
- **Chinese State-Sponsored Groups**: Operating expanded JDY botnet with over 1,500 compromised SOHO devices for reconnaissance against U.S. military networks
- **Nightmare-Eclipse**: Independent researcher releasing Windows Defender exploit called RoguePlanet, continuing ongoing disputes with Microsoft
- **The Gentlemen**: Emerging as second most active ransomware group by victim count with aggressive recruitment strategies
- **Various Threat Actors**: Actively exploiting newly disclosed vulnerabilities in Cisco, Chrome, and Arista products