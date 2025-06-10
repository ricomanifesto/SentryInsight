# Exploitation Report

Recent security articles have highlighted significant exploitation activity, particularly focusing on a critical remote code execution vulnerability in Roundcube (CVE-2025-49113) that is actively being exploited. Additionally, Microsoft has addressed an exploited zero-day vulnerability during their June 2025 Patch Tuesday, alongside numerous other flaws. The threat landscape is further complicated by the activities of various threat actor groups, including FIN6 and the Rare Werewolf APT, who are employing sophisticated techniques to compromise systems and steal sensitive data.

## Active Exploitation Details

### Roundcube Remote Code Execution Vulnerability
- **Description**: A critical remote code execution vulnerability in Roundcube webmail software that allows attackers to execute arbitrary code on the server.
- **Impact**: Successful exploitation can lead to full server compromise, allowing attackers to access sensitive data and potentially pivot to other systems within the network.
- **Status**: Actively exploited with a publicly available exploit. Organizations are urged to patch their systems immediately.
- **CVE ID**: CVE-2025-49113

### Microsoft Zero-Day Vulnerability
- **Description**: A zero-day vulnerability that was actively exploited prior to the June 2025 Patch Tuesday.
- **Impact**: Attackers could leverage this vulnerability to gain unauthorized access or execute malicious code on affected systems.
- **Status**: Addressed in the June 2025 Patch Tuesday updates, but details on the specific CVE ID were not disclosed.

## Affected Systems and Products

- **Roundcube Webmail**: All versions prior to the patch addressing CVE-2025-49113.
- **Microsoft Windows**: Various versions affected by the zero-day vulnerability addressed in the June 2025 updates.

## Attack Vectors and Techniques

- **Remote Code Execution**: Attackers exploit the Roundcube vulnerability to execute arbitrary code on the server.
- **Phishing and Social Engineering**: FIN6 has been observed using fake resumes to deliver malware, targeting recruiters and job seekers.

## Threat Actor Activities

- **Actor/Group**: FIN6
  - **Activities**: Leveraging fake resumes hosted on AWS to deliver the More_eggs malware, targeting individuals in recruitment processes.
  - **Campaign**: This operation aims to backdoor recruiters’ devices, facilitating further attacks on their networks.

- **Actor/Group**: Rare Werewolf APT
  - **Activities**: Targeting hundreds of Russian enterprises using legitimate software to evade detection while stealing data.
  - **Campaign**: Focused on espionage and data theft within the Commonwealth of Independent States (CIS).

This report underscores the critical need for organizations to remain vigilant and proactive in their cybersecurity measures, particularly in light of the active exploitation of vulnerabilities and the sophisticated tactics employed by threat actors.