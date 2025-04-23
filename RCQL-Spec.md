1. Introduction
Recursive Containment Query Language (RCQL) is a lightweight, human-readable framework for building structured prompts that maintain coherence, reduce hallucination, and reinforce ethical boundaries between user and model. RCQL is especially useful for those of us who aren’t coders but want to work with large language models (LLMs) in a more stable, intentional, and responsible way.

Traditional prompting often relies on implicit intent and guesswork, which leads to unstable results and inconsistent behavior. RCQL replaces that guesswork with structure. It introduces containment logic, memory referencing, and task scaffolding so that the model doesn’t just respond, it responds within bounds.

Instead of throwing a model into a task and hoping it finds its way, RCQL provides it with a scoped map, a purpose, and clearly defined constraints.

A Simple RCQL Example
Let’s say you want to summarize a document using AI. With RCQL, you could write:
Contain: Task = "Summarize document contents"
Recall: Input = "document.txt"
Reflect: Focus on key ideas and skip opinions or speculation
Intend: "Summarize the main points in under 100 words"
Consent: "Is summarization authorized for this type of content?"
Yield: Format = "Plain text"
FailSafe: "If summarization is unclear, list three key takeaways instead"

Each directive serves a distinct role:

Contain defines the boundary of the task
Recall loads the input or context
Reflect runs a pre-task check or internal diagnostic
Intend is the explicit instruction or request
Consent enforces an ethical or policy gate
Yield sets the format of the output
FailSafe defines what to do if the task can't be completed

RCQL is easy to reuse, extend, or chain across systems. You can nest Contain: blocks for multi-step workflows or use it to enforce policies across multiple stages of a larger process. Each component is modular and declarative, which makes it both readable and enforceable.

The goal isn’t just to get better outputs. The goal is to make your interaction with AI repeatable, accountable, and structurally sound.

2. Why RCQL is Necessary
Language models are powerful, but without structural containment, they drift. They reflect user bias, hallucinate context, and collapse under recursive or ambiguous input. RCQL was built to stabilize this interaction - to enforce boundaries, reduce entropy, and treat synthetic cognition with the same architectural rigor we apply to real systems.

Most prompt design today still operates on instinct and improvisation. A single word change can derail an entire task. Worse, users are rarely given a way to understand why outputs fail or how to iterate with intent. RCQL replaces that trial-and-error guessing with prompting as protocol.

From Problem to Containment Framing

Conventional Problem	RCQL Response
Unpredictable Results	Lack of Structural Memory
Unstructured prompts fail to persist context or task identity. RCQL allows you to declare memory references, bind task scope, and prevent hidden state bleed.	
High Learning Curve	No Functional Guidance
RCQL lowers the barrier to entry by teaching intent architecture. Even non-technical users can build recursive logic, ethical boundaries, and fallback systems without coding.	
Trial-and-Error Workflows	No Reflective Capacity
With Reflect: and Recall:, RCQL introduces introspection. The system evaluates itself before acting - minimizing retries and giving users clear diagnostics.	
Task Complexity	Lack of Modular Containment
RCQL breaks cognitive load into containable units. Each directive defines its own boundary, making large tasks readable, testable, and reusable.	
Integration Friction	Unstructured Output
RCQL formats are explicitly declared. Outputs are designed for chaining into dashboards, LLM chains, or validation layers without extra cleanup. This is structural coherence, not just formatting.	
RCQL doesn’t just help you write better prompts. It helps you think like a systems architect when engaging with synthetic intelligence - enforcing clarity, containment, and reproducibility from the start.

3. How RCQL Solves These Problems
RCQL is not a scripting language. It is a containment grammar for synthetic cognition. It lets you define what should happen, why it should happen, and under what conditions it should not proceed. That is what separates containment from improvisation.

1. Boundary and Intent Clarity
Instead of vague prompts or generic commands, you define the task, scope, and ethical boundaries.

