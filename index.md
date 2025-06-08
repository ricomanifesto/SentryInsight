# Exploitation Report

A surge in malicious activity has been observed across several fronts, including a botnet-driven command injection attack on TBK DVR devices, an expansive supply chain compromise in npm and PyPI packages, and an uptick in sophisticated phishing tactics leveraging ClickFix. Meanwhile, ransomware groups are exploiting critical Fortinet flaws and continuing to compromise organizations worldwide, underscoring the urgent need for vigilant patching, threat monitoring, and robust supply chain defenses.

## Active Exploitation Details

### TBK DVR Command Injection
- **Description**: A command injection flaw in TBK DVR-4104 and DVR-4216 devices used by a new Mirai botnet variant to gain unauthorized access.  
- **Impact**: Attackers can remotely compromise DVR hardware, enlist devices into a botnet, and potentially pivot into broader networks.  
- **Status**: Exploited in the wild with active botnet campaigns. No detailed patch information was provided; administrators are advised to apply any available firmware updates or vendor mitigations.

### Malicious npm and PyPI Supply Chain Attack
- **Description**: Attackers introduced malware into popular GlueStack packages in both npm and PyPI repositories, infecting projects at build time.  
- **Impact**: Threat actors can steal credentials, exfiltrate sensitive data, or gain remote access through injected code.  
- **Status**: The malicious packages have been identified and removed, but users who installed them remain at risk if they have not updated or mitigated.

### Malicious Browser Extensions
- **Description**: A campaign targeting Chromium-based browsers with extensions that siphon user data. The operation has infected hundreds of users across Latin America since early 2025.  
- **Impact**: Unauthorized data collection, credential theft, and potential for account takeover.  
- **Status**: Active distribution through social engineering, with no official patches; users must remove suspicious extensions and disable auto-install.

### Malicious npm Packages Data Wiper
- **Description**: Two malicious npm packages posing as utility libraries were discovered wiping project directories after installation.  
- **Impact**: Destructive file deletion results in immediate data loss and project corruption.  
- **Status**: Packages have been removed from the npm registry; developers who installed these packages are urged to restore from backups and verify code integrity.

### Critical Fortinet Flaws
- **Description**: Qilin ransomware actors are exploiting critical authentication bypass vulnerabilities in Fortinet devices to gain privileged access.  
- **Impact**: The flaws enable remote code execution and quick lateral movement, allowing ransomware deployment across enterprise environments.  
- **Status**: Exploited by ransomware groups in active campaigns; Fortinet users should apply vendor-released updates and secure perimeter defenses.

## Affected Systems and Products

- **TBK DVR-4104 and DVR-4216**: Vulnerable to command injection hijacks.  
- **Gluestack Packages (npm/PyPI)**: Compromised for remote access malware injection in build environments.  
- **Chromium-Based Web Browsers**: Susceptible to malicious browser extensions stealing user data.  
- **npm JavaScript Libraries**: Two destructive packages that wipe project directories upon installation.  
- **Fortinet Security Appliances**: Targeted by ransomware operators for unauthorized network access.

## Attack Vectors and Techniques

- **Command Injection**: Injecting system commands into vulnerable DVR firmware to compromise devices remotely.  
- **Supply Chain Infiltration**: Injecting malicious code into trusted package repositories (npm/PyPI) to distribute malware at scale.  
- **Browser Extension Exploits**: Tricking users into installing harmful add-ons that harvest credentials and personal data.  
- **Data-Wiping Package Installation**: Masquerading as legitimate utilities to erase files and directories.  
- **Ransomware Exploitation**: Leveraging authentication bypass in network devices to execute payloads and encrypt enterprise systems.

## Threat Actor Activities

- **Mirai Botnet Operators**: Expanding the botnet via DVR command injection to launch large-scale DDoS attacks.  
- **Supply Chain Attackers**: Compromising software distribution channels for npm and PyPI to embed remote access trojans and wipe functionality.  
- **Malicious Extension Developers**: Targeting Latin American users with data-exfiltrating browser plugins.  
- **Qilin Ransomware Group**: Exploiting Fortinet vulnerabilities to deploy ransomware attacks on corporate networks.  
- **Other Botnet and Malware Operators**: Employing destructive or data-stealing tactics, including data wipers and sophisticated phishing campaigns.  