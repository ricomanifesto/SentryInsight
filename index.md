# Exploitation Report

Recent reporting highlights a diverse set of active exploitation campaigns ranging from firmware-level attacks on Gigabyte motherboards to novel prompt-injection flaws in Google Gemini. Threat actors are abusing default credentials, poisoned software-supply-chain artifacts, and Secure-Boot bypasses to gain persistence, steal data, and deploy ransomware. Particularly notable are North Korean operators seeding 67 malicious npm packages with the XORIndex loader, the “Diskstation” ransomware crew exploiting NAS devices across Europe, and wide-scale deployment of Interlock’s new “FileFix” technique for RAT delivery. Defensive teams should prioritise firmware patching, AI-prompt hardening, supply-chain integrity monitoring, and credential hygiene to counter these currently observed attacks.

## Active Exploitation Details

### Gigabyte UEFI Secure Boot Bypass Vulnerabilities
- **Description**: Multiple security issues in Gigabyte motherboard UEFI firmware allow the installation of bootkit malware that executes before the operating system and persists across re-installation, effectively bypassing Secure Boot protections.  
- **Impact**: Full device compromise with kernel-level persistence, invisibility to OS-level security tools, and ability to implant additional payloads.  
- **Status**: Actively exploited in the wild to deploy stealth bootkits; firmware updates are being released by Gigabyte, but many systems remain unpatched.

### Google Gemini Prompt-Injection Flaw
- **Description**: An input-validation weakness lets attackers craft “invisible” or obfuscated prompts masquerading as legitimate Google Security alerts, hijacking Gemini’s response logic.  
- **Impact**: Users can be socially engineered into divulging credentials or executing malicious actions while believing they are following genuine security guidance.  
- **Status**: Exploitation observed in phishing-style campaigns. Mitigations are rolling out on Google’s side, but no client-side patch is available yet.

### McDonald’s McHire Default-Credential Exposure
- **Description**: The McHire recruiting platform was left running with its factory-default administrator credentials, exposing backend resources and approximately 64 million job-applicant records.  
- **Impact**: Unauthorised attackers could access or exfiltrate large volumes of personally identifiable information (PII) and potentially inject malicious code into the application workflow.  
- **Status**: Credentials have now been reset and the instance hardened, but data theft already occurred.

### XORIndex Supply-Chain Attack on npm
- **Description**: North Korean threat actors published 67 malicious npm packages that install a new loader dubbed “XORIndex” during package installation.  
- **Impact**: Developer workstations become initial footholds, enabling remote command execution, credential theft, and subsequent lateral movement into corporate environments.  
- **Status**: Packages have been removed, but clones and forks continue to appear; downstream projects that pulled the packages remain at risk.

### “Diskstation” NAS Exploitation
- **Description**: A Romanian ransomware group targeted network-attached storage (NAS) devices, abusing exposed services and unpatched firmware flaws to deploy a custom ransomware strain.  
- **Impact**: Encrypted corporate backups and production file shares, causing significant business disruption.  
- **Status**: International law-enforcement operation dismantled core infrastructure, but victims must still remediate vulnerable NAS installations.

### Interlock “FileFix” Delivery Mechanism
- **Description**: The Interlock ransomware group weaponised a new technique named “FileFix,” leveraging manipulated download prompts and legitimate web injections to drop a PHP-based variant of its bespoke RAT.  
- **Impact**: Remote access, data theft, and follow-on ransomware deployment against multiple industry sectors.  
- **Status**: Campaigns are ongoing; no vendor patches apply, but hardening download controls and web-application firewalls reduces exposure.

## Affected Systems and Products

- **Gigabyte Motherboards**: Numerous Intel and AMD consumer- and enterprise-grade boards running vulnerable UEFI firmware versions  
  - **Platform**: Windows and Linux systems relying on affected firmware  
- **Google Gemini AI Assistant**: Gemini integrations across Gmail, Google Chat, and web/mobile clients  
  - **Platform**: Web browsers, Android, iOS  
- **McHire Recruiting Platform (McDonald’s)**: Cloud-hosted hiring application instances with unchanged default credentials  
  - **Platform**: Public-facing web application  
- **npm Ecosystem**: Projects that included any of the 67 malicious packages (cross-platform JavaScript/Node.js environments)  
  - **Platform**: Developer workstations (Windows, macOS, Linux) and CI/CD pipelines  
- **Synology and Other NAS Devices**: DiskStation Manager (DSM) versions lacking recent security updates or exposing management services to the Internet  
  - **Platform**: Network-attached storage appliances  
- **Enterprise Web Servers Hosting “FileFix” Payloads**: Legitimate sites compromised to serve malicious PHP-based Interlock RAT installers  
  - **Platform**: Apache/Nginx on Linux and Windows IIS servers

## Attack Vectors and Techniques

- **UEFI Bootkit Implantation**  
  - **Vector**: Direct firmware flashing or exploitation of insecure update mechanisms to write malicious code into the SPI flash region.  
- **Invisible Prompt Injection**  
  - **Vector**: Special Unicode characters, styling tricks, or hidden-text segments embedded in emails/chats to alter Gemini instructions.  
- **Default-Credential Abuse**  
  - **Vector**: Automated scanning for internet-reachable services (e.g., McHire) using factory usernames/passwords.  
- **Supply-Chain Poisoning (npm)**  
  - **Vector**: Publishing typosquatted or dependency-confused packages that execute post-install scripts.  
- **Ransomware via Exposed NAS Services**  
  - **Vector**: Brute-forcing weak NAS credentials or exploiting outdated DSM vulnerabilities over SMB/SSH/WebDAV.  
- **FileFix Drive-By Download**  
  - **Vector**: Injected JavaScript on compromised sites presents a deceptive “file fixer” prompt, tricking users into executing a RAT installer.

## Threat Actor Activities

- **North Korean Operators (XORIndex Campaign)**  
  - **Campaign**: Continual seeding of malicious npm packages targeting developers in tech and crypto sectors to establish footholds for espionage.  

- **“Diskstation” Ransomware Gang**  
  - **Campaign**: Targeted small-to-medium businesses in Italy’s Lombardy region, encrypting NAS-hosted data; infrastructure seized by law enforcement, but variant may resurface.  

- **Interlock Ransomware Group**  
  - **Campaign**: Widespread FileFix-based web-inject operation distributing new PHP Interlock RAT; observed across manufacturing, healthcare, and finance verticals.  

- **Unknown State-Backed APT (HazyBeacon)**  
  - **Campaign**: Espionage against Southeast Asian government entities using AWS Lambda for covert C2; leverages cloud service abuse rather than specific software flaws.  

- **Miscellaneous Cybercriminals**  
  - **Campaign**: Opportunistic exploitation of McHire default credentials and Gigabyte firmware weaknesses for data theft and stealth persistence, respectively.

