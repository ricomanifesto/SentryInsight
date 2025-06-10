# Exploitation Report

Recent cybersecurity activities have highlighted significant exploitation of vulnerabilities, particularly focusing on a zero-day vulnerability addressed by Microsoft in their June 2025 Patch Tuesday. This patch fixed 66 flaws, including one actively exploited vulnerability. Additionally, CISA has added critical flaws in Erlang SSH and Roundcube to its Known Exploited Vulnerabilities Catalog, indicating ongoing exploitation in the wild. The landscape is further complicated by the emergence of new attack vectors and techniques employed by threat actors, including the FIN6 group, which has been leveraging social engineering tactics to deliver malware.

## Active Exploitation Details

### Microsoft Zero-Day Vulnerability
- **Description**: A zero-day vulnerability that was actively exploited before being patched in the June 2025 Patch Tuesday.
- **Impact**: Attackers could potentially execute arbitrary code, leading to unauthorized access and control over affected systems.
- **Status**: The vulnerability has been patched as of June 2025, but exploitation was confirmed prior to the patch release.
- **CVE ID**: Not specified in the articles.

### Erlang SSH Vulnerability
- **Description**: A critical security flaw in the Erlang/Open Telecom Platform (OTP) SSH that allows unauthorized access.
- **Impact**: This vulnerability could enable attackers to gain control over systems running affected versions of Erlang.
- **Status**: Added to CISA's Known Exploited Vulnerabilities Catalog, indicating active exploitation.
- **CVE ID**: Not specified in the articles.

### Roundcube Vulnerability
- **Description**: A critical flaw in Roundcube that could be exploited to gain unauthorized access to sensitive information.
- **Impact**: Attackers could potentially access user data and compromise email accounts.
- **Status**: Also included in CISA's Known Exploited Vulnerabilities Catalog, suggesting ongoing exploitation.
- **CVE ID**: Not specified in the articles.

## Affected Systems and Products

- **Erlang/Open Telecom Platform (OTP)**: Vulnerable versions of Erlang SSH.
- **Roundcube**: Affected versions of the Roundcube webmail client.

## Attack Vectors and Techniques

- **Social Engineering**: FIN6 has been observed using fake resumes hosted on AWS to deliver malware, targeting recruiters and job seekers.
- **Phishing**: The group employs convincing phishing tactics to backdoor devices of recruiters, leveraging social engineering to gain access.

## Threat Actor Activities

- **Actor/Group**: FIN6
  - **Activities**: Leveraging fake resumes and phishing sites to deliver malware, specifically targeting recruiters to gain access to their devices.
  - **Campaign**: The group has been active in delivering the More_eggs malware through social engineering tactics, indicating a shift in their operational methods.

- **Actor/Group**: Rare Werewolf APT
  - **Activities**: Targeting Russian enterprises using legitimate software to conduct cyber attacks.
  - **Campaign**: Engaging in sophisticated attacks that utilize legitimate tools to evade detection while stealing sensitive data.

This report underscores the critical need for organizations to remain vigilant and proactive in patching vulnerabilities and educating employees about social engineering tactics to mitigate risks associated with these active exploitations.