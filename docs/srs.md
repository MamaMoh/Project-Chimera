# Software Requirements Specification (SRS)
# Project Chimera: Autonomous Influencer Network

## 1. Introduction

### 1.0 Repository Cross-References
This SRS maps to the repository layout to keep intent and implementation aligned.

- Orchestrator and control plane: `orchestrator/`
- Planner-Worker-Judge services: `services/planner/`, `services/worker/`, `services/judge/`
- MCP providers and integrations: `mcp_servers/`
- Agent governance and policies: `agents/AGENTS.md`, `agents/`
- Personas and SOUL definitions: `agents/personas/SOUL.md`
- HITL processes and review rules: `hitl/`
- Policy enforcement (disclosure, sensitive topics): `policies/`
- Data and memory contracts: `memory/`
- Commerce and wallet governance: `commerce/`
- Schemas (Task, Result, MCP Tool): `schemas/`
- Dashboard UI and review workflows: `dashboard/`
- Architecture decisions: `architecture/adr/`
- Research inputs: `research/`

### 1.1 Purpose and Strategic Scope
This Software Requirements Specification (SRS) establishes the definitive architectural, functional, and operational blueprints for Project Chimera. It is designed to guide the engineering, product, and deployment teams in the construction of the AiQEM Autonomous Influencer Network. This document supersedes all prior specifications, serving as the sole source of truth for the system's development.

The strategic objective of Project Chimera is to transition from automated content scheduling to the creation of Autonomous Influencer Agents. These are not static scripts but persistent, goal-directed digital entities capable of perception, reasoning, creative expression, and economic agency. The system is architected to support a scalable fleet of these agents - potentially numbering in the thousands - managed by a centralized Orchestrator but operating with significant individual autonomy.

The defining characteristic of the 2026 Edition is its reliance on two breakthrough architectural patterns: the Model Context Protocol (MCP) for universal, standardized connectivity to the external world, and the Swarm Architecture for internal task coordination and parallel execution. Furthermore, this system introduces Agentic Commerce, integrating the Coinbase AgentKit to endow agents with non-custodial crypto wallets, enabling them to transact, earn, and manage resources on-chain without direct human intervention for every micro-transaction.

### 1.2 The Single-Orchestrator Operational Model
Traditional enterprise AI deployments have historically required vast teams of engineers to manage infrastructure, monitor model drift, and handle edge cases. Project Chimera adopts a Fractal Orchestration pattern. In this model, a single human Super-Orchestrator manages a tier of AI "Manager Agents," who in turn direct specialized "Worker Swarms." This architecture allows a solopreneur or a small agile team to operate a network of thousands of virtual influencers without succumbing to cognitive overload.

The feasibility of this model rests on two pillars: Self-Healing Workflows and Centralized Context Management. Drawing from "self-healing" infrastructure patterns, the system includes automated triage agents that detect and resolve operational errors - such as API timeouts or content generation failures - without human intervention. Escalation to the human orchestrator occurs only in true edge cases, adhering to the principle of "Management by Exception." Furthermore, the system utilizes the BoardKit governance pattern, where a centralized configuration repository (utilizing AGENTS.md standards) defines the ethical boundaries, brand voice, and operational rules for the entire fleet. This ensures that an update to a single policy file propagates instantly across the entire network, maintaining coherence without the need for micromanaging individual agents.

### 1.3 Business Model Evolution and Economic Agency
The technical evolution of the Chimera platform enables three distinct and scalable business models for AiQEM.tech, transitioning the company from a SaaS tool provider to a comprehensive ecosystem operator.

First, the Digital Talent Agency Model allows AiQEM to develop, own, and manage a proprietary stable of AI influencers. These "in-house" Chimeras serve as revenue-generating assets, monetizing their audiences through advertising, brand sponsorships, and direct affiliate sales. Unlike human talent, these agents are available 24/7, scalable to any niche or language, and immune to the scandals that often plague human influencers.

Second, the Platform-as-a-Service (PaaS) Model licenses the underlying "Chimera OS" to external brands and agencies. In this scenario, corporate clients leverage the platform to build and operate their own brand ambassadors. The architecture's robust multi-tenancy ensures that each client's agents operate in secure, isolated environments, while the centralized orchestration dashboard provides them with the tools to manage their virtual workforce effectively.

Third, the Hybrid Ecosystem Model combines these approaches. AiQEM operates a flagship fleet of high-profile influencers to demonstrate the platform's capabilities - generating "Alpha" and proving the technology - while simultaneously providing the infrastructure to third-party developers. A critical enabler of this ecosystem is the integration of Coinbase AgentKit and Agentic Commerce Protocols (ACP). These technologies transform the Chimeras from passive media channels into active economic participants. Each agent is equipped with a non-custodial crypto wallet, allowing it to receive payments, execute on-chain transactions, and autonomously manage a Profit and Loss (P&L) statement. This capability opens the door to entirely new forms of autonomous commerce, where agents can negotiate deals, purchase digital assets, and pay for their own computational resources, effectively operating as self-sustaining economic entities.

