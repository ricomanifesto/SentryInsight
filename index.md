# Exploitation Report

Critical zero-day vulnerabilities are currently under active exploitation across multiple platforms, with attackers targeting Windows systems, open-source Git services, and enterprise infrastructure. The most severe threats include an unpatched Gogs zero-day that has compromised over 700 servers worldwide, a Windows RasMan service vulnerability causing denial of service attacks, and a GeoServer XML External Entity injection flaw that CISA has added to its Known Exploited Vulnerabilities catalog. Additionally, attackers are exploiting hard-coded cryptographic keys in Gladinet's enterprise file sharing products and leveraging a high-severity Chrome browser vulnerability in active in-the-wild attacks.

## Active Exploitation Details

### Gogs Zero-Day Remote Code Execution
- **Description**: An unpatched high-severity vulnerability in Gogs, a popular self-hosted Git service, that bypasses a previous RCE bug fix disclosed last year
- **Impact**: Remote code execution on Internet-facing instances, leading to complete server compromise
- **Status**: Actively exploited with over 700 compromised instances identified; remains unpatched

### Windows RasMan Zero-Day
- **Description**: A vulnerability in the Windows Remote Access Connection Manager (RasMan) service that allows attackers to crash the service
- **Impact**: Denial of service attacks against Windows systems through service crashes
- **Status**: Zero-day vulnerability with unofficial patches available

### GeoServer XXE Vulnerability
- **Description**: A high-severity XML External Entity (XXE) injection vulnerability in OSGeo GeoServer
- **Impact**: Data exfiltration, server-side request forgery, and potential remote code execution
- **Status**: Actively exploited in the wild; added to CISA's Known Exploited Vulnerabilities catalog

### Gladinet CentreStack/Triofox Cryptographic Flaw
- **Description**: Hard-coded cryptographic keys in Gladinet's CentreStack and Triofox products for secure remote file access
- **Impact**: Unauthorized access and remote code execution on affected systems
- **Status**: Actively exploited with nine organizations confirmed compromised

### Chrome High-Severity Vulnerability
- **Description**: An undisclosed high-severity flaw in Google Chrome browser
- **Impact**: Active in-the-wild exploitation enabling various attack scenarios
- **Status**: Under active exploitation; security updates released by Google

### React2Shell Vulnerability
- **Description**: A critical vulnerability affecting React Server Components that has escalated into large-scale global attacks
- **Impact**: Potential denial of service and source code exposure
- **Status**: Widespread exploitation prompting CISA emergency directive for federal agencies to patch by December 12, 2025

## Affected Systems and Products

- **Gogs Git Service**: Self-hosted Git service instances accessible over the internet
- **Windows Systems**: All versions running RasMan service
- **OSGeo GeoServer**: Geographic information system servers
- **Gladinet Products**: CentreStack and Triofox secure file sharing solutions
- **Google Chrome**: Web browsers with the undisclosed high-severity vulnerability
- **React Applications**: Systems using React Server Components
- **VSCode Extensions**: Malicious marketplace extensions targeting developers
- **Notepad++**: WinGUp update tool in versions prior to 8.8.9

## Attack Vectors and Techniques

- **Zero-Day Exploitation**: Attackers leveraging unpatched vulnerabilities in Gogs and Windows RasMan
- **XXE Injection**: XML External Entity attacks against GeoServer installations
- **Hard-Coded Key Abuse**: Exploitation of embedded cryptographic keys in enterprise software
- **Supply Chain Attacks**: Malicious VSCode extensions hiding trojans in fake PNG files
- **Browser Exploitation**: In-the-wild attacks targeting Chrome vulnerabilities
- **Social Engineering**: ConsentFix attacks hijacking Microsoft accounts via Azure CLI OAuth
- **Malware Distribution**: NANOREMOTE backdoor using Google Drive API for command and control

## Threat Actor Activities

- **Storm-0249**: Initial access broker weaponizing EDR platforms and Windows utilities in high-precision attacks
- **Hamas-Linked Hackers**: Targeting Middle Eastern diplomats with improved malware capabilities
- **WIRTE APT Group**: Using AshenLoader sideloading to install AshTag espionage backdoor against government and diplomatic entities in the Middle East
- **VSCode Marketplace Attackers**: Campaign active since February 2024 with 19 malicious extensions targeting developers
- **Gogs Exploiters**: Mass compromise campaign affecting hundreds of Git service instances globally
- **Gladinet Attackers**: Targeting enterprise file sharing infrastructure with cryptographic key exploitation