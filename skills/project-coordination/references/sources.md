# Sources and limits

Checked on 2026-10-13. These are design references, not certification or performance guarantees. The rules express engineering trade-offs; no organization model is claimed to be optimal for every project.

| Primary source | Limited lesson used | What it does not establish |
| --- | --- | --- |
| [Agent Skills specification](https://agentskills.io/specification) | Standard entrypoint and on-demand references | Format compliance does not prove reliable behavior or security |
| [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | Start with simple composition; add complexity when justified | No required vendor, framework, or fixed agent count |
| [Anthropic: Multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) | Delegation needs scope, evidence, and evaluable outputs; coordination consumes resources | Research-system gains or costs cannot be transferred directly to software projects |
| [Skills directory documentation](https://skills.sh/docs) | Public discovery and installation channels | Listing or install counts do not constitute official quality endorsement |

No article body or source code was copied. Examples are generic; the public package contains no project credentials, internal chats, user documents, or machine-specific paths.

The skill itself starts no background tasks, creates no agents, changes no permissions, and uploads no files. Users still need actual authorization and tools. Without delegation tools, one agent can maintain the necessary state and roles.

Use the project's existing implementation language and structure. TypeScript discipline applies to TypeScript projects, not as a mandate to migrate Python, Go, or other projects. Follow the user's reporting language and frequency; one user's preference for complete tables does not make long reports mandatory for every task.

Record format checks, link/privacy checks, independent scenario exercises, and real-project trials separately. Scenario exercises cannot demonstrate token savings or universal reliability. Revise in response to observed failures or feedback, then retest the affected scenarios instead of accumulating repetitive rules.