### 1.4 Definitions, Acronyms, and Abbreviations
- Chimera Agent: A sovereign digital entity possessing a unique persona, hierarchical memory, and financial wallet, operating within the network.
- Orchestrator: The central control plane managing the agent fleet, responsible for high-level strategy, resource allocation, and fleet-wide monitoring.
- MCP (Model Context Protocol): An open standard that standardizes how AI models interact with external data (Resources) and functionality (Tools), serving as the "USB-C for AI applications".
- FastRender Pattern: A hierarchical swarm coordination architecture utilizing Planner, Worker, and Judge roles to manage complex, multi-step tasks with high parallelism and quality control.
- OCC (Optimistic Concurrency Control): A non-locking concurrency mechanism used by the Swarm to manage state updates. Agents operate on a local snapshot of the state and validate validity only upon commit, maximizing throughput.
- Agentic Commerce: The capability of AI agents to autonomously execute financial transactions, manage assets, and interact with blockchain protocols using specialized SDKs like Coinbase AgentKit.
- HITL (Human-in-the-Loop): A governance framework where human operators review agent actions based on dynamic confidence scoring and risk thresholds.
- RAG (Retrieval-Augmented Generation): A technique for enhancing LLM output by retrieving relevant information from an external knowledge base (Weaviate) before generating a response.

## 2. Overall Description

### 2.1 Product Perspective
Project Chimera operates as a cloud-native, distributed system designed for high availability and horizontal scalability. Unlike monolithic chatbot architectures, Chimera is a constellation of independent services. The system interacts with the external world - Social Media Platforms, News Feeds, Blockchain Networks, and Vector Databases - exclusively through the Model Context Protocol (MCP). This design decision ensures that the core reasoning logic of the agents is decoupled from the implementation details of third-party APIs.

The system topology is Hub-and-Spoke. The Central Orchestrator serves as the hub, maintaining the global state of the network, managing user accounts (multi-tenancy), and hosting the primary Dashboard. The Agent Swarms operate as the spokes. Each active agent is effectively a dynamic swarm of sub-processes (Planners, Workers, Judges) that spin up to execute tasks and spin down to conserve resources.

This architecture supports multiple business models, including a "Digital Talent Agency" model where the platform manages a stable of in-house influencers, and a "Platform-as-a-Service" (PaaS) model where external brands lease the infrastructure to run their own custom agents. The infrastructure must strictly enforce data isolation between tenants, ensuring that the memories and financial assets of one agent are never accessible to another.

### 2.2 User Characteristics
The platform serves three distinct user categories, each with specific interaction patterns:

**Network Operators (Strategic Managers)**
- Role: Define high-level campaigns and goals for the agents (e.g., "Promote the new summer fashion line in Ethiopia"). They do not write content; they set objectives.
- Interaction: Use the Orchestrator Dashboard to monitor fleet health, review aggregated analytics, and intervene in high-level strategy.
- Technical Proficiency: Moderate. They understand marketing strategy but may not be technical.

**Human Reviewers (HITL Moderators)**
- Role: Provide the Human-in-the-Loop safety layer. They receive escalated tasks from the Judge Agents - content that is flagged as low-confidence, sensitive, or high-risk.
- Interaction: Use a streamlined Review Interface (part of the Dashboard) to quickly Approve, Reject, or Edit agent-generated content.
- Technical Proficiency: Low to Moderate. Focus on brand safety and content quality.

**Developers and System Architects**
- Role: Extend system capabilities by deploying new MCP Servers, refining system prompts, and maintaining infrastructure.
- Interaction: Work via CLI, API, and code repositories.
- Technical Proficiency: High. Expert knowledge of Python, Docker, LLMs, and MCP.

### 2.3 Operational Environment
**Compute Infrastructure:** Hybrid cloud (AWS/GCP) using Kubernetes (K8s) for containerized agent workloads. The system must support auto-scaling to handle burst workloads during viral events or high-activity periods.

**AI Inference:**
- Reasoning: Gemini 3 Pro or Claude Opus 4.5 via API for high-complexity planning and judging.
- Routine Tasks: Gemini 3 Flash or Haiku 3.5 for high-volume, low-latency tasks like comment classification.

