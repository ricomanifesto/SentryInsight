# Exploitation Report

Recent security articles have highlighted several critical vulnerabilities currently being exploited in the wild. Notably, a zero-click vulnerability in Microsoft 365 Copilot, dubbed 'EchoLeak', allows attackers to exfiltrate sensitive data without user interaction. Additionally, a zero-day vulnerability in Windows WebDAV has been actively exploited by the APT group Stealth Falcon, targeting defense and government organizations. Furthermore, a newly disclosed Secure Boot flaw (CVE-2025-3052) poses a significant risk by enabling the installation of bootkit malware. These vulnerabilities underscore the urgent need for organizations to apply patches and enhance their security measures.

## Active Exploitation Details

### EchoLeak (Microsoft 365 Copilot)
- **Description**: A zero-click vulnerability that allows attackers to exfiltrate sensitive data from Microsoft 365 Copilot without any user interaction.
- **Impact**: Attackers can access and extract sensitive user data from the application context, potentially leading to data breaches.
- **Status**: Currently under active exploitation; no patch has been mentioned yet.

### Windows WebDAV Zero-Day
- **Description**: A remote code execution (RCE) vulnerability in the Windows WebDAV service that has been exploited since March 2025.
- **Impact**: Attackers can execute arbitrary code on vulnerable systems, allowing them to deploy malware or gain unauthorized access.
- **Status**: Actively exploited in the wild; Microsoft has released patches as part of their June 2025 updates.

### Secure Boot Flaw
- **Description**: A vulnerability that allows attackers to bypass Secure Boot protections, enabling the installation of bootkit malware.
- **Impact**: Successful exploitation can lead to persistent malware installation, compromising the integrity of the operating system.
- **Status**: Recently disclosed and actively being exploited; tracked as CVE-2025-3052, with patches available.

## Affected Systems and Products

- **Microsoft 365 Copilot**: All versions susceptible to the EchoLeak vulnerability.
- **Windows Operating Systems**: Specifically, versions affected by the WebDAV zero-day and Secure Boot flaw.
- **Wazuh Security Platform**: Vulnerable to exploitation by Mirai botnets.

## Attack Vectors and Techniques

- **Zero-Click Attack**: The EchoLeak vulnerability allows data exfiltration without user interaction, making it particularly dangerous as it requires no action from the victim.
- **Remote Code Execution**: The Windows WebDAV vulnerability enables attackers to execute arbitrary code remotely, often through crafted requests.
- **Bootkit Installation**: The Secure Boot flaw allows attackers to disable security features and install persistent malware.

## Threat Actor Activities

- **Stealth Falcon APT Group**: This group has been observed exploiting the Windows WebDAV zero-day to target defense and government organizations in the Middle East.
- **Mirai Botnets**: These botnets are actively exploiting vulnerabilities in the Wazuh Security Platform, showcasing a trend of rapid exploitation following the disclosure of new vulnerabilities.
- **Former Black Basta Members**: Engaging in phishing campaigns using Microsoft Teams and email bombing to establish persistent access to targeted networks.

This report highlights the critical vulnerabilities currently being exploited and the associated risks, emphasizing the importance of timely patching and proactive security measures.