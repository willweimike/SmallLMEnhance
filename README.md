# SmallLMEnhance

## Using small LM with agent to get a better performance on unfamiliar task

For privacy corcerns, local LM models which run on device are a good solution for user. 

### The limit of RAM

Small local LM models would be about only 2~3B params. Due to their size, complex task would be challenging.

### Using another Large LM as Agent actor

Instead of directly using small LM models as agent actor, I tried to use another Large LM as agent as a provider and agent actor, and seems like it works!

### Workflow

![SmallLMEnhance](https://github.com/user-attachments/assets/77ce919b-a163-49db-8c9a-0434fc0f9abe)