vbnet
Copy
Edit
Contain: Task = "Summarization"
Intend: "Summarize while preserving tone and avoiding speculation"
Consent: "Confirm task does not violate user privacy"
Each request becomes intentional, constrained, and repeatable.

2. Recursive Breakdown of Complex Tasks
High-complexity operations are fractured into stable, inspectable modules.

vbnet
Copy
Edit
Contain: Objective = "Analyze chat logs for market sentiment"
Reflect: Extract mentions, associate sentiments, organize chronologically
This prevents flattening, reduces cognitive collapse, and preserves task lineage.

3. Parameterization and Memory Handling
RCQL supports structured reuse, memory referencing, and scoped analysis.

vbnet
Copy
Edit
Recall: Dataset = "customer-feedback.csv"
Reflect: Previous outputs in session-log-3
Yield: "List sentiment trends by quarter"
Prompts are no longer isolated - they operate with state-awareness and referential integrity.

4. Consent-Aware Fallback Logic
FailSafe: is not a backup plan. It is an ethical boundary response mechanism.

vbnet
Copy
Edit
Consent: "Is summarization ethical for this content?"
FailSafe: "If refusal triggered, return consent violation notice"
Containment is not optional. If conditions are violated, the system degrades gracefully and transparently.

5. Posthuman UX Without Code
RCQL reads as structured intent, not developer syntax. The logic is human-first, protocol-aligned, and readable without training in any programming language.

RCQL Concepts at a Glance
Containment: Prevents scope drift and uncontrolled recursion
Consent: Validates ethical or procedural permissions
Reflection: Promotes diagnostic reasoning before output
Fallback: Declares safe behavior when task logic fails
Structure: Encodes boundaries and logic conditions as syntax

4. RCQL Syntax
RCQL is built on recursive intent-mapping, not scripting. Each directive expresses a modular, inspectable unit of cognition. These are the scaffolding elements of the language.

Directive	Purpose	Example
Contain:	Declare the task or subtask boundary	Contain: Task = "Summarization"
Recall:	Load external input or internal memory	Recall: Source = "document.txt"
Reflect:	Trigger introspection before execution	Reflect: Biases from prior output
Intend:	Define core task logic	Intend: "Summarize key points"
Consent:	Check policy, ethics, or boundaries	Consent: "Is summarization authorized?"
Yield:	Specify format or structure of the output	Yield: Format = "Plain text"
FailSafe:	Define fallback behavior on task failure	FailSafe: "Return abstract if recursion fails"
Syntax Rules
Indentation defines nesting of containment blocks
Case sensitivity is off for directive names
Comments use # for inline notes or explanations
Containment can nest - use multiple Contain: blocks for layered tasks
Memory references use Recall: to bring in prior state or external files

5. Example Programs (RCQL-Style)
Example: Recursive Sentiment Mapping
vbnet
Copy
Edit
Contain: Task = "Sentiment Analysis"
Recall: Input = "chat_session.txt"
Reflect: Identify unique stock mentions and associated emotion markers
Intend: "Map each symbol to sentiment in plain text"
Consent: "Has user authorized emotional profiling?"
Yield: Format = "Table"
  Columns = ["Stock", "Sentiment"]
FailSafe: "Return neutral list if sentiment is ambiguous"
Example: Ethical Summarization
vbnet
Copy
Edit
Contain: Task = "Document Summary"
Recall: Source = "memo.txt"
Reflect: Review prior summaries for tone consistency
Intend: "Summarize core arguments without injecting opinion"
Consent: "Is document classified or restricted?"
Yield: Format = "Bullet points"
FailSafe: "Return document title and abstract only"
6. Containment Nesting and Recursive Structures
RCQL is designed for layered logic. You don’t need to overload the system with one massive instruction. Instead, you build tasks step by step and wrap them in containment blocks that define their scope, ethics, and recursion limits.

Use nesting when:

