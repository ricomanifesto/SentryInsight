# Exploitation Report

Multiple critical security incidents are currently impacting global organizations across diverse sectors. North Korean threat actors continue their unprecedented cryptocurrency theft operations, stealing 76% of all crypto assets in 2026. Supply chain attacks targeting popular development packages like PyTorch Lightning and Ruby Gems are enabling widespread credential theft through compromised CI/CD pipelines. A newly discovered Linux privilege escalation vulnerability dubbed "Copy Fail" affects major distributions released since 2017, allowing unprivileged attackers to gain root access. Additionally, sophisticated phishing campaigns are leveraging Google AppSheet services to compromise Facebook accounts, while cybercrime groups are conducting rapid SaaS extortion attacks through voice phishing and SSO abuse techniques.

## Active Exploitation Details

### Copy Fail Linux Privilege Escalation
- **Description**: A local privilege escalation vulnerability affecting Linux kernels released since 2017
- **Impact**: Allows unprivileged local attackers to gain root permissions on major Linux distributions
- **Status**: Exploit code has been published; patches are available

### PyTorch Lightning Supply Chain Compromise
- **Description**: Threat actors compromised the popular Python package Lightning on PyPI to distribute malicious versions
- **Impact**: Credential theft from developers and organizations using the compromised package
- **Status**: Actively exploited with malicious versions pushed to package repository

### Ruby Gems and Go Modules CI Pipeline Exploitation
- **Description**: Sleeper packages in Ruby Gems and Go modules designed to exploit CI/CD pipelines
- **Impact**: Credential theft, GitHub Actions tampering, and supply chain compromise
- **Status**: Active campaign targeting development environments

### Google AppSheet Phishing Relay
- **Description**: Vietnamese-linked operation using Google AppSheet as a phishing relay to distribute malicious emails
- **Impact**: Compromise of approximately 30,000 Facebook accounts
- **Status**: Active campaign leveraging legitimate Google services

### SAP Package Compromise (Mini Shai-Hulud)
- **Description**: TeamPCP threat group compromised multiple npm packages for SAP's cloud application development ecosystem
- **Impact**: Supply chain attacks targeting SAP development environments
- **Status**: Active compromise affecting SAP cloud development packages

### French Government Agency Data Breach
- **Description**: Cyberattack on France Titres (ANTS), the country's agency for issuing administrative documents
- **Impact**: Theft and sale of sensitive government data
- **Status**: Under investigation with suspect detained

## Affected Systems and Products

- **Linux Distributions**: Major distributions with kernels released since 2017 vulnerable to Copy Fail exploit
- **PyPI Package Repository**: Lightning package compromised with malicious versions
- **Ruby Gems and Go Modules**: Multiple packages compromised in sleeper package campaign
- **Facebook Accounts**: Approximately 30,000 accounts compromised through Google AppSheet phishing
- **SAP Cloud Development**: npm packages for SAP's cloud application ecosystem
- **Windows 11**: KB5083769 update causing backup software failures on 24H2 and 25H2 versions
- **France Titres (ANTS)**: French administrative document agency systems breached

## Attack Vectors and Techniques

- **Supply Chain Poisoning**: Compromising legitimate package repositories to distribute malicious code
- **Phishing Relay Services**: Using legitimate platforms like Google AppSheet to distribute phishing emails
- **Voice Phishing (Vishing)**: Cybercrime groups using voice calls combined with SSO abuse for SaaS extortion
- **CI/CD Pipeline Exploitation**: Targeting continuous integration environments for credential theft
- **Local Privilege Escalation**: Exploiting kernel vulnerabilities to gain root access
- **Cryptocurrency Theft**: Advanced persistent operations targeting crypto exchanges and wallets
- **Data Exfiltration**: Stealing and monetizing sensitive government and personal data

## Threat Actor Activities

- **North Korean Groups**: Conducting historic cryptocurrency heists with potential AI assistance, controlling 76% of stolen crypto in 2026
- **Vietnamese-Linked Operators**: Running sophisticated phishing campaigns using Google services to compromise social media accounts
- **TeamPCP**: Expanding supply chain attacks to target SAP development ecosystems with Mini Shai-Hulud operations
- **China-Aligned Groups**: Targeting Asian governments, NATO states, journalists, and activists in espionage campaigns
- **BlackCat Ransomware Affiliates**: Former cybersecurity professionals sentenced for facilitating ransomware attacks
- **Brazilian DDoS Operators**: Anti-DDoS firm enabling botnet attacks against Brazilian ISPs
- **Cybercrime Groups**: Conducting rapid SaaS extortion attacks using minimal traces and advanced social engineering