"""All copy for michaellehman.me. Edit here, then run build.py.

Body blocks: a plain string is a paragraph. Lists are lists of strings.
Nothing here is invented contact data: add LinkedIn or an email to LINKS when you choose to publish them.
"""

SITE = {
    "name": "Michael Lehman",
    "title": "IT Service and Platform Automation Architect",
    "location": "Ohio, USA (remote)",
    "description": "Michael Lehman designs service management, automation, observability and agentic AI solutions for large managed infrastructure.",
    "url": "https://michaellehman.me/",
    "domain": "michaellehman.me",       # writes docs/CNAME for GitHub Pages; set to "" to skip
    "drawing": "ML-001",                 # the drawing number in the title block
    "revision": "REV 2026.09",
}

INTRO = ("I design the tooling and automation that keep large managed infrastructure running, "
         "and, more and more, the AI agents that work alongside the people who run it.")

ABOUT = [
    "I decided young that I would work with computers when I grew up, and I did. I started programming at 12, spent late nights "
    "through my teens at friends’ houses learning operating systems, web pages and networking, and at 18 we started our own company. "
    "I was the CEO. I had no idea how to run a business, but we gave it a good go.",
    "At 20 I moved into IT outsourcing, and I have spent the years since supporting infrastructure for Fortune 500 companies: "
    "Windows servers, VMware, storage, and a lot of automation. I went from systems administrator to the person people escalated "
    "the hard problems to, then to leading and managing infrastructure teams, and now to architecture.",
    "My title has never said developer, but I have written scripts, services and tools the whole way, and I still love the "
    "problem solving. Today my job is to design, not to build: I work with bid teams, clients, and development and infrastructure "
    "teams to shape service management, automation, observability and agentic AI solutions, and to make sure they hold up long after go-live.",
    "Outside of work I run a homelab and write about the projects that take more than one try at 4th Try Tech.",
]

# Current role. Written from the role description Michael wrote for the position.
ROLE = {
    "summary": ("I bridge business strategy and modern service operations. I design service management, automation, agentic AI and "
                "observability solutions across the whole client lifecycle, from pursuit and bid support through transition, "
                "implementation and post-go-live optimization, and I partner with development and infrastructure teams who build them."),
    "areas": [
        ("Solution architecture and pre-sales", [
            "Design and present service management, automation and observability solutions to bid teams and clients during pursuits and RFP responses.",
            "Translate business, operational and non-functional requirements into tool-based architectures, with the value, trade-offs and outcomes spelled out.",
            "Contribute solution architectures, proposals, demonstrations and executive-level presentations.",
        ]),
        ("Automation and integration", [
            "Set automation strategy within service management: workflow, infrastructure and application automation, and event-driven remediation.",
            "Architect web services, APIs, integrations and automation frameworks on modern standards (REST, JSON, event streams), partnering closely with development teams on implementation.",
            "Keep automation and integrations aligned with business requirements as scope evolves.",
            "Provide L2 and L3 architectural guidance for integration and automation solutions, and mentor production support teams.",
        ]),
        ("Agentic AI architecture and enablement", [
            "Architect and pilot agentic AI in service management and operations, both to augment existing delivery roles and as a designed part of the platform.",
            "Context and retrieval management: RAG, graph-based retrieval, knowledge grounding and context engineering, so agents stay accurate to the client environment.",
            "Architectural direction for agent harnesses: tool and function-calling permissions, guardrails and prompt-injection defenses, in partnership with development teams.",
            "Ontologies and knowledge structures that agents and integrations reason over.",
            "Evaluation as part of the delivery lifecycle (accuracy, reliability, drift, regression), not a one-time check.",
            "Agent observability: tracing, monitoring and explainability of agent decisions, integrated with infrastructure and application observability.",
            "Integration mapping between agents, ESM and ITSM tooling, and enterprise systems.",
            "AI governance and responsible AI: data privacy, model risk, human oversight and auditability.",
            "Human-in-the-loop design: approval gates, escalation thresholds, and clear lines between automated and human-owned decisions.",
            "Cost, token usage and latency as architecture decisions: model selection, context sizing and caching.",
            "Helping clients and teams through the change and adoption questions agents raise for existing roles.",
        ]),
        ("Observability and operational intelligence", [
            "Observability and monitoring architectures spanning infrastructure, applications, services, AI components and user experience.",
            "Metrics, logs, traces, events and dependency mapping.",
            "Integrating monitoring with service management for proactive incident management, automated response and faster root cause analysis.",
            "AIOps and analytics to reduce noise, detect anomalies and support predictive and preventative operations.",
        ]),
        ("Transition and delivery", [
            "Take part in every phase of transition programs, from pursuit and design through implementation and stabilization.",
            "Planning, estimation, resourcing, risk and issue management, and technical decisions.",
            "Make sure delivered solutions meet architectural, operational and security standards and are supportable at scale.",
        ]),
        ("Practice and capability development", [
            "Build Service Integration and ESM practice capabilities.",
            "Create reusable assets: reference architectures, design patterns, accelerators, white papers and business cases, now extending into agentic AI patterns.",
            "Support innovation work in automation, agentic AI, observability and service operations.",
        ]),
    ],
}

