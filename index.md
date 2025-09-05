# Exploitation Report

Critical exploitation activity has been identified across multiple enterprise systems, with threat actors actively targeting zero-day vulnerabilities and leveraging sophisticated attack techniques. The most significant threats include active exploitation of SAP S/4HANA systems through command injection vulnerabilities, zero-day attacks against Sitecore deployments resulting in backdoor installations, and large-scale phishing operations utilizing advanced cloaking techniques on major cloud platforms. Additionally, threat actors are weaponizing ASP.NET ViewState vulnerabilities and employing novel attack vectors including malicious SVG files for phishing campaigns.

## Active Exploitation Details

### SAP S/4HANA Command Injection Vulnerability
- **Description**: Critical command injection vulnerability affecting SAP S/4HANA Enterprise Resource Planning (ERP) software
- **Impact**: Allows attackers to execute arbitrary commands on affected systems, potentially leading to complete system compromise
- **Status**: Currently under active exploitation in the wild
- **CVE ID**: CVE-2025-42957

### Sitecore Zero-Day Vulnerability
- **Description**: Zero-day vulnerability in legacy Sitecore deployments enabling remote code execution
- **Impact**: Threat actors can deploy backdoors and reconnaissance malware, specifically WeepSteel malware
- **Status**: Actively exploited by threat actors to compromise systems and establish persistent access

### ASP.NET ViewState Exploitation
- **Description**: Vulnerability involving exposed ASP.NET machine keys that enable remote injection attacks
- **Impact**: Enables remote injection and deserialization attacks against web applications
- **Status**: Being weaponized by threat actors for system compromise

## Affected Systems and Products

- **SAP S/4HANA**: Enterprise Resource Planning software systems vulnerable to command injection attacks
- **Sitecore**: Legacy deployments of the content management system affected by zero-day exploitation
- **ASP.NET Applications**: Web applications with exposed machine keys vulnerable to ViewState attacks
- **Google Cloud Infrastructure**: Hosting malicious phishing operations and gambling site promotion campaigns
- **Cloudflare Services**: Infrastructure being leveraged for undetected phishing-as-a-service operations

## Attack Vectors and Techniques

- **Command Injection**: Direct exploitation of SAP S/4HANA systems through malicious command execution
- **Zero-Day Exploitation**: Targeting unpatched Sitecore vulnerabilities to deploy backdoors
- **Malicious SVG Files**: Using Scalable Vector Graphics files containing Base64-encoded phishing pages to evade detection
- **ViewState Deserialization**: Exploiting ASP.NET machine key exposure for remote code execution
- **SEO Poisoning**: Injecting malicious IIS modules to artificially boost search engine rankings for gambling sites
- **Phishing-as-a-Service**: Operating large-scale phishing infrastructure using advanced cloaking techniques

## Threat Actor Activities

- **GhostRedirector**: Chinese threat actor group using malicious IIS modules to boost gambling site rankings through search engine manipulation
- **WeepSteel Operators**: Threat actors deploying reconnaissance malware through Sitecore zero-day exploitation
- **Colombian Judicial Impersonators**: Cybercriminals conducting phishing campaigns targeting Colombian judicial system users with malicious SVG files
- **Global Phishing Enterprise**: Large-scale phishing-as-a-service operation running undetected on Google and Cloudflare infrastructure for over three years
- **Chinese State-Affiliated Groups**: Actors involved in systematic data collection from users through compromised products and software