# Exploitation Report

Critical exploitation activity is currently dominated by several high-impact vulnerabilities across multiple sectors. The most concerning developments include active exploitation of a FileZen vulnerability (CVE-2026-25108) confirmed by CISA, critical remote code execution flaws in Zyxel routers and SolarWinds Serv-U, and sophisticated supply chain attacks targeting software developers through malicious packages. Additionally, threat actors are leveraging advanced social engineering techniques, including telephone-oriented attack delivery (TOAD) methods that bypass traditional email security gateways, while the Lazarus Group has been observed deploying Medusa ransomware in targeted attacks against healthcare and Middle Eastern organizations.

## Active Exploitation Details

### FileZen Vulnerability
- **Description**: Recently disclosed vulnerability in FileZen file transfer software
- **Impact**: Active exploitation confirmed by CISA, suggesting significant risk to organizations using this software
- **Status**: CISA has added to Known Exploited Vulnerabilities (KEV) catalog due to confirmed active exploitation
- **CVE ID**: CVE-2026-25108

### Zyxel Router Remote Code Execution Flaw
- **Description**: Critical vulnerability affecting over a dozen Zyxel router models that allows unauthenticated remote command execution
- **Impact**: Attackers can gain complete control of affected routers without authentication
- **Status**: Security updates have been released by Zyxel to address the vulnerability

### SolarWinds Serv-U Critical Flaws
- **Description**: Four critical security vulnerabilities in SolarWinds Serv-U 15.5 file transfer software
- **Impact**: Successful exploitation could result in remote code execution with root privileges on affected servers
- **Status**: Patches have been released by SolarWinds to address all four vulnerabilities

### GitHub Codespaces RoguePilot Flaw
- **Description**: Vulnerability in GitHub Codespaces that could be exploited by injecting malicious Copilot instructions
- **Impact**: Attackers could seize control of repositories and potentially leak GITHUB_TOKEN credentials
- **Status**: Vulnerability has been disclosed and likely addressed

## Affected Systems and Products

- **Zyxel Routers**: Over a dozen router models vulnerable to unauthenticated remote command execution
- **FileZen**: File transfer software actively being exploited in the wild
- **SolarWinds Serv-U 15.5**: File transfer software with four critical remote code execution vulnerabilities
- **GitHub Codespaces**: Development environment vulnerable to malicious instruction injection
- **NuGet Packages**: Four malicious packages targeting ASP.NET web application developers
- **npm Packages**: Malicious packages designed to drop malware on developer systems
- **Windows 11**: Systems receiving security updates through KB5077241

## Attack Vectors and Techniques

- **Telephone-Oriented Attack Delivery (TOAD)**: Attackers bypass email gateways by including only phone numbers in emails, using social engineering over phone calls
- **Supply Chain Attacks**: Malicious packages uploaded to NuGet and npm repositories to target software developers
- **Unauthenticated Remote Code Execution**: Direct exploitation of network-accessible services without authentication requirements
- **Social Engineering**: Sophisticated campaigns targeting freight and logistics organizations using spoofed domains
- **Malicious Google Ads**: Use of 1Campaign platform to run persistent malicious advertisements that evade detection
- **Repository Control**: Injection of malicious instructions into GitHub Copilot to gain repository access

## Threat Actor Activities

- **Lazarus Group**: North Korean state-backed hackers deploying Medusa ransomware against U.S. healthcare organizations and Middle Eastern entities, also using Comebacker backdoor, Blindingcan RAT, and Infohook stealer
- **ShinyHunters**: Extortion gang responsible for multiple data breaches including Wynn Resorts, CarGurus (12.4 million accounts), and claims of breaching Dutch telecommunications provider Odido
- **Diesel Vortex**: Financially motivated threat group targeting freight and logistics operators in the U.S. and Europe using 52 domains for phishing attacks
- **UAC-0050**: Russia-aligned threat actor conducting social engineering attacks against European financial institutions using spoofed domains and RMS malware
- **Russian Exploit Broker**: Recently sanctioned individual who purchased eight zero-day exploits from a former L3Harris defense contractor employee
- **OpenClaw Campaign**: Supply chain attack generating significant discussion on Telegram and dark web platforms, though showing more research interest than mass exploitation