**Data Persistence Layer:**
- Semantic Memory: Weaviate (Vector Database) to store agent memories, persona definitions, and world knowledge.
- Transactional Data: PostgreSQL for user data, campaign configurations, and operational logs.
- Episodic Cache: Redis for short-term memory and task queuing (Celery/BullMQ).
- Ledger: On-chain storage (Base, Ethereum, Solana) for the immutable record of all financial transactions executed by the agents.

### 2.4 Constraints and Assumptions
- Regulatory Compliance: Must comply with emerging AI transparency laws (e.g., EU AI Act). Agents must be capable of self-disclosure.
- Cost Management: AI inference and high-quality media generation are expensive. The system must implement rigorous budget controls ("Resource Governor") to prevent runaway costs.
- Platform Volatility: Social media APIs (Twitter/X, Instagram, TikTok) change frequently. MCP Servers shield core agent logic from disruption.

## 3. System Architecture
The architectural core of Project Chimera is defined by the convergence of two patterns: the FastRender Swarm for internal cognition and execution, and MCP for external interaction.

### 3.1 The FastRender Swarm Architecture
To manage the complexity of autonomous behavior, Chimera uses a hierarchical, role-based swarm architecture: Planner, Worker, and Judge.

#### 3.1.1 The Planner (The Strategist)
- Responsibility: Monitors GlobalState (campaign goals, trends, budget) and generates a directed acyclic graph (DAG) of tasks.
- Dynamic Re-planning: Updates the plan when context changes or tasks fail.
- Sub-Planners: May spawn for specialized domains.

#### 3.1.2 The Worker (The Executor)
- Responsibility: Executes a single atomic task and returns a result artifact.
- Isolation: Shared-nothing architecture between workers to prevent cascading failures.
- Tool Usage: Primary consumer of MCP Tools.

#### 3.1.3 The Judge (The Gatekeeper)
- Responsibility: Reviews Worker output against acceptance criteria, persona constraints, and safety guidelines.
- Authority: Approve, Reject, or Escalate to HITL.
- Optimistic Concurrency Control (OCC): Validates state_version before commit to prevent race conditions.

### 3.2 The Integration Layer: Model Context Protocol (MCP)
Project Chimera uses MCP as the universal interface for external interactions.

#### 3.2.1 MCP Topology
Hub-and-Spoke topology with Central Orchestrator as MCP Host and MCP Servers as capability providers.

#### 3.2.2 Protocol Primitives
- Resources: Passive data sources agents can read.
- Tools: Executable functions agents can call.
- Prompts: Reusable templates that structure interactions.

## 4. Specific Requirements: Functional

### 4.1 Cognitive Core and Persona Management
**FR 1.0 Persona Instantiation via SOUL.md**  
The system SHALL support the definition of agent personas via SOUL.md with backstory, voice/tone, core beliefs/values, and directives.

**FR 1.1 Hierarchical Memory Retrieval**  
The system SHALL implement short-term (Redis) and long-term (Weaviate) memory retrieval before reasoning steps.

**FR 1.2 Dynamic Persona Evolution**  
The Judge SHALL summarize successful interactions to update long-term memories.

### 4.2 Perception System (Data Ingestion)
**FR 2.0 Active Resource Monitoring**  
The system SHALL poll configured MCP Resources for updates.

**FR 2.1 Semantic Filtering and Relevance Scoring**  
Only content above a configurable relevance threshold triggers a Task.

**FR 2.2 Trend Detection**  
Background Worker generates Trend Alerts based on aggregated data.

### 4.3 Creative Engine (Content Generation)
**FR 3.0 Multimodal Generation via MCP Tools**  
Text, image, and video generation MUST use MCP Tools.

**FR 3.1 Character Consistency Lock**  
Image generation requests MUST include a character_reference_id or style LoRA.

**FR 3.2 Hybrid Video Rendering Strategy**  
Tiered generation based on priority and budget.

### 4.4 Action System (Social Interface)
**FR 4.0 Platform-Agnostic Publishing**  
All social actions SHALL execute via MCP Tools. Direct API calls are prohibited.

**FR 4.1 Bi-Directional Interaction Loop**  
Planner receives Resource events, Worker generates replies, Judge verifies prior to execution.

### 4.5 Agentic Commerce (Coinbase AgentKit)
**FR 5.0 Non-Custodial Wallet Management**  
Each agent SHALL have a unique non-custodial wallet.

**FR 5.1 Autonomous On-Chain Transactions**  
Support transfer, deploy_token, and get_balance actions via AgentKit.

**FR 5.2 Budget Governance (CFO Sub-Agent)**  
Dedicated Judge enforces configurable budget limits and flags anomalies.

### 4.6 Orchestration and Swarm Governance
**FR 6.0 Planner-Worker-Judge Implementation**  
Planner, Worker, and Judge run as decoupled services with task queues.

**FR 6.1 Optimistic Concurrency Control (OCC)**  
Judge checks state_version before commit; invalidates stale results.

