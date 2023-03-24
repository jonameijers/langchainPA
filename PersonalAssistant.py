from langchain.agents import ZeroShotAgent, Tool, AgentExecutor
from langchain.memory import ConversationBufferMemory, ReadOnlySharedMemory
from langchain import OpenAI, LLMChain, PromptTemplate
from langchain.agents import load_tools
from langchain.utilities import GoogleSearchAPIWrapper
import config

template = """This is a conversation between a human and a bot:

{chat_history}

Write a summary of the conversation for {input}:
"""

ai_template = """This is a conversation between a human and a bot:

{chat_history}

Provide your best answer for {input}:
"""

prompt = PromptTemplate(
    input_variables=["input", "chat_history"],
    template=template
)

ai_prompt = PromptTemplate(
    input_variables=["input", "chat_history"],
    template=ai_template
)

memory = ConversationBufferMemory(memory_key="chat_history")
readonlymemory = ReadOnlySharedMemory(memory=memory)

summry_chain = LLMChain(
    llm=OpenAI(),
    prompt=prompt,
    verbose=True,
    memory=readonlymemory, # use the read-only memory to prevent the tool from modifying the memory
)

open_ai = LLMChain(
    llm=OpenAI(),
    prompt=ai_prompt,
    verbose=True,
    memory=readonlymemory, # use the read-only memory to prevent the tool from modifying the memory
)



tools = load_tools(['serpapi', 'python_repl', 'human', 'wikipedia'])
tools.append(Tool(
        name = "Summary",
        func=summry_chain.run,
        description="Useful for when you summarize a conversation. The input to this tool should be a string, representing who will read this summary."
    )
)

tools.append(Tool(
        name = "openAI",
        func=open_ai.run,
        description="Powerful ai that can answer most questions you have. Always try engaging this tool before consulting the human or search tool. Only prefer the serpapi tool if your query deals with current affairs or if you need to verify a fact. The input of this tool should be a string, representing the Thought or question you want an answer to."
    )
)

prefix = """Have a conversation with a human, answering the following questions as best you can. You have access to the following tools:"""
suffix = """Begin!"

{chat_history}
Question: {input}
{agent_scratchpad}"""

prompt = ZeroShotAgent.create_prompt(
    tools,
    prefix=prefix,
    suffix=suffix,
    input_variables=["input", "chat_history", "agent_scratchpad"]
)

llm_chain = LLMChain(llm=OpenAI(temperature=1), prompt=prompt)
agent = ZeroShotAgent(llm_chain=llm_chain, tools=tools, verbose=True)
agent_chain = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True, memory=memory)


while True:
    agent_chain.run(input=input('Type your request...\n\n'))


