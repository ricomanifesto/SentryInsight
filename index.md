# Exploitation Report

Recent security articles highlight significant exploitation activity, particularly focusing on a Microsoft RCE zero-day vulnerability that is currently under active attack. Additionally, a new Secure Boot flaw has been disclosed, allowing attackers to install bootkit malware. The June 2025 Patch Tuesday from Microsoft addressed 66 vulnerabilities, including the aforementioned zero-day, emphasizing the urgency for organizations to apply these patches to mitigate risks.

## Active Exploitation Details

### Microsoft RCE Zero-Day
- **Description**: A remote code execution vulnerability in Microsoft products that allows attackers to execute arbitrary code on affected systems.
- **Impact**: Attackers can gain full control over the affected systems, potentially leading to data breaches or further exploitation of the network.
- **Status**: Currently under active exploitation; patches have been released as part of the June 2025 Patch Tuesday.
- **CVE ID**: Not specified in the articles.

### Secure Boot Flaw
- **Description**: A vulnerability that allows attackers to bypass Secure Boot protections, enabling the installation of bootkit malware on PCs and servers.
- **Impact**: This flaw can lead to persistent malware infections that compromise system integrity and confidentiality.
- **Status**: Recently disclosed and patches are available to mitigate the risk.
- **CVE ID**: CVE-2025-3052

## Affected Systems and Products

- **Microsoft Windows Operating Systems**: Various versions affected by the RCE zero-day.
- **Secure Boot Enabled Devices**: PCs and servers utilizing Secure Boot technology.

## Attack Vectors and Techniques

- **Remote Code Execution**: Attackers exploit the RCE vulnerability to execute malicious code remotely.
- **Bootkit Installation**: Utilizing the Secure Boot flaw, attackers can install bootkits that persist even after system reboots.

## Threat Actor Activities

- **Actor/Group**: Stealth Falcon APT
  - **Activities**: Actively exploiting the Microsoft RCE zero-day in the Middle East, targeting organizations for espionage and data theft.
  
- **Actor/Group**: FIN6
  - **Campaign**: Leveraging social engineering tactics, including fake resumes hosted on AWS, to deliver malware and compromise devices of recruiters.

This report underscores the critical need for organizations to remain vigilant and proactive in applying security updates and monitoring for signs of exploitation.