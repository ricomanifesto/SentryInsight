# Exploitation Report

Recent reporting highlights a surge in practical exploitation techniques rather than classic software bugs alone. Low-privilege data enumeration in ServiceNow, unpatched remote-code-execution flaws in Ruckus Networks’ management controllers, a novel Android “TapTrap” UI-overlay attack, and real-time MFA-bypass phishing kits all demonstrate how threat actors are combining misconfigurations, design weaknesses, and social-engineering tradecraft to achieve compromise. Concurrently, ransomware crews (SafePay, DragonForce) and APT groups such as Andariel and DoNot are actively weaponizing these weaknesses to steal data and gain persistent access to enterprise environments.

## Active Exploitation Details

### Count(er) Strike – ServiceNow Data Enumeration Flaw
- **Description**: A logic flaw lets any authenticated but low-privileged ServiceNow user craft table API requests that return row counts for restricted tables. By iterating requests, an attacker can infer sensitive data values and relationships.
- **Impact**: Stealthy exfiltration of confidential records (customer PII, incident tickets, financial information) without direct table access; can be chained with other weaknesses for privilege escalation.
- **Status**: Public disclosure with working proof-of-concept code; researchers observed exploitation attempts in customer environments. ServiceNow has issued mitigation guidance while a permanent fix is in development.

### Unpatched Ruckus Wireless Management Device Vulnerabilities
- **Description**: Multiple critical flaws in SmartZone network controllers, ZoneDirector appliances, and their accompanying APIs allow unauthenticated command execution, credential leakage, and full device takeover.
- **Impact**: Full compromise of Wi-Fi infrastructure, lateral movement into wired networks, unauthorized firmware deployment, and persistent man-in-the-middle positioning.
- **Status**: No vendor patches available at publication time. Exploit details were released by researchers, and scanning activity against Internet-exposed devices has been observed.

### TapTrap Android Permission-Bypass Technique
- **Description**: A tapjacking method abuses animation frame delays to overlay invisible UI elements on legitimate app screens, tricking users into granting permissions or executing actions they cannot see.
- **Impact**: Silent enabling of accessibility services, installation of malicious APKs, or initiation of destructive operations (e.g., factory reset, data exfiltration).
- **Status**: Proof-of-concept exploits demonstrated in the wild against older and fully-patched Android 13/14 builds; Google is assessing remediation options.

### Real-Time MFA Phishing Kits (Legacy Authenticator Bypass)
- **Description**: Adversary-in-the-middle (AitM) kits proxy login flows, capture session cookies, and relay time-based one-time passwords (TOTP) to the legitimate IdP in real time, defeating app-based MFA.
- **Impact**: Immediate hijack of authenticated sessions, enabling email takeover, cloud resource compromise, and fraudulent financial transactions.
- **Status**: Commercially available on dark markets; multiple ransomware crews leverage the kits during initial access operations. No vendor patch (design limitation); hardware-bound passkeys and FIDO2 tokens recommended.

## Affected Systems and Products

- **ServiceNow SaaS**: All instances lacking the latest table ACL hardening; any role below system administrator.  
- **Ruckus SmartZone / ZoneDirector**: Unpatched versions of vSZ-H, vSZ-E, SmartZoneOS-based hardware controllers, ZoneDirector 1200/3000 series.  
- **Android (A11 – A14)**: Devices where overlay and accessibility permission policies are unmodified.  
- **Any Web-SSO Platform using TOTP/Push MFA**: Microsoft 365, Google Workspace, Okta, Duo, and on-prem ADFS deployments susceptible to AitM relay.

## Attack Vectors and Techniques

- **API Enumeration Abuse**  
  - **Vector**: Crafted ServiceNow sysparm_count requests enumerate restricted table data.

- **Unauthenticated RCE via Management Interface**  
  - **Vector**: Direct HTTP/HTTPS calls to vulnerable Ruckus controller endpoints execute shell commands as root.

- **UI Overlay (TapTrap)**  
  - **Vector**: Malicious app draws 0-opacity views timed between animation frames to capture taps.

- **Adversary-in-the-Middle MFA Relay**  
  - **Vector**: Phishing site proxies authentication traffic, captures TOTP/push approvals, and replays tokens to IdP.

## Threat Actor Activities

- **Andariel (North Korea)**  
  - **Campaign**: Revenue-generation via fraudulent IT-worker accounts; sanctions note malware-enabled access to U.S. networks and possible use of MFA bypass tooling.

- **DoNot APT**  
  - **Campaign**: “LoptikMod” malware deployed against European foreign ministries; leverages social-engineering and potential ServiceNow enumeration for reconnaissance.

- **SafePay Ransomware (Ingram Micro)**  
  - **Activities**: Leveraged real-time MFA phishing to breach corporate VPN, encrypt internal servers, disrupt logistics.

- **DragonForce Ransomware (M&S breach)**  
  - **Activities**: Sophisticated impersonation (deepfake voice & text) enabled initial access; lateral movement suspected through unpatched Ruckus Wi-Fi controllers.

- **Commodity Botnets & Proxy Services**  
  - **Activities**: Mass scanning of Ruckus management ports following public disclosure; opportunistic compromise attempts observed in honeypots within 24 hours.

- **Deepfake Social-Engineering Operators**  
  - **Campaign**: High-fidelity voice clones used to impersonate diplomats (e.g., “Rubio impersonator”) to elicit credential resets and MFA push approvals.

---

Stay vigilant for emerging exploit code and apply vendor work-arounds or compensating controls immediately where patches are not yet available.