## 5. Specific Requirements: Non-Functional

### 5.1 Human-in-the-Loop (HITL) and Confidence Thresholds
- **NFR 1.0 Confidence Scoring:** Each action SHALL include confidence_score.
- **NFR 1.1 Automated Escalation Logic:** Tiered routing based on confidence score.
- **NFR 1.2 Sensitive Topic Filters:** Mandatory HITL for sensitive categories.

### 5.2 Ethical and Transparency Framework
- **NFR 2.0 Automated Disclosure:** Use platform-native AI labeling features.
- **NFR 2.1 Identity Protection and Honesty:** Mandatory disclosure when asked.

### 5.3 Performance and Scalability
- **NFR 3.0 Swarm Horizontal Scalability:** Support minimum 1,000 concurrent agents.
- **NFR 3.1 Interaction Latency:** High-priority interactions within 10 seconds (excluding HITL).

## 6. Interface Requirements

### 6.1 Network Orchestration Dashboard
- **UI 1.0 Fleet Status View:** States, financial health, HITL queue depth.
- **UI 1.1 Campaign Composer:** Natural language goals with editable task tree.

### 6.2 Data Models and Schemas
**Schema 1: Agent Task (JSON)**
```
{
  "task_id": "uuid-v4-string",
  "task_type": "generate_content | reply_comment | execute_transaction",
  "priority": "high | medium | low",
  "context": {
    "goal_description": "string",
    "persona_constraints": ["string"],
    "required_resources": ["mcp://twitter/mentions/123", "mcp://memory/recent"]
  },
  "assigned_worker_id": "string",
  "created_at": "timestamp",
  "status": "pending | in_progress | review | complete"
}
```

**Schema 2: MCP Tool Definition (JSON Schema)**
```
{
  "name": "post_content",
  "description": "Publishes text and media to a connected social platform.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "platform": {
        "type": "string",
        "enum": ["twitter", "instagram", "threads"]
      },
      "text_content": {
        "type": "string",
        "description": "The body of the post/tweet."
      },
      "media_urls": {
        "type": "array",
        "items": {"type": "string"}
      },
      "disclosure_level": {
        "type": "string",
        "enum": ["automated", "assisted", "none"]
      }
    },
    "required": ["platform", "text_content"]
  }
}
```

## 7. Implementation Roadmap and Genesis Prompts

### 7.1 Phase 1: The Core Swarm (Timeframe 1)
Objective: Establish the Planner-Worker-Judge loop and Task Queue infrastructure.

Genesis Prompt:
```
I am building a multi-agent system using the FastRender swarm pattern in Python.
Please create a project structure with three main service folders: planner, worker, judge.
Planner Service: Write a Python service that reads a goals.json file, decomposes it using a mock LLM call, and pushes Task objects to a Redis queue named task_queue.
Worker Service: Write a Python service that pops tasks from task_queue, simulates work (async sleep 2s), and pushes a Result object to a Redis queue named review_queue.
Judge Service: Write a Python service that pops from review_queue, checks if result.status == 'success', and logs the outcome.
Use pydantic to define strict schemas for Task and Result. Use redis-py for queuing.
```

### 7.2 Phase 2: MCP Integration (Timeframe 2)
Objective: Connect the swarm to external data and tools via MCP.

Genesis Prompt:
```
I need to integrate the Model Context Protocol (MCP) into my agent system.
Install the mcp python SDK.
Create a class MCPClient that can connect to a local MCP server process via Stdio transport.
Implement a method call_tool(server_name, tool_name, arguments) that sends a standard JSON-RPC request to the connected server.
Write a script to spawn an instance of the mcp-server-sqlite (as a reference implementation) and use your client to query a test database table.
```

### 7.3 Phase 3: Agentic Commerce (Timeframe 3)
Objective: Enable financial autonomy and wallet management.

Genesis Prompt:
```
Integrate the Coinbase AgentKit into the Worker service.
Set up a wallet provider using CdpEvmWalletProvider from the coinbase-agentkit library.
Create an Action Provider class that exposes transfer_asset and get_wallet_balance functionality.
Write a test script where an agent checks its own balance. If the balance is greater than 10 USDC, it transfers 1 USDC to a hardcoded 'Savings Wallet' address.
Ensure that the API keys and Private Keys are read strictly from os.environ and raise an error if they are missing.
```

## 8. Conclusions
Project Chimera (2026 Edition) represents the convergence of three transformative technologies: the MCP standard for universal connectivity, Swarm Architectures for robust autonomous coordination, and Agentic Commerce for economic independence. By adhering to this SRS, the development team will deliver a resilient, scalable network of virtual influencers capable of operating with genuine agency in the digital economy.
