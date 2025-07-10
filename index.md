# Exploitation Report

A cluster of new and ongoing attacks highlights how quickly threat actors pivot from novel zero-days to misconfiguration abuse and supply-chain tampering. The most pressing activity observed over the last week includes a still-unpatched Microsoft Exchange zero-day weaponized by a North-American APT against Chinese entities, large-scale abuse of leaked ASP.NET machine keys by the Gold Melody initial-access broker, and a surge in developer-focused macOS infections delivered through a trojanized copy of the Termius SSH client carrying the ZuRu malware family. Collectively, these operations enable remote code execution, full application take-over, and wide-ranging data exfiltration across on-premises, cloud, and endpoint environments.

## Active Exploitation Details

### Microsoft Exchange Zero-Day
- **Description**: An undisclosed vulnerability in Microsoft Exchange Server that allows unauthenticated remote code execution and mailbox access.  
- **Impact**: Attackers can implant web shells, steal email, move laterally, and establish persistent footholds inside victim networks.  
- **Status**: Confirmed in-the-wild exploitation by a North-American APT; no official patch released at publication time.  
 
### Leaked ASP.NET Machine-Key Abuse
- **Description**: Gold Melody leverages publicly exposed `machineKey` values to forge authentication cookies and ViewState data, granting administrative sessions in ASP.NET applications.  
- **Impact**: Full takeover of web applications, credential theft, and resale of enterprise access on underground markets.  
- **Status**: Actively exploited; mitigation requires immediate rotation of machine keys and hardening of configuration management.  

### Trojanized Termius macOS App (ZuRu Malware)
- **Description**: A supply-chain attack where a maliciously modified Termius installer sideloads the ZuRu backdoor, bypassing Gatekeeper notarization checks through ad-hoc code-signing.  
- **Impact**: Exfiltration of SSH keys, source code, cloud credentials, and system telemetry from developer workstations.  
- **Status**: Campaign ongoing; no vendor patch required—organizations must validate installer integrity and enforce notarization restrictions.  

## Affected Systems and Products

- **Microsoft Exchange Server 2016 / 2019**  
  - **Platform**: On-premises Windows Server deployments  
- **ASP.NET Web Applications**  
  - **Platform**: Windows IIS; applications using static `machineKey` settings exposed via repos or misconfiguration  
- **Termius SSH Client (macOS Trojanized Build)**  
  - **Platform**: macOS 13 and 14 systems used by software engineers and DevOps staff  

## Attack Vectors and Techniques

- **Zero-Day Remote Code Execution**  
  - **Vector**: Crafted HTTPS requests to Microsoft Exchange endpoints resulting in web-shell deployment.  
- **Machine-Key Forgery**  
  - **Vector**: Downloading leaked `machineKey` values from public repos, then generating valid authentication cookies/ViewState to bypass login.  
- **Supply-Chain Trojanization**  
  - **Vector**: Hosting a repackaged Termius installer on developer forums; installer invokes a malicious payload signed with an ad-hoc certificate, evading Gatekeeper.  

## Threat Actor Activities

- **North-American APT**  
  - **Campaign**: Targeted Chinese government and research networks using the Exchange zero-day; objectives include intelligence collection and email exfiltration.  
- **Gold Melody (Initial Access Broker)**  
  - **Campaign**: Mass-scanning for exposed ASP.NET machine keys, followed by unauthorized access sales to ransomware affiliates.  
- **ZuRu Malware Operators**  
  - **Campaign**: Focusing on software developers and DevSecOps professionals; aims to harvest credentials and proprietary code for later monetization or espionage.