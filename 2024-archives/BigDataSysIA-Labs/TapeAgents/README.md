## TapeAgents 
A new holistic agent framework that supports practitioners at both the agent development and data-driven agent optimization stages.

## Tape
A comprehensive, structured, granular, semantic-level log of the agent session

## Nodes
Agents are built from Nodes. They are the basic atoms of intelligence. Node is responsible for making the LLM call and processing of the call’s output.

Nodes generate new tape entries that we call steps.

## Steps
**Thought steps** to express reasoning and **action steps** to request external inputs.
Examples of what an agent can do in a step include making a long-term plan, reasoning about how to fulfill the plan or how to use a tool, requesting a tool call.

Examples- 

From TapeAgents/examples/gaia_agent/steps.py 

**Thoughts**

Chain of thoughts of logical reasoning to find the answer.

    class ReasoningThought(GaiaThought):
        kind: Literal["reasoning_thought"] = "reasoning_thought"
        reasoning: list[str] = Field(description="reasoning sentences that describe how to move forward with the task")
    
**Actions**

Action that provides parameters for a search function call. Could search in the web_search or wikipedia. Search results will be ordered by relevance from top to bottom

    class SearchAction(GaiaAction):
        kind: Literal["search_action"] = "search_action"
        source: str = Field(description="source to search in, could be web_search or wikipedia")
        query: str = Field(description="search query")
    
The **environment** responds to the action steps at the end of the tape with **observation steps** that it likewise
 appends to the tape.

 ## Environment 

 The main method of an environment object is:
       
    def react(self, tape)-> Tape.
    
 The environment.react searches for the unfulfilled actions in the tape and adds the corresponding observation steps to the tape.

 The orchestrator invokes the agent and the environment in an alternate fashion and maintains full control over their interactions.

 ![image](https://github.com/user-attachments/assets/5a342914-85d4-416c-9a02-8c57646ed74c)

## Agents

The **agents** in TapeAgents read the tape to make the LLM prompt and then process the LLM output to append
new steps to the tape.
 TapeAgent agent generates steps and makes a new tape by appending the generated steps to the input tape.
 Specifically, agent.run(tape) runs an iterative reasoning loop that, at every iteration, selects a node, lets it make the prompt
 and generates the next steps. By default, the
 agent will run its nodes sequentially. The loop continues as long as the nodes only
 generate thoughts. When a node produces an action, the agent
 stops and returns a new tape with the generated steps from
 all iterations appended to it. More precisely, agent.run(tape)
 returns an AgentStream object for streaming events like partial
 tapes and steps. An agent may have subagents for whom this agent is the
 manager.

 ![image](https://github.com/user-attachments/assets/8a98be1b-a2eb-45f5-b669-42c09b186894)


## Tape Metadata

 1. tape.metadata.author: which agent or environment made this tape; either by authoring it, or by
 adding steps to it, or by making a revision of another tape.
 2. tape.metadata.parent_id: the ID of the parent tape of which the current tape is a continuation
 (when applicable).
 3. step.metadata.agent: the hierarchical name of the agent that generated the step.
 4. step.metadata.node: the name of the node that generated the step.
 5. step.metadata.prompt_id: the identifier (id) of the prompt that led to the generation of this step,
 see the explanation below.

## Redis
Redis (Remote Dictionary Server) is an open-source, in-memory data structure store primarily used as a database, cache, and message broker.

Redis is an in-memory key-value store, meaning it keeps its data in memory (RAM) rather than on disk, which makes it extremely fast. Unlike traditional databases that rely on disk-based storage, Redis can process a large volume of read and write requests per second, making it well-suited for real-time applications

Key Features And Why we chose Redis 
1. In-Memory Storage: All data is stored in RAM, which significantly increases read/write speed.
2. Versatile Data Types: Redis supports various data types, such as strings, lists, sets, sorted sets, hashes, bitmaps, hyperloglogs, geospatial indexes, and streams.
Versatile Data Types