# Oldest last. "span" is the length shown on the dimension line.
EXPERIENCE = [
    {"company": "Capgemini", "role": "Architect", "dates": "Jul 2020 to present", "span": "6Y 3M", "current": True,
     "points": ["IT service and platform automation architecture for managed infrastructure services: monitoring and observability, AIOps, ITSM, automation, analytics and agentic AI.",
                "Solution design for pursuits and RFP responses, including statements of work, responsibility matrices and KPI catalogs.",
                "The full scope of the role is on the role page."]},
    {"company": "Capgemini", "role": "Infrastructure Manager", "dates": "Jan 2016 to Jul 2020", "span": "4Y 7M",
     "points": ["Managed the Wintel infrastructure team supporting Honeywell."]},
    {"company": "Capgemini", "role": "Senior IT Consultant", "dates": "Apr 2013 to Jan 2016", "span": "2Y 10M",
     "points": ["Wintel lead for an operations team supporting Fortune 500 accounts, until promotion to Infrastructure Manager."]},
    {"company": "EDS, an HP company (later HPE)", "role": "IT Systems Technician, Senior", "dates": "2003 to Apr 2013", "span": "10Y",
     "points": ["Started on the Marathon account under Analysts International and transferred to EDS in 2004.",
                "Set the standards for server naming, time, printing, server builds, VMware ESX, DFS, large file servers and documentation, including a wiki.",
                "Ran the Hitachi and Brocade SAN for three to four years before the EDS SAN team took it on: disk configuration, LUN publishing, fabric zoning, cabling and HBA configuration.",
                "Subject-matter expert for Active Directory, DNS, Windows, VMware ESX, disaster recovery and server automation, and the escalation point for difficult problems and projects.",
                "Designed and built a high-uptime distributed scheduling environment on CA AutoSys, with clustered database, file and web tiers, SAN storage, VMware job servers and a custom web management interface.",
                "Wrote the scripts, programs and services that supported it, in several languages."]},
    {"company": "Analysts International", "role": "Systems Administrator", "dates": "Feb 1999 to Nov 2003", "span": "4Y 10M",
     "points": ["Desktop support, and designed and led a desktop imaging solution.",
                "Escalation point for difficult tickets and for projects that improved the environment.",
                "Networking, Check Point FireWall-1, Cisco routing and switching, Linux VPN, backup and restore, and application support."]},
]

SKILLS = [
    ("Service management", "ITIL practices (incident, problem, change, CMDB), Site Reliability Engineering (SLOs, error budgets, toil reduction), Agile delivery, domain-driven design for service boundaries"),
    ("Automation and integration", "Workflow and event-driven automation, APIs and web services (REST, SOAP, JSON), scripting across several languages"),
    ("Agentic AI", "RAG and graph retrieval, context engineering, agent harnesses and guardrails, evaluations, agent observability, AI governance"),
    ("Observability", "Monitoring and telemetry architecture, metrics, logs, traces and events, AIOps, dependency mapping"),
    ("Infrastructure", "Windows and Linux servers, databases, Active Directory, DNS, VMware, SAN storage and fabrics, disaster recovery, job scheduling"),
    ("Communication", "Executive presentations, storytelling, RFP responses, statements of work, KPI catalogs and responsibility matrices"),
]

LINKS = [
    ("4th Try Tech", "https://4thtry.tech/", "My working log of projects, experiments and misadventures."),
    ("GitHub", "https://github.com/4thTryTech", "Code and brand files for 4th Try Tech."),
    # ("LinkedIn", "https://www.linkedin.com/in/<your-handle>/", "Full work history."),
]
