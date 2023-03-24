# flake8: noqa
PREFIX = """Answer the following questions as best you can. You have access to the following tools:"""
FORMAT_INSTRUCTIONS = """Make sure to always use the following format:

Question: the input request you must perform
Thought: you should always think about what to do, unless the final answer or action can be directly inferred from the question or previous chat history, in which case you skip Action and Observation and present the final result.
Action: the action to take, can be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
Execution: Any action that must be performed to get closer to achieving the final result
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know how to perform or answer the request
Final Result: Performs the action that completes the original request. This is the final result I came up with"""
SUFFIX = """Begin!

Question: {input}
Thought:{agent_scratchpad}"""


# # flake8: noqa
# PREFIX = """Perform the following request as best you can. You have access to the following tools:"""
# FORMAT_INSTRUCTIONS = """Use the following format:
#
# Request: the input request you must perform
# Thought: you should always think about what to do
# Action: the action to take, can be one of [{tool_names}] or you can reply yourself
# Action Input: the input to the action
# Observation: the result of the action
# ... (this Thought/Action/Action Input/Observation can repeat N times)
# Final summary: This is the final result I came up with"""
# SUFFIX = """Begin!
#
# Question: {input}
# Thought:{agent_scratchpad}"""