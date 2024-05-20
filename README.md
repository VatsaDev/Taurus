# Taurus

Idea: Programming Agent like devin, but based on gemini flash/pro (gemini flash is the cheaper option, also supposedly good at code)
 - also keep gemini flash due to less latency, thats the free version, the paid version may use big gemini
 - it works because Devin AI itself is oai backed, and an equivalently powerful version, but run on gemini, could be a future google victory point, one that helps google win long term, and so they might pick us.

**Note to self: store any and all data beta users and testers have to finetune the local first model when making that**
**Note to samanyu: the competitors were asians whose parents were actually proud of them, beware**

## Features

 - use a browser (read documentation, access links, run apps to localhost, google guides/howtos, etc.)
 - Terminal (run commands, files, cpu/gpu utils, etc)
 - code editor (vscode for the AI, this is where its edits show?)
 - chat with human (check requirements, ask for api keys, etc)
 - Try to have a really intuitive UI
 - maybe have a start with github repo, go through it all context mode

stuff it needs:
 - try to build in agentic prompting, https://swe-agent.com/, etc
 - a way to break out of a infinite stuck stage, or a way to derail it off a terrible plan, and steer/overwrite to a good one
 - keep track of file system
 - build a plan, break it down to stages, code one thing at a time
 - reason over errors, needs to understand whats in each files
 - vector DB for similarities checks in stuff, code sourcegraph for AI code understanding
 - add unit tests and review functionality from time to time
     - model explores its own work, makes sure UI works right (needs vision language model with actions we tell it to call)
 - devops/serverless crendentials, needs to be able to use vercel/netlify to deploy its work

## Ways to validate our software, hype tests:

 - use unfamiliar tech (run latest AI models, run some diffusion, operate comfyUI)
 - end to end App deployment (builds a game and deploys it on netlify)
 - novely improving an AI model (have it start with the NanoGPT repo and add features like RoPE, lilith optimizer, etc)
  - after it does that, have it follow karpathys neural network recepie, all the way to optimize said network 
 - solve codeforces contests, former USACO problems
 - solve a bug in a real repo
 - compete in a CTF (show basic linux and cybersec skills)
 - dataslave, show it making a VLM dataset end to end and putting it on HF
 - solve real jobs on upwork, bountylist.org
 - build a 3d FPS using javascript/three.js
 - visualizer agent, show it making good graphs off okay to poor data
 - it can install and config cuda, then run a cupy script
 - use https://docs.google.com/document/d/e/2PACX-1vTjLCQcWE_n-uUHFhtBkxTCIJ4FFe5ftY_E4_q69SjXhuEZv_CYpLaQDh3HqrJlAxsgikUx0sTzf9le/pub for more
 - have it recreate itself

## sources/links
 - https://x.com/itsandrewgao/status/1767576901088919897
 - https://x.com/itsandrewgao/status/1786613503471829485
 - https://www.cognition.ai/introducing-devin
 - https://www.cognition.ai/post/swe-bench-technical-report
 - https://github.com/entropy-research/Devon
 - https://swe-agent.com/
 - https://docs.google.com/document/d/e/2PACX-1vTjLCQcWE_n-uUHFhtBkxTCIJ4FFe5ftY_E4_q69SjXhuEZv_CYpLaQDh3HqrJlAxsgikUx0sTzf9le/pub
