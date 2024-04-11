# safety_evaluation_with_llm

The advancement of autonomous driving technology raises significant safety concerns, necessitating careful attention 
and robust safety measures. Challenges include ensuring the reliability of sensors, perception systems, and 
decision-making processes. To address these challenges, research proposes integrating Large Language Models (LLMs) 
into autonomous vehicle software, particularly focusing on enhancing safety through contextual understanding.
LLMs can improve decision-making and safety assessment by incorporating linguistic and contextual knowledge, aiming to 
handle complex driving scenarios. Translating LLM decisions into warnings, leveraging human-like reasoning to predict 
hazards and understand other road users' intentions, thereby enhancing awareness from environment during driving.

## installation

```bash
cd safety_evalution_with_llm
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

## Running Demo
```bash
cd safety_evalution_with_llm
python auto_safety_framework.py output_video1.mp4

```
We can do this for output_video2.mp4 and output_video3.mp4. These videos are created from KITTIMOTS dataset.

The expected output is a string. The example for `output_video1.mp4` is:

`Exercise caution and maintain awareness of cyclists while driving`
