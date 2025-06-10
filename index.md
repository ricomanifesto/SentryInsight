# Exploitation Report

Recent threat intelligence indicates ongoing exploitation of critical vulnerabilities and active threat actor operations. Attackers target unpatched systems and employ creative social engineering tactics, highlighting the importance of timely updates and vigilant security measures. Notably, a zero-day in Microsoft products has been actively exploited in the wild, while newly disclosed weaknesses in Roundcube Webmail continue to be leveraged by attackers at scale. Threat groups like FIN6 and Rare Werewolf also demonstrate sophisticated campaigns targeting enterprises worldwide.

## Active Exploitation Details

### Microsoft Windows Zero-Day
- **Description**: A critical flaw addressed in the June 2025 Patch Tuesday update allowing adversaries to remotely compromise Windows systems.  
- **Impact**: Successful exploitation can grant attackers the ability to execute arbitrary code, elevate privileges, or gain unauthorized system access.  
- **Status**: Actively exploited prior to patch release; fixes now available in cumulative Windows updates.  

### Roundcube Critical RCE
- **Description**: A remote code execution vulnerability in Roundcube Webmail software that attackers exploit by sending specially crafted requests or messages to unpatched instances.  
- **Impact**: Attackers can run arbitrary commands on the hosting server, potentially leading to total system compromise.  
- **Status**: Documented as actively exploited with a publicly available exploit; patches are available from the vendor.  
- **CVE ID**: CVE-2025-49113  

### Erlang/OTP SSH Vulnerability
- **Description**: A critical flaw in Erlang/Open Telecom Platform (OTP) SSH that allows malicious actors to leverage SSH connections for unauthorized access or further lateral movement.  
- **Impact**: Compromise of SSH services can enable full control over affected systems, including data theft and persistent footholds.  
- **Status**: Added to CISA’s Known Exploited Vulnerabilities Catalog; security updates and mitigations are available.  

## Affected Systems and Products

- **Microsoft Windows (10, 11, and Server)**: Specifically impacted by a zero-day addressed in June 2025 updates  
- **Roundcube Webmail**: Vulnerable to remote code execution in unpatched versions  
- **Erlang/Open Telecom Platform (OTP) SSH**: Critical flaw in the SSH implementation affecting Erlang-based systems  

## Attack Vectors and Techniques

- **Fake Resume Phishing**: Threat actors leverage fraudulent job application documents (e.g., FIN6) to deliver malware via cloud-hosted files  
- **Malicious npm Packages**: Poisoned repositories disguised as utilities that can destroy critical files or systems  
- **Publicly Available Exploits**: Attackers capitalize on remote code execution flaws in webmail or web-facing apps (e.g., Roundcube)  
- **Legitimate Software Abuse**: Use of official tools and platforms (e.g., Erlang/OTP SSH) for stealth and persistence  

## Threat Actor Activities

- **FIN6**  
  - Campaign: Embedding malware (More_eggs) in AWS-hosted files shared on LinkedIn; targeting recruiters through fake resumes  

- **Rare Werewolf**  
  - Campaign: Employing legitimate software in cyberattacks on Russian and CIS organizations, focusing on stealth and lateral movement  

- **Librarian Ghouls**  
  - Campaign: Conducting nighttime operations against Russian targets, installing cryptominers and exfiltrating data  

- **Arkana Security Extortion Gang**  
  - Campaign: Briefly relisting previously stolen Ticketmaster data from earlier Snowflake-based attacks  

- **Nation-State Threat Actors on ChatGPT**  
  - Campaign: Exploiting AI-driven social engineering and malicious activities on compromised accounts, prompting OpenAI bans on identified actors  