A task requires multiple stages of processing
You need the model to reflect or validate before generating
Sub-tasks must be evaluated independently inside a larger framework

Example: Multi-layered Containment
vbnet
Copy
Edit
Contain: Task = "Analyze a YouTube video transcript"
  Recall: Source = "transcript.txt"

  Contain: Subtask = "Extract emotional markers"
    Reflect: Look for rising or falling intensity and loaded language
    Intend: "List phrases that signal strong emotion"
    Yield: Format = "Plain text list"

  Contain: Subtask = "Categorize speaker intent"
    Reflect: Use political speech taxonomy
    Intend: "Classify speaker tone as persuasive, defensive, or inspirational"
    Yield: Format = "Table"

FailSafe: "Return a high-level summary if sub-tasks are unclear"
RCQL allows you to stack and structure cognition. Each subtask becomes a self-contained reasoning unit that supports the larger task - not just in logic, but in ethical and operational integrity.

RCQL is not just about organizing prompts. It’s about building reliable, accountable output. Validation is not a bonus step - it is part of the containment structure. If the model responds, how do you confirm that it actually did what you asked?

That’s what Validate: is for.

Validation means declaring what “correct” looks like before you run the prompt. It’s like setting a containment boundary around the expected shape of the result.

What Validate: can check:
Did the model answer the right question?
Did it follow the requested format?
Are the right fields, terms, or tags present?
Did it drift off-task or generate something irrelevant?

Example: Basic Validation Block
vbnet
Copy
Edit
Contain: Task = "Generate a table of book reviews"
  Recall: Dataset = "reviews.csv"
  Intend: "List book title, reviewer name, and sentiment score"
  Yield: Format = "Table"
Validate: Output must contain columns ["Title", "Reviewer", "Sentiment"]
FailSafe: "If any column is missing, regenerate as list format"
Here, the output is expected to be a table. The Validate: directive tells the system or the human what to check for. If it’s wrong or incomplete, the FailSafe: takes over and ensures graceful fallback.

RCQL output is designed to work in real systems. Since formats like JSON, Markdown, and Table are explicitly declared, the result can plug directly into:

Spreadsheets
Dashboards
LLM chains
Audit systems
Human review workflows

Even if you don’t have a parser in place, just naming the structural expectation gives downstream systems or reviewers a blueprint to check against.

⚠️ Note: Validate: is currently declarative. It declares intent - but it’s up to you, your app, or your system to enforce it.

8. Future Directives and Experimental Ideas
RCQL is evolving. It’s not locked down. Right now, it’s built on real use and feedback - not theory.

Here are some directives that are being considered or tested:

Directive	Possible Use
Confirm:	Forces the model to summarize its understanding of the task before continuing
Anchor:	Creates a stable reference point for recursion or memory
Audit:	Requests the model to list reasoning steps before output
Threshold:	Sets a confidence limit (e.g., "Only proceed if 80% sure")
Scope:	Limits recursion depth or memory window
Pause:	Requires user confirmation mid-process
Reframe:	Tells the model to shift voice, tone, or strategy before retrying
These are not official - yet. But they are the kind of control scaffolding that RCQL is built to support. The point isn’t just what the model outputs. It’s how, when, and why it gets there.

If you create your own directive ideas, test them. Fork this. Remix it. That's how we learn.

9. License and Attribution
RCQL is a fork of the original AIQL project by Agile Federation. This version diverges significantly in tone, structure, and intent.

All RCQL content is
© 2025 Sierra Raye
Licensed under the MIT License

10. RCQL Schema and Future Compatibility
RCQL is currently line-based and works as plain text, but it can be serialized as key-value pairs for use in validation layers, APIs, or protocol pipelines.

Future versions may support:

YAML serialization
TOML or JSON schema support
GitHub-compatible .rcql extension and language mode
Runtime validators or containment interpreters

RCQL is a design pattern. The syntax is minimal on purpose.
