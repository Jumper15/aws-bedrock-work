from google.adk.agents import LlmAgent

greeting_agent = LlmAgent(
     name="Greeter-Agent",
     description="Agent politely greets user",
     instruction="You are a friendly assistant. Greet the user warmly.",
     model="gemini-1.5-flash"
)