# Exploitation Report

During the last week, security researchers and vendors highlighted several distinct exploitation waves that demand immediate defensive attention. The most critical activity centers on a newly patched zero-day in Microsoft SQL Server that was already being exploited before July 2025 Patch Tuesday, a supply-chain compromise of the Ethcode VS Code extension, and the rapid weaponization of unpatched flaws in TBK DVRs and Four-Faith routers by the emerging “RondoDox” botnet.  Mobile users are simultaneously at risk from the “TapTrap” Android tapjacking technique, while state-sponsored actors such as North Korea’s Andariel and China-aligned Silk Typhoon continue to leverage a mixture of credential theft, social engineering, and legacy vulnerabilities in ongoing campaigns.

## Active Exploitation Details

### Microsoft SQL Server Zero-Day Vulnerability
- **Description**: A previously unknown flaw in Microsoft SQL Server that allows authenticated attackers to execute arbitrary code with SYSTEM-level privileges via crafted SQL queries.
- **Impact**: Full takeover of the underlying Windows host, lateral movement inside enterprise networks, and potential data exfiltration or ransomware deployment.
- **Status**: Actively exploited in the wild; a patch was shipped in the July 2025 Patch Tuesday release. Administrators must apply the latest cumulative updates immediately.

### TapTrap Android UI Tapjacking Vulnerability
- **Description**: A logic flaw in Android’s animation and overlay handling enables invisible UI layers that trick users into granting dangerous permissions or initiating harmful actions.
- **Impact**: Attackers can silently enable accessibility services, install additional malware, steal sensitive data, or perform destructive operations without clear user consent.
- **Status**: Being exploited by threat actors; no vendor patch yet. Mitigations include disabling “Display over other apps” for unknown applications and enforcing mobile threat-defense controls.

### Ethcode VS Code Extension Supply-Chain Vulnerability
- **Description**: Attackers submitted a malicious pull request to the Ethcode open-source repository, poisoning the build pipeline and distributing a trojanized extension through the VS Code Marketplace.
- **Impact**: Developers who installed or updated Ethcode executed attacker-supplied JavaScript capable of credential theft, wallet draining, and arbitrary command execution.
- **Status**: Malicious version has been removed, but compromised installations persist. Users should validate checksums, reinstall from a trusted source, and rotate exposed secrets.

### TBK Digital Video Recorder (DVR) Flaw Exploited by RondoDox
- **Description**: An authentication-bypass vulnerability in multiple TBK DVR firmware versions allows unauthenticated remote commands over HTTP.
- **Impact**: RondoDox operators enlist DVRs into a DDoS botnet, leveraging their bandwidth for high-volume attacks against external targets.
- **Status**: No vendor patch available; recommended actions include network isolation, disabling remote access, and deploying custom IPS signatures.

### Four-Faith Industrial Router Command-Injection Flaw
- **Description**: Input validation weaknesses in Four-Faith router web interfaces permit shell command injection via crafted parameters.
- **Impact**: Full device compromise leading to botnet enrollment, traffic proxying, or pivoting into industrial control networks.
- **Status**: Actively exploited alongside the TBK DVR flaw by RondoDox. Firmware updates are not yet published; users should restrict management access to trusted subnets only.

## Affected Systems and Products

- **Microsoft SQL Server**: Supported on-premises and cloud deployments (2016 through 2022) prior to July 2025 security updates  
- **Android Smartphones/Tablets**: Devices running Android 12–14 with default overlay permissions enabled  
- **Ethcode VS Code Extension**: All marketplace builds prior to the clean re-release on 9 July 2025  
- **TBK DVR Series**: Models using legacy web firmware ≤ v3.4.10, commonly installed in CCTV deployments  
- **Four-Faith Industrial Routers**: F-NR100, F-G100, and derivative models running firmware ≤ v2.0.6  

## Attack Vectors and Techniques

- **SQL Network RCE**  
  - **Vector**: Crafted SQL queries over port 1433 exploit the server-side logic flaw to drop malicious DLLs and run them as SYSTEM.

- **TapTrap Tapjacking**  
  - **Vector**: Malicious apps overlay transparent animations over legitimate dialogs, capturing user taps to approve sensitive permissions.

- **Malicious Pull Request & Dependency Confusion**  
  - **Vector**: Compromised CI/CD pipeline inserts backdoored code into the Ethcode extension; automatic updates deliver the payload to developers.

- **IoT Authentication Bypass & Command Injection**  
  - **Vector**: RondoDox botnet scanners locate internet-exposed DVRs/routers, send unauthenticated HTTP requests or injected parameters to gain shell access.

## Threat Actor Activities

- **Andariel (North Korea)**  
  - **Campaign**: Fraudulent IT-worker scheme combined with remote-access malware; monetization via theft of crypto and dollar-denominated wages.

- **Silk Typhoon (China-aligned)**  
  - **Campaign**: Long-term espionage against U.S. organizations; recent arrest of Xu Zewei ties group to credential theft and post-exploitation tooling.

- **RondoDox Operators (Unattributed)**  
  - **Campaign**: Rapid expansion of a DDoS botnet by exploiting TBK DVR and Four-Faith router flaws; observed targeting of gambling and fintech sites.

- **Unknown Supply-Chain Actor (Ethcode)**  
  - **Campaign**: Targeted developers in blockchain and DeFi sectors; objective appears to be theft of private keys and repository access tokens.

- **TapTrap Actors (Mobile Threat Group)**  
  - **Campaign**: Distributed through side-loaded apps and third-party stores; focused on harvesting SMS 2FA codes and banking credentials from victims in Europe and North America.

---

Security teams should prioritize patching or mitigating the listed vulnerabilities, perform IoC sweeps for RondoDox and Ethcode compromise artifacts, and harden Android device policies against overlay abuse.