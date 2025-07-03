# Exploitation Report

Over the last week threat hunters have observed a sharp rise in real-world exploitation of critical vulnerabilities spanning enterprise voice infrastructure, secure-access gateways, mainstream browsers, and popular web platforms. Most pressing is Cisco’s revelation of a backdoor root account in Unified Communications Manager, which is already being probed in the wild. Simultaneously, an initial-access broker with links to China is abusing multiple unpatched Ivanti gateway flaws, then “self-patching” compromised appliances to maintain exclusive control. Google has rushed an emergency Chrome update after another zero-day was used for remote code execution, while Citrix, WordPress, and browser security researchers have all disclosed newly exploited weaknesses that enable authentication bypass, full site takeover, and Mark-of-the-Web circumvention. The campaigns are being driven by well-known state-sponsored groups such as North Korea’s BabyShark operators, Russia’s Gamaredon, and a variety of financially motivated actors.

## Active Exploitation Details

### Cisco Unified CM Hardcoded Root SSH Credential
- **Description**: Unified Communications Manager and Session Management Edition contained a static, undocumented root account accessible over SSH.  
- **Impact**: Remote, unauthenticated attackers can obtain full root privileges, allowing complete takeover, call interception, and lateral movement across VoIP infrastructure.  
- **Status**: Actively scanned and exploited; Cisco has issued patches that remove the backdoor account.

### Ivanti Secure Gateway Zero-Days
- **Description**: Multiple unpatched vulnerabilities in Ivanti VPN / gateway appliances are being chained for initial access, including authentication bypass and command execution flaws.  
- **Impact**: Attackers gain privileged shell access, deploy web shells, harvest credentials, and pivot into internal networks.  
- **Status**: Exploitation confirmed; Ivanti has released fixes, but many devices remain unpatched.

### Google Chrome Remote Code Execution Zero-Day
- **Description**: A high-severity memory corruption flaw in the Chrome renderer was leveraged in the wild to execute arbitrary code.  
- **Impact**: Visiting a malicious webpage can result in sandbox escape and full user compromise.  
- **Status**: Google shipped an emergency update for Windows, macOS, and Linux; exploitation continues against out-of-date browsers.

### Citrix NetScaler Authentication Bypass
- **Description**: Recently disclosed flaws in NetScaler ADC and Gateway permit unauthenticated access and denial-of-service attacks.  
- **Impact**: Attackers can bypass login pages, hijack sessions, or render gateways unusable, disrupting remote access for entire organizations.  
- **Status**: Hotfixes available, but early adopters report login breakage, delaying rollout while attacks are ongoing.

### WordPress Forminator Plugin Arbitrary File Deletion
- **Description**: A vulnerability in the Forminator plugin allows unauthenticated users to delete any file on the webserver.  
- **Impact**: File deletion can remove wp-config.php or critical core files, leading to full site takeover and potential arbitrary code upload.  
- **Status**: Exploited in the wild; patched version released in the WordPress plugin repository.

### ClickFix / FileFix Mark-of-the-Web Bypass
- **Description**: Attackers craft HTML files that modern browsers save without a Mark-of-the-Web attribute, defeating built-in protections.  
- **Impact**: Users who download and open the file execute embedded scripts without security prompts, enabling malware delivery.  
- **Status**: Technique observed in active campaigns by North Korean and commodity phishing actors; no vendor patch yet.

## Affected Systems and Products

- **Cisco Unified Communications Manager & Session Management Edition**  
  - Platform: On-premises and virtualized UC environments (all supported releases prior to fixed builds)

- **Ivanti Connect Secure / Policy Secure VPN Gateways**  
  - Platform: Hardware and virtual appliances running vulnerable firmware versions

- **Google Chrome**  
  - Platform: Windows, macOS, Linux prior to the latest stable channel release

- **Citrix NetScaler ADC & NetScaler Gateway**  
  - Platform: On-prem and cloud appliances affected on all major firmware trains before Hotfix roll-outs

- **Forminator WordPress Plugin (< patched release)**  
  - Platform: WordPress sites running the vulnerable plugin, any PHP supported hosting

- **All modern desktop browsers (Edge, Chrome, Firefox) when handling locally saved HTML**  
  - Platform: Windows clients primarily, but technique is browser agnostic

## Attack Vectors and Techniques

- **Backdoor Credential Abuse**  
  - Vector: Remote SSH login using hardcoded root credentials (Cisco Unified CM)

- **Zero-Day Chaining & Self-Patching**  
  - Vector: Exploiting Ivanti gateway flaws for shell access, followed by attacker-applied vendor patches to maintain exclusivity

- **Drive-By RCE**  
  - Vector: Malicious website triggers Chrome memory corruption leading to arbitrary code execution

- **Auth Bypass & DoS**  
  - Vector: Crafted HTTP requests exploit NetScaler flaws to skip authentication or crash the service

- **Unauthenticated File Deletion**  
  - Vector: HTTP POST to vulnerable Forminator endpoint specifying path traversal to critical files

- **Mark-of-the-Web Evasion (ClickFix / FileFix)**  
  - Vector: Social-engineering victims into saving weaponized HTML files lacking MOTW, enabling script execution on open

## Threat Actor Activities

- **Unnamed China-Nexus Initial Access Broker**  
  - Campaign: Exploits Ivanti zero-days, patches appliances post-compromise, then sells access to ransomware affiliates and espionage groups

- **North Korean “BabyShark” Operators**  
  - Campaign: Target Web3 and cryptocurrency firms using NimDoor malware delivered via ClickFix-style MOTW bypass, enabling persistent macOS backdoors

- **Russian APT Gamaredon**  
  - Campaign: Conducts spear-phishing against Ukrainian government networks, leveraging weaponized network drives and rapid lateral movement

- **Silver Fox**  
  - Campaign: Uses DLL sideloading and Gh0stRAT variants disguised as DeepSeek installers to infiltrate Taiwanese organizations

- **Various Commodity Phishers**  
  - Campaign: Weaponize AI tools (Vercel’s v0, generative AI services) to fabricate convincing Okta and Microsoft 365 login pages within seconds, coupled with MOTW bypass methods for payload delivery

- **Bulletproof Hosting Provider “Aeza Group” (Sanctioned)**  
  - Activity: Provides resilient infrastructure to ransomware crews (BianLian, Lumma Stealer), facilitating sustained exploitation operations across the vulnerabilities listed above

These converging exploits highlight the urgent need for immediate patching, layered defenses against MOTW-bypass techniques, and continuous monitoring for anomalous gateway behavior indicative of self-patched compromises.