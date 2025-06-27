# Exploitation Report

During the past week, defenders observed a sharp rise in real-world exploitation of enterprise-grade remote-access and file-transfer platforms.  The most urgent concern is a new memory-leak vulnerability dubbed **“Citrix Bleed 2” (CVE-2025-5777)** in NetScaler ADC/Gateway appliances, now confirmed to be weaponised in the wild and reminiscent of Heartbleed-style credential harvesting.  At the same time, scanners are again sweeping the Internet for unpatched Progress MOVEit Transfer instances, foreshadowing another round of data-theft campaigns similar to last year’s mass extortions.  Parallel spear-phishing and supply-chain attacks by Chinese actors Mustang Panda and Silver Fox, abuse of Microsoft 365 “Direct Send” for internal-looking phishing, and new ClickOnce/Golang backdoor deployments against the energy sector round out an increasingly aggressive threat landscape.

## Active Exploitation Details

### Citrix Bleed 2 – NetScaler ADC/Gateway Memory-Leak
- **Description**: A bounds-check failure allows unauthenticated attackers to extract chunks of memory from vulnerable NetScaler ADC and Gateway appliances, exposing session cookies, credentials, and other sensitive data over HTTPS.  
- **Impact**: Credential theft leads to full VPN or application gateway compromise, lateral movement, and potential breach of internal systems.  
- **Status**: ReliaQuest telemetry shows live exploitation against Internet-facing devices.  Citrix has released patched builds; mitigation requires urgent upgrade and session revocation.  
- **CVE ID**: CVE-2025-5777  

### MOVEit Transfer Pre-Auth Vulnerabilities (SQLi / RCE)
- **Description**: A set of pre-authentication SQL-injection flaws in Progress MOVEit Transfer permit database exfiltration and remote code execution.  
- **Impact**: Attackers can steal files stored in MOVEit, add new admin users, or run arbitrary code on the underlying Windows server, enabling large-scale data theft and ransomware deployment.  
- **Status**: GreyNoise reports a “notable surge” in global scanning beginning 27 May 2025, indicating renewed exploit activity against still-unpatched instances.  Vendor patches are available and should be applied immediately.  

### Microsoft 365 “Direct Send” Internal-Phishing Abuse
- **Description**: Threat actors leverage the little-known “Direct Send” feature to relay messages through a customer’s Microsoft 365 SMTP endpoint without authentication safeguards, making malicious emails appear as legitimate internal traffic.  
- **Impact**: High-success credential-phishing that bypasses external-sender warnings and many secure email gateways, leading to account takeover and BEC.  
- **Status**: Campaign ongoing; Microsoft guidance recommends disabling Direct Send where not required and enforcing MFA plus transport rules.  

## Affected Systems and Products

- **NetScaler ADC / Gateway**: Appliances running vulnerable builds prior to fixed versions 13.1-xx.x, 14.0-xx.x  
  - **Platform**: On-prem or cloud-hosted NetScaler deployments terminating VPN, ICA, or reverse-proxy traffic  

- **Progress MOVEit Transfer**: All on-prem releases prior to latest cumulative hotfix  
  - **Platform**: Windows Server installations exposed to the Internet  

- **Microsoft 365 Tenants** with “Direct Send” (SMTP client submission) enabled  
  - **Platform**: Exchange Online; affects all major OS/email clients receiving spoofed internal mail  

## Attack Vectors and Techniques

- **Memory-Extraction over TLS**: Repeated HTTPS requests leverage CVE-2025-5777 to leak NetScaler memory buffers containing plaintext session data.  
- **Pre-Auth SQL Injection**: Crafted HTTP POST to MOVEit endpoint inserts SQL commands, enabling data exfiltration and RCE without credentials.  
- **SMTP “Direct Send” Abuse**: Attackers enumerate tenant MX records, authenticate anonymously through customer relay, and spoof internal addresses.  
- **Spear-Phishing with Weaponised Docs**: Mustang Panda distributes PUBLOAD and Pubshell via Tibet-themed lures to compromise activists.  
- **Malvertising & Fake Software Sites**: Silver Fox clones download portals for WPS Office, Sogou, DeepSeek to implant Sainbox RAT and Hidden rootkit.  
- **ClickOnce Deployment Hijack**: OneClik campaign hosts malicious .application manifests, sidestepping SmartScreen, to drop Golang backdoors in energy firms.  
- **Social-Engineering “ClickFix / FileFix”**: Fake CAPTCHA images coerce users into enabling macros or downloading trojanised documents—volume up 517 % YoY.  

## Threat Actor Activities

- **Mustang Panda**  
  - **Campaign**: Tibet-focused espionage using PUBLOAD loader and Pubshell backdoor; phishing emails reference cultural and political topics.  

- **Silver Fox**  
  - **Campaign**: Supply-chain poisoning via counterfeit software sites; delivers Sainbox RAT and Hidden rootkit to Chinese-language users.  

- **ReliaQuest-Observed Actors**  
  - **Campaign**: Opportunistic exploitation of CVE-2025-5777 (“Citrix Bleed 2”) across finance, healthcare, and tech verticals.  

- **GreyNoise-Tracked Scanners**  
  - **Campaign**: Automated enumeration of MOVEit Transfer endpoints ahead of anticipated data-extortion wave.  

- **Energy-Sector Intrusion Set (“OneClik”)**  
  - **Campaign**: Uses ClickOnce and bespoke Golang payloads for foothold in OT/IT networks, followed by credential dumping and persistence.  

- **Hacktivist Group “Cyber Fattah”**  
  - **Campaign**: Data-leak operations against Saudi entities amid regional tensions; leveraging public exploit kits for initial access.  

- **Scattered Spider**  
  - **Campaign**: Shift from retail to U.S. insurance carriers; combines SIM-swapping, MFA fatigue, and off-the-shelf remote-admin tools for ransomware-as-a-service facilitation.  

Security teams should prioritise patching NetScaler appliances and MOVEit Transfer servers, audit Microsoft 365 SMTP configurations, and reinforce user awareness against sophisticated phishing and malvertising tactics now proliferating across multiple threat actor sets.