# Exploitation Report

Recent security intelligence highlights two critical vulnerabilities under active exploitation: one affecting Roundcube webmail and another targeting ConnectWise ScreenConnect deployments. Attackers are leveraging these flaws to gain unauthorized access and, in some cases, achieve remote code execution. Alongside these vulnerabilities, multiple threat actors and malware campaigns continue to expand their tactics, targeting a range of industries and government organizations worldwide.

## Active Exploitation Details

### Roundcube Remote Code Execution Vulnerability
- **Description**: A critical flaw in the Roundcube webmail platform that allows attackers to execute arbitrary code remotely when exploited. Attackers have publicly disclosed technical details and are actively offering exploit kits for purchase.
- **Impact**: Successful exploitation grants full control of the underlying server, enabling data theft, lateral movement, or deployment of additional malware.
- **Status**: Actively exploited in the wild, with patches and updates available from the Roundcube project.
- **CVE ID**: CVE-2025-49113

### ConnectWise ScreenConnect Flaw
- **Description**: An undisclosed vulnerability in ConnectWise’s remote support and management software (“ScreenConnect”) that attackers have leveraged in ongoing campaigns. ConnectWise issued a patch but has not fully disclosed the technical details.
- **Impact**: Allows threat actors to gain unauthorized access to managed endpoints, potentially leading to system compromise and data exfiltration.
- **Status**: Confirmed in active attacks; security updates are available from ConnectWise.

## Affected Systems and Products

- **Roundcube Webmail**: Deployments running the vulnerable version allowing remote code execution exploits  
  • Platform: Typically self-hosted Linux/UNIX servers or shared hosting environments

- **ConnectWise ScreenConnect**: Remote support and management installations where the unpatched flaw can be used to hijack remote sessions  
  • Platform: Windows-based remote management software, potentially expanded to multi-OS environments

## Attack Vectors and Techniques

- **Remote Code Execution via Webmail**: Attackers send maliciously crafted requests or payloads targeting Roundcube’s vulnerable components  
  • Vector: Exploitation through publicly facing Roundcube instances

- **Unauthorized Remote Access in Remote Management Tools**: Threat actors exploit weaknesses in ConnectWise ScreenConnect to gain privileged access  
  • Vector: Use of unpatched installations and potentially stolen admin credentials

## Threat Actor Activities

- **Bitter APT**: Continues to evolve, expanding geographic targets while pursuing espionage campaigns  
  • Campaign: Intelligence gathering aimed at government agencies across multiple regions

- **BladedFeline (Iran-Linked)**: Maintains extended presence in compromised networks for espionage and data theft  
  • Campaign: Targeting Iraqi and Kurdish entities using Whisper and Spearal malware

- **BADBOX 2.0 Malware Operators**: Infecting consumer Android devices to build large-scale proxy botnets  
  • Campaign: More than a million devices co-opted and leveraged for malicious activities

- **PathWiper Attackers**: Launched disruptive cyberattacks on critical Ukrainian infrastructure  
  • Campaign: Destructive wiper malware campaigns to degrade operational capacity

- **Backdoored Malware Syndicates**: Luring inexperienced cybercriminals with trojanized tools on GitHub  
  • Campaign: Distributing malicious “how-to” kits that secretly provide access back to the malware authors

- **BidenCash Carding Marketplace**: DoJ led takedown of domains and funds linked to illicit carding operations  
  • Campaign: Global law enforcement collaboration shutting down stolen credit card sales

- **ViLE Gang**: Indicted for breaching a federal law enforcement portal and extorting victims  
  • Campaign: Exploited system flaws to gain access to restricted data and demanded ransoms

- **Interlock Ransomware**: Claims credit for compromising healthcare provider Kettering Health  
  • Campaign: Data exfiltration and extortion, threatening public exposure of stolen information

- **RedLine Infostealer Operators**: Facing $10M reward bounties for information on state-sponsored hackers using the malware  
  • Campaign: Credential theft across various platforms, aiming for large-scale financial and espionage gains